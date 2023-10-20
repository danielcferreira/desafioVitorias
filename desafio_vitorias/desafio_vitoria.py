

def desafioVitoria(nome, numVitoria):
    if numVitoria < 10:
        return print('{} esta no nivel ferro com {} vitorias  '.format(nome,numVitoria))
    elif numVitoria > 10 and numVitoria < 20:
        return print('{} esta no nivel Bronze com {} vitorias  '.format(nome,numVitoria))
    elif numVitoria > 20 and numVitoria < 50:
        return print('{} esta no nivel prata com {} vitorias  '.format(nome,numVitoria))
    elif numVitoria > 50 and numVitoria < 80:
        return print('{} esta no nivel ouro com {} vitorias  '.format(nome,numVitoria))
    elif numVitoria > 80 and numVitoria < 90:
        return print('{} esta no nivel Diamante com {} vitorias  '.format(nome,numVitoria))
    elif numVitoria > 90 and numVitoria < 100:
        return print('{} esta no nivel lendario com {} vitorias  '.format(nome,numVitoria))
    else:
        return print('{} esta no nivel imortal com {} vitorias  '.format(nome,numVitoria))
        
   
    
    
desafioVitoria('ronald', 110)
