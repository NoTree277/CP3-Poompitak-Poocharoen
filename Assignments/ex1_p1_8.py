# 1
FEET_IN_MILE = 5280
miles = 13
feet = FEET_IN_MILE * miles
print(feet)
# 2
hours = 7
minutes = 21
seconds = 37
total_in_sec = (hours*60*60)+(minutes*60)+seconds
print(total_in_sec)
# 3
width = 4
height = 7
length = 2*width + 2*height
print(length)
# 4
radius = 8
circle_area = 3.14*(8**2)
print(circle_area)
# 5
present_value = 1000
annual_rate = 7
years = 10
Future_value = present_value*(1+0.01*7)*years
print(Future_value)
# 6
a0 = 2
b0 = 2
a1 = 5
b1 = 6
distance = ((a1-a0)*2+(b1-b0)*2)**0.5
print(distance)
# 7
x0 = 1
y0 = 1
x1 = 4
y1 = 1
x2 = 4
y2 = 5
a = 3
b = 4
c = ((x2-x0)*2+(y2-y0)*2)**0.5
s = 0.5*(a+b+c)
triangle_area =(s*(s-a)*(s-b)*(s-c))**0.5
print(triangle_area)
# 8
user_want = int(input("How many cups coffee you need:"))
water = 200*user_want
milk = 50*user_want
coffee = 15*user_want
print(water,"ml of water")
print(milk,"ml of milk")
print(coffee,"g of coffee beans")