Center=open('README_for_start\LKK.txt','r',encoding="UTF-8")
line=Center.readlines()
for i in range(0,63,1):
    print(line[i])
Center.close()
center=input('請輸入你想看的中心代碼= ')
if center=='A':
    for i in range(67,79):
        print(line[i])
else:
    print('tahh')