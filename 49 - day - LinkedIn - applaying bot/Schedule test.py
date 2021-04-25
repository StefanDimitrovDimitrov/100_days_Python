import time
import schedule


def print_something():
    print("It's working")

# schedule.every(10).seconds.do(print_something)
schedule.every().day.at('12:35').do(print_something)

while True:
    schedule.run_pending()
    time.sleep(1)
