# importing the module 
import random
from pytube import YouTube 
from datetime import date
import secrets
import string

class My:
    #tool number 1
    def age():
        today = date.today()
        userYear = int(input("enter your date of birth: "))
        print(f"your age is: {today.year-userYear}\n")



    # tool number 2
    def gpa():
        # list for saving 
        SubjectsAndGrades = []

        # storing values
        MultiOfGradesAndCridit = 0
        TotalCridit = 0
        TotalOfMultibly = 0

        NumberOfSubjects = int(input("enter number of subjects: "))

        for l in range(NumberOfSubjects):

            NameOfSub = str(input(f"{l+1}# Subject name: "))
            Grade = input(f"{l+1}# enter grade number or letter: ")
            Cridit = float(input(f"{l+1}# Enter Credit : "))

            match Grade.lower():

                case("a+"): Grade = 5

                case("a"): Grade = 4.75

                case("b+"): Grade = 4.5

                case("b"): Grade = 4

                case("c+"): Grade = 3.5

                case("c"): Grade = 3

                case("d+"): Grade = 2.5

                case("d"): Grade = 2

                case("f"): Grade = 1

                case _: Grade = float(Grade)

            # formula
            MultiOfGradesAndCridit = Grade * Cridit
            # ubdating 
            TotalCridit += Cridit
            TotalOfMultibly +=  MultiOfGradesAndCridit

            # to add in list
            SubjectsAndGrades.append(f"{NameOfSub} your grade in the subject is {Grade}") 
        # the second  formula
        YourGpa = TotalOfMultibly/TotalCridit



        #Acadamic standing
        print(f"\nthe total GPA is : {YourGpa}")
        print(f"\nthe total credit is : {TotalCridit}")

        if YourGpa >= 4.5: 
            print("\nYour Academic Standing is: Excellent\n")
        elif YourGpa >= 3.75:
            print("\nYour Academic Standing is: Very Good\n")
        elif YourGpa >= 2.75:
            print("\nYour Academic Standing is: Good\n")
        elif YourGpa >= 2.00:
            print("\nYour Academic Standing is: Pass\n")
        else:
            print("\nFall\n")
        

        #honor roll
        if YourGpa >= 4.75:
            print(f"\nCongrats you got First honor roll with GPA of: {YourGpa}\n")
        elif YourGpa >= 4.25:
            print(f"\nCongrats you got Second honor roll with GPA of: {YourGpa}\n")

        #subjects with their grades
        x = 1
        for i in SubjectsAndGrades:
            print(f"{x}# {i}")
            x +=1
        print("\n")




    # tool number 3 
    def Calculator():
        calc = eval(input("enter numbers and operation: "))
        print(f"the total is = {calc}\n")
            



    # tool number 4
    def dice():
        print(f"\nthe number you got from the dice is:{random.randint(1,6)}\n")



    # tool number 5
    def password():
        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation


        
        AllCharachters = letters + digits + special_chars
        leng= int(input("enter the number of the character "))

        #making normal password
        '''METHOD FOR SIMPLE PASSWORD  password= "".join(secrets.choice(AllCharachters , leng))'''


        #making strong password
        while True:
            password = ''
            for i in range(leng):
                password += ''.join(secrets.choice(AllCharachters))

            if (any(char in special_chars for char in password) and sum(char in digits for char in password)>=2):
                break

        print(f"\npassword: {password}\n")



    #tool number 6 (still doesn't work)
    def Yout():
        # where to save 
        UrPath = str(input("enter your full Path for saving"))

        # link of the video to be downloaded 
        link= str(input("enter the URl for the video"))

        try: 
            # object creation using YouTube
            # which was imported in the beginning 
            yt = YouTube(link) 
        except: 
            print("Connection Error") #to handle exception 

        yt = yt.stream.get_highest_resolution()
        # filters out all the files with "mp4" extension 
        mp4files = yt.filter('mp3') 

        #to set the name of the file
        yt.set_filename(yt.title)  

        try: 
            # downloading the video 
            yt.download() 
        except: 
            print("Some Error!") 
        print('Task Completed!')
