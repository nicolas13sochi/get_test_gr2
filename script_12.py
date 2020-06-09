import random

abcd = 'qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()_+'
pw = ''
for i in range(12): pw += random.choice(abcd)
print(pw)
