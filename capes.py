def somme_pairs(l):
    somme=0
    for element in l:
        if (element%2) == 0:
            somme+=element
    return somme

def compte_occ(l,x):
    compteur = 0
    for i in range(len(l)):
        if l[i] == x:
            compteur +=1
    return compteur

def ligne_a_zero(mat):
    for line in mat:
        is_zero = False
        for number in line:
            if number == 0:
                is_zero = True
            else:
                return is_zero
    return is_zero

def colonne_toute_1(mat):
    n = len(mat) #longueur colonne
    p = len(p) #longueur ligne

    for c in range(p):
        prec = True
        for l in range(n):
            if(mat[l][c]) != 1:
                prec = False
                break
        if prec:
            return c
    return None



def lettre_majoritaire(s):
    count = {}
    max = 0
    maxLetter = ""
    for letter in s:
        if letter in count:
            count[letter]+= 1
        else:
            count[letter] = 1

    for letter in count:
        if count[letter] > max:
            max = count[letter]
            maxLetter = letter

    return maxLetter



def fibonacci(n):
    f0 = 0
    f1 = 1
    flist = [f0,f1]

    for i in range(2,n):
        flist.append(flist[i-1]+flist[i-2])
    return flist


def indice_min(li):
    int_min = li[0]
    i_min = 0
    for i in range(len(li)):
        if li[i] < int_min:
            int_min=li[i]
            i_min = i
    return i_min



def zero_sur_lignes(mat):

    for line in mat:
        is_zero = False
        for number in line:
            if number == 0: 
                is_zero = True
                break
        if is_zero == False:
            return False
    return True


def lettre_majoritaire(ch):
    count = {}
    l_max = ""  #letter la plus présente
    c_max = 0   #Nombre d'apparition de la lettre la plus présente
    for letter in ch:
        if letter in count:
            count[letter] +=1
        else :
            count[letter] = 1
    
    for letter in count:
        if count[letter] > c_max:
            c_max = count[letter]
            l_max = letter

    return l_max



def valeur(li,saut):
    return li[saut[1]]-li[saut[0]]


def saut_max_naif(li):
    saut_max = (0,0)
    val_max = li[0]-li[0]
    n = len(li)
    for i in range(n):
        for j in range(i, n):
            if li[j]-li[i] > val_max:
                saut_max = (i,j)
                val_max = li[j]-li[i]
    return saut_max


print(saut_max_naif([2.0,0.2,3.0,5.3,2.0]))