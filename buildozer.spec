
[app]
title = Notification Forwarder
package.name = notiforwarder
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,requests,pyjnius
orientation = portrait
fullscreen = 0

# Permissions
android.permissions = INTERNET, BIND_NOTIFICATION_LISTENER_SERVICE

# Entry point
entrypoint = main.py
android.minapi = 21
android.sdk = 30
android.ndk = 23b
android.ndk_api = 21

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (bool) Android service declaration
android.services = mynotification

# (str) Supported architectures
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
