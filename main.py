import datetime as dt

# There are no docstring comments below classes and methods in order to explain what is
# each thing doing
class Record: 
    def __init__(self, amount, comment, date=''):
        self.amount = amount
        self.date = ( 
            dt.datetime.now().date() if # use extra identation and a conditional continuation line
            not
            # the closing parenthesis on multiple constructs may either linne
            # up under the first non-whitespace character of last line
            date else dt.datetime.strptime(date, '%d.%m.%Y').date())
            # place here  ) closing brace
        self.comment = comment 
class Calculator:
    '''
    It is recommended to add docstring comments in order to 
    know about the class or methods detalis 
    (inputs, outputs, etc).
    '''
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_stats = 0
        for Record in self.records:
            if Record.date == dt.datetime.now().date():
                today_stats = today_stats + Record.amount  
        return today_stats

    def get_week_stats(self):
        week_stats = 0
        today = dt.datetime.now().date()
        for record in self.records:
            if (
                (today - record.date).days < 7 and #avoid using trailing whitespaces in parenthesis/brackets
                (today - record.date).days >= 0
            ):
                week_stats += record.amount
        return week_stats


class CaloriesCalculator(Calculator):
    '''
    Add docstring documentation in order to know 
    what this class is doing.
    '''
    def get_calories_remained(self):  # Gets the remaining calories for today
        x = self.limit - self.get_today_stats()
        if x > 0: #backslash is not recommended to be used for continuation of strings
            return f'You can eat something else today,' \
                   f' but with a total calorie content of no more than {x} kcal' #more than 78 characters, it is
                   #recommended to break this line into segments
        else:
            return('Stop eating!')


class CashCalculator(Calculator):
    '''
    Add docstring documentation in order to know 
    what this class is doing.
    '''
    USD_RATE = float(60)  # US dollar exchange rate.
    EURO_RATE = float(70)  # Euro exchange rate.

    def get_today_cash_remained(self, currency,
                                USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        currency_type = currency
        cash_remained = self.limit - self.get_today_stats()
        if currency == 'usd':
            cash_remained /= USD_RATE
            currency_type = 'USD'
        elif currency_type == 'eur':
            cash_remained /= EURO_RATE
            currency_type = 'Euro'
        elif currency_type == 'rub':
            cash_remained == 1.00
            currency_type = 'rub'
        if cash_remained > 0:
            return (
                f'Left for today {round(cash_remained, 2)} ' #it is not recommended to add logical/arithmetic operations in f strings
                f'{currency_type}'
            )
        elif cash_remained == 0:
            return 'No money, keep it up!'
        elif cash_remained < 0: #backslash is not recommended for continuation of strings
            return 'No money, keep it up:' \
                   ' your debt is - {0:.2f} {1}'.format(-cash_remained,
                                                     currency_type)

    def get_week_stats(self):
        super().get_week_stats()

# Missing if __name__=="main": to execute the code and construct clases (recommended for .py files)
