# Import OS and RE libraries
import os
import re

# Get a LIST of all files in the "./files" folder
fileList = os.listdir("./files")

# Concatenate all files from LIST into one single output file
with open('./concatenated.txt', 'w') as outfile:
    for fname in fileList:
        with open(fname) as infile:
            for line in infile:

                # Remove all numbers and emails
                removeNum = re.sub(r'\d+', '', line)
                removeEmails = re.sub(r'\S*@\S*\s?', '', removeNum)
                outfile.write(removeEmails)

print(outfile)


# Testing strings
# removeNum = re.sub(r'\d+', '', '123hello 456world alma@gmail.com asdasf d 32fwdv asfv544243mdgsv')
# removeEmails = re.sub(r'\S*@\S*\s?', '', removeNum)
# print(removeEmails)
