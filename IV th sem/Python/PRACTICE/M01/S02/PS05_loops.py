'''
count=5
while count>0:
    print("hello world")
    count-=1

x,y=map(int,input("Enter two numbers: ").split())
for i in range(x,y+1):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
'''
for i in range(1,5,1):
    print("hello world")

