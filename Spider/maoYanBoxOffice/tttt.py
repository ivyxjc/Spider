# class Aa(object):
#     def __init__(self):
#         pass
#
#
#
# class AaSon(Aa):
#     def __init__(self,name):
#         super(AaSon,self).__init__()
#         print(name)
#
#
# test=AaSon('name')


# print(f)
# f()
# from functools import wraps
#
#
# def AAA(func):
#     @wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
# @AAA
# def nowA():
#     print("2016-06-10")
#
# f=nowA
#
# f=AAA(f)
# print(f.__name__)
#
# def BBB(text):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             print("%s %s():" % (text, func.__name__))
#             return func(*args,**kwargs)
#         return wrapper
#     return decorator
#
# @BBB("ssss")
# def nowB():
#     print("2016-06-10-b")
#
# now=BBB("sss")(nowB)
# print(now.__name__)

from faker import Factory
import datetime
fake=Factory.create()
print(fake.text())
print(fake.email())
print(fake.name())
print(fake.date())
print(datetime.datetime.utcnow())