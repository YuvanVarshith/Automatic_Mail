import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login("sender@gmail.com", "hzrvwmuetzxuffpk")

server.sendmail("sender@gmail.com", "recevier@gmail.com", "This is Automatic generated mail from python")

print("Mail Sent")
