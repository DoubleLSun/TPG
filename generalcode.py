#Module name  : generalcode.py
#created by   : Chia Ji Xuan,Lee Mei Lin,Leong Lek Sun,Tan Wen Zhe,Wong Jea Sen,Yew Fu Li
#created date : 23/4/2023
#import       : json
import json
# write file
def writefile(data,filename,ind):
    with open(filename,'w') as f:
        json.dump(data,f,indent=ind)

#write file
def readfile(filename):
    with open(filename,'r') as f:
        read_data=json.load(f)
    return read_data

#for display the course use
def courseDict(filename):
    courses=readfile(filename)
    cLst=courses['Courses']
    cDict={}
    idx=0
    for idx in range(len(cLst)):
        key=cLst[idx].get('COURSES')[:8]
        value=cLst[idx].get('COURSES')[9:]
        cDict[key]=value
    return cDict
