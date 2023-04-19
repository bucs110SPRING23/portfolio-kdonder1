import turtle

# class == type
# use 'class' for user-defined types
# 'complex-type'

# class data" instance variables

class Num:
    def _init(self, n) -> None:
        self.data = n # instance variables for Num type objects
        self.x = "string"

    # double under
    # no parameters other 'self'
    # must return a string
    def __str__(self):
        obj_str = f"The number is: {self.n}"
        return obj_str
    # NO PRINTING

    def __add__(self, num)
        self.data = self.data + num

    def __next__():

    def __iter__():
        

    # object functions are called methods
    # using self as the first parameter makes it a method
    def addone(self):
        self.data += 1
        # by using self.var i change the scope of the data to the object, not the method (function)
        self.val = "This is a value"


    def printval(self):
        print(self.val)

    
class Foo:
    # def __init__(self, x, y, z, a, b, c)
    #     self.x = x
    #     self.y = y
    #     self.... # rest of parameters
    def __init__(self, **kwargs) -> None:
        print(kwargs)

def main() -> None:
    mynum = Num(7)
    mynum2 = Num(9)
    # mynum3 = {'data':7, "x": "string"}

    print(mynum.data)
    print(mynum2.data)
    # print(mynum3['data'])
    # print(mynum.__dict__)

    mynum.addone() # objects from a class are called instances of the class
    print(mynum.data)
    mynum2.addone()
    print(mynum2.data)





    dictionary = {'x':1, 'y':2, 'z':3}
    foo = Foo(**dictionary) # x = 1, y = 2, z = 3

    # print(mynum.data)
    # print(mynum2.data)

    # t = turtle.Turtle()
    # t.forward(56)

    # mylist = [] # list()
    # # mylist.forward() # error
    # mylist.append()
    # index = 0
    # mylist.pop(index)

    mystr = "Hello"

    length = len(mystr)
    list_length = len([1,2,3])

    # call a method on an object
    upper_str = mystr.upper()
    split_str = mystr.split("ll")
    mylist.upper() #Error




    num = 5
    print(f"The number is: {num}")
    mynewnum = Num(5)
    print(f"The number is: {mynewnum}")

    print(num) # num.__str__()
    str(mynewnum)
    mynewnum + 6

main()