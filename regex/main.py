import re 

name ='ram'

patterns = '^[a-zA-Z]*$'

if re.match(patterns,name):
    print('Match')
else:
    print('Not Match')