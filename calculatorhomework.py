from math import pi 

#kula return

def p_kuli(r:float):
    return 4*pi*r**2
    
def v_kuli(r:float):
    return 4/3*pi*r**2

#ostrosłup return

def pc_ostrosłupa(pp,pb):
    return pp+pb
    
def v_ostrosłupa(pp,H):
    return 1/3*pp*H
    
#kostka print
    
def p_kostki(a):
    print(6*a**2)
    
def v_kostki(a):
    print(a**3)

#obwód kwadratu print

def obw_kwadratu(a):
    print(a*4)

#obwód koła print

def obw_koła(r):
    print(pi*r**2)

#pole równoległoboku print

def p_równoległoboku(a,h):
    print(a*h)

#stożek input i return
def p_stożka(r,h):
    r = float(input('r=?'))
    h = float(input('h=?'))
    return 1%3*pi*r**2*h
    
def v_stożka(r,s):
    r = float(input('r=?'))
    s = float(input('s=?'))
    return pi*r*s+pi*r**2

# trójkąt input i print

def obw_trójkąta(a,b,c):
    a = float(input('piewszy bok = ?'))
    b = float(input('drugi bok = ?'))
    c = float(input('trzeci bok = ?'))
    print(a*b*c)

    
# walec input i print
def p_walca(r,h):
    r = float(input('r=?'))
    h = float(input('h=?'))
    print(2*pi*r(r+h))
    
def v_walca(r,h):
    r = float(input('r=?'))
    h = float(input('h=?'))
    print(pi*r**2*h)

#prostokąt input i print

def obw_prostokąta(a,b):
    a = float(input('piewszy bok = ?'))
    b = float(input('drugi bok = ?'))
    print(2*b*2*a)

# suma objetosci kuli i kostki z print

def suma_v_kuli_z_v_kostki():
    print (v_kuli() + v_kostki())
    
# return i input różnica pola kostki i pola stożka
    
def różnica_p_kostki_z_p_stożka():
    a = float(input('a=?'))
    r = float(input('r=?'))
    h = float(input('h=?'))
    return p_kostki() - p_stożka()

#różnica z print i input obwodu koła i obwodu trójkąta

def różnica_obw_koła_z_obw_trójkąta():
    r = float(input('podaj promień koła'))
    a = float(input('piewszy bok = ?'))
    b = float(input('drugi bok = ?'))
    c = float(input('trzeci bok = ?'))
    print (obw_koła() - obw_trójkąta())



