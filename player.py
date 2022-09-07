import random
from boot import ia

def jogador(self):
    
    if self.jogada == 'A1':
        if self.TA1 == 'A __':
            self.abc1 += 1
            self.t1 += 1
            self.tabuleiro()
            ia(self)
    if self.jogada == 'A2':
        if self.TA2 == '|__|':
            self.TA2 = '|X |'
            self.a += 1
            self.abc2 += 1
            self.tabuleiro()
            ia(self)
    if self.jogada == 'A3':
        if self.TA3 == '__':
            self.TA3 = 'X'
            self.a += 1
            self.abc3 += 1
            self.t2 += 1
            self.tabuleiro()
            ia(self)

    if self.jogada == 'B1':
        if self.TB1 == 'B __':
            self.TB1 = 'B  X'
            self.b += 1
            self.abc1 += 1
            self.tabuleiro()
            ia(self)
    if self.jogada == 'B2':
        if self.TB2 == '|__|':
            self.TB2 = '|X |'
            self.abc2 += 1
            self.b += 1
            self.t1 += 1
            self.t2 += 1
            self.tabuleiro()
            ia(self)
    if self.jogada == 'B3':
        if self.TB3 == '__':
            self.TB3 = 'X'
            self.b += 1
            self.abc3 += 1
            self.tabuleiro()
            ia(self)

    if self.jogada == 'C1':
        if self.TC1 == 'C   ':
            self.TC1 = 'C  X'
            self.c += 1
            self.abc1 += 1
            self.t2 += 1
            self.tabuleiro()
            ia(self)
    if self.jogada == 'C2':
        if self.TC2 == '|  |':
            self.TC2 = '|X |'
            self.abc2 += 1
            self.c += 1
            self.tabuleiro()
            ia(self)
    if self.jogada == 'C3':
        if self.TC3 == '  ':
            self.TC3 = 'X'
            self.c += 1
            self.abc3 += 1
            self.t1 += 1
            self.tabuleiro()
            ia(self)

