def add(x,y):
    z=x+y
    print('add() fonksiyonu ana alan içinde yürütülüyor',__name__)
    return z

x=input('birinci sayıyı giriniz')
y=input('ikinci sayıyı giriniz')

result=add(int(x), int(y))

print(x,'+',y,'=',result)

print("bu kod ana alanda yürütülüyor",__name__)


