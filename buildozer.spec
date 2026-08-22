[app]

title = Flappy Bird
package.name = flappybird
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,jpeg,mp3,wav,kv,atlas

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0


[buildozer]

log_level = 2
warn_on_root = 1


[android]

android.api = 33
android.minapi = 24
android.ndk_api = 24
android.archs = arm64-v8a

android.accept_sdk_license = True
android.permissions = INTERNET
