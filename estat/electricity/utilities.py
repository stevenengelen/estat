from datetime import datetime, timedelta

class Utilities(object) :

    @staticmethod
    def date_is_in_the_future(date) :
        # this formats the variable to YYYY-MM-DD
        date_tomorrow = str(datetime.today() + timedelta(days = 1))[:10]
        if str(date) < date_tomorrow :
            return False
        return True
