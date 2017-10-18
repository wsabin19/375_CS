#This program calculates ones average with the input of scores
#Average or Mean = the sum of the inputs (total) / the number of inputs (denomonator)
def main():
    total = 0
    denominator = 0
    score = input("Enter Score")
    while score !="":
        total = total + eval (score)
        denominator = denominator + 1
        score = input("Enter Score (Press enter to quit)")
    average = total / denominator
    print (average)

main()
