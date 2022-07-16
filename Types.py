from importlib.resources import open_text
from pydoc import importfile


print('「類型」如下(請輸入代碼): ')
print('顯示者=A')
print('顯示生產者=B')
print('生產者=C')
print('投射者=D')
print('反映者=E')
a=input('類型代碼: ')

if a=="A":
    Menfestor=open("C:\\Users\\Owner\\Documents\\GitHub\\-\\Types_txt\\Menfestor.txt","r",encoding="utf-8")
    print(Menfestor.read())
    Menfestor.close
elif a=="B" or a=="C":
    Manifesting_Generator=open("C:\\Users\\Owner\\Documents\\GitHub\\-\\Types_txt\\Manifesting_Generator.txt","r",encoding="utf-8")
    print(Manifesting_Generator.read())
    Manifesting_Generator.close
elif a=="D":
    Projector=open("C:\\Users\\Owner\\Documents\\GitHub\\-\\Types_txt\\Projector.txt","r",encoding="utf-8")
    print(Projector.read())
    Projector.close
elif a=="E":
    Reflector=open("C:\\Users\\Owner\\Documents\\GitHub\\-\\Types_txt\\Reflector.txt","r",encoding="utf-8")
    print(Reflector.read())
    Reflector.close
else:
    print("輸入的只能是A、B、C、D、E，Problems?")
