import datetime


class Utility(object):
    @staticmethod
    def clean_date_stamp():
        now = datetime.datetime.now()

        return now.replace(microsecond=0)
