import random
import _bootsubprocess
from player import jogador
from boot import ia

class jogo_da_velha():
    def __init__(self):
        self.TA1 = 'A __'
        self.TA2 = '|__|'
        self.TA3 = '__'
        self.TB1 = 'B __'
        self.TB2 = '|__|'
        self.TB3 = '__'
        self.TC1 = 'C   '
        self.TC2 = '|  |'
        self.TC3 = '  '

        self.a = 0
        self.b = 0
        self.c= 0
        self.abc1 = 0
        self.abc2 = 0
        self.abc3 = 0
        self.t1 = 0
        self.t2 = 0
        
        self.tabuleiro()

        cont =0
        while self.a != 3 or self.b != 3 or self.c !=3 or self.abc1 != 3 or self.abc2 !=3 or self.abc3 !=3 or self.t1 != 3 or self.t2 != 3:
            self.jogada = input('Jogador: ')
            jogador(self)
            ia(self)
            cont = cont + 1
            if cont == 4:
                print('Você perdeu')
                break

    def tabuleiro(self):
        print('    1   2  3\n', self.TA1, self.TA2, self.TA3,'\n',self.TB1, self.TB2, self.TB3,'\n',self.TC1, self.TC2, self.TC3)

    

        
jogo_da_velha()