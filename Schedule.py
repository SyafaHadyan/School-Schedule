Day = "Saturday"

Monday = ["PPkn", "Bahasa Indonesia", "Matematika Wajib", "Kimia"]
Tuesday = ["Matematika Minat", "Bahasa Inggris Minat", "Biologi", "Kimia", "Sejarah"]
Wednesday = ["Agama Islam", "PJOK", "Matematika Wajib", "Bahasa Inggris Minat"]
Thursday = ["Fisika", "Bahasa Inggris Wajib", "Matematika Minat", "Prakarya", "Seni Budaya"]
Friday = ["Fisika", "Bahasa Indonesia", "Biologi"]
Saturday = "It's Weekend"
Sunday = "It's Weekend"

if Day == "Monday" or Day == "Tuesday" or Day == "Wednesday" or Day == "Thursday" or Day == "Friday":
    print("Today's School Schedule:")

elif Day == "Saturday" or Day == "Sunday":
    print("No Schedule for today")

if Day == "Monday":
    for mon in Monday:
        print(mon)

elif Day == "Tuesday":
    for tue in Tuesday:
        print(tue)

elif Day == "Wednesday":
    for wed in Wednesday:
        print(wed)

elif Day == "Thursday":
    for thu in Thursday:
        print(thu)

elif Day == "Friday":
    for fri in Friday:
        print(fri)

elif Day == "Saturday":
    print(Saturday)

elif Day == "Sunday":
    print(Sunday)

else:
    print("Invalid Day, please insert a valid day and use sentence case")