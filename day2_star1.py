file1 = open("d2s1.txt") 
files= file1.read()
inputs=files.splitlines()
# print(inputs)
score=0
for i in inputs:
    o,m=i.split(" ")


    if (m=='X' and o=='A') or (m=='Y' and o=='B') or (m=='Z' and o=='C'):
        score+=3
    elif (m=='Y' and o=='A') or (m=='Z' and o=='B') or (m=='X' and o=='C'):
        score+=6

    if m=='X':
        score+=1
    elif m=='Y':
        score+=2
    elif m=='Z':
        score+=3
print(score)