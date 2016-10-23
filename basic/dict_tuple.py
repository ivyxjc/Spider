import math
import  copy
a=(1,2,3)
b=(1,[2,3])
aa={"ass":"bb",
    a:"aa",
    "sss":"cc"}

for key in aa:
    print(key)

def func(x:int,y:int):
    print(x+y)


func(3.4,4.5)

print("the anser is ",2*2,"asfdf",9)
x="asdfsd"
y="zzzasdf"
print ((x,y))
print(oct(438))
print(0o666)

print("---------------")
class C(object):
    def __init__(self,a):
        self.a=a;
    def getA(self):
        print(self.a)

class D(C):
    def __init(self,a):
        super().__init(a)


ddd=D(8)
print(ddd.getA())

print("------------")

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("arguments are wrong")
    if x>=0:
        return x
    else:
        return -x

print(my_abs(44))

print("----------")
def move(x,y,step,angle=0):
    nx=x+step+math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny
print(move(1,3,4))
for i in move(1,2,3):
    print(i)

#默认参数必须指向不变对象
#下面的程序会有意想不到的结果发生
def add_some(L=[]):
    if L is None:
        L=[]
    L.append("some")
    return L

print(add_some())
print(add_some())



def replace_punctuation(str):
    origint_length=len(str)
    count=1
    res=copy.deepcopy(str)
    str_copy=copy.deepcopy(str)
    for i in range(origint_length):
        if(str[i]=='\''):
            tmp=copy.deepcopy(res[i+count:])
            res=res[:i+count]
            print("++++"+res)
            res+='\''
            print("::::"+res)
            res+=tmp
            count+=1
    return res

print("---------")
print(replace_punctuation("aa''assa's'''ss"))
