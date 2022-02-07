#!/bin/python3
p = [1, 4, 3, 2, 5]
d = [8, 16, 25, 9, 36]
p1=[]
d2=[]
final_ans=[]
for i in p:
    l = i**2
    p1.append(l)
for n in d:
    k = round(n**(1/2), 3)
    d2.append(k)
#print(p1)
#print(d2)
for t in range(0, len(p1)):
    f_val = round(p1[t] - d2[t], 2)
    final_ans.append(f_val)
print(final_ans)

"""
wanted_ip=[]
ip_values =["192.168.121.50","17.7.8.49", "193.155.145.24", "
"""
'''
INFO ABOUT THE SCRIPT
This script subtract array'P' from array 'D
'''
