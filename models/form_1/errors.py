__author__ = 'myidispg'


class Form1Error(Exception):
    def __init__(self, message):
        self.message = message


class Form1InsertionError(Form1Error):
    pass


class Form1AlreadySubmitted(Form1Error):
    pass
