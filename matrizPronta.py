#Variaveis Globais do código
matrix = []#Esse é o "m" nas funções, Aqui onde vai ser montado a matriz
vazio = "_"
Alocado = "X"
max_esp = 0
brc_esp = max_esp

tempo = "T"
tempo_vazio = "E"
tempo_vazioI = "I"

#========Funções do código========#
def matrix_setup(m): #Função para montar o array de espaços
    posx = input("Coloque número de colunas: \n")
    while not posx.isdigit():
        print('Coloque apenas números')
        posx = input("Coloque número de colunas: \n")

    posy = input("Coloque número de linhas:\n")
    while not posy.isdigit():
        print('Coloque apenas números')
        posx = input("Coloque número de linhas:\n")
    x = int(posx) #Transforma a pergunta em int
    y = int(posy) #Transforma a pergunta em int
    if x == 0:
        print('Não consigo fazer coluna = 0')
        matrix_setup(m) #Para não fazer a matriz bugado
    if y == 0:
        print('Não consigo fazer linha = 0')
        matrix_setup(m)
    espaço_maximo = x*y
    espaço_branco = espaço_maximo

    #Adiciona espaços vazios
    ## Gera as matrizes
    for i in range(y):#linha
        a = []
        for j in range(x):#coluna
            a.append("_")
        m.append(a)

    return x, y, espaço_maximo, espaço_branco

#Monta a matrix num formato melhor para o usuário
def print_matrix(m, x, y):
    res = ""
    for i in range(y):
        res+="┃"
        for j in range(x): 
            res += str(m[i][j]) + "┃"
        res += 'linha \n'
    return res

def organiza_Matrix(m, x, y):
    # Organiza a matriz, colocando ou retirando os X.
    spaces = 0
    for i in range(y):
        for j in range(x):
            # Substitui os "E" por "_" 
            if m[i][j] == tempo_vazio:
                m[i][j] = vazio
                spaces+=1

            # Substitui os "T" por "X"
            elif m[i][j] == tempo:
                m[i][j] = Alocado
            
            # Conta o numero de espaços e retorna pela função
            elif m[i][j] == vazio:
                spaces+=1
    return spaces

def limparMatriz():
    for i in range(Y): #Através desse for ele percorre toda a lista 
        for j in range(X):
            matrix[i][j] = vazio #Em todas as posições ele adc o vazio = "_"
    brc_esp = organiza_Matrix(matrix, X, Y) #Organiza a matriz de volta
    return brc_esp #Retorna a organização

def verificaMatriz(): #Essa função verefica se a matriz está vazia
    print(print_matrix(matrix, X, Y))

    volta = True
    for i in range(Y): #Percorre toda a lista 
        for j in range(X):
            if matrix[i][j] == "X":
                volta = False #Se tiver X o return irá retornar False
    
    return volta

def first_fit():
    print(print_matrix(matrix, X, Y)) #Printa a matriz
    quantity = int(input("Quantidade de memoria a ser alocada: ")) #Pergunta a quantidade

    counter = 0
    ko = True #Esse true serve para parar
    for i in range(Y):
        for j in range(X): #Percorre a matriz
            if matrix[i][j] == '_': #Verefica se tem nada naquela posição
                counter += 1 #Adiciona ao contdor
                if counter == quantity:
                    matrix[i][j] = tempo #Na posição que foi colocado o ultimo contador recebe "T"
                    searching = False
                    break
            elif ko:
                counter = 0

        #Nessa parte o programa
    counter = 0
    while counter < quantity -1:
        # Nao sei o porque do -1, mas funcionou então está ótimo kk
        for i in range(Y):
            for j in range(X):
                try:
                    if matrix[i][j] == tempo:
                        matrix[prev_i][prev_j] = tempo
                    prev_i = i
                    prev_j = j
                except:
                    counter = quantity
        counter += 1
    if searching: #Se não Houver espaço ele retorna
        print("Espaço insuficiente.")
    brc_esp = organiza_Matrix(matrix, X,Y) #Atualiza a matriz
    return brc_esp #Retorna a matriz

