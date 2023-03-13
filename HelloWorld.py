''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
'''
N = int(input())
n = 1

while(n <= N):
    A, B = list(map(str,input().split()))
    if A[-len(B):] == B:
        print("encaixa")
    else:
        print("nao encaixa")
    n+=1