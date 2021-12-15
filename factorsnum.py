#python program to find the factor of a number
#this function computers the factor of the arguments passed
def print_factor(x):
    print("the factor if ",x,"are:")
    for i in range(1,x+1):
        if x % i==0:
            print(i)
            num=320
            print_factors(num)
