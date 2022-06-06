def ggg(b):
    for i in a:
        for j in i:
            print(j, end = ' ')
        print()

def hhh(c):
    if a[0][0] == a[0][1] == a[0][2]:
        return a[0][0]
    elif a[2][0] == a[2][1] == a[2][2]:
        return a[2][0]
    elif a[0][0] == a[1][0] == a[2][0]:
        return a[0][0]
    elif a[0][2] == a[1][2] == a[2][2]:
        return a[0][2]
    elif a[2][0] == a[1][1] == a[0][2]:
        return a[2][0]
    elif a[0][0] == a[1][1] == a[2][2]:
        return a[0][0]
    elif a[1][0] == a[1][1] == a[1][2]:
        return a[1][0]
    elif a[0][1] == a[1][1] == a[2][1]:
        return a[0][1]

n = 1
a = [['.','.','.'],['.','.','.'],['.','.','.']]
while True:
    x,y = input('Введите координаты : ').split()
    x,y = int(x), int(y)

    if a[x][y]=='x' or a[x][y]=='0':
        continue
    if n % 2 == 0:
        a[x][y]='0'
    else:
        a[x][y]='x'

    if hhh(a) == 'x':
        print('выйграл x')
        print('Игра закончена')
        break
    elif hhh(a) == '0':
        print('выйграл 0')
        print('Игра закончена')
        break
    n += 1
    ggg(a)




    
        
        
    
    
    
        
    

    
        