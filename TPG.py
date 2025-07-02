#Module name   : TPG.py
#Created by    : Wong Jea Sen,Leong Lek Sun
#Created when  : 25th Feb 2023
#import        : os, json ,random,time,generalcode

import os, json ,random ,time ,generalcode as ge
DASHLEN=50
    

def TestPG():
    #read file
    courses=ge.readfile("courses.json")
    data=ge.readfile("studentlist.json")
    ttdata=ge.readfile("tdates.json")
    Qdata=ge.readfile('QuesDict.txt')
    
    courseLst=[]
    nameLst=[]
    ttLst=[]
    
    loop1=True
    step=1
    while loop1:
        if step==1:
            os.system("cls")
            print("-"*DASHLEN)
            print("Generate/Create Student Course Test paper  <Q>uit")
            print("-"*DASHLEN)
            #print course
            for key in courses["Courses"]:
                valid = (key.get("COURSES")[:8] )
                print(valid,end=' ')
                courseLst.append(valid)
                
            print()
            #input course ID
            cid=input("Course ID <Q>uit -->").upper()
            #validation
            if cid == "Q":
                step=99
            elif cid not in courseLst:
                print("Invalid Course Id ")
                time.sleep(0.5)
            else:
                step+=1
                #find the course name of the input course ID 
                for cornam in courses['Courses']:
                    valid = (cornam.get('COURSES')[:8])
                    if cid == valid:
                        cornm=cornam.get('COURSES')[9:]
                        pcnm="".join(cornm)
                os.system('cls')

        if step==2:
            os.system("cls")
            #print course that selected
            print("Generating Test File -->")
            print("course ID : %s  (%s) "%(cid,pcnm))
            print()
            print("-"*DASHLEN)
            #print name list
            max_name_width = max(len(student["StudName"]) for student in data["Studlst"])
            max_nric_width = max(len(student["NRIC Number"]) for student in data["Studlst"])
            printstdn1=f"{'StudID':<15}{'StudName':<{max_name_width+2}}{'NRIC Number':<{max_nric_width+2}}"
            print("Student List")
            print("-"*DASHLEN)
            print(printstdn1)
            print("-"*DASHLEN)
            for student in data["Studlst"]:
                val1 = (student.get("StudID")[:8] )
                printstudn2=f"{student['StudID']:<15}{student['StudName']:<{max_name_width+2}}{student['NRIC Number']:<{max_nric_width+2}}"
                nameLst.append(val1)
                print(printstudn2)
            print("-"*DASHLEN)
            #input student ID
            studid=input("Student ID (YY####)   <B>ack <Q>uit -->").upper()
            #validation
            if studid =="Q" :
                step=1
            elif studid =="B" :
                step-=1
                
            elif studid not in nameLst:
                print("Invalid Student Id ")
                time.sleep(0.5)
                
            else:
                step+=1
                #find the student name of the input student ID 
                for studidd in data["Studlst"]:
                    val1 = (studidd.get("StudID")[:8] )
                    if studid == val1:
                        studname=studidd.get("StudName")
                        pname="".join(studname)
                os.system('cls')

        if step==3:
            os.system("cls")
            #print course that selected
            print("Generating Test File -->")
            print("course ID : %s  (%s) "%(cid,pcnm))
            #print student that selected
            print("StudentID : %s   (%s) "%(studid,pname))
            print()
            print("-"*DASHLEN)
            print("Test Date Setup - Available slots")
            print("-"*DASHLEN)
            print("%s   (%s) "%(cid,pcnm))
            print("-"*DASHLEN)
            print("Date          Slots     Number of questions(Size)")
            print("-"*DASHLEN)
            #check if test date got record
            if cid not in ttdata:
                print("No record found")
                print()
                print("-"*DASHLEN)
                input("Press enter restart")
                step=1
            else:
                #print test date , time slots and number of question
                for tdate in ttdata[cid]:
                    print(tdate["Date"], "   ", tdate["Slots"], "        ",tdate["Number of question(size)"])
                    val2 = (tdate.get("Date")[:10])
                    ttLst.append(val2)

                print("-"*DASHLEN)
                #input test dates 
                testd=input("Test Dates        <B>ack <Q>uit >> ").upper()
                if testd =="Q":
                    step=1 

                elif testd =="B" :
                    step-=1

                elif testd not in ttLst:
                    print("Invalid Time Slots ")
                    time.sleep(0.5)
                        
                else:
                    step+=1
                    #find the time slots and number of question of the input test dates
                    for testdd in ttdata[cid]:
                        val3 = (testdd.get("Date")[:10] )
                        if testd == val3:
                            timeslot=testdd.get("Slots")
                            numqsize=testdd.get("Number of question(size)")
                            pslot="".join(timeslot)
                            pnumq="".join(numqsize)
                    os.system('cls')


        if step==4:
            os.system("cls")
            #print all the data that selected
            print("Generating Test File -->")
            print("course ID : %s         (%s) "%(cid,pcnm))
            print("StudentID : %s          (%s) "%(studid,pname))
            print("TestDate  : %s       (Slots: %s  Ques Size: %s)"%(testd,pslot,pnumq))
            print()
            #ask user conform or not
            cfrm=input("Generate <Y>es/<N>o    <Q>uit >> ").upper()
            
            if cfrm == "N":
                input("Press enter to move back...")
                step-=1

            elif cfrm == "Q":
                step=1
    
            elif cfrm == "Y":
                #check if enough question or not
                if len(Qdata.get(cid, {})) < int(pnumq):
                    print("Invalid number of questions requested.")
                    input("Press enter to restart...")
                    step=1
                else:
                    print("File generate...")
                    input("Press enter to restart...")
                    step+=1
                    
            #validation
            else:
                print("Invalid input")
                time.sleep(0.5)


        if step==5:
            #generate test paper
            courseid = "course ID : %s         (%s)\n" % (cid, pcnm)
            studentid = "StudentID : %s          (%s)\n" % (studid, pname)
            testdate = "TestDate  : %s       (Slots: %s  Ques Size: %s)\n" % (testd, pslot, pnumq)

            #random question
            questions = []
            question_str = ''
            question_indices = list(Qdata[cid].keys())[:int(pnumq)]
            random.shuffle(question_indices)
            for i, index in enumerate(question_indices):
                question = Qdata[cid][index]
                questions.append([str(i + 1) + '. ' + question['Q'], 'A. ' + question["O"]["A"],
                                  'B. ' + question["O"]["B"], 'C. ' + question["O"]['C'],
                                  'D. ' + question['O']['D'] + '\n'])
    
            for item1 in questions:
                if isinstance(item1, list):
                    question_str += '\n'.join(item1) + '\n'
                else:
                    question_str += item1
                    
            testpaper = [courseid, studentid, testdate, '\n', 'Questions\n', '\n', question_str]
            testpaper_str = ""
            for item in testpaper:
                if isinstance(item, list):
                    testpaper_str += '\n'.join(item) + '\n'
                else:
                    testpaper_str += item

            #open file
            pdate="".join(testd)        
            with open('TP_{}_{}_{}.txt'.format(cid, studid,pdate.replace('/', '-')), 'w') as g:
                g.write(testpaper_str)

            step=1

        #loop false
        if step==99:
            loop1=False

                          

