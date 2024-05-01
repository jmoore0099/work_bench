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

# Q2 Following the instructions, write a script that counts duplicate words.
# Techniques like word frequency counting are often used to analyze published work.
# Other document analysis techniques are in natural language processing. Write a
# script that uses a dictionary to determine and print the number of duplicate
# words in a sentence. Treat uppercase and lowercase letters the same and assume
# there is no punctuation in the sentence. Words with counts larger than one have duplicates.
#
# Input Text  is a tongue twister from "John Harris's Peter Piper's
# Practical Principles of Plain and Perfect Pronunciation" (1813):
#
# Peter Piper picked a peck of pickled peppers
# A peck of pickled peppers Peter Piper picked if Peter Piper picked a peck of pickled peppers
# Where is the peck of pickled peppers Peter Piper picked

t_twister = 'Peter Piper picked a peck of pickled peppers ' \
            'A peck of pickled peppers Peter Piper picked if Peter ' \
            'Piper picked a peck of pickled peppers Where is the ' \
            'peck of pickled peppers Peter Piper picked'

tl_twister = t_twister.lower()
peter = (tl_twister.split())
compare = dict()
# print(tl_twister)
for word in peter:
     if word not in compare:
          compare[word] = 1
     else:
          compare[word] = compare[word] + 1

s_compare = dict(sorted(compare.items(), key = lambda x: x[1]))
print('WORD'.ljust(10), 'COUNT'.rjust(10))
for key in s_compare:
     print(key.ljust(10), str(compare[key]).rjust(8))

# Q3 The Python list stores a collection of objects in an ordered
# sequence. In contrast, the dictionary stores objects in an unordered
# collection. Give three examples of real-world objects that can be
# stored in a dictionary.
# 1. Cars amke and model
# 2. Type and number of fish
# 3. a dictionary

# Q4 Which of the following are immutable data structures? Why ? Please explain
# a. dictionaries and lists
# a. strings and tuples

# Strings and tuples are immutable because they can't be changed.
