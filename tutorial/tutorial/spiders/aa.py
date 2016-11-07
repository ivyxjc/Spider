# import math
#
# def answer(area):
#     # your code here
#     res=[]
#     if(area==0):
#         return res
#
#     tmp_area = area
#
#     while(True):
#         sqrt = math.sqrt(tmp_area)
#         sqrt = int(sqrt)
#         t=sqrt**2
#         tmp_area -= t
#         res.append(t)
#         if(tmp_area == 0):
#             break
#
#     return res


# def answer(x, y):
#     # your code here
#
#     res=(y**2-3*y+2+x**2-x)/2+y*x
#     res=str(int(res))
#     return res
#
# print(answer(5,10))



def answer(total_lambs):
    # your code here

    fib_i=1
    fib_sum=0
    while(True):
        fib_sum+=fib(fib_i)
        if(fib_sum>total_lambs):
            fib_i-=1
            break
        fib_i+=1


    square_i=1
    square_sum=0
    while(True):
        square_sum+=2**(square_i-1)
        if(square_sum>total_lambs):
            square_i-=1
            break
        square_i+=1

    return fib_i-square_i

def fib(n):
    x, y = 0, 1
    while (n):
        x, y, n = y, x + y, n - 1
    return x

print(answer(142))





