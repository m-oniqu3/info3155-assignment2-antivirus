import os
from pathlib import Path

print("********************************************************")
print("**                                                    **")
print("**               Welcome To The Antivirus             **")
print("**                                                    **")
print("********************************************************")

print("This program checks whether or not a specific python file is infected.")

n='true'
while  n:
    filepath = input ("Please enter the file path to the python file you wish to check.")
    if os.path.isfile(filepath):
        print("This file exists")
        [file, extension] = os.path.splitext(filepath)
        print (file)
        print(extension)
        
        if (extension == '.py'):
            print("This is a python file")
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