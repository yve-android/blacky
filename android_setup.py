#!/usr/bin/env python3
"""
Android Projekt Komplett-Setup Script
Erstellt eine vollständige Android-Projektstruktur von Grund auf
"""

import os
import sys
from pathlib import Path

class AndroidProjectSetup:
    def __init__(self, repo_path=".", package_name="com.yve.blacky"):
        self.repo_path = Path(repo_path)
        self.package_name = package_name
        self.package_path = package_name.replace(".", "/")
        self.app_name = "Blacky"
        
    def log(self, message, level="INFO"):
        print(f"[{level}] {message}")
    
    def create_directory_structure(self):
        """Erstellt die komplette Android-Verzeichnisstruktur"""
        self.log("Erstelle Android-Verzeichnisstruktur...")
        
        directories = [
            "app/src/main/java/" + self.package_path,
            "app/src/main/res/layout",
            "app/src/main/res/values",
            "app/src/main/res/mipmap-hdpi",
            "app/src/main/res/mipmap-mdpi",
            "app/src/main/res/mipmap-xhdpi",
            "app/src/main/res/mipmap-xxhdpi",
            "app/src/main/res/mipmap-xxxhdpi",
            "app/src/androidTest/java/" + self.package_path,
            "app/src/test/java/" + self.package_path,
        ]
        
        for directory in directories:
            dir_path = self.repo_path / directory
            dir_path.mkdir(parents=True, exist_ok=True)
            self.log(f"✓ {directory}", "SUCCESS")
    
    def create_root_build_gradle(self):
        """Erstellt root build.gradle"""
        self.log("Erstelle root build.gradle...")
        
        content = """// Top-level build file where you can add configuration options common to all sub-projects/modules.
plugins {
    id 'com.android.application' version '8.2.0' apply false
    id 'com.android.library' version '8.2.0' apply false
    id 'org.jetbrains.kotlin.android' version '1.9.20' apply false
}

allprojects {
    repositories {
        google()
        mavenCentral()
    }
}

task clean(type: Delete) {
    delete rootProject.buildDir
}
"""
        
        build_gradle = self.repo_path / "build.gradle"
        build_gradle.write_text(content)
        self.log("✓ build.gradle erstellt", "SUCCESS")
    
    def create_settings_gradle(self):
        """Erstellt settings.gradle"""
        self.log("Erstelle settings.gradle...")
        
        content = """pluginManagement {
    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}

rootProject.name = "Blacky"
include ':app'
"""
        
        settings_gradle = self.repo_path / "settings.gradle"
        settings_gradle.write_text(content)
        self.log("✓ settings.gradle erstellt", "SUCCESS")
    
    def create_app_build_gradle(self):
        """Erstellt app/build.gradle"""
        self.log("Erstelle app/build.gradle...")
        
        content = f"""plugins {{
    id 'com.android.application'
    id 'org.jetbrains.kotlin.android'
}}

android {{
    namespace '{self.package_name}'
    compileSdk 34

    defaultConfig {{
        applicationId "{self.package_name}"
        minSdk 24
        targetSdk 34
        versionCode 1
        versionName "1.0"

        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
    }}

    buildTypes {{
        release {{
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }}
    }}
    
    compileOptions {{
        sourceCompatibility JavaVersion.VERSION_17
        targetCompatibility JavaVersion.VERSION_17
    }}
    
    kotlinOptions {{
        jvmTarget = '17'
    }}
    
    buildFeatures {{
        viewBinding true
    }}
}}

dependencies {{
    implementation 'androidx.core:core-ktx:1.12.0'
    implementation 'androidx.appcompat:appcompat:1.6.1'
    implementation 'com.google.android.material:material:1.11.0'
    implementation 'androidx.constraintlayout:constraintlayout:2.1.4'
    
    testImplementation 'junit:junit:4.13.2'
    androidTestImplementation 'androidx.test.ext:junit:1.1.5'
    androidTestImplementation 'androidx.test.espresso:espresso-core:3.5.1'
}}
"""
        
        app_build_gradle = self.repo_path / "app" / "build.gradle"
        app_build_gradle.write_text(content)
        self.log("✓ app/build.gradle erstellt", "SUCCESS")
    
    def create_android_manifest(self):
        """Erstellt AndroidManifest.xml"""
        self.log("Erstelle AndroidManifest.xml...")
        
        content = f"""<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">

    <application
        android:allowBackup="true"
        android:dataExtractionRules="@xml/data_extraction_rules"
        android:fullBackupContent="@xml/backup_rules"
        android:icon="@mipmap/ic_launcher"
        android:label="{self.app_name}"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.AppCompat.Light.DarkActionBar"
        tools:targetApi="31">
        
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:theme="@style/Theme.AppCompat.Light.DarkActionBar">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>
"""
        
        manifest_path = self.repo_path / "app" / "src" / "main" / "AndroidManifest.xml"
        manifest_path.write_text(content)
        self.log("✓ AndroidManifest.xml erstellt", "SUCCESS")
    
    def create_main_activity(self):
        """Erstellt MainActivity.kt"""
        self.log("Erstelle MainActivity.kt...")
        
        content = f"""package {self.package_name}

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import android.widget.TextView

class MainActivity : AppCompatActivity() {{
    
    override fun onCreate(savedInstanceState: Bundle?) {{
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        val textView = findViewById<TextView>(R.id.textView)
        textView.text = "Welcome to {self.app_name}!"
    }}
}}
"""
        
        main_activity_path = self.repo_path / "app" / "src" / "main" / "java" / self.package_path / "MainActivity.kt"
        main_activity_path.write_text(content)
        self.log("✓ MainActivity.kt erstellt", "SUCCESS")
    
    def create_layout_files(self):
        """Erstellt Layout-Dateien"""
        self.log("Erstelle Layout-Dateien...")
        
        # activity_main.xml
        activity_main_content = """<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout 
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <TextView
        android:id="@+id/textView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Hello World!"
        android:textSize="24sp"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

</androidx.constraintlayout.widget.ConstraintLayout>
"""
        
        layout_path = self.repo_path / "app" / "src" / "main" / "res" / "layout" / "activity_main.xml"
        layout_path.write_text(activity_main_content)
        self.log("✓ activity_main.xml erstellt", "SUCCESS")
    
    def create_string_resources(self):
        """Erstellt strings.xml"""
        self.log("Erstelle strings.xml...")
        
        content = f"""<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">{self.app_name}</string>
</resources>
"""
        
        strings_path = self.repo_path / "app" / "src" / "main" / "res" / "values" / "strings.xml"
        strings_path.write_text(content)
        self.log("✓ strings.xml erstellt", "SUCCESS")
    
    def create_color_resources(self):
        """Erstellt colors.xml"""
        self.log("Erstelle colors.xml...")
        
        content = """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="black">#FF000000</color>
    <color name="white">#FFFFFFFF</color>
    <color name="purple_200">#FFBB86FC</color>
    <color name="purple_500">#FF6200EE</color>
    <color name="purple_700">#FF3700B3</color>
    <color name="teal_200">#FF03DAC5</color>
    <color name="teal_700">#FF018786</color>
</resources>
"""
        
        colors_path = self.repo_path / "app" / "src" / "main" / "res" / "values" / "colors.xml"
        colors_path.write_text(content)
        self.log("✓ colors.xml erstellt", "SUCCESS")
    
    def create_proguard_rules(self):
        """Erstellt proguard-rules.pro"""
        self.log("Erstelle proguard-rules.pro...")
        
        content = """# Add project specific ProGuard rules here.
# You can control the set of applied configuration files using the
# proguardFiles setting in build.gradle.

# Keep common Android classes
-keep public class * extends android.app.Activity
-keep public class * extends android.app.Application
-keep public class * extends android.app.Service
-keep public class * extends android.content.BroadcastReceiver
-keep public class * extends android.content.ContentProvider

# Keep Kotlin metadata
-keep class kotlin.Metadata { *; }
"""
        
        proguard_path = self.repo_path / "app" / "proguard-rules.pro"
        proguard_path.write_text(content)
        self.log("✓ proguard-rules.pro erstellt", "SUCCESS")
    
    def create_gitignore(self):
        """Erstellt/erweitert .gitignore"""
        self.log("Erstelle/erweitere .gitignore...")
        
        gitignore_content = """# Android Studio
*.iml
.gradle
/local.properties
/.idea
.DS_Store
/build
/captures
.externalNativeBuild
.cxx
*.apk
*.ap_
*.dex

# Gradle
.gradle/
build/

# Local configuration
local.properties

# Log Files
*.log
"""
        
        gitignore_path = self.repo_path / ".gitignore"
        if gitignore_path.exists():
            existing = gitignore_path.read_text()
            if "*.iml" not in existing:
                gitignore_path.write_text(existing + "\n" + gitignore_content)
                self.log("✓ .gitignore erweitert", "SUCCESS")
            else:
                self.log("✓ .gitignore bereits vorhanden", "SUCCESS")
        else:
            gitignore_path.write_text(gitignore_content)
            self.log("✓ .gitignore erstellt", "SUCCESS")
    
    def run_setup(self):
        """Führt das komplette Setup aus"""
        self.log("=" * 60)
        self.log("🚀 Starte Android Projekt Setup")
        self.log("=" * 60)
        self.log(f"Package: {self.package_name}")
        self.log(f"App Name: {self.app_name}")
        self.log("")
        
        self.create_directory_structure()
        self.log("")
        
        self.create_root_build_gradle()
        self.create_settings_gradle()
        self.create_app_build_gradle()
        self.log("")
        
        self.create_android_manifest()
        self.create_main_activity()
        self.log("")
        
        self.create_layout_files()
        self.create_string_resources()
        self.create_color_resources()
        self.log("")
        
        self.create_proguard_rules()
        self.create_gitignore()
        
        self.log("")
        self.log("=" * 60)
        self.log("✅ Android Projekt Setup abgeschlossen!")
        self.log("=" * 60)
        self.log("")
        self.log("📋 Nächste Schritte:")
        self.log("1. Führe './gradlew build' aus")
        self.log("2. Prüfe mit 'ls -la app/'")
        self.log("3. Teste mit './gradlew assembleDebug'")
        self.log("4. Führe dann das repair_actions.py Script aus")
        self.log("5. Committe alles: git add . && git commit -m 'Initial Android project setup'")
        self.log("")

if __name__ == "__main__":
    repo_path = sys.argv[1] if len(sys.argv) > 1 else "."
    package_name = sys.argv[2] if len(sys.argv) > 2 else "com.yve.blacky"
    
    setup = AndroidProjectSetup(repo_path, package_name)
    setup.run_setup()