def best_fit():
    print(print_matrix(matrix, X, Y)) #Mostra a matriz do antes do best acontecer
    quantity = int(input("Quantidade de memoria a ser alocada: ")) # Pergunta para o usuário quanto de memoria ele quer adc

    contador = 0
    counter_offset = 0
    counter = 0
    volta = verificaMatriz() #Verifica se a matriz está vazia
    if volta == True:
        first_fit()#Efetua um first fit, pois tem nada na matriz
        return print(print_matrix(matrix, X, Y)) 
        
    P = True
    if quantity > 1: #Se maior q um
        while P:
            prev_i = 0
            prev_j = 0

            next_i = 0
            next_j = 0

            first_i = 0
            first_j = 0

            for i in range(Y): #Verefica a matriz
                for j in range(X):
                    if counter == counter_offset: #Se o contador for igual ao segundo
                        first_i = i #Adc na primeira posição o i e j atual da vereficação
                        first_j = j
                    if j == X - 1: #Se o j estiver na ultima posição
                        next_j = 0 #Adc o proximo valores
                        next_i = i + 1
                    else:
                        next_j = j + 1 #Adc os próximos valores
                        next_i = i
                    if matrix[i][j] == '_': #Se tiver nada conta um
                        counter += 1
                    else:
                        counter = counter_offset #Se não for nenhumas das opções adc no contador o valor do segundo
                    if counter == quantity and P and matrix[next_i][next_j] == "X": #Verefica se está ok para montar
                        counter = counter_offset
                        matrix[first_i][first_j] = "X"
                        P = False #Para parar
                        break
                    prev_i = i 
                    prev_j = j
            counter_offset -= 1
        counter = 0
        #Essa parte é para preencher a matriz com X
    if quantity>1:
        while counter < quantity - 1:
            for i in range(Y): #Percorre a matriz
                for j in range(X):
                    if counter == quantity - 1:
                        break
                    if j == X - 1:
                        next_j = 0
                        next_i = i + 1
                    else:
                        next_j = j + 1
                        next_i = i

                    try:
                        if matrix[i][j] == "X" and matrix[next_i][next_j] == '_':
                            matrix[next_i][next_j] = "X"
                            counter += 1
                    except:
                        counter = quantity
            counter += 1
    #Esse segundo for é para se caso o numero for um ele entra em outras condições
    for i in range(Y):
        if contador == quantity:
            break
        for j in range(X):
            '''if quantity > 1:    #Era uma das ideias do best fit, não conseguimos realizar, mas optamos em deixar o comentário.
                if matrix[i][j] == "X":
                    contador = 0
                elif j == X-1:
                    if matrix[i][j] == "_" and matrix[i+1][0] == "X":
                        contador = 0
                elif matrix[i][j] == "_" and matrix[i][j+1] == "X":
                    contador = 0
                elif matrix[i][j] == "_":
                    contador = contador + 1
                    matrix[i][j] = "E" '''

            if quantity == 1: #Verefica se a quantidade é igual a um, pois é um caso especifico.
                if matrix[i][j] == "X": #Se a posição atual for X ele não conta
                    contador = 0
                elif j == X-1:
                    if matrix[i][j] == "_" and matrix[i+1][0] == "_": #Se tiver dois espaços em branco ele não conta
                        contador = 0
                elif matrix[i][j] == "_" and matrix[i][j+1] == "_": #Se tiver dois espaços em branco ele não conta
                    contador = 0
                elif j == X-1:
                    if matrix[i][j] == "_" and matrix[i+1][0] == "X": #Se for a posição correta ele coloca e finaliza o for
                        contador = 1
                        matrix[i][j] = "X"
                elif matrix[i][j] == "_" and matrix[i][j+1] == "X": #Se for a posição correta ele coloca e finaliza o for
                    contador += 1
                    matrix[i][j] = "X"
                    break


    while contador < quantity -1: #Se entrar na condição x>1 ele preenche o código
    
        for i in range(Y):
            for j in range(X):
                try:
                    if matrix[i][j] == tempo:
                        matrix[prev_i][prev_j] = tempo
                    prev_i = i
                    prev_j = j
                except:
                    contador = quantity
        contador += 1
    if quantity > max_esp:
        print("Espaço insuficiente.")
    brc_esp = organiza_Matrix(matrix, X,Y)
    return brc_esp

