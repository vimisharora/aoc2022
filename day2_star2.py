file1 = open("d2s1.txt") 
files= file1.read()
inputs=files.splitlines()
# print(inputs)
# x is lose , y is draw and z is win
score=0
for i in inputs:
    o,m=i.split(" ")

    if m=='X':
        score+=0
        if o=='A': #rock so we had sissors
            score+=3
        elif o=='B':# paper - rock
            score+=1
        elif o=='C':
            score+=2

    elif m=='Y':
        score+=3
        if o=='A':
            score+=1
        elif o=='B':
            score+=2
        elif o=='C':
            score+=3

    elif m=='Z':
        score+=6
        if o=='A':
            score+=2
        elif o=='B':
            score+=3
        elif o=='C':
            score+=1
print(score)