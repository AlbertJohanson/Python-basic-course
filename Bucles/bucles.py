def run():
    number = int(input("Enter a number: "))
    potencias = 1;

    while potencias <= 10:
        print(number, "^", potencias, "=", number ** potencias)
        potencias += 1



if __name__ == '__main__':
    run()