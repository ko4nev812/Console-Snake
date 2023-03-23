import time
import keyboard
import random
import subprocess
import os
subprocess.run('', shell=True)
clear = lambda: os.system('cls')

x, y=40, 20

os.system(f'mode con: cols={x+4} lines={y+4}')
print('\0337', end='')


sost_fun='menu'

def game():
    z = [[10, 10, 0], [9, 10, 0], [8, 10, 0]]
    def nap(n, ii):
        if n == 0:
            if ii == 0:
                return '\u2550'  # -
            else:
                return '\u2500'
        else:
            if ii == 0:
                return '\u2551'  # |
            else:
                return '\u2502'
    def appl():
        return([random.randrange(x), random.randrange(y)])
    def sok(u, oc):
        if u >= oc:
            return u % oc
        elif u < 0:
            return oc - abs(u)%oc
        else:
            return u
    
    
    press='d'
    apple = appl()
    
    while True:
        
        
        
        for i in 'wsad':
            if keyboard.is_pressed(i):
                press=i
        
        
        
        
        if press=='d':
            z.insert(0, [sok(z[0][0]+1, x), z[0][1], 0])
        elif press=='a':
            z.insert(0, [sok(z[0][0]-1, x), z[0][1], 0])
        elif press=='s':
            z.insert(0, [z[0][0], sok(z[0][1]+1, y), 1])
        elif press=='w':
            z.insert(0, [z[0][0], sok(z[0][1]-1, y), 1])
        
        
        if z[0][0] == apple[0] and z[0][1] == apple[1]:
            apple=appl()
        else:
            z.pop(len(z)-1)
        
        out = ''
        for iy in range(y):
            for ix in range(x):
                if ix==apple[0] and iy == apple[1]:
                    out+= '+'
                else:
                    prov = False
                    for i in range(len(z))[::-1]:
                        if z[i][0] == ix and z[i][1] == iy:
                            prov = True
                            pi = z[i]
                            pind = i
                    if prov:
                        out += nap(pi[2], pind)
                    else:
                        out += '\u2591'
            out+='\n'
        
        
    
        print('\0338\0337', end='')
        print(out)
        
        time.sleep(0.1)
        if keyboard.is_pressed('esc'):
            global sost_fun
            sost_fun='menu'
            break



def menu():
    cl_menu=[{'text':'Играть', 'x':10, 'y':4}, {'text':'Выход', 'x':10, 'y':5}]
    cl_nom=0
    while True:

        out = ''
        for iy in range(y):
            ix = 0
            while ix < x:
                click=True
                for i in range(len(cl_menu)):
                    if iy == cl_menu[i]['y'] and ix == cl_menu[i]['x']:
                        click=False
                        if cl_nom==i:
                            out+='\033[7m'+cl_menu[i]['text']+'\033[0m'
                        else:
                            out+=cl_menu[i]['text']
                        ix+=len(cl_menu[i]['text'])-1
                        
                if click:
                    out+='\u2591'
                ix+=1
        

                
                
                
                
                
            out+='\n'

        
    
        print('\0338\0337', end='')
        print(out)
        
        time.sleep(0.1)
        
        
        events_key=['s', 'w', 'space']
        events=None
        while events==None:
            for event in events_key:
                if keyboard.is_pressed(event):
                    events = event
                    break
        
        
        if events== 'space':
            if cl_nom == 0:
                global sost_fun
                sost_fun='game'
                break
            elif cl_nom == 1:
                exit()
        if events == 'w':
            if cl_nom > 0:
                cl_nom -= 1
        if events == 's':
            if cl_nom <len(cl_menu)-1:
                cl_nom += 1
                
while True:
    if sost_fun == 'menu':
        menu()
    elif sost_fun == 'game':
        game()