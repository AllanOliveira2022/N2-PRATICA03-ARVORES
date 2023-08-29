from collections import deque

class Node:
    def __init__(self, valor):
        self.valor = valor 
        self.esquerda = None 
        self.direita = None 
    
    def _repr_(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.valor, self.valor, self.direita and self.direita.valor) 

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
    
    def inserirEmNiveis(self, valor):
        if self.raiz is None:
           self.raiz = Node(valor)
        else:
            self.inserirEmNivelRecursivo(valor, self.raiz)
    
    def inserirEmNivelRecursivo(self, valor, node):
        if valor < node.valor:
            if node.esquerda is None:
                node.esquerda = Node(valor)
            else:
                self.inserirEmNivelRecursivo(valor, node.esquerda)
        else:
            if node.direita is None:
                node.direita = Node(valor)
            else:
                self.inserirEmNivelRecursivo(valor, node.direita) 
    
    def PreOrdem(self):
        if self.raiz is None:
            print("A árvore está vazia")
        else:
            self.preOrdemRecursiva(self.raiz)  
    
    def preOrdemRecursiva(self, node):
        print(node.valor, end = " ")
        if node.esquerda is not None:
            self.preOrdemRecursiva(node.esquerda)
        if node.direita is not None:
            self.preOrdemRecursiva(node.direita)
    
    def PosOrdem(self):
        if self.raiz is None:
            print("A árvore está vazia")
        else:
            self.posOrdemRecursiva(self.raiz)
    
    def posOrdemRecursiva(self, node):
        if node.esquerda is not None:
            self.preOrdemRecursiva(node.esquerda)
        if node.direita is not None:
            self.preOrdemRecursiva(node.direita)
        print(node.valor, end = " ")
    
    def InOrdem(self):
        if self.raiz is None:
            print("A árvore está vazia")
        else:
            self.inOrdemRecursiva(self.raiz)
    
    def inOrdemRecursiva(self, node):
        if node is not None:
            self.inOrdemRecursiva(node.esquerda)
            print(node.valor, end = " ")
            self.inOrdemRecursiva(node.direita)

    def OrdemEmNiveis(self):
        if self.raiz is None:
            print("A árvore está vazia")
        else:
            self.ordemEmNiveisRecursivo(self.raiz)
    
    def ordemEmNiveisRecursivo(self, node):
        a = deque()
        a.append(node)
        
        while len(a):
            node = a.pop()
            if node:
                print(node.valor, end = " ")
            if node.esquerda:
                a.append(node.esquerda)
            if node.direita:
                a.append(node.direita)
           
    
# TESTES
arvore = ArvoreBinaria()
arvore.inserirEmNiveis(5)
arvore.inserirEmNiveis(3)
arvore.inserirEmNiveis(7)
arvore.inserirEmNiveis(2)
arvore.inserirEmNiveis(4)
arvore.inserirEmNiveis(6)
arvore.inserirEmNiveis(8)

print("Percorrendo em Pré-ordem: ")
arvore.PreOrdem()

print("\nPercorrendo em Pós-ordem: ")
arvore.PosOrdem()

print("\nPercorrendo em In-ordem: ")
arvore.InOrdem()

print("\nPercorrendo em Ordem de Níveis: ")
arvore.OrdemEmNiveis()