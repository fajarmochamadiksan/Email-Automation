# Final Project - Basic Python
# Program untuk mengirimkan email kepada beberapa penerima
# Menggunakan smtp GMAIL, sebelumnya email pengirim di setting untuk menerima low security.

# Imports Library smtplib
import smtplib
import getpass

# SETUP EMAIL LOGIN
gmail_user = input(str("Masukkan akun gmail: "))
gmail_app_password = input(str("Masukkan password gmail: "))

# SETUP PENERIMA EMAIL
with open('receiver_list.txt', 'r') as file_x:
    receipentemail = file_x.read()
    penerima = receipentemail.split("\n")

# SETUP Pengirim, penerima, judul dan isi email

sent_from = gmail_user
sent_to = penerima
#sent_to = input(str("Masukkan gmail penerima lalu akhiri dengan enter: "))
sent_subject = input(
    str("Masukkan  subjek atau judul lalu akhiri dengan enter: "))
sent_body = input(
    str("Masukkan pesan yang akan dikirim lalu akhiri dengan enter: "))

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(penerima), sent_subject, sent_body)


# =============================================================================
# Mengirim Email atau Gagal
# Detail Sumber: http://www.samlogic.net/articles/smtp-commands-reference.htm
# =============================================================================

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_app_password)
    server.sendmail(receipentemail, sent_to, email_text)
    server.close()

    print('Email sent!')
except Exception as exception:
    print("Error: %s!\n\n" % exception)

