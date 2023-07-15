import smtplib
from random import randint
import datetime as dt
import pandas

my_email = 'sarveshkr9808@gmail.com'
my_password = 'password'
now = dt.datetime.now()
today = now.day
current_month = now.month

data = pandas.read_csv('birthdays.csv')

for ind in data.index:
    if today == data['day'][ind] and current_month == data['month'][ind]:
        name = data['name'][ind]
        receiver_email = data['email'][ind]
        with open(f'letter_templates\letter_{randint(1, 3)}.txt') as letter_file:
            letter = letter_file.read()
            letter = letter.replace('[NAME]', name)

with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=receiver_email,
                        msg=f'Happy birthday!!!\n\n{letter}')
