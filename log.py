import time

class  Log(object):

    @classmethod
    def __get_localtime(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    @classmethod
    def log_str(self,*args):
        res=self.__get_localtime()
        for i in args:
            res+="  "+str(i)
        return res