def worst_fit(brc_esp):
    print(print_matrix(matrix, X, Y))
    quantity = int(input("Quantidade de memoria a ser alocada: "))

    contador = 0
    contador2 = 0

    posx_T = 0
    posy_T = 0

    if brc_esp < quantity:
        brc_esp = organiza_Matrix(matrix, X, Y)
        return brc_esp
    for i in range(Y):
        for j in range(X):
            #contando os espaços vazios...
            if matrix[i][j] == "_":
                contador += 1
            if matrix[i][j] == "X":
                contador = 0
            if contador == 1:
                posx_T = i
                posy_T = j
            if contador > contador2:
                contador2 = contador
    #adicionando o ponto inicial "T"
    matrix[posx_T][posy_T] = tempo

    contador = 0
    while contador < quantity - 1:
        for i in range(Y):
            for j in range(X):
                #adicionando os pontos de memorias a serem alocados
                if contador == quantity - 1:
                    break
                if j == X - 1:
                    prox_jT = 0
                    prox_iT = i + 1
                else:
                    prox_jT = j + 1
                    prox_iT = i

                try:
                    #procurando o maior espaço
                    if matrix[i][j] == "T" and matrix[prox_iT][prox_jT] == vazio:
                        matrix[prox_iT][prox_jT] = tempo
                        contador += 1
                except:
                    contador = quantity
    #função para substituir "T" por "X"
    brc_esp = organiza_Matrix(matrix, X, Y)
    return brc_esp


def desalocacao():
    v = False
    print(print_matrix(matrix, X, Y))

    m_inicial = input('Linha inicial:')
    n_inicial = input('Coluna inicial:')
    # laço para inserir apenas digitos.
    while not m_inicial.isdigit() and not n_inicial.isdigit():
        print("Apenas números")
        m_inicial = input('Linha inicial:')
        n_inicial = input('Coluna inicial:')
    m_final = input('Linha final:')
    n_final = input('Coluna final:')
    while not m_final.isdigit() and not n_final.isdigit():
        print("Apenas números")
        m_final = input('Linha final:')
        n_final = input('Coluna final:')
# transformando em inteiros....
    inicial_X = int(m_inicial) - 1
    inicial_Y = int(n_inicial) - 1
    final_X = int(m_final) - 1
    final_Y = int(n_final) - 1
# marcando os pontos finais e inciais
    matrix[inicial_X][inicial_Y] = tempo_vazioI
    matrix[final_X][final_Y] = tempo_vazio
# se todos os pontos forem iguais...
    if inicial_X == final_X and inicial_Y == final_Y:
        # Ele vai substituir o I por E e depois vai direto para a linha 161.
        matrix[inicial_X][inicial_Y] = tempo_vazio
    else:
        v = True
# se não forem iguais
    while v:
        for i in range(Y):
            for j in range(X):
                #substituindo os pontos a serem retirados por "E"
                if matrix[i][j] == tempo_vazio:
                    if matrix[prev_i][prev_j] == tempo_vazioI:
                        matrix[inicial_X][inicial_Y] = tempo_vazio
                        v = False
                        break
                    matrix[prev_i][prev_j] = tempo_vazio
                prev_i = i
                prev_j = j
    # função para substituir "E" por "X"
    brc_esp = organiza_Matrix(matrix, X, Y)
    return brc_esp

#=================================#
X, Y, max_esp, brc_esp = matrix_setup(matrix)#Pergunta para montar a matrix, ele retorna uma tupla#

#==============MENU===============#
while True:
    #Opções do usuário
    print('='*60)
    print('- '*30)
    print('|1|- First fit ')
    print('|2|- Best fit ')
    print('|3|- Worst fit')
    print('|4|- Desalocação')
    print('|5|- Sair')
    print('- '*30)
    print('-----Funções extras-----')
    print('Fazer nova matriz: |6|')
    print('|7|- Limpar matriz')
    print('- '*30)
    pergunta = input('Qual das opções: ')
    while not pergunta.isdigit(): #Verefica se no input tem apenas números
        print('Apenas Números')
        pergunta = input('Qual das opções: ')
    print('='*60)
    
    pergunta = int(pergunta) #Refaz a matriz
    if pergunta == 6:
        matrix = []
        X, Y, max_esp, brc_esp = matrix_setup(matrix) #Fazer Matriz
        print(print_matrix(matrix, X, Y))
        print(f'Tamanho da Matriz:{max_esp}')


    elif pergunta == 1:
        first_fit()#Função que faz o first fit
        print(print_matrix(matrix, X, Y))
        print(f'Tamanho da Matriz:{max_esp}')
    
    elif pergunta == 2:
        best_fit()
        print(print_matrix(matrix, X, Y)) #Printa a nova matriz
    
    elif pergunta == 3:
        worst_fit(brc_esp)
        print(print_matrix(matrix, X, Y)) #Printa a nova matriz
        
    elif pergunta == 4:
        desalocacao()
        print(print_matrix(matrix, X, Y)) #Printa a nova matriz
        print(f'Tamanho da Matriz:{max_esp}') #Mostra o novo tamanho
    elif pergunta == 5:
        exit() #Sai do programa
    elif pergunta == 7:
        limparMatriz() #Limpa a matriz por completo
#=================================#