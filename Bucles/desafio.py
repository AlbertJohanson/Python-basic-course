def tables(no_table):
    
    for i in range(10):
        if i == 5:
            break
        print(i * no_table)

if __name__ == '__main__':
    no_table = int(input("Enter the Table: "))
    tables(no_table)