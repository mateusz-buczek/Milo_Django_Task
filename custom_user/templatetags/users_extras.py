from django import template
import datetime
from dateutil.relativedelta import relativedelta

register = template.Library()


@register.filter()
def is_eligible(birth_date):
    difference = relativedelta(datetime.date.today(), birth_date)
    if difference.years >= 13:
        return 'allowed'
    elif difference.years < 13:
        return 'blocked'
    elif birth_date is None:
        return 'add birthday date!'


@register.filter()
def bizz_fuzz(random_number):
    if random_number % 3 == 0 and random_number % 5 == 0:
        return 'BizzFuzz'
    elif random_number % 3 == 0:
        return "Bizz"
    elif random_number % 5 == 0:
        return "Fuzz"
    else:
        return random_number

