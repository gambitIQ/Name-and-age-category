# CS 110A Zamambo Mkhize Names_and_Age Categories Program

def names_and_age():
    name_1 = input('\nPlease enter the name of one person: ')
    age_1 = int(input(f"Please enter {name_1}'s age: "))

    name_2 = input('Please enter the name of another person: ')
    age_2 = int(input(f"Please enter {name_2}'s age: "))

#Check of both people are between 18 and 64
    if (18 <= age_1 <= 64) and (18 <= age_2 <= 64):
        print("Both people are between 18 and 64")
    elif (18 <= age_1 <= 64) and not (18 <= age_2 <= 64):
        print(f"{name_1} is between 18 and 64, but {name_2} is not.")
    elif not (18 <= age_1 <= 64) and (18 <= age_2 <= 64):
        print(f"{name_2} is between 18 and 64, but {name_1} is not.")
    else:
        print("Neither person is between 18 and 64.")
  
 
for i in range(3):
    names_and_age()
  
'''
  Sample Output1
Please enter the name of one person: Mambo
Please enter Mambo's age: 30
Please enter the name of another person: Havier
Please enter Havier's age: 35
Both people are between 18 and 64

    Sample Output2
Please enter the name of one person: Ulo
Please enter Ulo's age: 66
Please enter the name of another person: Apple
Please enter Apple's age: 19
Apple is between 18 and 64, but Ulo is not.
    
    Sample Output3
Please enter the name of one person: Khothi
Please enter Khothi's age: 15
Please enter the name of another person: Khotso
Please enter Khotso's age: 9
Neither person is between 18 and 64.
'''

