# File: chaos.py
# A Simple program illustrating chaotic behavior

def main():

    print("This program illustrates a chaotic function")
    y = eval(input("Enter the number of loops"))
    x = eval(input("Enter a number between 0 and 1:"))
    for i in range(y):
        x = 3.9 * x * (1-x)
        print(x)

main()
