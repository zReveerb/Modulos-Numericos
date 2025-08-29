import numpy as np
import matplotlib

def malthus (q, n0, r, t):  #Define-se a equação de Malthus
    return q*n0*np.exp(r*t) #r é a taxa de crescimento populacional, t é o tempo em anos
                            #n0 é a população inicial e q é a taxa de geração de lixo por pessoa



def temperatura(x, k, dx, dt):                      #Calcula a distribuição de temperatura para o próximo passo de tempo. Manda lista de temperatura nos pontos (x)
    lista_novos = [273.15+25]                              #Manda o dx (variação de distancia dos pontos), dt (variacao de tempo)
    variacao = np.diff(np.diff(x)) / dx ** 2        #Manda k, coeficiente de condutividade térmica
                                                    # Os extremos de temperatura por padrão são 20 e 60 graus.

    for i in range(1, len(x) - 1):
        lista_novos.append(k * dt * variacao[i - 1] + x[i])

    lista_novos.append(273.15+40)
    return lista_novos






def mt(A, Ea, T, B, C):
    R = 8.314                                        #mt é: A massa da substância que passa para o lixiviado por unidade de tempo.taxa de geração de poluição.
    return A*np.exp(-Ea / (R * T))*B*C                 #A representa a frequencia de colisões entre as moleculas de reaçoes
                                                     #Ea representa a energia de ativação para a reação de decomposiçao ocorrer
                                                     #R é a constante universal dos cases, T é a temperatura no aterro
                                                     #B e C são as concentrações dos reagentes








def chorume(h, s, w, d, q,n0,r,t, p, mt):
    Mt = malthus(q,n0,r,t)                          #h é a taxa anual de chuva na área
    return mt/(h*s+w*d*Mt - p*s + mt)               #S é a área da superfície do aterro sanitário.
                                                    #w é o teor de umidade dos resíduos alimentares em média,
                                                    #d é afração de resíduos no total de lixo (RSM), a partir da tabela
                                                    #M(t) é a massa de lixo gerada ou adicionada ao aterro no ano t
                                                    #p é o coeficiente anual de evoparaçao da umidade
                                                    #mt é: A massa da substância que passa para o lixiviado por unidade de tempo.taxa de geração de poluição.


def aceitavel(C, L):                                #C é a concentraçao de chorume, L é o limite de aceitação dessa concentração
    if  C < L:
        print("CONCENTRAÇÃO DE CHORUME ACEITAVEL")
    else:
        print("CONCENTRAÇÃO DE CHORUME MAIOR QUE O LIMITE")




