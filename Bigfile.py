import rlcompleter

Center=open('README_for_start\LKK.txt','r',encoding="UTF-8")
line=Center.readlines()
for i in range(0,63,1):
    print(line[i])
Center.close()

center=input('請輸入你想看的中心代碼= ')
Center=open('README_for_start\LKK.txt','r',encoding="UTF-8")
line=Center.readlines()

while center=='A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
    if center=='A':
        for i in range(67,79):
            print(line[i])
    elif center=='B':
        for i in range(79,92):
            print(line[i])
    elif center=='C':
        for i in range(92,106):
            print(line[i])
    elif center=='D':
        for i in range(106,124):
            print(line[i])
    elif center=='E':
        for i in range(124,141):
            print(line[i])
    elif center=='F':
        for i in range(141,159):
            print(line[i])
    elif center=='G':
        for i in range(159,180):
            print(line[i])
    elif center=='H':
        for i in range(180,195):
            print(line[i])
    elif center=='I':
        for i in range(195,210):
            print(line[i])
    break
else:
    print('您要輸入代碼(大寫英文)')
    print("1. 頭腦中心 (最上面三角形) (有顏色=黃)                代碼=A")
    print('2. 邏輯中心 (第二個三角形(倒)) (有顏色=綠)            代碼=B')
    print('3. 喉嚨中心 (第三個，正方形) (有顏色=褐)              代碼=C')
    print('4. G中心(自我中心) (第四個，菱形) (有顏色=黃)         代碼=D')
    print('5. 意志力中心 (第五個，小三角形) (有顏色=紅)          代碼=E')
    print('6. 直覺中心 (最左邊，向右指的三角形) (有顏色=褐)  	  代碼=F')
    print('7. 薦骨中心 (中間下面數上來第二個，正方形) (有顏色=紅)  代碼=G')
    print('8. 情緒中心 (最右邊，向左指的三角形) (有顏色=褐)        代碼=H')
    print('9. 根部中心 (最下面的，正方形) (有顏色=褐)              代碼=I')
    center=input('請輸入你想看的中心代碼= ')
    


if center!='A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I':
    print('掰掰~感謝您耐心的觀看')

    
print("資料來源: ",line[211])