from phoneAndEmail import phoneRegex, emailRegex
import os

matches = []

directory = '/Users/hunterbaker/python/code/automate/regex/phone_nums'
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        with open(os.path.join(directory, filename)) as f:
            text = f.read()
            for groups in phoneRegex.findall(text):
                phoneNum = '-'.join([groups[1], groups[3], groups[5]])
                if groups[8] != '':
                    phoneNum += ' x' + groups[8]
                matches.append(phoneNum)
            for groups in emailRegex.findall(text):
                matches.append(groups[0])

if len(matches) > 0:
    phoneEmail = open('phoneAndEmail.txt', 'w')
    for item in matches:
        phoneEmail.write(f'{item}\n')
else:
    print('No phone numbers or email addresses found.')