import termcolor
import sys

class Logging:
    flag = True

    @staticmethod
    def error(msg):
        if Logging.flag == True:
            print("".join(  [ termcolor.colored("ERROR", "red"), ": ", termcolor.colored(msg, "white") ] ))
    @staticmethod
    def warn(msg):
        if Logging.flag == True:
            print("".join(  [ termcolor.colored("WARN", "yellow"), ": ", termcolor.colored(msg, "white") ] ))
    @staticmethod
    def info(msg):
        # attrs=['reverse', 'blink']
            print("".join(  [ termcolor.colored("INFO", "magenta"), ": ", termcolor.colored(msg, "white") ] ))
    @staticmethod
    def debug(msg):
        if Logging.flag == True:
            print("".join(  [ termcolor.colored("DEBUG", "magenta"), ": ", termcolor.colored(msg, "white") ] ))
    @staticmethod
    def success(msg):
        if Logging.flag == True:
            print("".join(  [ termcolor.colored("SUCCES", "green"), ": ", termcolor.colored(msg, "white") ] ))

    def info_important(msg):
        if Logging.flag == True:
            origin=sys.stdout
            with open("logging.txt",'w') as f:
                sys.stdout=f
                print(msg)
                sys.stdout =origin



class LoginPasswordError(Exception):
    def __init__(self, message):
        if type(message) != type("") or message == "": self.message = u"帐号密码错误"
        else: self.message = message
        Logging.error(self.message)

class NetworkError(Exception):
    def __init__(self, message):
        if type(message) != type("") or message == "": self.message = u"网络异常"
        else: self.message = message
        Logging.error(self.message)

class AccountError(Exception):
    def __init__(self, message):
        if type(message) != type("") or message == "": self.message = u"帐号类型错误"
        else: self.message = message
        Logging.error(self.message)


class ParseError(Exception):
    def __init__(self, message):
        if type(message) != type("") or message == "": self.message = u"未解析出结果"
        else: self.message = message
        Logging.error(self.message)