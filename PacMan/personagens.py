import pygame
from pygame.locals import *
from variaveis_globais import *

import random
import time
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)

def ajustarVelocidade(personagem):
    if personagem.movx > 0:
        personagem.movx = personagem.velocidade
    elif personagem.movx < 0:
        personagem.movx = -personagem.velocidade
    
    if personagem.movy > 0:
        personagem.movy = personagem.velocidade
    elif personagem.movy < 0:
        personagem.movy = -personagem.velocidade
    
        
class Objeto(pygame.sprite.Sprite):
    #Funcao construtora
    def __init__(self, x, y, lista_imagens = [], largura = 0, altura = 0, cor = None):
        #Chama o construtor pai
        pygame.sprite.Sprite.__init__(self)

        self.ident = 0
        #self.numero = 
        self.x = x
        self.y = y
        
        self.casaX = 0
        self.casaY = 0
        
        self.lista_imagens = lista_imagens
        self.lista_imagens_ant = lista_imagens
        
        self.num_imagem = 0
        self.cor = None
        
        if len(lista_imagens) == 0:
            self.cor = cor
            #Desenha um bloco, tamanho especificado nos parametros
            self.imagem = pygame.Surface([largura, altura])
            if not cor is None:
                self.imagem.fill(cor)
            else:
                self.imagem.fill(blue)
        else:     
            self.imagem = pygame.image.load(self.lista_imagens[self.num_imagem]).convert_alpha()

        self.tam = self.imagem.get_rect()
        self.rect = pygame.rect.Rect(self.x, self.y, self.tam.width, self.tam.height)
        
        self.margem_decisao = 11
        
        self.velocidade = 2
        self.velocidade_ant  = 2
        
        self.sinal_imagem = 1
        self.ciclo_imagem = True
        self.movx = 0
        self.movy = 0
        self.movx_ant = 0
        self.movy_ant = 0
        self.angulo_giro = 0
        self.angulo_giro_ant = 0
        
        self.relogio = pygame.time.Clock()
        self.tempo_passado = 0
        self.tempo_troca_imagem = 120
        self.tempo_troca_imagem_ant = 120
        
        self.poder = 0
        self.alterarImagemMesmoParado = True
        self.revivido = True

        self.ultima_pressionada = None
        
        
    def verificarEvento(self):
        
        pressed_keys = pygame.key.get_pressed()
        
        #ajuste no dia da apresentacao: deveria pegar o tamanho do bloco, mas...
        posx = self.x % 50
        posy = self.y % 50
        dentroX = posx < 50 - self.tam.width+2
        dentroY = posy < 50 - self.tam.height+2
    
        #self.movx_ant = self.movx
        #self.movy_ant = self.movy
                
        #if self.movx <> 0 and dentroX:
        #    self.movx = 0
            #self.ultima_pressionada  = None
        #if self.movy <> 0 and dentroY:
        #    self.movy = 0
            #self.ultima_pressionada  = None
        
        if pressed_keys[K_LEFT] or self.ultima_pressionada == 0:
            self.ultima_pressionada = 0
            if dentroY:
                self.movx = -self.velocidade
                self.movy = 0
                self.angulo_giro = 180
        if pressed_keys[K_RIGHT] or self.ultima_pressionada == 1:
            self.ultima_pressionada = 1
            if dentroY:
                self.movx = +self.velocidade
                self.movy = 0
                self.angulo_giro = 0            
        if pressed_keys[K_UP] or self.ultima_pressionada == 2:
            self.ultima_pressionada = 2
            if dentroX:
                self.movy = -self.velocidade
                self.movx = 0
                self.angulo_giro = 90
        if pressed_keys[K_DOWN] or self.ultima_pressionada == 3:
            self.ultima_pressionada = 3
            if dentroX:
                self.movy = +self.velocidade
                self.movx = 0
                self.angulo_giro = 270
        
        
    def mover(self):
        obj_aux = Objeto(self.x + self.movx, self.y + self.movy, self.lista_imagens)
                
        bateu = False
        if not self.blocos is None:
            bateu = obj_aux.rect.collidelist(self.blocos.lista_personagens) >= 0
            
        if bateu:
            #self.movx = self.movx_ant
            #self.movy = self.movy_ant
            x=0
        else:
            self.x += self.movx
            self.y += self.movy
            self.rect = pygame.rect.Rect(self.x, self.y, self.tam.width, self.tam.height)
            
            self.tempo_passado += self.relogio.tick()
            if self.tempo_passado > self.tempo_troca_imagem:
                self.tempo_passado = 0
                self.relogio.tick()
                if (not (self.movx == 0 and self.movy == 0)) or self.alterarImagemMesmoParado:
                    if self.ciclo_imagem:
                        if self.num_imagem >= len(self.lista_imagens)-1:
                            self.sinal_imagem = -1
                        elif self.num_imagem == 0:
                            self.sinal_imagem = 1
                        
                        self.num_imagem += self.sinal_imagem
                        
                    else:
                        if self.num_imagem == len(self.lista_imagens):
                            self.num_imagem == 0
                        else:
                            self.num_imagem += 1
        
        return not (self.movx == 0 and self.movy == 0)
    
    
    def mostrar(self):
        if len(self.lista_imagens) > 0:
            self.imagem = pygame.image.load(self.lista_imagens[self.num_imagem]).convert_alpha()
            
        self.imagem = pygame.transform.rotate(self.imagem, self.angulo_giro)
        self.screen.blit(self.imagem, (self.x, self.y))

    
    #############################################################################################            
        
    def gerarMovimentoAtrasPacX(self, pac):
        sinal = 1
        if pac.poder > 0:
            sinal = -1
            
        self.pac = pac
        if self.x < pac.x:
            self.movx = +self.velocidade * sinal
            
        elif self.x >= pac.x:
            self.movx = -self.velocidade * sinal

            
    def gerarMovimentoAtrasPacY(self, pac):
        sinal = 1
        if pac.poder > 0:
            sinal = -1
            
        self.pac = pac
        if self.y < pac.y:
            self.movy = +self.velocidade * sinal
        elif self.y >= pac.y:
            self.movy = -self.velocidade * sinal

    def gerarMovimentoAtrasPac(self, pac):
        self.pac = pac
        self.gerarMovimentoAtrasPacX(pac)
        self.gerarMovimentoAtrasPacY(pac)
    
    def gerarMovimentoAleatorio(self, pac):
        if not self.blocos is None:
            if self.movx <> 0:
                fantasma_aux = Objeto(self.x + self.movx, self.y, self.lista_imagens)
                
                if not self.blocos.verificarColisao_N_para_1(fantasma_aux) is None:
                    self.movx = 0
                    self.gerarMovimentoAtrasPacY(pac)
                    #testa e verifica se a mudanca de direcao vai gerar impacto
                    fantasma_aux = Objeto(self.x, self.y + 10*self.movy, self.lista_imagens)
                    
                    if not self.blocos.verificarColisao_N_para_1(fantasma_aux) is None:
                        #altera o sentido do movimento
                        self.movy = -self.movy
                        #
                        fantasma_aux = Objeto(self.x, self.y + 10*self.movy, self.lista_imagens)
                        if not self.blocos.verificarColisao_N_para_1(fantasma_aux) is None:
                            self.movy = 0
                            self.gerarMovimentoAtrasPacX(pac)
            
            elif self.movy <> 0:
                fantasma_aux = Objeto(self.x, self.y + self.movy, self.lista_imagens)
                
                if not self.blocos.verificarColisao_N_para_1(fantasma_aux) is None:
                    self.movy = 0
                    self.gerarMovimentoAtrasPacX(pac)
                    #testa e verifica se a mudanca de direcao vai gerar impacto
                    fantasma_aux = Objeto(self.x + 10*self.movx, self.y, self.lista_imagens)
                    
                    if not self.blocos.verificarColisao_N_para_1(fantasma_aux) is None:
                        #altera o sentido do movimento
                        self.movx = -self.movx 
                        #
                        fantasma_aux = Objeto(self.x + 10*self.movx, self.y, self.lista_imagens)
                        if not self.blocos.verificarColisao_N_para_1(fantasma_aux) is None:
                            self.movx = 0
                            self.gerarMovimentoAtrasPacY(pac)
            else:
                self.gerarMovimentoAtrasPac(pac)

    
    def alterarImagens(self, lista_imagens, guardar_antigas = False):
        self.num_imagem = 0
        
        if guardar_antigas:
            self.lista_imagens_ant = []
            for imagem in self.lista_imagens:
                self.lista_imagens_ant.append(imagem)
            
        self.lista_imagens = lista_imagens
    
        
