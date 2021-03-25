'''
    Funcion que permite ver si una persona es mutante o no,
    tiene como parametro una lista y devuelve True si es mutante
    o False si no lo es
'''
def Mutant(adn):
    try:
        '''
            Funcion que permite verificar si la matriz es correcta
            siendo NxN y que solo tenga las letras A T C G.
            Devuelve True si todo esta correcto
        '''
        def check(adn):
            contador=0
            verificacion=0
            for elemento in adn:
                for letra in elemento:
                    if letra=="A" or letra=="T" or letra=="C" or letra=="G":
                        contador+=1
                if contador!=len(adn):
                    raise Exception
                else:
                    verificacion+=1
                    contador=0
            return verificacion==len(adn)
        '''
            Esta funcion permita verificar si es mutante
            de manera horizontal
        '''
        def is_mutant_horizontal(adn):
            mutacion=False
            for elemento in adn:
                for letra in elemento:
                    if elemento.count(letra)>=4:
                        mutan=letra+letra+letra+letra
                        if mutan in elemento:
                            mutacion= True
                            break
            return mutacion
        '''
            Esta funcion permite crear una nueva lista con los 
            valores verticales y se aplica
            la funcion is_mutant_horizontal
        '''
        def is_mutant_vertical(adn):
            vertical=""
            new_adn=[]
            for i in range(len(adn)):
                for a in range(len(adn)):
                    vertical+=adn[a][i]
                new_adn.append(vertical)
                vertical=""
            return is_mutant_horizontal(new_adn)
        '''
            funcion que permite encontrar las diagonales de la matriz
        '''
        def get_diagonals(matrix):
            n = len(matrix)
            # diagonals_1 = []  # lower-left-to-upper-right diagonals
            # diagonals_2 = []  # upper-left-to-lower-right diagonals
            for p in range(2*n-1):
                yield [matrix[p-q][q] for q in range(max(0, p - n + 1), min(p, n - 1) + 1)]
                yield [matrix[n-p+q-1][q] for q in range(max(0, p - n + 1), min(p, n - 1) + 1)]
        '''
            Esta funcion permite crear una nueva lista con los 
            valores de todas las diagonales y se aplica
            la funcion is_mutant_horizontal para ver si es mutante
        '''
        def is_mutant_oblicua(adn):    
            new=[]
            new_word=""
            for i in get_diagonals(adn):        
                for element in i:
                    new_word+=element
                new.append(new_word)
                new_word=""       
            return is_mutant_horizontal(new)

        check(adn)
        if is_mutant_horizontal(adn):
            return True
        elif is_mutant_oblicua(adn):
            return True
        elif is_mutant_vertical(adn):
            return True
        else:
            return False

    except Exception:
        return None 


                

