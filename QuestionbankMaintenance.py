#Module name  : QuestionbankMaintenance.py
#created by   : Chia Ji Xuan, Lee Mei Lin
#created date : 25/2/2023
#import       : os, generalcode.py, time

import os,generalcode as gc, time
# create question bank 
if os.path.exists('QuesDict.txt'):
#except JSONDecodeError
    try:
        questionbank=gc.readfile('QuesDict.txt')
    except gc.json.JSONDecodeError:   
        questionbank={}
else:
    questionbank={}

#add option'A','B','C','D'
def add_options():  
    ques_options={}
    i=0
    charLst=['A','B','C','D']
    for i in range(4):
        option=input("Enter option %s\t\t\t >> "%charLst[i])
# to make sure user input an option
        while option=='':
            print("Please enter option")
            option=input("Enter option %s\t\t\t >> "%charLst[i])
        else:    
            ques_options[charLst[i]]=option
            i+=1
    return ques_options

#print out question, option and answer
def print_q(courseid,questionNum):
    question=questionbank[courseid][questionNum]['Q']
    print(question)
    optLst=['A','B','C','D']
    ans = 'Answer:'+questionbank[courseid][questionNum]['ans']
    for i in optLst:
        option=i+':'+questionbank[courseid][questionNum]['O'][i]
        print(option)
    print(ans)


#to add question 
def add_question(courseid):
    # will create a new dictionary if there is a new course added       
    if courseid not in questionbank:
        questionbank[courseid]={}
    loop=True
    step=1
    # add_question loop
    while loop:
        #step 1--> enter a question 
        #validation(s): display reminder message if user press 'enter'
        if step==1:
        # we do not require user input question number, instead we make it auto add the question number
            ques_no = str(len(questionbank[courseid].keys())+1)
            ques_desc_opt={}  
            question=input("Enter question\t\t <Q>Quit >> ")
            step+=1
            if question =='':
                print("Please enter question")
                step=1
            elif question in ['q','Q']:
                step=99
        #step 2 --> add option 
        if step==2: 
            ques_desc_opt["Q"]=question 
            ques_desc_opt["O"]=add_options()
            step+=1
        #step 3 --> input the correct answer option
        #validation(s): display error message if input is not 'A','B','C','D' or 'Q'
        if step==3:
            answer=input("Answer<ABCD>\t\t <Q>Quit >> ").upper()
            if answer == 'Q':
                step=99
            elif answer not in ['A','B','C','D']:
                print('Invalid input')
                step=3
            else:
                step+=1
        #step 4 --> confirm the add question input 
        #validation(s):display error message if user did not input 'Y' or 'N'
        # 'Y'--> question added
        # 'N'--> Back to step 1 to re-enter question
        if step==4:
            confirm = input('Confirm your input?\t <Y/N>   >> ').upper()
            if confirm not in ['Y','N']:
                print('Invalid input')
                step=4
            elif confirm == 'Y': 
                ques_desc_opt["ans"]=answer
                questionbank[courseid][ques_no]=ques_desc_opt
                gc.writefile(questionbank,'QuesDict.txt',4)
                step=99
            else:
                step=1
        #step 99 --> exit loop
        if step==99:
            loop=False

#Update the question 
def upd_ques(courseid):
    loop=True
    step=1
    # update loop
    while loop:
        if step==1:
            #step 1 --> enter the question number want to update
            ques_no=input("Question Number\t\t<Q>Quit >> ").upper()
            if ques_no == 'Q':
                loop=False
            #validation(s):display error message if user not enter a number or the number does not exist
            elif not ques_no.isdigit():
                print("Invalid input")
            elif ques_no not in questionbank[courseid]:
                print("Question not exist")
            else:
                print()
                #display the question, options and answer for user
                print_q(courseid,ques_no)
                step+=1
        if step==2:
            #step 2 --> confirm to update question or not
            u_ques=input("Update question?\t   <Y/N> >> ").upper()
            if u_ques not in ['Y','N']:
                #validation(s):display error message if user did not input Y or N
                print("Invalid input")
            elif u_ques == 'Y':
                #update a new question or quit
                question=input("New question\t\t <Q>Quit >> ")
                if question in ['Q','q']:
                    loop=False
                else:
                    step+=1
            else:
                #question remain unchange
                question=questionbank[courseid][ques_no]["Q"]
                step+=1
        if step==3:
            #step 3 --> confirm to update options or not
            u_opt=input("Update options?\t\t   <Y/N> >> ").upper()
            if u_opt not in ['Y','N']:
                #validation(s):display error message if user did not input Y or N
                print("Invalid input")
            elif u_opt == 'Y':
                #update option A,B,C,D
                option=add_options()
                step+=1
            else:
                #options remain unchange
                option=questionbank[courseid][ques_no]["O"]
                step+=1
        if step==4:
            #step 4 --> confirm to update answer or not
            u_ans=input("Update answer?\t\t   <Y/N> >> ").upper()
            if u_ans not in ['Y','N']:
                #validation(s):display error message if user did not input Y or N
                print("Invalid input")
            else:
                step+=1
        if step==5:
            #step 5 --> update answer and save the updated question, options and answer into "QuesDict.txt"
            if u_ans == 'Y':
                #update new answer
                answer=input("Answer<ABCD>\t\t <Q>Quit >> ").upper()
                if answer not in ['A','B','C','D','Q']:
                    #validation(s):display error message if user did not input A,B,C,D,Q
                    print("Invalid input")
                elif answer != 'Q':
                    #update answer and save the updated question,options and answer into "QuesDict.txt"
                    questionbank[courseid][ques_no]["Q"]=question
                    questionbank[courseid][ques_no]["O"]=option
                    questionbank[courseid][ques_no]["ans"]=answer
                    gc.writefile(questionbank,'QuesDict.txt',4)
                    step=99
                else:
                    #quit update 
                    loop=False
            else:
                #answer did not updated, save the updated question, options into "QuesDict.txt"
                questionbank[courseid][ques_no]["Q"]=question
                questionbank[courseid][ques_no]["O"]=option
                gc.writefile(questionbank,'QuesDict.txt',4)
                step=99
        if step==99:
            #step 99 --> display the updated question 
            if u_ques==u_opt==u_ans=='N':
                #if nothing updated
                print()
                print("Question remain unchanged...")
            else:
                #if something updated
                print()
                print("Question updated...")
            #display the updated question
            print_q(courseid,ques_no)
            input("Press enter to quit...")
            #exit the loop
            loop=False

