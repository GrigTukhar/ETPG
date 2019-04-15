import json

def loadData(week,day):
    with open('main.json') as data_file:
        data = json.load(data_file)
    schedule = data["schedule"][week][day]
    return(schedule)

def loadPredef():
    with open('main.json') as data_file:
        predata = json.load(data_file)
    preworkouts = predata["workouts"]
    return(preworkouts)

def currDay(schedule,day,preworkouts):
    curr_work = {day: {}}
    for key in schedule:
        if (schedule[key] != -1 and "predefinedworkout" in schedule[key].keys()):
            curr_work[day][key] = preworkouts[schedule[key]["predefinedworkout"]]
        else:
            curr_work[day][key] = schedule[key]

    return curr_work

def saveWorkouts(workouts):
    file = open("current_workouts.json", "w")
    file.write(json.dumps(workouts))
    file.close()

def printWorkouts(curr_work,day):
    for key in curr_work[day]:
        if curr_work[day][key]== -1:
            print(key, ":", "no excerisize for this time of day")
        else:
            print(key, ":",curr_work[day][key])


def main():
    week = "x"
    while week !="week1" and week !="week2" and week !="week3" and week !="week4" and week !="week5":
        week = input(str("Input week (week1, week2, week 3, week 4, or week5): "))
        if week !="week1" and week !="week2" and week !="week3" and week !="week4" and week !="week5":
            print("That does not exist, try again")
        else:
            day ="x"
            while day!="day1" and day!="day2" and day!="day3" and day!="day4" and day!="day5" and day!="day6" and day!="day7":
                day = input(str("Input day (day1, day 2, day 3, day4, day5, day6, or day7): "))
                if day!="day1" and day!="day2" and day!="day3" and day!="day4" and day!="day5" and day!="day6" and day!="day7":
                    print("That does not exist, try again")
                else:
                    schedule = loadData(week,day)
                    preworkouts = loadPredef()
                    current_workout = currDay(schedule,day,preworkouts)
                    saveWorkouts(current_workout)
                    printWorkouts(current_workout,day)
main()
