file1 = open("d1s1.txt") 
files= file1.read()
inputs=files.splitlines()
elfmax3,elfmax2,elfmax1=0,0,0
elf=(0)
for i in inputs:
    if i=='':
        print(elf)        
        if elfmax3<elf :
            elfmax3=elf
            
        elf=0
    elif int(i):
        elf+=int(i)
    if elfmax3>=elfmax2:
        temp=elfmax2
        elfmax2=elfmax3
        elfmax3=temp
    if elfmax2>=elfmax1:
        temp=elfmax1
        elfmax1=elfmax2
        elfmax2=temp
print(elfmax1+elfmax2+elfmax3)
file1.close()
