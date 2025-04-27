[app]
title = Notification Forwarder
package.name = notiforwarder
package.domain = org.example
source.dir = .
source.include_exts = py
version = 1.0

requirements = python3,kivy,requests,pyjnius

android.permissions = INTERNET
android.services = mynotification

# Добавляем разрешение на доступ к уведомлениям
android.permissions = android.permission.BIND_NOTIFICATION_LISTENER_SERVICE