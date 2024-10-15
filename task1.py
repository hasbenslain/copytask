def check_grade(grade):

    if grade >= 80 and grade <= 100:
        return "you did the best"
    elif grade >= 70 and grade <= 79:
        return "keep it up"
    elif grade >= 60 and grade <= 69:
        return"you pass but there's room for improvement"
    else:
        return "better luck next time"
    
grade = int(input("enter a grade: "))
print(check_grade(grade))
    
                


