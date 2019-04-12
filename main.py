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
    week = input(str("Input week: "))
    day = input(str("Input day: "))
    schedule = loadData(week,day)
    preworkouts = loadPredef()
    current_workout = currDay(schedule,day,preworkouts)
    saveWorkouts(current_workout)
    printWorkouts(current_workout,day)
main()
