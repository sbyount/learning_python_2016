import re

str = 'purple alice-b@google.com monkey dishwasher'
# first group: match any word char, plus literal "." or literal"-" + any other chars
# match @
# seconde group: same
# re.search - find the first match of a pattern
match = re.search('([\w.-]+)@([\w.-]+)', str)
if match:
    print match.group()   ## 'alice-b@google.com' (the whole match)
    print match.group(1)  ## 'alice-b' (the username, group 1)
    print match.group(2)  ## 'google.com' (the host, group 2)
print '--------------------'
## Suppose we have a text with many email addresses
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str) ## ['alice@google.com', 'bob@abc.com']
print emails
print '--------------------'
for email in emails:
# do something with each found email string
    print email
print '--------------------'
# Open file
f = open('cdp_data.py', 'r')
# Feed the file text into findall(); it returns a list of all the found strings
strings = re.findall(r'ht+p:/+', f.read())
print strings
f.close()
