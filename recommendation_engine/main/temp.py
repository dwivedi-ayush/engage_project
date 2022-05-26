# contents = []
# while True:
#     try:
#         line = input()
#     except EOFError:
#         break
#     contents.append(line.strip())
# lst=[]    
# for i in contents:
#     if(i != ""):
#         lst.append(i)
# print('"cast":["',end='')        
# print(*lst, sep = '", "',end='')  
# print('"],')
# print('        "length":,')

a=input()
b=a.split(";")
for i in b:
    print('"',end='')
    print(i,end='')
    print('"',end=',')