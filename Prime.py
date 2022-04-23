# Function to check whether a number is prime or not
def prime_check(num):
    # Checking that given number is more than 1
    if num > 1:
        # Iterating over the given number with for loop
        for j in range(2, int(num / 2) + 1):
            # If the given number is divisible or not
            if (num % j) == 0:
                print(num, "is not a prime number")
                break
                # Else it is a prime number
        else:
            print(num, "is a prime number")
            # If the given number is 1
    else:
        print(num, "is not a prime number")
    # Taking an input number from the user


num = int(input("Enter an input number:"))
prime_check(num)
