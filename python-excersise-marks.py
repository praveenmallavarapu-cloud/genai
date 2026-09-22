#CBSE subjects

subjects = ["Maths", "Science", "English", "Social Studies", "Hindi"]
Maths = int(input("Enter marks for Maths: "))
Science = int(input("Enter marks for Science: "))
English = int(input("Enter marks for English: "))
Social_Studies = int(input("Enter marks for Social Studies: "))
Hindi = int(input("Enter marks for Hindi: "))

total_marks = Maths + Science + English + Social_Studies + Hindi 
average_marks = total_marks / len(subjects)

print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

if average_marks >= 85:
    print("Grade: A+")
elif average_marks >= 80:
    print("Grade: A")
elif average_marks >= 70:
    print("Grade: B")
else:
    print("Grade: C")