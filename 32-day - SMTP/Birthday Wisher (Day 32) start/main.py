#import smtplib

#my_email = "dimitrov22@yahoo.com"
#password = ""

#with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    #connection.starttls()
    #connection.login(user=my_email, password=password)
    #connection.sendmail(from_addr=my_email,
                        #to_addrs="stefan.dimitrov.dimitrov@gmail.com",
                        #msg="Subject:Hello\n\nThis is the body of my email.")

import datetime as dt

now = dt.datetime.now()
year = now.year
print (type(now))

date_of_birth = dt.datetime(year=1995, month=12, day=15)
print(date_of_birth)