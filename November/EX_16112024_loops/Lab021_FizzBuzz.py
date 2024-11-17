# code to print FIZZ if number is multiple of 3 print BUZZ id number is multiple of 5 and print FIZZBUZZ is number is not multiple of 3 or 5 .

for a in range(1,100):
    if a%3 == 0:
        print("FIZZ")
    elif a%5 == 0:
        print("BUZZ")
    else:
        print("FIZZBUZZ")