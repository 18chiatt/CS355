import functools
import sys
from typing import Counter
import numpy as np

def getCharGrade(x):
    if x <= -15:
        return 'E'
    if x < -5:
        return 'D'
    if x <= 5:
        return 'C'
    if x < 15:
        return 'B'
    return 'A'

lines = list(map(lambda x : (x[:-1] if x[:-1] == '\n' else x).split(' '), open(sys.argv[1]).readlines() ))[1:]
names, scores = [entry[0] + " " + entry[1] for entry in lines], np.vectorize(int)(np.array([ [entry[i] for i in range(3,len(entry))] for entry in lines]))
averages = np.array([ sum(np.vectorize(float)(scores[:,i])) / float(len(scores[:,i])) for i in range(len(scores[0]))])
errors = np.array([ [float(scores[i,j]  - averages[j] )   for j in range(len(scores[i]))] for i in range(len(scores)) ])
letters = np.vectorize(getCharGrade)(errors)
functools.reduce(lambda prev, i: print(names[i], " ", scores[i]), range(len(scores)))

#solved, now just print


for index,average in enumerate(averages):
    print('    Exam ',index+1, " Average: " , "{:.1f}".format(average) )

for index, student in enumerate(names):
    string = functools.reduce(lambda previous, curr : previous + str(scores[index,curr]) + " (" +str(letters[index,curr])+")   ", range(len(scores[0])),'')
    print("    ", names[index], " ", string)

iterableLetters = ["A",'B','C','D','E']
for index in range(len(scores[0])):
    counter = Counter(letters[:,index])
    string = functools.reduce(lambda prev, curr: prev + str(counter[curr]) +"(" + curr + ")    " , iterableLetters, "    Exam " + str(index+1)+ ": ")
    print(string)
