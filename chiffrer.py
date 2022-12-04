from hashlib import  sha256

def encryptfile():
    entree = input('nom du fichier')
    sortie = input('fichier sortie')
    key = input('entrez la cle')
    keys = sha256(key.encode('utf-8')).digest()
    with open(entree, 'rb') as f_entree:
        with open(sortie, 'wb') as f_sortie:
            i=0
            while f_entree.peek():
                c = ord(f_entree.read(1))
                j = i%len(keys)
                b = bytes([c^keys[j]])
                f_sortie.write(b)
                i+=1
                

def hackfile():
    entree = input('nom du fichier')
    sortie = input('fichier sortie')
    key = input('entrez la cle')
    keys = sha256(key.encode('utf-8')).digest()
    print(keys)
    with open(entree, 'rb') as f_entree:
        with open(sortie, 'wb') as f_sortie:
            i=0
            while f_entree.peek():
                c = ord(f_entree.read(1))
                j = i%len(keys)
                b = bytes([c^keys[j]])
                f_sortie.write(b)
                i+=1
                
hackfile()