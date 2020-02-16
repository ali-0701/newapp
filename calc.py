def divide(x,y):
    if y == 0:
        return x/y
    else:
        return 0

def multiply(x,y):
    return x*y

def sum(x,y):
    return x+y

def sub(x,y):
    return x-y

def main():
    x = 10.0
    y = 5.0
    # to add
    print("%f + %f = %f" % (x, y, sum(x,y)))

    # to subtract
    print("%f - %f = %f" % (x, y, sub(x,y)))

    # to add
    print("%f * %f = %f" % (x, y, multiply(x,y)))

    # to add
    print("%f / %f = %f" % (x, y, divide(x,y)))
