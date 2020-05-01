import math

def fastexp(base, a):
    counter = 0
    output = 1
    while a > 0:
        if a%2==1:
            output *= base
            counter += 1
        base *= base
        counter +=1
        a = math.floor(a/2)
    print("Fast method:", counter, "steps")
    return output

def normalexp(base,a):
    counter = 0
    output = 1
    for i in range(a):
        output *= base
        counter += 1
    print("Normal method:", counter, "steps")
    return output

input1 = int(input("Basis: "))
input2 = int(input("Exponent: "))
print("")
print("Result:", fastexp(input1, input2))
print("--------------------------------")
print("Result:", normalexp(input1, input2))
