#!/usr/bin/env python3

original = [2, 8, 9, 48, 8, 22, -12, 2]

lis = []
for i in original :
    if i > 5 :
        lis.append(i + 2)
    
new_set = set(lis)

print(original)
print(new_set)
