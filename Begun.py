#importing the modules 
from  AllFun import My

print("****************************************************************************welcome****************************************************************************\n")
# Starting UI
while True:
    try:    
            user = int(input("""1: Age 
2: GPA 
3: simple calculator 
4: roll a dice 
5: random password 
6:Youtube (Not work yet)
7: Exit
choose one of the tools: """))
#switch case for getting into functions
            match user:
                case 1: My.age()

                case 2: My.gpa()

                case 3: My.Calculator()

                case 4: My.dice()   

                case 5: My.password()

                case 6: My.Yout()

                case 7: break
                #defult case
                case _: print("\nthe value does not exist\n")

    except:
        print("\nError enter numbers only")


print("\n****************************************************************************Bye Bye****************************************************************************")
