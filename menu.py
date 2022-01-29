from rich.console import Console
from rich.table import Table
from readchar import readchar

console = Console()

class Menu:
    def __init__(self):
        console.clear()
    
    def main(self):
        choice = 1
        while True:
            console.clear()
            selector1='[cyan bold]<'
            selector2='[cyan bold]<'
            selector3='[cyan bold]<'
            
            line1_1='1'
            line1_2='Singleplayer'
            line2_1='2'
            line2_2='Multiplayer'
            line3_1='3'
            line3_2='Wyjdź'
            table = Table(title='Menu główne')
            table.add_column('Nr', justify='center')
            table.add_column('Nazwa opcji', justify='center')
            table.add_column('Wybór', justify='center')
            
            if choice==1:
                selector2=''
                selector3=''
                line1_1='[green bold]'+line1_1
                line1_2='[green bold]'+line1_2
            elif choice==2:
                selector1=''
                selector3=''
                line2_1='[green bold]'+line2_1
                line2_2='[green bold]'+line2_2
            elif choice==3:
                selector1=''
                selector2=''
                line3_1='[green bold]'+line3_1
                line3_2='[green bold]'+line3_2
            
            table.add_row(line1_1, line1_2, selector1)
            table.add_row(line2_1, line2_2, selector2)
            table.add_row(line3_1, line3_2, selector3)
            
            for i in range(int(console.size.height/2-8)):
                console.print('')
            console.print(table, justify='center')
            
            char = readchar()
            if char=='w' or char=='W':
                choice-=1
            elif char=='s' or char=='S':
                choice+=1
            elif char==' ':
                return choice
            if choice==0:
                choice=1
            elif choice==4:
                choice=3
            
    def multiplayer(self):
        choice = 1
        while True:
            console.clear()
            selector1='[cyan bold]<'
            selector2='[cyan bold]<'
            selector3='[cyan bold]<'
            
            line1_1='1'
            line1_2='Hostuj'
            line2_1='2'
            line2_2='Dołącz'
            line3_1='3'
            line3_2='Wróć'
            table = Table(title='Multiplayer - menu')
            table.add_column('Nr', justify='center')
            table.add_column('Nazwa opcji', justify='center')
            table.add_column('Wybór', justify='center')
            
            if choice==1:
                selector2=''
                selector3=''
                line1_1='[green bold]'+line1_1
                line1_2='[green bold]'+line1_2
            elif choice==2:
                selector1=''
                selector3=''
                line2_1='[green bold]'+line2_1
                line2_2='[green bold]'+line2_2
            elif choice==3:
                selector1=''
                selector2=''
                line3_1='[green bold]'+line3_1
                line3_2='[green bold]'+line3_2
            
            table.add_row(line1_1, line1_2, selector1)
            table.add_row(line2_1, line2_2, selector2)
            table.add_row(line3_1, line3_2, selector3)
            
            for i in range(int(console.size.height/2-8)):
                console.print('')
            console.print(table, justify='center')
            
            char = readchar()
            if char=='w' or char=='W':
                choice-=1
            elif char=='s' or char=='S':
                choice+=1
            elif char==' ':
                return choice
            if choice==0:
                choice=1
            elif choice==4:
                choice=3
    
    def multiplayer_tab(self, host_nick, client_nick):
        console.clear()
        table = Table(title='Poczekalnia')
        table.add_column('Gracz')
        table.add_column('Symbol')
        table.add_row(f'[HOST]{host_nick}', 'O')
        table.add_row(client_nick, 'X')
        for i in range(int(console.size.height/2-8)):
                console.print('')
        console.print(table, justify='center')
        
    
    def game_over(self, text):
        choice = 1
        while True:
            console.clear()
            selector1='[cyan bold]<'
            selector2='[cyan bold]<'
            selector3='[cyan bold]<'
            
            line1_1='1'
            line1_2='Zagraj ponownie'
            line2_1='2'
            line2_2='Menu główne'
            line3_1='3'
            line3_2='Wyjdź'
            table = Table(title=text)
            table.add_column('Nr', justify='center')
            table.add_column('Nazwa opcji', justify='center')
            table.add_column('Wybór', justify='center')
            
            if choice==1:
                selector2=''
                selector3=''
                line1_1='[green bold]'+line1_1
                line1_2='[green bold]'+line1_2
            elif choice==2:
                selector1=''
                selector3=''
                line2_1='[green bold]'+line2_1
                line2_2='[green bold]'+line2_2
            elif choice==3:
                selector1=''
                selector2=''
                line3_1='[green bold]'+line3_1
                line3_2='[green bold]'+line3_2
            
            table.add_row(line1_1, line1_2, selector1)
            table.add_row(line2_1, line2_2, selector2)
            table.add_row(line3_1, line3_2, selector3)
            
            for i in range(int(console.size.height/2-8)):
                console.print('')
            console.print(table, justify='center')
            
            char = readchar()
            if char=='w' or char=='W':
                choice-=1
            elif char=='s' or char=='S':
                choice+=1
            elif char==' ':
                return choice
            if choice==0:
                choice=1
            elif choice==4:
                choice=3
        
        