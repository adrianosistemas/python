import pygame
from pygame.locals import *

preto = (0,0,0)
branco = (255,255,255)
azul = (0,0,255)
verde = (0,255,0)

#utilizado para selecao aleatoria de direcao do fantasma
class PontoDeDecisao(pygame.sprite.Sprite):
    #Funcao construtora
    def __init__(self, x, y, largura, altura, esquerda = True, direita = True, acima = True, abaixo = True, cor = None):
        #Chama o construtor pai
        pygame.sprite.Sprite.__init__(self)

        #Desenha um bloco verde, tamanho especificado nos parametros
        self.imagem = pygame.Surface([largura, altura])
        if not cor is None:
            self.imagem.fill(cor)
        else:
            self.imagem.fill(verde)

        self.x = x
        self.y = y
        self.rect = pygame.rect.Rect(x, y, largura, altura)
        
        self.esquerda = esquerda
        self.direita  = direita
        self.acima = acima
        self.abaixo = abaixo
        self.ativo = True
        
        
class PontosDeDecisao(object):
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.lista_pontos = []
        
    def criarObjeto(self, x, y, largura, altura, esquerda = True, direita = True, acima = True, abaixo = True, cor = None):
        ponto = PontoDeDecisao(x, y, largura, altura, esquerda, direita, acima, abaixo, cor)
        self.lista_pontos.append(ponto)
        return ponto
    
    def criarPonto(self, casaX, casaY, qtdeX, qtdeY, coeficienteMultipl = 50, lado = 5, esquerda = True, direita = True, acima = True, abaixo = True, cor = None):
        if cor == None:
            cor = verde
        ponto = None
        for x in range(qtdeX):
            for y in range(qtdeY):
                ponto = self.criarObjeto( (x + casaX - 1) * coeficienteMultipl + ((coeficienteMultipl - lado)/2), 
                                          (y + casaY - 1) * coeficienteMultipl + ((coeficienteMultipl - lado)/2), 
                                           lado, lado, esquerda, direita, acima, abaixo, cor)
        return ponto
    
    
    def mostrarTodos(self):
        for ponto in self.lista_pontos:
            self.screen.blit(ponto.imagem, (ponto.x, ponto.y))
    
    def verificarColisoes(self, personagem):
        colidiuPonto = None
        for ponto in self.lista_pontos:
            if ponto.ativo:
                if pygame.sprite.collide_rect(personagem, ponto):
                    colidiuPonto = ponto
        return colidiuPonto
    
    def ativar(self):
        for ponto in self.lista_pontos:
            ponto.ativo = True
    
    def desativar(self):
        for ponto in self.lista_pontos:
            ponto.ativo = False
    