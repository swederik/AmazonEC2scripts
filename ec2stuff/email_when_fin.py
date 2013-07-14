import smtplib

#itisfinishedprocessing@gmail.com.
def send_email(TO=["erik.ziegler@ulg.ac.be"], SUBJECT="DONE", TEXT="Finished"):
    SERVER = "smtp.gmail.com:587"
    username = "itisfinishedprocessing"
    password = "throwawaypassword"

    FROM = "itisfinishedprocessing@gmail.com"

    #TEXT = "This message was sent with Python's smtplib."
    # Prepare actual message

    message = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    # Send the mail
    server = smtplib.SMTP(SERVER)
    server.starttls()
    server.login(username,password)
    server.sendmail(FROM, TO, message)
    server.quit()