def read_data():
    try:

        global students_list,grades_list,courses_list
        students_list=[]
        grades_list=[]
        courses_list=[]

        students_file = open("students.txt", "a")
        students_file.close()
        students_file = open("students.txt", "r")
        for line in students_file:
            students_list.append(line.strip().split(","))
        students_file.close()
    
        grades_file = open("grade.txt", "a")
        grades_file.close()        
        grades_file = open("grade.txt", "r")
        for line in grades_file:
            grades_list.append(line.strip().split(","))
        grades_file.close()

        courses_file = open("course.txt", "a")
        courses_file.close()
        courses_file = open("course.txt", "r")
        for line in courses_file:
            courses_list.append(line.strip().split(","))  
        courses_file.close()

    except FileNotFoundError:
        print ('No such file') 
    
def Add_Student():
    try:

        ID = int(input('Enter student ID:'))
        l=True
        for student in students_list:
            if int(student[0]) == ID:
                l=False
                print('There are already a student with that ID\n')
                return Main_Menu()
        if l:       
            name = input('Enter student name:')
            mobile = int(input('Enter student mobile:'))
            students_list.append([ID, name, mobile])
            adding = open('students.txt', 'a')
            adding.write(f'\n{ID},{name},{mobile}')
            adding.close()
            return Main_Menu()

    except FileNotFoundError:
        print ('No such file')
    except ValueError:
        print ('There are a value error')
    
def Add_Course():
    try:

        course_no = input('Enter course no.:')
        l=True
        for course in courses_list:
            if course[0]==course_no:
                l=False
                print('There are already a course with that number')
                return Main_Menu()
        if l:        
            course_name = input('Enter course name:')
            credits = int(input('Enter course credits:'))
            adding = open('course.txt', 'a')
            adding.write(f'\n{course_no},{course_name},{credits}')
            courses_list.append([course_no,course_name,credits])
            adding.close()
            return Main_Menu()

    except FileNotFoundError:
        print ('No such file')
    except ValueError:
        print ('There are a value error')
    
def Add_Grade():
    try:

        studentID=input('Enter student id: ')
        l=True

        for i in students_list:
            if studentID in i[0]:
                l=False
                print(f'Student name: {i[1]}')
                courseNo=input('Enter course No: ')
                k=True

                for j in courses_list:
                    if courseNo == j[0]:
                        k=False

                        CourseGrade=input('Enter student grade:')
                        while CourseGrade!='A' and CourseGrade!='B' and CourseGrade!='C' and CourseGrade!='D' and CourseGrade!='F':
                            print('Invalid input! ')
                            CourseGrade=input('Enter student grade:')
                        grades_list.append([studentID,courseNo,CourseGrade])
                        grades_file = open("grade.txt", "a")
                        grades_file.write(f'\n{studentID},{courseNo},{CourseGrade}')
                        grades_file.close()
                        return Main_Menu()

                if k==True:
                    print('There is no course with this number')
                    return Main_Menu()
                
        if l==True:
            print('There is no student with this ID')
            return Main_Menu()

    except FileNotFoundError:
        print ('No such file')
    except ValueError:
        print ('There are a value error')

def Calculate_GPA():
    try:

        new_list=[]
        cal_credit=0
        cal_p_cret=0
        id=input("Enter student ID: ")
        c=True
        d={"A":4,"B":3,"C":2,"D":1,"F":0}

        for student in students_list:
            if student[0]==id:
                c=False
                print("Name:",student[1])

                for grade in grades_list:
                    if grade[0]==id:
    
                        for course in courses_list:
                            if grade[1]==course[0]:
                                cal_credit+=int(course[2])
                                cal_p_cret+=int(course[2])*int(d[grade[2]])
                                new_list.append([course[0],course[1],grade[2]])
        if cal_credit>0:
            print("GPA:",(format((cal_p_cret/cal_credit),".2f")))
            print("")
            for Totalcourses in new_list:
                for coure in Totalcourses:
                    print(coure,end=" ")
                print("")
            return Main_Menu() 
        else:
            print("Sorry, this id student didn't complete any cousre ")
            return Main_Menu()

        if c==True:
            print("There is no student with this ID")
            return Main_Menu()

    except ZeroDivisionError:
        print ('There are dividing by zero')
    except FileNotFoundError:
        print ('No such file')
    except ValueError:
        print ('There are a value error')

def Student_Pass():
    try:

        course=input('Enter course No:')
        l=True
        for c in courses_list:
            if c[0] == course:
                l=False
                for grade in grades_list:
                    if grade[1]==course:
                            for student in students_list:
                                if grade[2]!='F':
                                    if student[0]==grade[0]:
                                        print(student[1])

        if l==True:
            print('There is no course with this number')
            return Main_Menu()
        
        return Main_Menu()        

        if l==True:
            print('There is no course with this number')
            return Main_Menu()

    except FileNotFoundError:
        print ('No such file')

def Exit():
    exit(0)

def Main_Menu():
    try:

        print('Please select one of the following:')
        print('1- Add a new student')
        print('2- Add a new course')
        print('3- Add a new grade')
        print("4- Print a student's transcript")
        print('5- Students who pass a subject')
        print('6- Exit')
        read_data()
        choice = int(input('Your choice:'))
        if choice == 1:
            Add_Student()
        if choice == 2:
            Add_Course()
        if choice == 3:
            Add_Grade()
        if choice == 4:
            Calculate_GPA()
        if choice == 5:
            Student_Pass()
        if choice == 6:
            Exit()

    except ValueError:
        print ('There are a value error')

Main_Menu()
