from gmailSend.gmail import Gmail
from flyPL.flypl import FlyPl
import time
from logins.logins import LIST_OF_HOTELS
import datetime
from datetime import timedelta

# Set up dates
date_one_from = datetime.datetime(2023, 5, 22)
date_one_to = datetime.datetime(2023, 6, 2)
date_two_from = datetime.datetime(2023, 6, 5)
date_two_to = datetime.datetime(2023, 6, 16)
date_three_from = datetime.datetime(2023, 6, 19)
date_three_to = datetime.datetime(2023, 6, 30)
stays_days = 8
alert_price_per_person = 3500
array_dates = []


def calc_dates(date_from: datetime, date_to: datetime, stays: int):
    formatted_date_from = int(str(date_from.strftime("%Y %m %d")).replace(' ', ''))
    formatted_date_to = int(str(date_to.strftime("%Y %m %d")).replace(' ', ''))
    for i in range(formatted_date_to - formatted_date_from):
        if date_from + timedelta(days=stays) + timedelta(days=i) <= date_to:
            array_dates.append(str((date_from + timedelta(days=i)).strftime("%Y%m%d")))


calc_dates(date_one_from, date_one_to, stays_days)
calc_dates(date_two_from, date_two_to, stays_days)
calc_dates(date_three_from, date_three_to, stays_days)

while True:
    for url in LIST_OF_HOTELS:
        for date in array_dates:
            with FlyPl() as bot:
                try:
                    bot.load_page(url)
                    time.sleep(5)
                    bot.accept_cookies()
                    time.sleep(5)
                    bot.change_date(int(date))
                    time.sleep(5)
                    price = bot.extract_price_data() / 2
                    print(date, ' ', price)
                    if price <= alert_price_per_person:
                        hotel = bot.extract_hotel_data()
                        date = datetime.datetime(int(date[0:4]), int(date[4:6]), int(date[6:]))
                        Gmail(hotel, price, date)
                except Exception as _:
                    print(f'''Data is incorrect {date} 
                    Trying another''')
    time.sleep(3600)
