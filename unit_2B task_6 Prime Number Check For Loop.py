n = int(input("Enter a number (1 to 100): "))

if n <= 1 or n > 100:
    print("Enter a number between 1 and 100")
else:
    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print("It is a prime number")
    else:
        print("It is not a prime number")
        