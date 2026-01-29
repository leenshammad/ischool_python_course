while True:
    grade_scale = int(input("enter grade 0-100: ")) 
    if grade_scale>100:
        print("wrong grade")
    elif grade_scale>=90:
        print("excellant you get A !")
    elif grade_scale>=80:
        print("very good  you get B!")
    elif grade_scale>=70:
        print("good job  you get C!")
    elif grade_scale>=60:
        print(" good you get D!")
    elif grade_scale>=0:
        print("study hard you get F!")
    else:
        print("wrong grade")