class Personagens(object):

    def __init__(self, blocos = None, tam_casaX = 0, tam_casaY = 0):
        
        self.blocos = blocos
        self.screen = pygame.display.get_surface()
        self.lista_personagens = []
        self.lista_personagens_colididos = []
        
        if self.blocos is None:
            self.tam_casaX = tam_casaX
            self.tam_casaY = tam_casaY
        else:
            try:
                imagem = pygame.image.load(self.blocos.lista_personagens[0].lista_imagens[0]).convert_alpha()
            except:
                imagem = pygame.Surface([tam_casaX, tam_casaY])
                imagem.fill(blue)
        
            tam = imagem.get_rect()
            self.tam_casaX = tam.width
            self.tam_casaY = tam.height    
        
    def criarRetangulo(self, x, y, largura, altura, cor = None):
        if cor == None:
            cor = blue
        
        bloco = Objeto(x, y, [], largura, altura, cor)
        bloco.screen = self.screen
        bloco.ident = len(self.lista_personagens)
        
        self.lista_personagens.append(bloco)
    
    def criarQuadrado(self, casaX, casaY, qtdeX, qtdeY, coeficienteMultipl = 50, lado = 5, centralizar = True, cor = None):
        if cor == None:
            cor = blue
        for x in range(qtdeX):
            for y in range(qtdeY):
                if not centralizar:
                    self.criarRetangulo( (x + casaX - 1) * coeficienteMultipl
                                        ,(y + casaY - 1) * coeficienteMultipl, lado, lado, cor)
                    
                else:
                    self.criarRetangulo( (x + casaX - 1) * coeficienteMultipl + (coeficienteMultipl - lado)/2 
                                        ,(y + casaY - 1) * coeficienteMultipl + (coeficienteMultipl - lado)/2
                                        ,lado, lado, cor)
                    
    
    def criarImagemcXcY(self, casaX, casaY, qtdeX, qtdeY, lista_imagens, centralizar = True):
        imagem = pygame.image.load(lista_imagens[0]).convert_alpha()
        tam = imagem.get_rect()
        
        if self.tam_casaX == 0 or self.tam_casaY == 0:
            if len(lista_imagens) > 0:
                self.tam_casaX = tam.width 
                self.tam_casaY = tam.height
            
        if self.blocos is None:
            coeficienteMultiplX = 50
            coeficienteMultiplY = 50
        else:
            coeficienteMultiplX = self.blocos.tam_casaX
            coeficienteMultiplY = self.blocos.tam_casaY
        
        for x in range(qtdeX):
            for y in range(qtdeY):
                if not centralizar:
                    personagem = Objeto( (x + casaX - 1) * coeficienteMultiplX
                                        ,(y + casaY - 1) * coeficienteMultiplY
                                        ,lista_imagens)
                else:
                    personagem = Objeto( (x + casaX - 1) * coeficienteMultiplX + (coeficienteMultiplX - tam.width)/2, 
                                         (y + casaY - 1) * coeficienteMultiplY + (coeficienteMultiplY - tam.height)/2
                                         ,lista_imagens)
                    
                personagem.screen = self.screen
                personagem.casaX = casaX
                personagem.casaY = casaY
                personagem.blocos = self.blocos
                personagem.ident = len(self.lista_personagens)
                
                self.lista_personagens.append(personagem)

                
    ######################################################
    
    def verificarEventoTodos(self):
        for personagem in self.lista_personagens:
            personagem.verificarEvento()
    
    def gerarNovasPosicoes(self, pacs):
        for fantasma in self.lista_personagens:
            for pac in pacs.lista_personagens:
                fantasma.gerarMovimentoAleatorio(pac)
    
    def moverTodos(self):
        for personagem in self.lista_personagens:
            personagem.mover()
            #if not self.blocos is None:
            #    personagem.casaX = int(personagem.x / self.blocos.lista_personagens[0].tam.width) + 4
            #    personagem.casaY = int(personagem.y / self.blocos.lista_personagens[0].tam.height) + 4
    
    def mostrarTodos(self):
        for personagem in self.lista_personagens:
            personagem.mostrar()

    def apagarTodos(self):
        self.lista_personagens = []
        #for personagem in self.lista_personagens:
        #    self.lista_personagens.remove(personagem)

    def verificarColisao_N_para_1(self, personagem):
        colidiuPersonagem = None
        
        indice = personagem.rect.collidelist(self.lista_personagens)
        if indice <> -1:
            colidiuPersonagem = self.lista_personagens[indice]
            self.lista_personagens_colididos.append(colidiuPersonagem)
        
        return colidiuPersonagem

    def verificarColisoes(self, classe_personagem):
        self.lista_personagens_colididos = []
        for person1 in classe_personagem.lista_personagens:
            self.verificarColisao_N_para_1(person1)
    
    def apagarColididos(self, nome_arquivo_som = "", tempo = 0):
        vg = VariaveisGlobais()
        
        for personagem in self.lista_personagens_colididos:
            if nome_arquivo_som <> "":
                vg.tocar(nome_arquivo_som, 1)
                time.sleep(tempo)

            self.lista_personagens.remove(personagem)
        
        self.lista_personagens_colididos = []
        
    def alterarImagensTodos(self, lista_imagens, guardar_antigas = True, revivido = True):
        for personagem in self.lista_personagens:
            personagem.alterarImagens(lista_imagens, guardar_antigas)
            personagem.revivido = revivido
    
    def piscarImagens(self, lista_lista_imagens, tempo = 90):
        for personagem in self.lista_personagens:
            if not personagem.revivido:
                personagem.num_imagem = 0
                personagem.lista_imagens = lista_lista_imagens
                personagem.tempo_troca_imagem = tempo
            
    def voltarImagensAnteriores(self, revivido = True):
        for personagem in self.lista_personagens:
            if not personagem.revivido:
                personagem.num_imagem = 0
                personagem.lista_imagens = personagem.lista_imagens_ant
                personagem.revivido = revivido

    def alterarVelocidadeTodos(self, veloc = 1, tempo_troca_img = 500, guardar_antigas = True):
        for personagem in self.lista_personagens:
            if guardar_antigas:
                personagem.velocidade_ant = personagem.velocidade
            personagem.velocidade = veloc
            personagem.tempo_troca_imagem_ant = personagem.tempo_troca_imagem 
            personagem.tempo_troca_imagem = tempo_troca_img
            
            ajustarVelocidade(personagem)
            
    def voltarVelocidadeAnteriorTodos(self):
        for personagem in self.lista_personagens:
            if not personagem.revivido:
                personagem.velocidade = personagem.velocidade_ant
                personagem.tempo_troca_imagem = personagem.tempo_troca_imagem_ant
                
                ajustarVelocidade(personagem)
                
            
    ###########################################################################################################################################

    def verificarMudancaDirecao(self, pacs, pontosDecisao, nivel_encontrar):
        for fantasma in self.lista_personagens:
            #aproxima os personagens - para colidir, devem estar bem juntos
            x = (fantasma.tam.width - fantasma.margem_decisao)/2
            y = (fantasma.tam.height - fantasma.margem_decisao)/2
            fantasma.rect = pygame.rect.Rect(fantasma.x + x, fantasma.y + y, fantasma.margem_decisao, fantasma.margem_decisao)
            
            if pontosDecisao is None:
                ponto = None
            else:
                ponto = pontosDecisao.verificarColisoes(fantasma)
            
            if not ponto is None:
                executar = random.randint(0, 100)
                if executar % nivel_encontrar == 0:
                    if ponto.esquerda or ponto.direita:
                        if fantasma.movy <> 0:
                            #ponto.ativo = False
                            fantasma.movy = 0
                            #n = random
                            n = 0
                            pac = pacs.lista_personagens[n]
                            fantasma.gerarMovimentoAtrasPacX(pac)
                            
                    elif ponto.acima or ponto.abaixo:
                        if fantasma.movx <> 0:
                            #ponto.ativo = False
                            fantasma.movx = 0
                            #n = random
                            n = 0
                            pac = pacs.lista_personagens[n]
                            fantasma.gerarMovimentoAtrasPacY(pac)
                
            #retorna rect normal
            fantasma.rect = pygame.rect.Rect(fantasma.x, fantasma.y, fantasma.tam.width, fantasma.tam.height)

            
    def ajustarImagens(self, lista_imagens_fantasmas):
        for fantasma in self.lista_personagens:
            if fantasma.movx > 0:
                fantasma.alterarImagens(lista_imagens_fantasmas[3][fantasma.ident], False)
            elif fantasma.movx < 0:
                fantasma.alterarImagens(lista_imagens_fantasmas[2][fantasma.ident], False)
            
            if fantasma.movy > 0:
                fantasma.alterarImagens(lista_imagens_fantasmas[1][fantasma.ident], False)
            elif fantasma.movy < 0:
                fantasma.alterarImagens(lista_imagens_fantasmas[0][fantasma.ident], False)
