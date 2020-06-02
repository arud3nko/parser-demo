import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from options import from_mail, from_passwd, smtp_server, smtp_port


def send_total(address, kol, file, to_mail):

    msg = MIMEMultipart()

    msg['Subject'] = 'Завершен парсинг страницы'
    msg['From'] = from_mail
    msg['To'] = to_mail

    msg.attach(MIMEText('''Доброго времени суток!
Завершен парсинг страницы %s

Всего объявлений: %s

-------
Не отвечайте на это сообщение, оно отправлено автоматически.
''' % (address, kol)))

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(file, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="total.xlsx"')

    msg.attach(part)

    server = smtplib.SMTP_SSL(smtp_server, smtp_port, timeout=5)  # SMTP('smtp.yandex.com', 587)
    server.ehlo()
    server.login(from_mail, from_passwd)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()