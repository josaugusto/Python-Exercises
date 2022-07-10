"""

    Autor: José Augusto 

    Exércicio

        Implemente uma estrutura de pilha estática, para resolver o cálculo de expressões lógicas 
        fornecidas na ordem a ser definida abaixo, considerando a prioridade dos operadores booleanos. 
        A entrada dessas expressões será:

            V para verdadeiro

            F para falso

            ^ para and - prioridade 3

            v para or - prioridade 2

            s para implicação simples - prioridade 1

            d para dupla implicação simples - prioridade 0

            3: infixa com chaves e colchetes

            1: parênteses
            2: colchetes
            3: chaves

V ^ V v F s V
V v F s V
V s V
R: V

[V v V] ^ F
V ^ F
R: F

[V v F] ^ V d F
V ^ V d F
V d F
R: F


V v F ^ V d F
V v F d F
V d F
R: F



V v V ^ F ^ V
V v F ^ F
V v F
R: V

V ^ V v F
V v F
R: V

V ^ V ^ V v F
V ^ V v F
V v F
R: V

{V s V d F ^[V v F s V ^ [V v F]]}
R: F

{V s V d F ^[V v F s V ^ [V ^ F]]}
R: F
"""


def main(ex):
    for i in range(0, len(ex)):
        if ex[i] in 'VF':
            pilhaoperandos.append(ex[i])
            mostrarpilhas()
        elif ex[i] in '^vsd':
            if len(pilhaoperadores) == 0:
                pilhaoperadores.append(operadores[ex[i]])
                mostrarpilhas()
            else:
                if pilhaoperadores[0] > operadores[ex[i]]:
                    pilhaoperadores.insert(0, operadores[ex[i]])
                elif pilhaoperadores[0] <= operadores[ex[i]]:
                    pilhaoperadores.append(operadores[ex[i]])
                mostrarpilhas()
        elif ex[i] == '{': 
            for k, v in operadores.items(): operadores[k] = v*10
        elif ex[i] == '}':
            while len(pilhaoperandos) >= 2: desempilhar()
            for k, v in operadores.items(): operadores[k] = int(v/10)
        elif ex[i] == '[':
            for k, v in operadores.items(): operadores[k] = v*100
        elif ex[i] == ']':
            while len(pilhaoperandos) >= 2: desempilhar()
            for k, v in operadores.items(): operadores[k] = int(v/100)


def conversor(valor):
    for k, v in operadores.items():
        if int(str(valor)[0]) == int(str(operadores[k])[0]):
            return k


def empilhar(v1, op, v2):
    if op == '^':
        if v1 == 'V' and v2 == 'V': pilhaoperandos.append('V') 
        else: pilhaoperandos.append('F') 
    elif op == 'v':
        if v1 == 'F' and v2 == 'F': pilhaoperandos.append('F')
        else: pilhaoperandos.append('V')
    elif op == 's':
        if v1 == 'V' and v2 == 'F': pilhaoperandos.append('F')
        else: pilhaoperandos.append('V')
    elif op == 'd':
        if v1 == v2: pilhaoperandos.append('V')
        else: pilhaoperandos.append('F')
    mostrarpilhas()

    
def desempilhar():
    v2 = pilhaoperandos.pop()
    mostrarpilhas()
    op = conversor(pilhaoperadores.pop())
    mostrarpilhas()
    v1 = pilhaoperandos.pop()
    mostrarpilhas()
    empilhar(v1, op, v2)


def mostrarpilhas():
    for i in range(len(pilhaoperandos)-1, -1, -1):
        print(f'{pilhaoperandos[i]}')
    print('Operandos')
    print()
    
    for i in range(len(pilhaoperadores)-1, -1, -1):
        print(f'{conversor(pilhaoperadores[i])}')
    print('Operadores')
    print('-='*20)


operadores = {
    '^': 4,
    'v': 3,
    's': 2,
    'd': 1
}
pilhaoperandos = []
pilhaoperadores = []

expressão = input().replace(' ', '')
print("Movimentação das Pilhas:")
print()
main(expressão)
while len(pilhaoperandos) >= 2: desempilhar()
print(f'Resposta: {pilhaoperandos[0]}')
