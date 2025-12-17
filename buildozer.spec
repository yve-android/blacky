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
