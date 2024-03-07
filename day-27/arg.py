#*args
#يحول المتغيرات لتيبل
def sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
#print(sum(1,2,3))

#**kwargs
def cal(n ,**kwargs):
    #print(kwargs)
    n += kwargs["add"]
    n *= kwargs["mulitply"]
    return n

#print(cal(2, add = 3, mulitply = 5))

class car:
    def __init__(self, **kw):
        #get() عشان لو لم يتم تمرير متغيرات ما يطلع ايرور
        self.make = kw.get("make")
        self.model = kw.get("model")
        #print(kw)
my_car = car(make="Ford", model="2018")
#print(my_car.model)
