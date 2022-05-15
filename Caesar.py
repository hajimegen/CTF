# coding: utf-8
# Your code here!
#def inn =(N,T)
N = int(input())
T = input()
#n = int(len(T))
answer = ''
for letter in T:
        answer += chr(ord('A') + (ord(letter)-ord('A')+N) % 26)
print(answer)

