import calendar
import datetime
import time


def str_to_datetime(datetime_str, pattern='%Y-%m-%d'):
    """
    返回datetime_str对应datetime类型对象
    :param datetime_str: 'YYYYMMDD'格式字符串日期
    :param pattern: 日期格式化类型 '%Y-%m-%d'
    :return: 对应的datetime类型的对象
    """
    datetime_obj = datetime.datetime.strptime(datetime_str, pattern)
    return datetime_obj


def datetime_to_str(datetime_obj, pattern="%Y-%m-%d"):
    """
    返回datetime对象对应的指定pattern的日期字符串
    :param datetime_obj: datetime对象
    :param pattern: 日期格式化类型 '%Y-%m-%d %H:%M:%S'
    :return: 时间对应的字符串
    """
    datetime_str = datetime_obj.strftime(pattern)
    return datetime_str


def datetime_day_modify(datetime_obj, days=0, return_type="str", pattern="%Y-%m-%d"):
    """
    获取给定的datetime对象往前或者往后推days天数得到的datetime对象或者字符串类型
    :param datetime_obj: datetime对象
    :param days: 要往前或者往后推的天数
    :param return_type: 返回的类型，str或者datetime
    :param pattern: 指定的日期字符串的格式
    :return:
    """
    timedelta = datetime.timedelta(days=days)
    res = datetime_obj + timedelta
    if return_type == "datetime":
        return res
    res = datetime_to_str(res, pattern)
    return res


def datetime_str_day_modify(datetime_str, days=0, return_type="str", datetime_pattern='%Y-%m-%d', pattern="%Y-%m-%d"):
    """
    获取给定的日期字符串往前或者往后推days天数得到的datetime对象或者字符串类型
    :param datetime_str: 日期字符串
    :param days: 要往前或者往后推的天数
    :param return_type: 返回的类型，str或者datetime
    :param datetime_pattern: datetime_str对应的格式
    :param pattern 返回字符串时的指定格式
    :return:
    """
    datetime_obj = datetime.datetime.strptime(datetime_str, datetime_pattern)
    timedelta = datetime.timedelta(days=days)
    res = datetime_obj + timedelta
    if return_type == "datetime":
        return res
    res = res.strftime(pattern)
    return res


def datetime_month_modify(datetime_str, n, pattern="%Y-%m-%d"):
    """
    根据指定日期的月份获取往前或往后的日
    :param datetime_str: 输入的日期字符
    :param n:   往前|或往后推几个月   n>0,往前推几个月，n小于0,往后推几个月
    :param pattern: 输入的日期格式字符串的标准格式
    :return:
    """
    date = datetime.datetime.strptime(datetime_str, pattern)
    if n == 0:
        return datetime_str
    month = date.month
    year = date.year
    day = date.day
    for i in range(abs(n)):
        if n > 0:
            if month == 12:
                year += 1
                month = 1
            else:
                month += 1
        if n < 0:
            if month == 1:
                year -= 1
                month = 12
            else:
                month -= 1
    month_range = calendar.monthrange(year, month)
    days = month_range[1]
    if day >= days:
        day = days
    return datetime.date(year, month, day).strftime(pattern)


def current_date(pattern="%Y-%m-%d %H:%M:%S"):
    """
    获取当前日期
    :param: pattern:指定获取日期的格式
    :return: 字符串 "20200615 14:57:23"
    """
    return time.strftime(pattern, time.localtime(time.time()))


def past_date(pattern="%Y-%m-%d %H:%M:%S", delta=1):
    '''
    获取当天日期的前或后delta天的日期
    @param pattern: 指定日期格式
    @param delta: 整数，delta>0往前推，delta<0往后推
    @return:
    '''
    past_day = datetime.datetime.today() + datetime.timedelta(delta)
    past_day_format = past_day.strftime(pattern)
    return past_day_format


def gen_dates(b_date, days):
    day = datetime.timedelta(days=1)
    for i in range(days):
        yield b_date + day * i


def get_date_list(start="", end="", datetime_pattern="%Y-%m-%d", pattern="%Y-%m-%d"):
    """
    获取日期列表
    :param start: 开始日期(str, eg:"2021-01-12")
    :param end: 结束日期(str, eg:"2021-01-19")
    :param datetime_pattern: 开始和结束日期的格式
    :param pattern: 结果中的日期格式，默认"%Y-%m-%d"
    :return: 字符串列表，包含start和end
    """
    try:
        start = datetime.datetime.strptime(start, datetime_pattern)
        end = datetime.datetime.strptime(end, datetime_pattern)
    except Exception as e:
        return []
    end = end + datetime.timedelta(days=1)
    data = []
    for date in gen_dates(start, (end - start).days):
        data.append(date.strftime(format=pattern))
    return data
