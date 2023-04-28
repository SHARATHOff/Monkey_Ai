import datetime
from plyer import notification

def send_notification(title, body):
    notification.notify(title=title,message=body)

send_notification("Notification","Drink Water")