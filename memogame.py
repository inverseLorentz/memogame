import os
import re
WIDTH = 20 # digits per line printed for corrections when a mistake is made

with open('paths.txt', 'r') as pathfile:
    paths = pathfile.read()
paths_dict = dict(re.split('\s*:\s*', path) for path in paths.splitlines()) # splits on colons with 0-infinity spaces around them

choice = ''
acceptable_indices = [str(i) for i in range(1,len(paths_dict)+1)]
acceptable_names = list(paths_dict.keys())
acceptable_choices = acceptable_indices + acceptable_names # choice indices and names
while choice.lower() not in acceptable_choices:
    print('constant:')
    for i,f in enumerate(list(paths_dict.keys()), start=1):
        print('['+str(i)+']: ' + f.split(':')[0])
    choice = input('>>> ')

if choice in acceptable_indices:
    filename = paths_dict[acceptable_names[int(choice)-1]]
elif choice in acceptable_names:
    filename = paths_dict[choice]

with open(filename, 'r') as file:
    digits = file.read()

print('begin')
attempt = input('>>> ')
if attempt == digits[:len(attempt)] and attempt != '':
    print('success with',max(len(attempt.split('.')[-1]), 0),'digits recalled')
else:
    print('failure with',max(len(attempt.split('.')[-1]), 0),'digits attempted')
    for i in range(0, len(attempt), WIDTH):
        attemptgroup = attempt[i:i+WIDTH]
        digitsgroup = digits[i:i+WIDTH]
        error = ''
        for i in range(len(attemptgroup)):
            if attemptgroup[i] == digitsgroup[i]:
                error += ' '
            else:
                error += '^'
        print(attemptgroup)
        print(error)
print('next 10 digits: '+digits[len(attempt):len(attempt)+10])
input()
