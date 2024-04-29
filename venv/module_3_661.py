# jmoore
# 20240428

# Module 3 Assignment

# Q1
# What does this code do?
# The dictionary temperatures contain four Fahrenheit samples for each of five days.
# What does the “for” statement do?

temperatures = {
'Monday': [67, 71, 74, 77],
'Tuesday': [52, 56, 66 , 50],
'Wednesday': [77, 80, 87 , 95],
'Thursday': [67, 77, 81 , 77],
'Friday': [54 , 60 , 67, 60],
}
for k, v in temperatures.items():
     print(f'{k}: {sum(v)/len(v):.0f}')


# This code gives an averave of the tempuratures for each day.
# The for stament loops through the dictionary and for each key it averages the values.

# Q2
