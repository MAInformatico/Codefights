import time
def validTime(Time):
    try:
        time.strptime(Time, '%H:%M')
        return True
    except ValueError:
        return False