# delete question
def del_ques(courseid):     
    loop=True
    step=1
    # del_quest loop
    while loop:
        #step 1--> let user input question number
        #validation(s): input must be digit, validate wether the question exist or not
        if step==1:
            quesno=input("Enter question number want to delete\t<Q>Quit >> ")
            if quesno in ['q','Q']:
                step=99
            elif not quesno.isdigit():
                print("Invalid input")
            elif quesno not in questionbank[courseid]:
                print("Question not exist")
            else:
                step+=1
        # step 2--> confirm the question number that want to be deleted
        # validation(s):isplay error message if user did not input 'Y' or 'N'
        #'Y'--> question deleted, question number will be re-correct 
        #'N'--> re-enter question number
        if step==2:
            confirm=input('Confirm your delete?\t\t\t<Y/N>   >>').upper()
            if confirm not in ['Y','N']:
                print('Invalid input')
                step=2
            elif confirm == 'Y': 
                del questionbank[courseid][quesno] 
                queslst=[]
                for qnum in range(1,len(questionbank[courseid].keys())+1):
                    queslst.append(str(qnum)) 
                questionbank[courseid]=dict(zip(queslst,questionbank[courseid].values()))
                gc.writefile(questionbank,'QuesDict.txt',4)
                step=99  
            else:
                step=1
        # step 99 --> exit loop
        if step==99:
            loop=False

#display the course id, course description, and the course's question bank. 
#input option to add, update or delete question
def displayLst(questionbank,courseid):
    loop=True
    while loop:
        os.system('cls') 
        questionbank=gc.readfile('QuesDict.txt')
        print("-"*133)
        #display the heading (course id + course description)
        cDict=gc.courseDict("courses.json")
        courseID=list(cDict.keys())
        courseDesc=list(cDict.values())
        idx=courseID.index(courseid)
        print(courseid+' '+courseDesc[idx])
        print("-"*133)
        #display the question bank
        print("No.    Question")
        print("-"*133)
        if not questionbank.get(courseid):
            #validation(s):if no question for this course found in "QuesDict.txt"
            print("No questions for this course found")
        else:
            #print the whole question for this course in "QuesDict.txt"
            for i in range(1,len(questionbank[courseid].items())+1):
                print("%2s     %s"%(str(i),questionbank[courseid][str(i)]['Q']))
        print("-"*133)
        #input A/U/D/E
        # A/U/D/E--> to add/update/delete question or exit Question bank maintainance
        opt=input("<A>Add   <U>Update   <D>Delete\t\t\t\t<E>Exit >> ").upper()
        if opt =='A':
            add_question(courseid)
        elif opt=='U':
            if not questionbank.get(courseid):
                print("No questions found")
                time.sleep(0.75)
            else:
                upd_ques(courseid)
        elif opt=='D':
            if not questionbank.get(courseid):
                print("No questions found")
                time.sleep(0.75)
            else:
                del_ques(courseid)
        elif opt=='E':
            loop=False
        else:
            #validation(s):display error message if user did not enter A/U/D/E
            print("Error in option entered")
            time.sleep(0.75)

# questionbank mainmenu 
def main():  
    loop=True
    while loop:
        os.system('cls')
        print("-"*90)
        print("Question Bank Maintenance")
        print("-"*90)
        cDict=gc.courseDict("courses.json")
        courseID=list(cDict.keys())
        courseDesc=list(cDict.values())
        idx=0
        # print courseid
        for idx in range(len(courseID)):
            print(courseID[idx]+'|'+courseDesc[idx])
            idx+=1
        # input courseid
        # validation(s): display reminder message if course id has not added
        #'E'--> exit loop
        cid = input("Course ID\t<E>Exit >> ").upper() 
        if cid =='E':
            loop=False
            os.system('cls')  
        elif cid not in courseID:
            print("Course have not added")
            time.sleep(0.75)                   
        else:
            displayLst(questionbank,cid)   

