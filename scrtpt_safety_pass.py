import random

abcd = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM1234567890!@#$%^&*()_+'
pw = ''
for i in range(24): pw += random.choice(abcd)
print(pw)
