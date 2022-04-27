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
  Turma: Turma 8
  Prof.: Paulo Miranda

  """

print('Modos de operacao: ')
print('1 - Valor presente de um financiamento')
print('2 - Valor minimo da prestacao para valor presente cobrir pagamento a vista')
print('3 - Comparacao de opcoes de pagamento')
print('4 - Tabela comparativa de opcoes de pagamento para taxas variadas')
md = int(input('Numero do modo desejado: \n'))

#modo 1
if md == 1:
    pr = int(input('Valor da prestacao: \n'))
    i = int(input('Taxa de juros: \n'))
    n = int(input('Numero de prestacoes: \n \n'))
    vp = (pr/(i/1000))*(1+(i/1000)-(1/(1+(i/1000))**(n-1)))
    print('Valor Presente:', int(vp))

#modo 2
elif md == 2:
    vv = int(input("Valor a vista: \n"))
    i = int(input("Taxa de juros: \n"))
    n = int(input("Numero de prestacoes: \n \n"))

    pr = vv/n
    vp = (pr/(i/1000))*(1+(i/1000)-(1/(1+(i/1000))**(n-1)))
    mp = (vp*i)/(1+i-(1/((1+i)**(n-1))))
    print("Menor prestacao cujo valor presente do financiamento cobre o valor a vista: ", int(mp))

#modo 3
elif md == 3:
    vv = int(input("Valor a vista: \n"))
    i = int(input("Taxa de juros: \n"))
    pr12 = int(input("Valor da prestacao em 12 vezes: \n"))
    pr24 = int(input("Valor da prestacao em 24 vezes: \n \n"))

    vp12 = (pr12/(i/1000))*(1+(i/1000)-(1/(1 + (i/1000))**(12-1)))
    vp24 = (pr24/(i/1000))*(1+(i/1000)-(1/(1 + (i/1000))**(24-1)))
    print("Valor presente em 12 vezes: ", int(vp12))
    print("Valor presente em 24 vezes: ", int(vp24))
    if vv <= vp12 and vp24:
        print("Numero de parcelas da melhor opcao de pagamento: 1")
    elif vp24 < vp12 and vv:
        print("Numero de parcelas da melhor opcao de pagamento: 24")
    elif vp12 <= vp24 and vv:
        print("Numero de parcelas da melhor opcao de pagamento: 12")
    
    

#modo 4
elif md == 4:
    vv = int(input("Valor a vista: "))
    pr12 = int(input("Valor da prestacao em 12 vezes: "))
    pr24 = int(input("Valor da prestacao em 24 vezes: "))
    seqi = int(input("Inicio da sequencia das taxas: "))
    seqn = int(input("Numero de taxas: "))
    inc = int(input("Incremento de uma taxa para a proxima: "))

    cont = 1
    i = seqi
    print("taxa | a vista | 12 vezes | 24 vezes | decisao")
    while cont <= seqn: 
        vp12 = (pr12/(i/1000))*(1+(i/1000)-(1/(1 + (i/1000))**(12-1)))
        vp24 = (pr24/(i/1000))*(1+(i/1000)-(1/(1 + (i/1000))**(24-1)))

        if vv < vp12 and vp24:
            dc = 1
        elif vp12 < vp24 and vv:
            dc = 12
        elif vp24 < vp12 and vv:
            dc = 24

        print(i, " | ", int(vv), " | ", int(vp12), " | ", int(vp24), " | ", dc)
        i += inc
        cont += 1
