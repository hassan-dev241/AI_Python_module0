students =[
{"name":"Lara","age":23,"track":"AI","hours_studied":40,"scores":[85,90,78]},
{"name":"Omar","age":31,"track":"Data","hours_studied":12,"scores":[60,55,70]},
{"name":"Rim","age":27,"track":"AI","hours_studied":55,"scores":[95,88,92]},
{"name":"Karim","age":19,"track":"Web","hours_studied":8,"scores":[50,65,40]},
{"name":"Nour","age":25,"track":"AI","hours_studied":30,"scores":[75,80,85]},
{"name":"Sami","age":35,"track":"Data","hours_studied":48,"scores":[88,91,79]},
]


#part 1

#1.
print(students[0]['name'])
print(students[-1]['name'])
###########################
#2.
print(students[2]['scores'])
###########################
#3.
for student in students:
    print(student['name'] + " is " + str(student['age']) +  " years old and studies " + student['track'])
#########################################################################################################
#part 2

#4.
AI_Track = []
for student in students:
    if(student["track"] == "AI"):
    
        AI_Track.append(student["name"])
print(AI_Track)
#5.
AI_Track2 = [student["name"] for student in students if student["track"] == "AI"]
print(AI_Track2)
#6.
hours_studied_Greather_than30 = []
for student in students:
    if student["hours_studied"] > 30:
        hours_studied_Greather_than30.append(student["name"])
        
print(hours_studied_Greather_than30)
#7.
student24_AI = []

for student in students:
    if(student["age"] > 24 and student["track"] == "AI"):
        student24_AI.append(student["name"])
        
print(student24_AI)
##########################################################

#part 3
#8.
total = 0
for student in students:
    total += student["age"]
avg = total / len(students)
print(round(avg, 2))
#9.
total = 0
for student in students:
    total += student["hours_studied"]  
print(total)
#10.
max_hours = 0
student_most_hours = ""
for student in students:
    if student["hours_studied"] > max_hours:
        max_hours = student["hours_studied"]
        student_most_hours = student["name"]
print("the student who studied the most hours : " + student_most_hours + " and her hours studies are: " +  str(max_hours))
#11.       
for student in students:
    total = 0
    for score in student["scores"]:
        total += score
    avg = total / len(student["scores"])
    print(student["name"], (round(avg, 1)))
########################################### 
#part 4
#12.
def calculate_average(scores):
    total = 0
    for score in student["scores"]:
        total += score
    return total / len(student["scores"])      
model_data = [
    {
    "name": student["name"], 
    "average_score": calculate_average(student["scores"]),
    } 
    for student in students
    ]
print(model_data)
#13.      
track_counts = {}

for student in students:
    track = student["track"]
    if track in track_counts:
        track_counts[track] += 1
    else:
        track_counts[track] = 1
        
print(track_counts)
#14.
# A set is the right tool because it automatically stores only unique tracks,
# while a list would allow duplicate track names.
tracks = set()
for student in students:
    track = student["track"]
    tracks.add(track)
print(tracks) 
#############################################################
#part 5
#15.
def filter_by_track(students, track):
    result = []
    for student in students:
        if student["track"] == track:
            result.append(student["name"])
    return result
            
ai_students = filter_by_track(students, "AI")
data_students = filter_by_track(students, "Data")

print("AI students:")
print(ai_students)

print("Data students:")
print(data_students)
#16.
def average_score(student):
    total = 0
    for score in student["scores"]:
        total += score

    return total / len(student["scores"])
#17.
def top_student(students):
    highest_average = 0
    top_name = ""
    for student in students:
            average = average_score(student)
            if average > highest_average:
                highest_average = average
                top_name = student["name"]
    return top_name

result = top_student(students)

print(result) 
#18.
def summary(students):
    Total_students = len(students)
    Total_age = 0
    tracks = set()
    
    for student in students: 
        
        Total_age += student["age"]
        
        average_age = Total_age / Total_students
        
        track = student["track"]
        tracks.add(track)
        
    return {
        "Total_students" : Total_students,
        "average_age" : average_age,
        "tracks" : tracks
    }

result = summary(students)
print(result)
############################################################
##Bonus##############################
def report(students, min_hours):
    result = []

    for student in students:

        if student["hours_studied"] >= min_hours:

            total_score = 0

            for score in student["scores"]:
                total_score += score

            average_score = round(
                total_score / len(student["scores"]),
                2
            )

            result.append({
                "name": student["name"],
                "average_score": average_score
            })

    result.sort(
        key=lambda student: student["average_score"],
        reverse=True
    )

    return result

result = report(students, 30)

print(result)
################################################################################c    c