num_of_labs= int(input("Enter the number of labs completed:"))
num_of_quizzes= int(input("Enter the number of labs completed:"))
ass_1= float(input("Enter grade for assignment 1:"))
ass_2= float(input("Enter grade for assignment 2:"))
ass_3= float(input("Enter grade for assignment 3:"))
ass_4= float(input("Enter grade for assignement 4:"))
mid_grade1= float(input("Enter grade for midterm 1:"))
mid_grade2= float(input("Enter grade for midterm 2:"))
final_grade= float(input("Enter grade for final exam:"))
mid_final_prep= float(input("Enter grade for midterm and final prep:"))

if (num_of_labs >=6):
    labs_weight=20
else:
    labs_weight=((num_of_labs/6)*20)
if (num_of_quizzes>=6):
    quiz_weight=15
else:
    quiz_weight=((num_of_labs/6)*15)
ass_weight=(((ass_1+ass_2+ass_3+ass_4)/4)*0.16)    
mid_weight= (((mid_grade1 + mid_grade2)/2)*0.25)
final_weight=(final_grade*0.18)
mid_final_prep_weight=(mid_final_prep*0.06)
End_grade= labs_weight + quiz_weight + mid_weight + final_weight + mid_final_prep_weight + ass_weight
print("Your grade is:" + str(int(round(End_grade,0))))
