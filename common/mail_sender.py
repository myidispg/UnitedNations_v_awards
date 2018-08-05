__author__ = 'myidispg'


class MailSender:

    @staticmethod
    def get_mail(arg_mail):
        global mail
        mail = arg_mail

    @staticmethod
    def send_mail(msg):
        mail.send(msg)
