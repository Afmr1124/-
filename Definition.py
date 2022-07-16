from configparser import LegacyInterpolation
import linecache


print('「定義」(代碼如下): ')
print(' 一分人 = 1 ')
print(' 二分人 = 2 ')
print(' 三分人 = 3 ')
print(' 四分人 = 4 ')
print(' 無定義 = 5 ')
definition=input('請輸入您的定義代碼 = ')

Definition=open("C:\\Users\\Owner\\Documents\\GitHub\\-\\Definition_txt\\All definition.txt",encoding="utf-8")
line = Definition.readlines()

if definition=="1":
    for i in range(0,11,1):
        print(line[i])
elif definition=="2":
    for i in range(12,31,1):
        print(line[i])
elif definition=="3":
    for i in range(32,48,1):
        print(line[i])
elif definition=="4":
    for i in range(49,60,1):
        print(line[i])
elif definition=="5":
    for i in range(61,63,1):
        print(line[i])
else:
    print('代碼錯誤')
for i in range(63,74,1):
    print(line[i])


        
        



    '''
    for i in range(0,8,1):
        S1=linecache.getlines('C:\\Users\\Owner\\Documents\\GitHub\\-\\Definition_txt\\All definition.txt',i)
        S1=S1
        print(S1)
    Definition.close
    '''