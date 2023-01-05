# importing the module 
import random

# tool number 1
def age():
    date = int(input("enter your date of birth: "))
    print("your age is: ", 2022-date)




# tool number 2
def gpa():
    # list for saving
    SubjectsAndGrades = []

    # storing values
    MultiOfGradesAndCridit = 0
    TotalCridit = 0
    TotalOfMultibly = 0

    NumberOfSubjects = int(input("enter number of subject: "))

    for l in range(NumberOfSubjects):

        NameOfSub = str(input("Subject name: "))
        Grade = input("enter grade number or letter: ")
        Cridit = float(input("Enter cridit : "))

        match Grade.lower():

            case("a+"): Grade = 5.0
                
            case("a"): Grade = 4.75
                
            case("b+"): Grade = 4.5
                
            case("b"): Grade = 4.0
                
            case("c+"): Grade = 3.5
                
            case("c"): Grade = 3.0
                
            case("d+"): Grade = 2.5
                
            case("d"): Grade = 2.0

            case("f"): Grade = 1.0
                
            case _: Grade = float(Grade)



        # formula
        MultiOfGradesAndCridit = Grade * Cridit
        # ubdating 
        TotalCridit += Cridit
        TotalOfMultibly +=  MultiOfGradesAndCridit

        # to add in list
        SubjectsAndGrades.append(NameOfSub), SubjectsAndGrades.append(" your grade in the subject is ") ,SubjectsAndGrades.append(Grade)
    # the second  formula
    YourGpa = TotalOfMultibly/TotalCridit



    #Acadamic standing
    print("\nthe total GPA is : ", YourGpa)
    if YourGpa >= 4.5: 
        print("\nYour Academic Standing is: Excellent")
    elif YourGpa >= 3.75:
        print("\nYour Academic Standing is: Very Good")
    elif YourGpa >= 2.75:
        print("\nYour Academic Standing is: Good")
    elif YourGpa >= 2.00:
        print("\nYour Academic Standing is: Pass")
    else:
        print("\nFall")
    

    #honor roll
    if YourGpa >= 4.75:
        print("\nCongrats you got First honor roll")
    elif YourGpa >= 4.25:
        print("\nCongrats you got Second honor roll")

    #subjects with their grades
    for i in SubjectsAndGrades:
        print(i , end=" ")






# tool number 3 
def Calculator():
    first     = float(input("enter the first number"))
    second    = float(input("enter the second number"))
    operation = input("choose one of the operation ^,+,*,-")
    if operation == '-':
        print(first-second)
    elif operation == '+':
        print(first+second)
    elif operation == '/' and second != 0:
        print(first/second)
    elif operation == '*':
        print(first*second)
    if operation == '/' and second == 0:
        print("can't devi using 0")






# tool number 4
def dice():
    print(random.randint(1,6))





# tool number 5
def password():
    upper= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower= "abcdefghijklmnopqrstuvwxyz"
    sympol= "!@#$%^&*"
    numb= "0123456789"

    cha= lower+upper+sympol+numb
    leng= int(input("enter the number of the character"))
    password= "".join(random.sample(cha,leng))

    print("password: "+ password)




# Starting
while True:
    try:    
            user = int(input("""1: Age 
2: GPA 
3: simple calculator 
4: roll a dice 
5: random password 
6: Exit
choose one of the tools: """))

            match user:
                case 1: age()

                case 2: gpa()
                
                case 3: Calculator()

                case 4: dice()   

                case 5: password()
                
                case 6: break

                case _: print("\nthe value does not exist\n")
    
    except:
        print("\nError enter numbers only")  
