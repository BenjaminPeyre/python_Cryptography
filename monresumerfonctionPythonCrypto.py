from collections import Counter

ALPHABET="abcdefghijklmnopqrstuvwxyz"
CRYPTOGRAMME="pgoyxjizginyigjikuvnnikrpykkiroioeinisgirojytgikioqpsdiregvyokjikeykoyrxoyvrkkvxypjikriziswiroiogimvreiksiksgjsoyjyoxvnnsri"
c=Counter(CRYPTOGRAMME)
freq=c.most_common(10)


def faireUnAlphabet(alphabet):
    dic={}
    for i in range(len(alphabet)):
        dic[alphabet[i]]=i
    return dic

  
def euclide_etendu(m,n):
    if m<n:
        cop=m
        m=n
        n=cop

        r0, r1 =m, n
        u0, v0 =1, 0
        u1, v1 =0, 1

        while r1 != 0:
            q = r0 // r1
            r2, u2, v2 = r0 -q*r1, u0 -q*u1, v0 -q*v1
            r0, u0, v0 = r1, u1, v1
            r1, u1, v1 = r2, u2, v2
        return (r0, u0, v0) #pgcd u v  
dictionnaireContenantAlphabet = faireUnAlphabet(ALPHABET)
def inversemod(nb,mod):
    reste, u, v = euclide_etendu(nb, mod)
    if ((reste == 1) or (reste == -1)):
        for inverse in range(mod):
            un = ((nb * inverse))%mod
            if (un == 1):
                return inverse
            if (un == mod-1):
                return -inverse
    else:
        return False
def retrouveLettreAvecCode(code):
    for lettre in dictionnaireContenantAlphabet:
        if dictionnaireContenantAlphabet[lettre]==code:
            return lettre

dictionnaireContenantAlphabet['p'] #doit retourner 0

def chiffreaffine(cryptogramme,a,b):
    message=""
    for lettre in cryptogramme:
        message+=retrouveLettreAvecCode((a*dictionnaireContenantAlphabet[lettre] + b)%len(dictionnaireContenantAlphabet))
    return message




def dechiffreAffine(message, a, b):
    if (inversemod(a, len(dictionnaireContenantAlphabet)) != False):
        x = inversemod(a, len(dictionnaireContenantAlphabet))
        y = -(x*b)
        return chiffreaffine(message, x, y)
    else:
        return("Message indéchiffrable")
for u in range(26):
    for v in range(26):
        print(dechiffreAffine(CRYPTOGRAMME, u,v), u,v)
        

def ChifCesar(message,cle):
    cryptogramme=''
    for lettre in message:
        decalage=(dictionnaireContenantAlphabet[lettre]+cle)%27
        cryptogramme+=retrouveLettreAvecCode(decalage)
    return cryptogramme


def DeChifCesar(cryptogramme,cle):
    message=''
    for lettre in cryptogramme:
        decalage=(dictionnaireContenantAlphabet[lettre]-cle)%27
        message+=retrouveLettreAvecCode(decalage)
    return message














msgPasChiffrer = "dansuntrouvivaitunhobbitcenetaitpasuntroudeplaisantsaleethumideremplideboutsdeversetduneatmospheresuintantenonplusquuntrousecnusablonneuxsansrienpoursasseoirnisurquoimangercetaituntroudehobbitcequiimpliqueleconfortjrrtolkienbilbolehobbit"
msgEspion = "pgoyxjizginyigjikuvnnikrpykkiroioeinisgirojytgikioqpsdiregvyokjikeykoyrxoyvrkkvxypjikriziswiroiogimvreikcsiksgjsoyjyoxvnnsri"
   
print("\n",dechiffreAffine(msgPasChiffrer, 15, 20))
print("\n",chiffreaffine(msgEspion, 15, 20))