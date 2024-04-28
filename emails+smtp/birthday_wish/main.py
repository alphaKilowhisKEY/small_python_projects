"""
Birthday Greeting Email Automation

This Python script automates sending birthday greeting emails to individuals listed in a CSV file. It reads the CSV file containing birthday data, matches the current date with birthdays, selects a random letter template, replaces the placeholder with the recipient's name, and sends an email using SMTP.

Libraries Used:
- smtplib: for sending emails via SMTP
- datetime: for working with dates and times
- random: for generating random numbers
- pandas: for reading CSV files and data manipulation


Process:
- Read birthday data from a CSV file into a pandas DataFrame.
- Convert the DataFrame into a dictionary with (month, day) tuples as keys.
- Check if the current date matches any birthday in the dictionary.
- If a match is found, select a random letter template, replace the placeholder with the recipient's name, and send an email.
- Use SMTP to establish a connection with the email provider's SMTP server, authenticate using sender's credentials, and send the email with subject "Happy Birthday!".

Usage:
- Replace "YOUR EMAIL", "YOUR PASSWORD", and "YOUR EMAIL PROVIDER SMTP SERVER ADDRESS" with appropriate values.
- Prepare letter templates in a directory named "letter_templates" with filenames formatted as "letter_1.txt", "letter_2.txt", etc.
- Make sure the CSV file "birthdays.csv" contains columns named "month", "day", "name", and "email" with birthday data.
- Run the script periodically to send birthday greeting emails automatically: $python3 main.py
"""

import smtplib
import datetime as dt
import random
import pandas

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        ) 