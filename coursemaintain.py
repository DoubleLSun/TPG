#Module name  : coursemaintain.py
#created by   : Yew Fu Li, Tan Wen Zhe
#created date : 25/2/2023
#import       : os, json, time, generalcode

import os,json,time,generalcode as g
# Open the courses.json file and load its contents into a variable called "data"
data=g.readfile("courses.json")
def display_courses():

# Print a table header    
    print('-'*50)
    print(f"{'Code':<15}{'Code Description':<30}")
    print('-'*50)
# Loop through each course in the "Courses" list of the "data" dictionary and print its code and description
    for course in data["Courses"]:
        code_desc = course["COURSES"].split("|")
        code_col = code_desc[0]
        desc_col = code_desc[1]
        print(code_col+"       "+desc_col)


def main():
    loop3=True
    while loop3:
# Clear the screen using the 'cls' command on Windows.
        os.system('cls')
# Call a function named 'display_courses()' to display a list of available courses.
        display_courses()
# Request that the user input one of four options: add, update, delete, or exit.
        opt=input('<A>dd  <U>pdate <D>elete <E>xit').upper()
        if opt=='A':
# If the user selects "add", set the "step" variable to 3 and call the "maintain" function
            step=3
            maintain(step,opt)
        elif opt in ['U','D']:
# If the user selects "update" or "delete", set the "step" variable to 1 and call the "maintain" function
            step=1
            maintain(step,opt)
        elif opt=='E':
# If the user selects "exit", set the "loop3" variable to False to exit the loop
            loop3=False
        else:
# If the user inputs an invalid option, print an error message
            print('invalid option entered')
            time.sleep(0.5)


def maintain(step,opt):

    coursecode=''
    loop1=True
    while loop1:
        if step==1:
            os.system('cls')
            display_courses()
# Request the user to input a course code to delete or update
            removecode=input('Enter course code to (delete/change) the course <Q>uit:').upper()
            if removecode=='Q':
# If the user inputs "Q", set the "step" variable to 99 and clear the screen
                step=99
                os.system('cls')
            elif (len(removecode)!=8 or removecode[:2]!='FH') or\
                     removecode[4:8].isdigit()==False or removecode[:4].isalpha()==False:
# If the user inputs an invalid course code, print an error message and prompt the user to input again
                print('Invalid course code entered')           
                time.sleep(0.5)
            else:
                found=False
                for code in data["Courses"]:
                    if code["COURSES"][:8]==removecode:
# If the course code entered by the user matches a course code in the "Courses" list of the "data" dictionary,
# set the "course" variable to the course description and set the "found" variable to True
                        course= code["COURSES"][9:]
                        found=True
                if found:
# If the course is found, move to next step
                    step+=1
                else:
# If the course is not found, print not found message for 1 second and prompt the user to input again.
                    print('The course that you want to delete/change is not found in file.')
                    time.sleep(1)
        
        
        if step==2:
            os.system('cls')
            display_courses()
# Request user to confirm deletion/update
            if opt in ['U','D'] and coursecode=='':
                print('The course that you want to delete/change:%s(%s)'%(removecode,course))
                confirm=input('Do you confirm to delete/change the course?(yes/no) <Q>uit').lower()
# Request user to confirm append/update        
            else:
                print('The course that you want to append/update:%s(%s)'%(coursecode,coursedesc))
                confirm=input('Do you confirm to append/update the course?(yes/no) <Q>uit').lower()
# If 'Q' is entered, set step to 99 to exit loop            
            if confirm=='q':
                step=99
                os.system('cls')
# Validate user's inputs
            elif not confirm in ['yes','no']:
# If invalid, print error message for 0.5 second
                print('Invalid input entered.')
                time.sleep(0.5)
            elif confirm=='yes':
                if opt=='A':
# Append new course to "data" variable                    
                    data["Courses"].append(courses)
                # Move to step 6 
                    step+=4
                elif opt=='U' and coursecode=='':
                # Move to step 3
                    step+=1
                else:
                # Move to step 5
                    step+=3
            else:
# If user's option is update or delete, move back to step 1 
                if opt in ['U','D'] and coursecode=='':
                    step=1
                # If not, move to step3
                else:
                    step=3                
        
        
        if step==3:
            os.system('cls')
            display_courses()
            if opt=='U':
# If the option is update, print a message that shows the course code and name that the user wants to change.
                print('The course that you want to delete/change:%s(%s)'%(removecode,course))
            coursecode=input('Course Code <Q>uit:').upper()
# Request the user to enter a course code, and store it in a variable named 'coursecode'. The input is converted to uppercase.
            if coursecode=='Q':
# If the user selects "quit", set the "step" variable to 99 to exit the loop and clear screen
                step=99
                os.system('cls')
# Check if the entered course code is valid
            elif (len(coursecode)!=8 or coursecode[:2]!='FH') or\
                     coursecode[4:8].isdigit()==False or coursecode[:4].isalpha()==False\
                     or coursecode in [code['COURSES'][:8] for code in data['Courses']]:
# If invalid, print error message for 0.5 second
                print('Invalid course code entered')
                step=3
                time.sleep(0.5)
            else:
                step+=1
        if step==4:
            os.system('cls')
            display_courses()
            print('course code:%s'%(coursecode))
# Request user to enter course description
            coursedesc=input('Course Desc <Q>uit:').upper()
            if coursedesc=='Q':
# If user entered 'Quit', set the "step" variable to 99 to exit the loop and clear screen
                step=99
                os.system('cls')
            elif coursedesc.replace(" ", "").isalpha()==False or coursedesc in [code['COURSES'][9:] for code in data['Courses']] :
                print('Invalid course name entered.')
                time.sleep(0.5)
            else:
                # Create a dictionary of the new course data
                courses={"COURSES":coursecode+'|'+coursedesc} 
                # Move back to step 2
                step-=2
        
        
        if step==5:
# Loop through each course in the "Courses" list of the "data" dictionary
            for code in data["Courses"]:
# Check if the first 8 characters of the course code match the code of the course to be removed/updated
                if code["COURSES"][:8]==removecode:
# Get the index of the course to be removed/updated
                    idx=data["Courses"].index(code)
# Remove the old course information from the "Courses" list
                    data["Courses"].remove(code)
# If the user chose to update the course information, insert the new course information in the same index
                    if opt=='U':
                        data["Courses"].insert(idx,courses)
                    # Move to step 6
                    step+=1
        
        
        if step==6:
# Write the updated course information to the "courses.json" file
            g.writefile(data,"courses.json",1)
# Set the loop flag to False to exit the while loop
            loop1=False
        
        
        if step==99:
# Clear the console screen and exit the while loop
            os.system('cls')
            loop1=False
    
        
