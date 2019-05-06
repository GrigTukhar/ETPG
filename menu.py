
import athlete
import coach
import predefined

choices = ("athlete", "coach", "predefined", "exit")

def main():
    choice = "x"
    print("ETPG® | The training schedule program for any endurance trainer and athlete")
    while (choice not in  choices) or choice !="exit":
        choice = str(input("General Menu | choose any of the following options (" + (", ").join(choices) + "): "))
        if (choice not in choices):
            print("Invalid input, try again")
        elif (choice == "athlete"):
            athlete.main()
        elif (choice == "coach"):
            coach.main()
        elif (choice == "predefined"):
            predefined.main()
main()
