from game import *
from menu import *
from network import *

menu_c = Menu()

def click_to_continue(text='Kliknij aby kontynuować...'):
    print(text)
    readchar()

def over(text, ip='0.0.0.0', port=0, nick=''):
    click_to_continue()
    choice = menu_c.game_over(text)
    if choice==1:
        if ip=='0.0.0.0':
            host_multiplayer(nick, port)
        elif ip:
            while True:
                try:
                    join_multiplayer(ip, port, nick)
                except:
                    click_to_continue('Host jeszcze nie zaczął gry...')
                    continue
        else:
            singleplayer()
        
    elif choice==2:
        menu()
    elif choice==3:
        quit()

def host_multiplayer(host_nick='', port=0):
    
    net = Network()
    game = Game()
    
    while not host_nick:
        host_nick = input('Nick: ')
    
    while port==0:
        port = int(input('Port: '))
    
    menu_c.multiplayer_tab(host_nick, 'Oczekiwanie')
    net.wait_for_client('0.0.0.0', port)
    client_nick = net.recv().replace('@!END', '')
    menu_c.multiplayer_tab(host_nick, client_nick)
    net.send(host_nick)
    click_to_continue()
    
    while True:
        net.send(game.format())
        check = game.check()
        
        if check=='O':
            net.send(game.format())
            game.render_layout(False)
            net.close()
            over('Wygrał O', nick=host_nick, port=port)
            return
        elif check=='X':
            net.send(game.format())
            game.render_layout(False)
            net.close()
            over('Wygrał X', nick=host_nick, port=port)
            return
        elif check=='max':
            net.send(game.format())
            game.render_layout(False)
            net.close()
            over('Maksymalna ilość ruchów', nick=host_nick, port=port)
            return
        
        
        game.render_layout()
        if game.tour=='X':
            game.unformat(net.recv())
        elif game.tour=='O':
            game.o_tour()
    
    
def join_multiplayer(ip='', port=0, client_nick=''):
    net = Network()
    
    if not ip:
        ip = input('IP: ')
    if port==0:
        port = int(input('Port: '))
    
    
    while not client_nick:
        client_nick = input('Nick: ')
    
    net.connect(ip, port)
    net.send(client_nick)
    menu_c.multiplayer_tab(net.recv(), client_nick)
    if True:
        game = Game()
        while True:
            game.unformat(net.recv())
            check = game.check()
            if check=='O':
                game.render_layout(False)
                over('Wygrał O', ip=ip, port=port, nick=client_nick)
                net.close()
                return
            elif check=='X':
                game.render_layout(False)
                over('Wygrał X', ip=ip, port=port, nick=client_nick)
                net.close()
                return
            elif check=='max':
                game.render_layout(False)
                over('Maksymalna ilość ruchów', ip=ip, port=port, nick=client_nick)
                net.close()
                return
            game.render_layout()
            if game.tour=='X':
                game.x_tour()
            elif game.tour=='O':
                game.unformat(net.recv())
            net.send(game.format())

def singleplayer():
    game = Game()
    while True:
        check = game.check()
        if check=='O':
            game.render_layout(False)
            over('Wygrał O')
            return
        elif check=='X':
            game.render_layout(False)
            over('Wygrał X')
            return
        elif check=='max':
            game.render_layout(False)
            over('Maksymalna ilość ruchów')
            return
        game.render_layout()
        if game.tour=='X':
            game.x_tour()
        elif game.tour=='O':
            game.o_tour()
        
def menu():
    while True:
        choice = menu_c.main()
        if choice==1:
            singleplayer()
            
        elif choice==2:
            choice = menu_c.multiplayer()
            if choice==3:
                continue
            elif choice==1:
                host_multiplayer()
                quit()
            elif choice==2:
                join_multiplayer()
                quit()
            
        elif choice==3:
            quit()
            
menu()