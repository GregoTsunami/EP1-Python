"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : Taumanni Ioannou
  NUSP : 13684130

  Referências:
  https://www.obaricentrodamente.com/2021/04/metodo-de-heron-para-calcular-raiz-quadrada.html
  
"""
GRAVIDADE = 9.81
PI = 3.14159265358979323846

def fatorial(n):
    fat = 1
    i = 2
    while i < n+1:
        fat = fat*i
        i = i + 1

    return fat

def seno(theta):
    angulo = theta*(PI/180)
    termoini = angulo - angulo**3/fatorial(3) #primeiro termo da série de taylor
    termoant = 0 #guarda o termo anterior
    sinx = termoini #termo atual
    i = 1
    n = 5
    while abs(sinx - termoant) > 10**-10:
        termoant = sinx
        sinx = sinx + (angulo**n)/fatorial(n)*i
        n = n + 2
        i = i*(-1)
    return sinx


    '''
    Esta função aproxima o valor da função seno para o ângulo theta
    usando a série de Taylor até que o módulo do próximo termo da
    série calculada seja menor 1e-10.
    Entrada: O ângulo theta que deve ser informado em graus.
    Saída: A aproximação do seno do ângulo theta.
    '''

def cosseno(theta):
    angulo = theta*(PI/180)
    termoini = 1 - angulo**2/fatorial(2) #primeiro termo da série de taylor
    termoant = 0 #guarda o termo anterior
    cosx = termoini #termo atual
    k = 1
    n = 4
    while abs(cosx - termoant) > 10**-10:
        termoant = cosx
        cosx = cosx + (angulo**n)/fatorial(n)*k
        n = n + 2
        k = k*(-1)
    return cosx

    '''
    Esta função aproxima o valor da função cosseno para o ângulo theta
    usando a série de Taylor até que o módulo do próximo termo da
    série calculada seja menor 1e-10.
    Entrada: O ângulo theta que deve ser informado em graus.
    Saída: A aproximação do cosseno do ângulo theta.
    '''


def raizQuadrada(x):
    ri = x
    r = 0
    while abs(ri - r) > 10**-10:
        r = ri
        ri = (ri+x/ri)/2
    return r
    '''
    Esta função aproxima o valor da raiz quadrada de x, através da
    fórmula de recorrência r_0 = x e r_{n+1} = 1/2 (r_n+ x/r_n)
    enquanto o módulo da diferença entre os dois últimos valores
    calculados for maior que 1e-10.
    Entrada: O valor de x
    Saída: A aproximação da raiz quadrada de x.
    '''


def atualizaPosicao(x, y, vx, vy, dt):
    xf = x + vx*dt
    yf = y + vy*dt - GRAVIDADE*(dt**2)/2
    return xf, yf
    '''
    Esta função calcula as atualizações das posições de x e y usando
    as velocidades escalares respectivamente dadas por vx e vy.
    Entrada: As posições x e y dadas em metros, as velocidades vx e
    vy em metros por segundo e o intervalo de tempo em segundos.
    Saída: Dois valores: o valor atualizado de x e o valor atualizado de y.
    '''


def atualizaVelocidade(vx, vy, dt):
    vxf = vx
    vyf = vy - GRAVIDADE*dt
    return vxf, vyf
    '''
    Esta função calcula e atualiza as velocidades vx e vy para o
    próximo intervalo de tempo.
    Entrada: As velocidades vx e vy em metros por segundo e o
    intervalo de tempo em segundos.
    Saída: Dois valores: o valor atualizado de vx e o valor atualizado de vy.
    '''

def distanciaPontos(x1, y1, x2, y2):
    d = raizQuadrada((x2-x1)**2 + (y2-y1)**2)
    return d
    '''
    Esta função calcula a distância entre dois pontos (x1, y1) e (x2, y2).
    Entrada: As coordenadas dos pontos do plano (x1, y1) e (x2, y2).
    Saída: A distância entre (x1, y1) e (x2, y2).
    '''



def simulaLancamento (xpokebola, ypokebola, rb, vlancamento, angulolancamento, xpokemon, ypokemon, rp, delta_t):
    temp = 0
    vx = vlancamento * cosseno(angulolancamento)
    vy = vlancamento * seno(angulolancamento)
    xb = xpokebola
    yb = ypokebola
    capture = False
    disMin = distanciaPontos(xpokebola, ypokebola, xpokemon, ypokemon) - (rb + rp)
    xMin = xb
    yMin = yb
    caiu = True

    while caiu and not(capture):
        temp = temp + delta_t
        xb, yb = atualizaPosicao(xb, yb, vx, vy, delta_t)
        vx, vy = atualizaVelocidade(vx, vy, delta_t)
        dist = distanciaPontos(xb, yb, xpokemon, ypokemon) - (rb + rp)

        if dist<disMin:
            distMin = dist
            xMin = xb
            yMin = yb
        if dist <= 0:
            capture = True
            distMin = 0
        if yb <= rb:
            caiu = False

    return capture, distMin, xMin, yMin
    '''
    Esta função simula o lançamento da bola até que ela capture o
    pokemon, ou atinja o chão.
    Entrada: Posição inicial da pokebola (xpokebola e ypokebola), em metros;
    Posição do pokemon (xpokemon e ypokemon), em metros;
    Velocidade escalar, em metros por segundo;
    e ângulo de lançamento, em graus;
    Os raios rb e rp, em metros;
    a granularidade de tempo delta_t usada na simulação, em segundos.
    Saída: Um booleano (True se o lançamento teve sucesso e acertou o 
    pokémon, ou False caso contrário), a menor distância do pokémon à
    pokébola e as coordenadas x e y da pokébola nesta posição mais próxima.
    '''


def main():
    xpokemon = float(input("Digite a coordenada x do pokemon: \n"))
    ypokemon = float(input("Digite a coordenada y do pokemon: \n"))
    rp = float(input("Digite o raio do pokemon (> 0) em metros: \n"))
    rb = float(input("Digite o raio da pokebola (> 0) em metros: \n"))
    delta_t = float(input("Digite a granularidade do tempo da simulacao em segundos: \n"))
    
    T = 1
    capture = False

    while T <= 3 and not(capture):
        print("Tentativa ", T)
        T = T + 1
        xtreinador = float(input("Digite a coordenada x do treinador: \n"))
        xpokebola = xtreinador
        ytreinador = float(input("Digite a coordenada y do treinador: \n"))
        ypokebola = ytreinador
        vlancamento = float(input("Digite a velocidade de lancamento em m/s: \n"))
        angulolancamento = float(input("Digite o angulo de lancamento em graus: \n"))

        capture, distMin, xMin, yMin = simulaLancamento(xpokebola, ypokebola, rb, vlancamento, angulolancamento, xpokemon, ypokemon, rp, delta_t)
        if capture:
            print("A pokebola captura o pokemon")
        else:
            print("A pokebola nao captura o pokemon por ", distMin, "metros, ao passar em ", xMin, yMin)
    #Complete o código da função principal.


# Não altere o código abaixo:
if __name__ == "__main__":
    main()
