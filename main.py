# input the main function to run the program
def main():
    average = get_average()
    check_average(average)

#Get the three test scores from user
def get_average():
    score1 = float(input("Enter the score for Score 1: "))
    score2 = float(input("Enter the score for Score 2: "))
    score3 = float(input("Enter the score for Score 3: "))

#Calculate the average
    average = (score1 + score2 + score3) / 3
    print("The average score is:", average)
    return average

# Check the average and display the message
def check_average(average):
    if average > 95:
        print("Congratulations! You did great!")
    elif 85 <= average <= 95:
        print("You did great, but did not reach the Top High.")
    elif 70 <= average <= 84:
        print("Good effort, but you could do better.")
    else:
        print("You need to study harder next time.")

if __name__ == "__main__":
    main()