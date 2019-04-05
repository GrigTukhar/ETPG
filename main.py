import json

def loadData(week,day):
    with open('main.json') as data_file:
        data = json.load(data_file)
    workouts = data["schedule"][week][day]
    return(workouts)

def currDay(workouts,day):
    curr_work = {day: {}}
    for key in workouts:
        curr_work[day][key] = workouts[key]
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
    week =input(str("Input week: "))
    day = input(str("Input day: "))
    workouts = loadData(week,day)
    current_workout = currDay(workouts,day)
    saveWorkouts(current_workout)
    printWorkouts(current_workout,day)
main()
