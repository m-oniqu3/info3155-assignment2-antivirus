import os
from pathlib import Path
import re

#qMeyivyOyh
#XNjklgrVtg

'''
print("********************************************************")
print("**                                                    **")
print("**               Welcome To The Antivirus             **")
print("**                                                    **")
print("********************************************************")
'''

print("This program checks whether or not a specific python file is infected.")

n='true'
while  n:
    
    filepath = input ("Please enter the file path to the python file you wish to check.")
    if os.path.isfile(filepath):
        [file, extension] = os.path.splitext(filepath)
              
        if (extension == '.py'):
            filecontents=""                       
            with open(filepath, "r") as pyfiles:
                for pyfile in pyfiles:
                    pystrip = pyfile.strip()
                    filecontents+=pystrip
                
            
            
            if (re.search('qMeyivyOyh',filecontents)) or (re.search('XNjklgrVtg',filecontents)):
                print ("This file has been infected")

            else:
                print("This file has not been infected")


            
            check = input ("Do you wish to check another file. Write yes or no")
            if (check=='yes'):
                continue
            if (check=="no"):
                print ("Thank you")
                break
                
            print("Your response is invalid")
            break


            
                
        else:
            print ("This is not a python file")
            continue
        

    else:
        print("This file does not exist")
        continue  






'''
while os.path.isfile(filepath):
    print("This file exists")
    [file, extension] = os.path.splitext(filepath)
    print (file)
    print(extension)
else:
    print("This file does not exist")
    continue  
    

    while (extension == '.py'):
        print("This is a python file")
        break
    else:
        print ("This is not a python file")
        break
    '''
