from lark import Lark, Transformer, v_args
from lark import logger
from lark.exceptions import UnexpectedInput, LarkError
import logging

from datetime import datetime

logger.setLevel(logging.DEBUG)

_period_grammar = """
    ?start: period
    
    ?period: datetime datetime

    datetime: date time
        | time      -> just_time
    
    date: month "/" day "/" year
    
    time: hour ":" minute ampm?
    
    ?ampm: AM | PM
    
    AM: "AM"i
    PM: "PM"i

    day: DIGIT12
    month: DIGIT12
    year: DIGIT4 | DIGIT2

    hour: DIGIT12
    minute: DIGIT2

    DIGIT12: /\d{1,2}/
    DIGIT4: /\d{4}/
    DIGIT2: /\d{2}/

    %import common.WS_INLINE
    %ignore WS_INLINE
"""

class _PeriodTree(Transformer):
    def period(self, t):
        initial = t[0]
        end = t[1]
        if t[1] <= t[0]:
            raise Exception("your starting date is after your ending date")
        return [t[0], t[1]]

    def datetime(self, t):
        mm, dd, yy = t[0]
        h, m = t[1]
        try:
            return datetime(yy, mm, dd, h, m)
        except:
            raise Exception("your entered date is not possible")

    def time(self, t):
        print(t)
        h = t[0]
        m = t[1]
        if len(t) == 3:
            if not( 1 <= h and h <= 12 ):
                raise Exception("you entered the time incorrectly")
            h %= 12
            if t[2].upper() == "PM":
                h += 12
        if not( 0 <= h and h <= 23 and 0 <= m and m <= 59 ):
            raise Exception("you entered the time incorrectly")
        return [h, m]
    
    def date(self, t):
        m = t[0]
        d = t[1]
        y = t[2]
        if len(str(y)) == 2:
            y = int("20" + str(y))
        if not( 1 <= m and m <= 12 and 1 <= d and d <= 31 ):
            raise Exception("you entered the date incorrectly")
        return [m, d, y]
    
    def hour(self, t):
        return int(t[0])
    def minute(self, t):
        return int(t[0])
    
    def day(self, t):
        return int(t[0])
    def month(self, t):
        return int(t[0])
    def year(self, t):
        return int(t[0])
    
    def pm(self,t): return "pm"
    

period_parser = Lark(_period_grammar, parser='lalr', debug=True, transformer=_PeriodTree())
period_grammar = period_parser.parse

#s = input('> ')
# print( dt(s) )

# def parse_period(period):
#     try:
#         return period_grammar(period)
#     except:
#         None

def parse_period(period):
    try:
        return period_grammar(period)
    except (UnexpectedInput, LarkError):
        raise Exception("your dates were not in the requested format")
    except Exception as e:
        raise e

if __name__ == "__main__":
    # s = "4/20/2021 6:10 am 4/20/2021 12:10 pm"
    s = input("> ")
    print(s)
    print(parse_period(s))
