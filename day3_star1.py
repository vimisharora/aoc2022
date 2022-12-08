file1 = open("day3.txt") 
files= file1.read()
inputs=files.splitlines()
# print(inputs)
file1.close()
def char_position(letter):
    return ord(letter)
counter1,counter2=0,0
score=0
for i in inputs:
    counter1+=1
    n=int(len(i)/2)
    for j in range (n):
        if i[j] in i[n:]:
            counter2+=1
            # print(i[j])
            if i[j].islower()==True:
                score+=(char_position(i[j])-96)
            else:
                score+=(char_position(i[j])-64+26)
            break

print('a')
print (char_position('a')-96)
print('z')
print (char_position('z')-96)
print (char_position('A')-64+26)
print (char_position('Z')-64+26)
print(counter1,counter2)
print(score)
