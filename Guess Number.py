import random
S = random.randint(1,100)
import os
print ("Give me a number")
B = 0
while (S != B):
    A = int(input())
    input()
    if (A > S):
        print ("Too big")
    if (A < S):
        print ("Too small")
    if A == S:
        print ("Bingo!")
os.system ("pause")
