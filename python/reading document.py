variables = {}
import numpy as np

f = open('variables.txt', 'r+')
lines = f.read().splitlines()
f.close()
i = 0
while i < len(lines):
    if '[' not in lines[i+1]:
        varisables.update({lines[i]:int(lines[i+1])})
    else:
        lines[i+1] = lines[i+1].replace("[","")
        lines[i+1] = lines[i + 1].replace("]", "")
        liste = lines[i+1].split(", ")
        list = []
        for eintrag in liste:
            list.append(int(eintrag))
        variables.update({lines[i]: np.asarray(list)})
    i = i+2


print(variables)