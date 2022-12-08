file1 = open("d1s1.txt") 
files= file1.read()
inputs=files.splitlines()
elfmax=0
elf=(0)
for i in inputs:
    if i=='':
        print(elf)        
        if elfmax<elf:
            elfmax=elf
            
        elf=0
    elif int(i):
        elf+=int(i)
        
print(elfmax)
file1.close()
