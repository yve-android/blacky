#!/bin/bash

echo "🚀 Erstelle Blacky App Dateien..."

# ==================
# main.py erstellen
# ==================
cat > main.py << 'EOF'
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
import os
import hashlib
from pathlib import Path

class BlackyApp(App):
    status_text = StringProperty("Bereit")
    
    def build(self):
        self.title = "Blacky - Datei-Assistent"
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        header = BoxLayout(size_hint_y=0.15, orientation='vertical')
        title_label = Label(
            text='[b]Blacky[/b]\nDatei-Organisations-Assistent',
            markup=True, font_size='20sp', size_hint_y=0.7
        )
        self.status_label = Label(
            text=self.status_text, size_hint_y=0.3, color=(0.5, 0.8, 1, 1)
        )
        header.add_widget(title_label)
        header.add_widget(self.status_label)
        
        self.file_chooser = FileChooserListView(
            path='/storage/emulated/0/', dirselect=True, size_hint_y=0.5
        )
        
        button_layout = BoxLayout(size_hint_y=0.35, orientation='vertical', spacing=5)
        
        scan_btn = Button(
            text='Ordner scannen', background_color=(0.2, 0.6, 1, 1),
            on_press=self.scan_folder
        )
        duplicates_btn = Button(
            text='Duplikate finden', background_color=(1, 0.6, 0.2, 1),
            on_press=self.find_duplicates
        )
        info_btn = Button(
            text='Info', background_color=(0.5, 0.5, 0.5, 1),
            on_press=self.show_info
        )
        
        button_layout.add_widget(scan_btn)
        button_layout.add_widget(duplicates_btn)
        button_layout.add_widget(info_btn)
        
        main_layout.add_widget(header)
        main_layout.add_widget(self.file_chooser)
        main_layout.add_widget(button_layout)
        return main_layout
    
    def update_status(self, text):
        self.status_text = text
        self.status_label.text = text
    
    def scan_folder(self, instance):
        selected = self.file_chooser.selection
        if not selected:
            self.show_popup("Fehler", "Bitte wähle einen Ordner aus!")
            return
        
        path = selected[0]
        self.update_status(f"Scanne: {os.path.basename(path)}...")
        
        try:
            files = list(Path(path).rglob('*'))
            file_count = len([f for f in files if f.is_file()])
            dir_count = len([f for f in files if f.is_dir()])
            
            result = f"Gefunden:\n{file_count} Dateien\n{dir_count} Ordner"
            self.show_popup("Scan-Ergebnis", result)
            self.update_status("Scan abgeschlossen")
        except Exception as e:
            self.show_popup("Fehler", f"Fehler:\n{str(e)}")
            self.update_status("Fehler")
    
    def find_duplicates(self, instance):
        selected = self.file_chooser.selection
        if not selected:
            self.show_popup("Fehler", "Bitte wähle einen Ordner aus!")
            return
        
        path = selected[0]
        self.update_status("Suche Duplikate...")
        
        try:
            file_hashes = {}
            duplicates = []
            
            for file_path in Path(path).rglob('*'):
                if file_path.is_file():
                    try:
                        file_hash = self.get_file_hash(file_path)
                        if file_hash in file_hashes:
                            duplicates.append((file_path, file_hashes[file_hash]))
                        else:
                            file_hashes[file_hash] = file_path
                    except:
                        continue
            
            if duplicates:
                dup_text = f"Duplikate: {len(duplicates)}\n\n"
                for dup, orig in duplicates[:5]:
                    dup_text += f"• {dup.name}\n"
                if len(duplicates) > 5:
                    dup_text += f"\n... und {len(duplicates)-5} weitere"
                self.show_popup("Duplikate", dup_text)
            else:
                self.show_popup("Ergebnis", "Keine Duplikate!")
            
            self.update_status("Fertig")
        except Exception as e:
            self.show_popup("Fehler", f"{str(e)}")
    
    def get_file_hash(self, file_path, chunk_size=8192):
        sha256 = hashlib.sha256()
        with open(file_path, 'rb') as f:
            while chunk := f.read(chunk_size):
                sha256.update(chunk)
        return sha256.hexdigest()
    
    def show_info(self, instance):
        self.show_popup(
            "Über Blacky",
            "[b]Blacky v1.0[/b]\n\nOffline-Assistent für\nDateiverwaltung\n\n© 2024 yve-android",
            markup=True
        )
    
    def show_popup(self, title, message, markup=False):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        msg_label = Label(text=message, markup=markup, halign='left', valign='top')
        msg_label.bind(size=msg_label.setter('text_size'))
        
        scroll = ScrollView(size_hint=(1, 0.8))
        scroll.add_widget(msg_label)
        content.add_widget(scroll)
        
        close_btn = Button(
            text='Schließen', size_hint=(1, 0.2),
            background_color=(0.3, 0.3, 0.3, 1)
        )
        content.add_widget(close_btn)
        
        popup = Popup(title=title, content=content, size_hint=(0.9, 0.7))
        close_btn.bind(on_press=popup.dismiss)
        popup.open()

if __name__ == '__main__':
    BlackyApp().run()
EOF

echo "✅ main.py erstellt"

# ==================
# buildozer.spec
# ==================
cat > buildozer.spec << 'EOF'
[app]

title = Blacky
package.name = blacky
package.domain = org.yveandroid

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3==3.11.6,kivy==2.3.0,pillow

orientation = portrait

android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]

log_level = 2
warn_on_root = 1
EOF

echo "✅ buildozer.spec erstellt"

# ==================
# GitHub Actions
# ==================
mkdir -p .github/workflows

cat > .github/workflows/build-apk.yml << 'EOF'
name: Build Blacky APK

on:
  push:
    branches: [ main, master ]
  workflow_dispatch:

jobs:
  build-apk:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout
      uses: actions/checkout@v4
    
    - name: Setup Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'
    
    - name: Install Dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y build-essential git ffmpeg \
          libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
          openjdk-17-jdk unzip autoconf libtool cmake libffi-dev libssl-dev
        pip install buildozer cython==0.29.36
    
    - name: Cache Buildozer
      uses: actions/cache@v4
      with:
        path: |
          .buildozer
          ~/.buildozer
        key: buildozer-${{ hashFiles('buildozer.spec') }}
    
    - name: Build APK
      run: buildozer android debug
    
    - name: Upload APK
      uses: actions/upload-artifact@v4
      with:
        name: blacky-apk
        path: bin/*.apk
        retention-days: 30
EOF

echo "✅ GitHub Actions Workflow erstellt"

echo ""
echo "🎉 Alle Dateien erfolgreich erstellt!"
echo ""
echo "Nächste Schritte:"
echo "1. git add ."
echo "2. git commit -m 'Add Blacky Android App'"
echo "3. git push origin main"
