#Module name  : testdates.py
#created by   : Yew Fu Li, Tan Wen Zhe
#created date : 25/2/2023
#import       : os, json, time, calendar, coursemaintain, generalcode
import os,json,coursemaintain as a,time,calendar,generalcode as g
data =g.readfile("tdates.json")
courses= g.readfile('courses.json')

def display_time(code):#display date,slot and number of questions
    
    found=True
    for cornm in courses['Courses']:
        if cornm["COURSES"][:8]==code:
            name=cornm.get('COURSES')[9:]
    print('-'*50)
    print("Time Slots available --->")
    print('-'*50)
    print('%s (%s):'%(code,name))
    print('-'*50)
    print("Date         Slots   Number of questions(Size)")
    print('-'*50)
    if not data.get(code):
        print('No record found')
    else:
        for course in data[code]:
            print('%-13s%02d      %02d' % (course['Date'], int(course['Slots']), int(course['Number of question(size)'])))



def main():#input course code
    loop3=True
    while loop3:
        os.system('cls')
        a.display_courses()
        coursecode=input('Course code <Q>uit:').upper()
        if coursecode=='Q':
            loop3=False
            os.system('cls')
        elif (len(coursecode)!=8 or coursecode[:2]!='FH') or\
              coursecode[4:8].isdigit()==False or coursecode[:4].isalpha()==False:
            print('Invalid course code entered.')
            time.sleep(0.5)
        else:
            found=False
            for course in courses['Courses']:
                if course['COURSES'][:8]==coursecode:
                    found=True
                    main2(coursecode)
            if not found:
                print("Course hasn't added")
                time.sleep(0.5)


def main2(coursecode):#menu
    loop=True
    while loop:
        os.system('cls')
        display_time(coursecode)
        opt=input('<A>dd  <U>pdate <D>elete <Q>uit').upper()
        if opt=='A':
            step=3
            maintain(step,opt,coursecode)
        elif opt in ['U','D']:
            step=1
            maintain(step,opt,coursecode)
        elif opt=='Q':
            loop=False
        else:
            print('invalid option entered')
            time.sleep(0.5)


def maintain(step,opt,code):
    coursedate=''
    loop1=True
    while loop1:
        if step==1:#input date that will be removed/changed
            os.system('cls')
            display_time(code)
            removedate=input('Enter date to (delete/change) the details (dd/mm/yyyy) <Q>uit:').upper()
            if removedate=='Q':
                step=99
                os.system('cls')
            elif (len(removedate)!=10 or removedate[:2].isdigit()==False or\
                  removedate[3:5].isdigit()==False or removedate[6:10].isdigit()==False\
                  or removedate[2]!='/' or removedate[5]!='/'):
                print('Invalid date entered')
                step=1
                time.sleep(0.5)
            elif not is_valid_date(removedate):
                print('Invalid date entered')
                step=1
                time.sleep(0.5)
            else:
                found=False
                for codes in data[code]:
                    if codes["Date"]==removedate:
                        slot=codes['Slots']
                        ques=codes['Number of question(size)']
                        found=True
                if found:
                    step+=1
                else:
                    print('The date that you want to delete/change is not found in file.')
                    time.sleep(0.5)

        if step==2:#confirmation about date,number of slots and number of questions that will be appended/updated/removed and
                   #append date,number of slots and number of questions
            os.system('cls')
            display_time(code)
            if opt in ['U','D'] and coursedate=='':
                print('The details in date that you want to delete/change:%s(slots: %s)(number of questions: %s)'%(removedate,slot,ques))
                confirm=input('Do you confirm to delete/change the details in date?(yes/no) <Q>uit').lower()
            else:
                print('The details in date that you want to append/update:%s(slots: %s)(number of questions: %s)'%(coursedate,courseslot,courseques))
                confirm=input('Do you confirm to append/update the details in date?(yes/no) <Q>uit').lower()
            if confirm=='q':
                step=99
                os.system('cls')
            elif not confirm in ['yes','no']:
                print('Invalid input entered.')
                time.sleep(0.5)
            elif confirm=='yes':
                if opt=='A':
                    if not data.get(code):
                        data[code]=[date]
                    else:
                        data[code].append(date)
                    step+=5
                elif opt=='U' and coursedate=='':
                    step+=1
                else:
                    step=6
            else:
                if opt in ['U','D'] and coursedate=='':
                    step=1
                else:
                    step=3                
        if step==3:#input date that will be appended/updated
            os.system('cls')
            display_time(code)
            if opt=='U':
                print('The details in date that you want to delete/change:%s(slots: %s)(number of questions: %s)'%(removedate,slot,ques))
            coursedate=input('Enter date (dd/mm/yyyy) <Q>uit:').upper()
            if coursedate=='Q':
                step=99
                os.system('cls')
            elif (len(coursedate)!=10 or coursedate[:2].isdigit()==False or\
                  coursedate[3:5].isdigit()==False or coursedate[6:10].isdigit()==False\
                  or coursedate[2]!='/' or coursedate[5]!='/') :
                print('Invalid date entered')
                step=3
                time.sleep(0.5)
            elif not is_valid_date(coursedate):
                print('Invalid date entered')
                step=3
                time.sleep(0.5)
            else:
                step+=1
        if step==4:#input number of slots that will be appended/updated
            os.system('cls')
            display_time(code)
            if opt=='U':
                print('The details in date that you want to delete/change:%s(slots: %s)(number of questions: %s)'%(removedate,slot,ques))
            print('Date: %s'%(coursedate))
            courseslot=input('Enter number of slots <Q>uit:').upper()
            if courseslot=='Q':
                step=99
                os.system('cls')
            elif courseslot.isdigit()==False or len(courseslot)>2 or float(courseslot)==True:
                print('Invalid number of slots entered.')
                step=4
                time.sleep(0.5)
            else: 
                step+=1
        if step==5:#input number of questions that will be appended/updated
            os.system('cls')
            display_time(code)
            if opt=='U':
                print('The details in date that you want to delete/change:%s(slots: %s)(number of questions: %s)'%(removedate,slot,ques))
            print('Date: %s'%(coursedate))
            print('Slots: %s'%(courseslot))
            courseques=input('Enter number of questions <Q>uit:').upper()
            if courseques=='Q':
                step=99
                os.system('cls')
            elif courseques.isdigit()==False or len(courseques)>2 or float(courseques)==True:
                print('Invalid number of questions entered.')
                step=5
                time.sleep(0.5)
            else:
                date={"Date":coursedate,"Slots":courseslot,"Number of question(size)":courseques}
                step=2
        if step==6:#remove date,number of slots and number of questions
            for codes in data[code]:
                if codes["Date"]==removedate: 
                    idx=data[code].index(codes)
                    data[code].remove(codes)
                    if opt=='U':
                        data[code].insert(idx,date)
                    step+=1
        if step==7:#write into json file
            g.writefile(data,"tdates.json",4)
            loop1=False
        if step==99:#quit
            os.system('cls')
            loop1=False    

# Validate a date string in 'DD/MM/YYYY' format
def is_valid_date(date_string):
    status=True
    day, month, year = map(int, date_string.split('/'))
    # Check if the month is valid
    if month < 1 or month > 12:
        status=False
    else:
    # Check if the day is valid for the given month and year
        days_in_month = calendar.monthrange(year, month)[1]
        if day < 1 or day > days_in_month:
            status=False
    return status       
