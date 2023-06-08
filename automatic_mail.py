import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login("kdyyuvan@gmail.com", "hzrvwmuetzxuffpk")

server.sendmail("kdyyuvan@gmail.com", "yuvanvarshith@outlook.com", "This is Automatic generated mail from python")

print("Mail Sent")