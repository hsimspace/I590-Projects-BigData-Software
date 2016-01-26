## building the fizzbuzz function

def fizzbuzz(input_num):
    for i in range(1,input_num):
        if((i%2 == 0) and (i%3 == 0)):
            print "fizzbuzz"
        elif(i%2 == 0):
            print "fizz"
        elif(i%3 == 0):
            print "buzz"
        else:
            print i

num = int(raw_input("Pleae enter a number: "))

fizzbuzz(num)
