from xml.dom import UserDataHandler
from datetime import date

def user_details():

    isNotValid = True
    while isNotValid == True:
        try:
            first_name = input("Insert your first name\n")
        except EOFError:
            return
        first_name = first_name + 'O' if len(first_name) < 3 else first_name
        if any(char.isdigit() for char in first_name):
             print("Invalid first name")
        else:
             isNotValid = False
   
    isNotValid = True
    while isNotValid == True:
        try:
            last_name = input("Insert your last name\n")
        except EOFError:
            return
        last_name = last_name + 'O' if len(last_name) < 3 else last_name
        if any(char.isdigit() for char in last_name):
             print("Invalid last name")
        else:
             isNotValid = False
   
    isNotValid = True
    while isNotValid == True:
        try:
            cohort = int(input("Insert your cohort\n"))
        except EOFError:
            return
        todays_date = date.today()
        current_year = todays_date.year
        if cohort < current_year:
             print("Invalid cohort")
        else:
             isNotValid = False


    camp = input("Insert the campus you will be attending in")
    # print("***********" + str(camp) + "*********")
    final_campus = user_campus(str(camp).lower())
    user_name = create_user_name(first_name, last_name, cohort, final_campus)
    print(user_name)
    return
    

def create_user_name(first_name, last_name, cohort, final_campus):
       
    username = first_name[-3:] + last_name[0:3] + user_campus(final_campus) + str(cohort)
    return username
    
    """
    Create and return a valid username
    """


def user_campus(campus_name):
   
    switcher={
                'johannesburg':'JHB',
                'cape town':'CPT',
                "durban":"DBN",
                'phokeng':'PHO'
             }
    return switcher.get(str(campus_name.strip()),"Invalid compus name")

    
    """
    Return valid campus abbreviations
    """


if __name__ == '__main__':
    user_details()
    