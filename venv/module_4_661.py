# 20240430
# jmoore
import os
from faker import Faker

fake = Faker()
names = [fake.name() for names in range(50)]
print(names)
with open('file.txt', 'w') as file:
        for line in names:
            file.write(line)

# Q1
# Write a code segment that opens a file named file.txt for
# input and prints the number of lines in that file.

with open('file.txt') as file:
    for line in file:
        print(line)



