import smtplib
import datetime as dt
import random

MY_EMAIL = "user_name@gmail.com"
MY_PASSWORD = "*********"

now = dt.datetime.now()
weekday = now.weekday

if weekday == 1: # if Monday

    with open("quotes.txt", mode="r") as quote_file:
        all_quotes = quote_file.readline()
        quote = random.choise(all_quotes)

    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:

        #for message encryption
        connection.starttls()

        connection.login(MY_EMAIL, MY_PASSWORD)

        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=MY_EMAIL, 
            msg=f"Subject:Monday Motivation\n\nT{quote}"
        ) 