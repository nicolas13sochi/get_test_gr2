import random

abcd = 'qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()_+'
pw = ''
for i in range(8): pw += random.choice(abcd)
print(pw)
