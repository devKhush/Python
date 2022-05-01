import smtplib

# https://www.geeksforgeeks.org/send-mail-gmail-account-using-python/
# https://www.tutorialspoint.com/python/python_sending_email.htm#:~:text=Simple%20Mail%20Transfer%20Protocol%20(SMTP,SMTP%20or%20ESMTP%20listener%20daemon.
# https://www.javatpoint.com/python-sending-email


def createFile():
    with open('text.txt', 'w') as file:
        content = '''
Here is little Joke below: 

Teacher: Why are you late?
Student: Because of the sign on the road.
Teacher: What type of sign?
Student: The sign that says, School Ahead, Go Slow.
Lol...'''
        file.write(content)

    with open('text.txt', 'r') as file:
        return file.read()


# send email using python
# smtp -> simple mail transfer protocol

sender = 'randomuser783810@gmail.com'
password = 'Kuch bhi 10'
receiver = 'khushharsh5699@gmail.com'
joke = createFile()

message = '''
Subject: SMTP e-mail test
From: %s
To: %s

Hi, Khush Harsh
This is a test email.
This e-mail is sent using Python language

Regards,
Python 

''' % (sender, receiver)

message += joke
print(message)


# How to spam email XD
times = 5
for i in range(0, times):
    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        # smtpObj.ehlo()

        smtpObj.starttls()

        smtpObj.login(sender, password)
        smtpObj.sendmail(sender, receiver, message)
        smtpObj.quit()
    except Exception as e:
        print(e)
        print('Email couldn\'t be sent')
    else:
        print('Email sent successfully!')
