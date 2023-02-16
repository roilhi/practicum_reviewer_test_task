import datetime as dt

class Record: 
    def __init__(self, amount, comment, date=''):
        self.amount = amount
        self.date = (
            dt.datetime.now().date() if
            not
            date else dt.datetime.strptime(date, '%d.%m.%Y').date())
        self.comment = comment
class Calculator:
    '''
    It is recommended to add docstring comments in order to know about the class 
    or methods detalis (inputs, outputs, etc)
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
                (today - record.date).days < 7 and
                (today - record.date).days >= 0
            ):
                week_stats += record.amount
        return week_stats

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):  
        x = self.limit - self.get_today_stats()
        if x > 0: 
            return f'You can eat something else today,' \
                   f' but with a total calorie content of no more than {x} kcal'
        else:
            return('Stop eating!')


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):  # Gets the remaining calories for today
        x = self.limit - self.get_today_stats()
        if x > 0:
            return f'You can eat something else today,' \
                   f' but with a total calorie content of no more than {x} kcal'
        else:
            return('Stop eating!')


class CashCalculator(Calculator):
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
                f'Left for today {round(cash_remained, 2)} '
                f'{currency_type}'
            )
        elif cash_remained == 0:
            return 'No money, keep it up!'
        elif cash_remained < 0:
            return 'No money, keep it up:' \
                   ' your debt is - {0:.2f} {1}'.format(-cash_remained,
                                                     currency_type)

    def get_week_stats(self):
        super().get_week_stats()

cash_calculator = CashCalculator(1000)

cash_calculator.add_record(Record(amount=145, comment="cofee"))
cash_calculator.add_record(Record(amount=300, comment="To mark for lunch"))
cash_calculator.add_record(Record(amount=3000, comment="At the bar for Tanya's birthday", date="08.11.2019"))

print(cash_calculator.get_today_cash_remained("rub"))
print(cash_calculator.get_today_stats())

calories_calculator = CaloriesCalculator(3000)
calories_calculator.add_record(Record(amount=450, comment="Breakfast"))
calories_calculator.add_record(Record(amount=345, comment="Little snack"))
calories_calculator.add_record(Record(amount=1300, comment="Lunch"))

print(calories_calculator.get_calories_remained())
print(calories_calculator.get_today_stats())

# Missing if __name__=="main": to execute the code.
# classes have been created but they are not called or imported
