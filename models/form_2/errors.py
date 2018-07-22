__author__ = 'myidispg'


class Form2Error(Exception):
    def __init__(self, message):
        self.message = message


class Form2AlreadySubmitted(Form2Error):
    pass