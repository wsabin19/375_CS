#this is a program that converts Meters per Second(m/s) to Miles per hour(mph)
def main() :

    print("Covert M/s to MPH")
    meters = eval(input("How fast?(m/s)"))
    if meters < 0 :
        print("invalid input")
    else:
        mph = meters*2.23694
        print("mph is:")
        print(mph)
main()
