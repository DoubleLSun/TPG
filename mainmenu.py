#Module name  : mainmenu.py
#created by   : Yew Fu Li, Tan Wen Zhe
#created date : 25/2/2023
#import       : os,QuestionbankMaintenance as Qbank,TPG,coursemaintain as cm,testdates as date,StudentListMaintenance as stud,time
import os,QuestionbankMaintenance as Qbank,TPG,coursemaintain as cm,testdates as date,StudentListMaintenance as stud,time

def mainmenu(): #Test management
    Loop=True
    while Loop:
        current_time = time.time()
        local_time = time.localtime(current_time)
        formatted_time = time.strftime("%d-%m-%Y %H:%M", local_time)
        os.system('cls')
        print("-"*50)
        print("Test management -> Process step %s"%formatted_time)
        print("-"*50)
        opt1=input("<1>Setup  <2>Generate Test Paper <3>Help <E>xit :").upper()
        if opt1=="E":
            Loop=False 
        elif opt1=="1":
            setup()
        elif opt1=="2":
            TPG.TestPG()
        elif opt1=='3':
            os.startfile('help.txt')
        else:
            print("Invalid option entered")
            time.sleep(0.75)


def setup():#system configuration
    Loop1=True
    while Loop1:
        os.system('cls')
        print('-'*50)
        print('System Configuration -> Process steps')
        print('-'*50)
        opt2 = input('<1>Student, <2>courses <3>Question Bank <4>Test Date <E>xit :').upper()
        if opt2=='E':
            os.system('cls')
            Loop1=False
        elif opt2=="1":
            stud.main()
        elif opt2=='2':
            cm.main()                    
        elif opt2=="3":
            Qbank.main()
           
        elif opt2=="4":
            date.main()
        else:
            print("Invalid option entered")
            time.sleep(0.75)
            

mainmenu()
