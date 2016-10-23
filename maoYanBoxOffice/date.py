# class date(object):
#     __year=0
#     __month=0
#     __day=0
#     month_days={
#         1:31,
#         2:28,
#         3:31,
#         4:30,
#         5:31,
#         6:30,
#         7:31,
#         8:31,
#         9:30,
#         10:31,
#         11:30,
#         12:31
#     }
#     def __init__(self,year,month,day):
#         self.__year=year
#         self.__month=month
#         self.__day=day
#
#
#     def get_date(self,days_before):
#         year=self.__year
#         month=self.__month
#         day=self.__day
#
#         for i  in range(0,days_before):
#             day-=1
#             if()

month_days={
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

def get_previous_date(year,month,day):
    day-=1
    if(day<=0):
        month-=1
        if(month<=0):
            year-=1
            month=12
            day=31
        else:
            if(is_year_leap(year)) and month==2:
                day=29
            else:
                day=month_days[month]



    return [year,month,day]

def is_year_leap(year):
    if(year%100==0):
        return year%400==0
    else:
        return year%4==0

