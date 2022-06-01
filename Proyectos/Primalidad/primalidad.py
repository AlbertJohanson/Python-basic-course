def is_prime(n):
    counter = 0

    for i in range(1, n + 1):
        if i == 1 or i == n:
            continue
        if n % i == 0:
            counter += 1

    if counter == 0:
        return True 
    else:
        return False

def run():
    number = int(input("Enter the number: "))

    if is_prime(number):
        print("The number is prime")
    else:
        print("The number is not prime")


if __name__ == "__main__":
    run()