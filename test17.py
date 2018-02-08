#Turn off allert spam in GMAIL and start this code
import smtplib
msg = "Hello There!"
mail=smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('sendem@gmail.com', 'password')
for Email in
mail.sendmail('sendem@gmail.com', 'recivemal@gmail.com', msg)
mail.close()
