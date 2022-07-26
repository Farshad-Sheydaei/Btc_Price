from datetime import datetime


def now():
    now_time = datetime.now()
    date = now_time.strftime("%d/%m/%Y %H:%M:%S")
    return date
