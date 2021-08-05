from math import pi, pow
import datetime

x = datetime.datetime.now()

print(x.strftime("Hello, today is: %A, %d %B"))


#First Text ----------------------------------------------------------------------------
print("Welcome to Arian's second project, V1 Beta!!!")
radius = float(input("please enter value here (circle radius): "))
#calc input ----------------------------------------------------------------------------
area = pow(radius, 2) * pi
prm = (radius * 2) * pi
#answer ;)  ----------------------------------------------------------------------------
print("for radius {}, (circle area)={}, and (perimeter)={}.".format(radius,
                                                                    area,
                                                                    prm))
