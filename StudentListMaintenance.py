#Module name   : addstudlst.py
#Created by    : Wong Jea Sen,Leong Lek Sun
#Created when  : 25th Feb 2023
#import        : os,time,generalcode



import os,time,generalcode as g
# Open the studentlist.json file and load its contents into a variable called "data"
data = g.readfile("studentlist.json")

def display_studLst():

# Print table & header
    max_name_width = max(len(student["StudName"]) for student in data["Studlst"])
    max_nric_width = max(len(student["NRIC Number"]) for student in data["Studlst"])
    printstdn1=f"{'StudID':<15}{'StudName':<{max_name_width+2}}{'NRIC Number':<{max_nric_width+2}}"
    print("Student List")
    print("-"*50)
    print(printstdn1)
    print("-"*50)
# Loop through each student in "Studlst" list of the "data" dictionary and print student ID,name,IC
    for student in data["Studlst"]:
        printstudn2=f"{student['StudID']:<15}{student['StudName']:<{max_name_width+2}}{student['NRIC Number']:<{max_nric_width+2}}"
        print(printstudn2)
    print("-"*50)


def main():
    loop3=True
    while loop3:
        # clear screen
        os.system('cls')
        # display student list
        display_studLst()
        # options of input
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
# Open the studentlist.json file and load its contents into a variable called "data"
    studentid=''
    loop1=True
    while loop1:
        if step==1:
            os.system('cls')
            display_studLst()
            # Request user to select student ID to delete/change
            removecode=input('Enter students ID  to (delete/change) the course <Q>uit:').upper()
            if removecode=='Q':
                # If the user inputs "Q", set the "step" variable to 99 and clear the screen
                step=99
                os.system('cls')
            # If the user inputs an invalid student ID, print an error message and prompt the user to input again
            elif (len(removecode)!=7 or removecode.isdigit()==False):
                  print('Invalid student ID entered')
                  time.sleep(0.5)
            else:
                found=False
                for studid in data["Studlst"]:
                    val1 = (studid.get("StudID")[:8] )
                    if val1 == removecode:
                    # match stud ID in the "Studlst" list of the "data" dictionary,
                    # get both studname and ic number of selected studID, then set the "found" variable to True
                        studname=studid.get("StudName")
                        studic  =studid.get("NRIC Number")
                        
                        found=True
                if found:
                    # Proceed to next step
                    step+=1
                else:
                    # Error message if student info not found.
                    print('The student that you want to delete/change is not found in file.')
                    time.sleep(1) 

        if step==2:
            os.system('cls')
            display_studLst()
            # Request user to confirm deletion/update
            if opt in ['U','D'] and studentid=='':
                print('The student that you want to delete/change:%s(%s)(%s)'%(studname,removecode,studic))
                confirm=input('Do you confirm to delete/change the student?(yes/no) <Q>uit').lower()
            # Request user to confirm append/update
            else:
                print('The course that you want to append/update:%s(%s)(%s)'%(studentname,studentid,Studentic))
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
                    # Append new student to "data" variable
                    data["Studlst"].append(student)
                    # Move to step 7
                    step+=5
                elif opt=='U' and studentid=='':
                    # Move to step 3
                    step+=1
                else:
                    # Move to step 6
                    step+=4
            else:
            # If user's option is update or delete, move back to step 1
                if opt in ['U','D'] and studentid=='':
                    step=1
                # If not, move to step3
                else:
                    step=3


        if step==3:
            os.system('cls')
            display_studLst()
            if opt=='U':
            # If the option update, display selected student info
                print('The course that you want to delete/change:%s(%s)(%s)'%(studname,removecode,studic))
            studentid  =input('Student ID   <Q>uit:').upper()
            # Request the user to enter a Student ID , and store it in a variable named 'studentid'. The input is converted to uppercase.
            if studentid=='Q':
            # If the user selects "quit", set the "step" variable to 99 to exit the loop and clear screen
                step=99
                os.system('cls')
            # Check if the entered student ID is valid
            elif (len(studentid)!=7 or studentid.isdigit()==False):
#                If invalid, print error message for 0.5 second
                print('Invalid Student ID entered')
                step=3
                time.sleep(0.5)
            elif studentid in [stud["StudID"] for stud in data["Studlst"]]:
                print("Invalid")
                step=3
                time.sleep(0.5)
            else:
                step+=1

        if step==4:
            os.system('cls')
            display_studLst()
            print("Student ID :%s"%(studentid))
            # Request user to enter student name
            studentname=input('Student Name <Q>uit:')
            if studentname in ['Q','q']:
            # If user entered 'Quit', set the "step" variable to 99 to exit the loop and clear screen
                step=99
                os.system('cls')
            elif not studentname.replace(" ", "").isalpha():
                print("Invalid student name")
                step=4
                time.sleep(0.5)
            else:
                step+=1

        if step==5:
            os.system('cls')
            display_studLst()  
            # Request user to enter student ic
            print("Student ID   :%s"%(studentid))
            print("Student Name :%s"%(studentname))
            Studentic  =input('Student IC   <Q>uit:').upper()
            if Studentic=='Q':
            # If user entered 'Quit', set the "step" variable to 99 to exit the loop and clear screen
                step=99
                os.system('cls')
#validation
            elif (len(Studentic)!=14 or (Studentic[6]and Studentic[9])!='-') or\
             Studentic[:6].isdigit()==False or Studentic[7:9].isdigit()==False or\
             Studentic[10:14].isdigit()==False:
                print("Invalid student IC")
                step=5
                time.sleep(0.5)

            else:
                # Create a dictionary of the new course data
                student={"StudID":studentid ,
                         "StudName":studentname,
                         "NRIC Number":Studentic} 
                # Move back to step 2
                step-=3


        if step==6:
# Loop through each studentlst in the "Studlst" list of the "data" dictionary
            for code in data["Studlst"]:                
# Check if the student ID match the code of the studens to be removed/updated
                if code["StudID"][:7]==removecode:
                    
# Get the index of the student ID to be removed/updated
                    idx=data["Studlst"].index(code)
                    
# Remove the old student information from the "Studlst" list
                    data["Studlst"].remove(code)
# If the user chose to update the student information, insert the new student information in the same index
                    if opt=='U':
                        data["Studlst"].insert(idx,student)
                    # Move to step 7
                    step+=1

        
        if step==7:
            g.writefile(data,"studentlist.json",1)
# Write the updated student information to the "studentlist.json" file
            #with open("studentlist.json", "w") as s:
                #json.dump(data, s, indent=4)
            
# Set the loop flag to False to exit the while loop
            loop1=False
        
        
        if step==99:
# Clear the console screen and exit the while loop
            os.system('cls')
            loop1=False
    
