#Author: 620122735

import os
from pathlib import Path
import re
import sys


#These statments informs the user on what the program is about as well as instructions on how to properly execute it.
print("                                                                          ")
print("This program checks whether or not a specific python file is infected.")
print("__________________________________________________________________________")
print("                                                                          ")
print("INSTRUCTIONS:\nTO RUN THIS PROGRAM SUCCESSFULLY, PLEASE ENTER THE FILEPATH TO AN EXISTING PYTHON FILE.\nIF YOU WISH CHECK ANOTHER FILE, WHEN PROMPTED PLEASE ENTER YES (yes) OR NO (no).\nANY OTHER RESPONSE WILL BE DEEMED AS INVALID.")
print("__________________________________________________________________________")
print("                                                                          ")

#Creating a while looping with a true condition that was stores in a variable.
run='true'
while run:
    #This statement prompts the use to enter the filepath and it is stored in the filepath variable.
    filepath = input ("Please enter the file path to the python file you wish to check.")
    
    #Here, the program checks if the file exists. If the file exists, it splits the submitted file path to extract the file name and the file extension.
    if os.path.isfile(filepath):
        [file, extension] = os.path.splitext(filepath)

        #If the extension is .py, this means its a python file, and the user's filepath was valid. The string filecontents is created. The program then opens the file located at the submitted filepath in a read only format. It then proceeds to loop through the file, and striping it to remove excess space and then adding the stripped data to the filecontents. 
        if (extension == '.py'):
            filecontents=""                       
            with open(filepath, "r") as pyfiles:
                for pyfile in pyfiles:
                    pystrip = pyfile.strip()
                    filecontents+=pystrip

            #The statement checks the filecontents for the presence of any of the infection patterns. If there was a match the program will tell the user that the file is infected. If there was no match, the program will tell the user that the file is not infected.
            if (re.search('qMeyivyOyh',filecontents)) or (re.search('XNjklgrVtg',filecontents)):
                print ("This file has been infected.")
            else:
                print("This file has not been infected.")
            
            #Here, the user is prompted to decide if they wish to check another filepath. If the answer yes, the will be prompted to enter the filepath again. If the answer is no then program will end. If the user enters anything other than no then their response will be deemd as invalid and they will...........
            check = input ("Do you wish to check another file? Write yes or no")
            if (check.lower()=='yes'):
                continue
            elif (check.lower()=="no"):
                sys.exit("This program will now terminate.")

            print("Your response is invalid")
            continue

        #Here, this response is triggered if the user has not entered a python file. They will then be prompted again to enter a python filepath.         
        else:
            print ("This is not a python file")
            continue
    
    #This response is triggered if the user has entered a python file that does not exist. They will then be prompted again to enter a python filepath. 
    else:
        print("This file does not exist.")
        continue  


