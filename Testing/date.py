from datetime import datetime

def today():
    now: datetime = datetime.now()
    year = f"{now:%m.%d.%y}"
    time = f"{now:%H:%M:%S%p}"
    date = f"{now:%c}"

    return f"Today is {year} at {time}"