import datetime
now = datetime.datetime.now()
Day = now.strftime("%A")

Monday = ["PPkn", "Bahasa Indonesia", "Matematika Wajib", "Kimia"]
Tuesday = ["Matematika Minat", "Bahasa Inggris Minat", "Biologi", "Kimia", "Sejarah"]
Wednesday = ["Agama Islam", "PJOK", "Matematika Wajib", "Bahasa Inggris Minat"]
Thursday = ["Fisika", "Bahasa Inggris Wajib", "Matematika Minat", "Prakarya", "Seni Budaya"]
Friday = ["Fisika", "Bahasa Indonesia", "Biologi"]
Saturday = "Enjoy the weekend!"
Sunday = "Tomorrow is monday!"

if Day == "Monday" or Day == "Tuesday" or Day == "Wednesday" or Day == "Thursday" or Day == "Friday":
    print("School schedule for" + " " + Day + ":")

elif Day == "Saturday" or Day == "Sunday":
    print("No school schedule for" + " " + Day)

if Day == "Monday":
    Schedule = len(Monday)
    print(f"{Schedule}" + " " + "Schedules")
    for mon in Monday:
        print(mon)

elif Day == "Tuesday":
    Schedule = len(Tuesday)
    print(f"{Schedule}" + " " + "Schedules")
    for tue in Tuesday:
        print(tue)

elif Day == "Wednesday":
    Schedule = len(Wednesday)
    print(f"{Schedule}" + " " + "Schedules")
    for wed in Wednesday:
        print(wed)

elif Day == "Thursday":
    Schedule = len(Thursday)
    print(f"{Schedule}" + " " + "Schedules")
    for thu in Thursday:
        print(thu)

elif Day == "Friday":
    Schedule = len(Friday)
    print(f"{Schedule}" + " " + "Schedules")
    for fri in Friday:
        print(fri)

elif Day == "Saturday":
    print(Saturday)

elif Day == "Sunday":
    Schedule = len(Monday)
    print(Sunday)
    print(f"{Schedule}" + " " + "Schedules tomorrow")


else:
    print("Invalid day value, please insert a valid day")