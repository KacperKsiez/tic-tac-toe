from rich.console import Console
from rich.table import Table
from rich import box
from rich.traceback import install
install()

console = Console()
class Game:
    def __init__(self):
        
        self.layout1=[' ', ' ', ' ']
        self.layout2=[' ', ' ', ' ']
        self.layout3=[' ', ' ', ' ']
        self.tour = 'O'
        
        
    def render_layout(self, infos=True):
        if infos==True:
            table = Table(title=f'Runda dla {self.tour}', show_edge=False,box=box.HEAVY)
            table.add_column(f'{self.tour}', header_style='red', style='red bold')
        else:
            table = Table(title='Kółko i krzyżyk', show_edge=False,box=box.HEAVY)
            table.add_column(' ', header_style='red', style='red bold')
        
        console.clear()
        
        table.add_column('A', header_style='red')
        table.add_column('B', header_style='red')
        table.add_column('C', header_style='red')
        
        table.add_row('1', f'{self.layout1[0]}', f'{self.layout1[1]}', f'{self.layout1[2]}')
        table.add_row('2', f'{self.layout2[0]}', f'{self.layout2[1]}', f'{self.layout2[2]}')
        table.add_row('3', f'{self.layout3[0]}', f'{self.layout3[1]}', f'{self.layout3[2]}')
        
        for i in range(int(console.size.height/2-6)):
                console.print('')
        
        console.print(table, justify='center')
        
    def o_tour(self):
        print('Teraz runda dla - [O]')
        
        abc = str(input('ABC: '))
        number = str(input('123: '))
        
        if not self.isOk(abc, 'abc'):
            return
        if not self.isOk(number, '123'):
            return
        
        if(number=='1'):
            if abc=='a':
                if self.layout1==['O', self.layout1[1], self.layout1[2]] or self.layout1==['X', self.layout1[1], self.layout1[2]]:
                    return
                else:
                    self.layout1=['O', self.layout1[1], self.layout1[2]]
            if abc=='b':
                if self.layout1==[self.layout1[0], 'O', self.layout1[2]] or self.layout1==[self.layout1[0], 'X', self.layout1[2]]:
                    return
                else:
                    self.layout1=[self.layout1[0], 'O', self.layout1[2]]
            if abc=='c':
                if self.layout1==[self.layout1[0], self.layout1[1], 'O'] or self.layout1==[self.layout1[0], self.layout1[1], 'X']:
                    return
                else:
                    self.layout1=[self.layout1[0], self.layout1[1], 'O']
                
        if(number=='2'):
            if abc=='a':
                if self.layout2==['O', self.layout2[1], self.layout2[2]] or self.layout2==['X', self.layout2[1], self.layout2[2]]:
                    return
                else:
                    self.layout2=['O', self.layout2[1], self.layout2[2]]
            if abc=='b':
                if self.layout2==[self.layout2[0], 'O', self.layout2[2]] or self.layout2==[self.layout2[0], 'X', self.layout2[2]]:
                    return
                else:
                    self.layout2=[self.layout2[0], 'O', self.layout2[2]]
            if abc=='c':
                if self.layout2==[self.layout2[0], self.layout2[1], 'O'] or self.layout2==[self.layout2[0], self.layout2[1], 'X']:
                    return
                else:
                    self.layout2=[self.layout2[0], self.layout2[1], 'O']
                
        if(number=='3'):
            if abc=='a':
                if self.layout3==['O', self.layout3[1], self.layout3[2]] or self.layout3==['X', self.layout3[1], self.layout3[2]]:
                    return
                else:
                    self.layout3=['O', self.layout3[1], self.layout3[2]]
            if abc=='b':
                if self.layout3==[self.layout3[0], 'O', self.layout3[2]] or self.layout3==[self.layout3[0], 'X', self.layout3[2]]:
                    return
                else:
                    self.layout3=[self.layout3[0], 'O', self.layout3[2]]
            if abc=='c':
                if self.layout3==[self.layout3[0], self.layout3[1], 'O'] or self.layout3==[self.layout3[0], self.layout3[1], 'X']:
                    return
                else:
                    self.layout3=[self.layout3[0], self.layout3[1], 'O']
        self.tour='X'
        
        return    
        
    def x_tour(self):
        print('Teraz runda dla - [X]')
        
        abc = str(input('ABC: '))
        number = str(input('123: '))
        
        if not self.isOk(abc, 'abc'):
            return
        if not self.isOk(number, '123'):
            return
        
        if(number=='1'):
            if abc=='a':
                if self.layout1==['O', self.layout1[1], self.layout1[2]] or self.layout1==['X', self.layout1[1], self.layout1[2]]:
                    return
                else:
                    self.layout1=['X', self.layout1[1], self.layout1[2]]
            if abc=='b':
                if self.layout1==[self.layout1[0], 'O', self.layout1[2]] or self.layout1==[self.layout1[0], 'X', self.layout1[2]]:
                    return
                else:
                    self.layout1=[self.layout1[0], 'X', self.layout1[2]]
            if abc=='c':
                if self.layout1==[self.layout1[0], self.layout1[1], 'O'] or self.layout1==[self.layout1[0], self.layout1[1], 'X']:
                    return
                else:
                    self.layout1=[self.layout1[0], self.layout1[1], 'X']
                
        if(number=='2'):
            if abc=='a':
                if self.layout2==['X', self.layout2[1], self.layout2[2]] or self.layout2==['O', self.layout2[1], self.layout2[2]]:
                    return
                else:
                    self.layout2=['X', self.layout2[1], self.layout2[2]]
            if abc=='b':
                if self.layout2==[self.layout2[0], 'X', self.layout2[2]] or self.layout2==[self.layout2[0], 'O', self.layout2[2]]:
                    return
                else:
                    self.layout2=[self.layout2[0], 'X', self.layout2[2]]
            if abc=='c':
                if self.layout2==[self.layout2[0], self.layout2[1], 'X'] or self.layout2==[self.layout2[0], self.layout2[1], 'O']:
                    return
                else:
                    self.layout2=[self.layout2[0], self.layout2[1], 'X']
                
        if(number=='3'):
            if abc=='a':
                if self.layout3==['X', self.layout3[1], self.layout3[2]] or self.layout3==['O', self.layout3[1], self.layout3[2]]:
                    return
                else:
                    self.layout3=['X', self.layout3[1], self.layout3[2]]
            if abc=='b':
                if self.layout3==[self.layout3[0], 'X', self.layout3[2]] or self.layout3==[self.layout3[0], 'O', self.layout3[2]]:
                    return
                else:
                    self.layout3=[self.layout3[0], 'X', self.layout3[2]]
            if abc=='c':
                if self.layout3==[self.layout3[0], self.layout3[1], 'X'] or self.layout3==[self.layout3[0], self.layout3[1], 'O']:
                    return
                else:
                    self.layout3=[self.layout3[0], self.layout3[1], 'X']
        self.tour='O'
        
        return
        
    def check(self):
        
        both=[]
        
        x_check1=[]
        x_check2=[]
        x_check3=[]
        
        o_check1=[]
        o_check2=[]
        o_check3=[]
        
        for i in range(3):
            both+=self.layout1[i].replace(' ', '')
        for i in range(3):
            both+=self.layout2[i].replace(' ', '')
        for i in range(3):
            both+=self.layout3[i].replace(' ', '')
        
        if len(both)==9:
            return 'max'
        
        for i in range(3):
            o_check1+=self.layout1[i].replace('X', ' ')
        for i in range(3):
            o_check2+=self.layout2[i].replace('X', ' ')
        for i in range(3):
            o_check3+=self.layout3[i].replace('X', ' ')
        
        for i in range(3):
            x_check1+=self.layout1[i].replace('O', ' ')
        for i in range(3):
            x_check2+=self.layout2[i].replace('O', ' ')
        for i in range(3):
            x_check3+=self.layout3[i].replace('O', ' ')
        
        #O - 1
        if o_check1==['O', 'O', 'O']:
            return 'O'
        if o_check2==['O', 'O', 'O']:
            return 'O'
        if o_check3==['O', 'O', 'O']:
            return 'O'
        #O - 2
        if o_check1[0]=='O' and o_check2[0]=='O' and o_check3[0]=='O':
            return 'O'
        if o_check1[1]=='O' and o_check2[1]=='O' and o_check3[1]=='O':
            return 'O'
        if o_check1[2]=='O' and o_check2[2]=='O' and o_check3[2]=='O':
            return 'O'
        #O - 3
        if o_check1[0]=='O' and o_check2[1]=='O' and o_check3[2]=='O':
            return 'O'
        if o_check1[2]=='O' and o_check2[1]=='O' and o_check3[0]=='O':
            return 'O'
        ###############################
        #X - 1
        if x_check1==['X', 'X', 'X']:
            return 'X'
        if x_check2==['X', 'X', 'X']:
            return 'X'
        if x_check3==['X', 'X', 'X']:
            return 'X'
        #O - 2
        if x_check1[0]=='X' and x_check2[0]=='X' and x_check3[0]=='X':
            return 'X'
        if x_check1[1]=='X' and x_check2[1]=='X' and x_check3[1]=='X':
            return 'X'
        if x_check1[2]=='X' and x_check2[2]=='X' and x_check3[2]=='X':
            return 'X'
        #O - 3
        if x_check1[0]=='X' and x_check2[1]=='X' and x_check3[2]=='X':
            return 'X'
        if x_check1[2]=='X' and x_check2[1]=='X' and x_check3[0]=='X':
            return 'X'
        
    def isOk(self, data, type):
        if type=='abc':
            if(data=='a' or data=='A'):
                return True
            elif(data=='b' or data=='B'):
                return True
            elif(data=='c' or data=='C'):
                return True
            else:
                return False
            
        if type=='123':
            if(data=='1'):
                return True
            elif(data=='2'):
                return True
            elif(data=='3'):
                return True
            else:
                return False
    
    def format(self):
        line = ''
        for i in self.layout1:
            line+=i
        for i in self.layout2:
            line+=i
        for i in self.layout3:
            line+=i
        line+=self.tour
        
        return line

    def unformat(self, line):
        self.layout1=[line[0], line[1], line[2]]
        self.layout2=[line[3], line[4], line[5]]
        self.layout3=[line[6], line[7], line[8]]
        self.tour = line[9]
