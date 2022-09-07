import random
from player import *

def ia(self):
    jogadaIA = str(random.randint(1, 9))

    if jogadaIA == '1':
        if self.TA1 == 'A __':
            self.TA1 = 'A  O'
            self.a += 1
            self.abc1 += 1
            self.t1 += 1
            self.tabuleiro()
    if jogadaIA == '2':
        if self.TA2 == '|__|':
            self.TA2 = '|O |'
            self.a += 1
            self.abc2 += 1
            self.tabuleiro()
    if jogadaIA == '3':
        if self.TA3 == '__':
            self.TA3 = 'O'
            self.a += 1
            self.abc3 += 1
            self.t2 += 1
            self.tabuleiro()
    if jogadaIA == '4':
        if self.TB1 == 'B __':
            self.TB1 = 'B  O'
            self.b += 1
            self.abc1 += 1
            self.tabuleiro()
    if jogadaIA == '5':
        if self.TB2 == '|__|':
            self.TB2 = '|O |'
            self.abc2 += 1
            self.b += 1
            self.t1 += 1
            self.t2 += 1
            self.tabuleiro() 
    if jogadaIA == '6':
        if self.TB3 == '__':
            self.TB3 = 'O'
            self.b += 1
            self.abc3 += 1
            self.tabuleiro()
    if jogadaIA == '7':
        if self.TC1 == 'C   ':
            self.TC1 = 'C  O'
            self.c += 1
            self.abc1 += 1
            self.t2 += 1
            self.tabuleiro()
    if jogadaIA == '8':
        if self.TC2 == '|  |':
            self.TC2 = '|O |'
            self.abc2 += 1
            self.c += 1
            self.tabuleiro()
    if jogadaIA == '9':
        if self.TC3 == '  ':
            self.TC3 = 'O'
            self.c += 1
            self.abc3 += 1
            self.t1 += 1
            self.tabuleiro()
            