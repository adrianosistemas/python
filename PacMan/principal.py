import pygame, comenu, time
from pygame.locals import *

from criarFase1 import *
from criarFase2 import *
from criarFase3 import *

from personagens import *
from ponto_decisao_direcao import *
from variaveis_globais import *

#************************************************************************************************************************************

class Principal:

    def iniciarFantasmasFase1(self, numero):
	if numero == -1 or numero == 0:
	    self.iniciarFantasmas(9, 8, 0)
	if numero == -1 or numero == 1:
	    self.iniciarFantasmas(10, 8, 1)
	if numero == -1 or numero == 2:
	    self.iniciarFantasmas(11, 8, 2)
	if numero == -1 or numero == 3:
	    self.iniciarFantasmas(12, 8, 3)

    def iniciarFantasmasFase2(self, numero):
	if numero == -1 or numero == 0:
	    self.iniciarFantasmas(9, 7, 0)
	if numero == -1 or numero == 1:
	    self.iniciarFantasmas(10, 7, 1)
	if numero == -1 or numero == 2:
	    self.iniciarFantasmas(11, 7, 2)
	if numero == -1 or numero == 3:
	    self.iniciarFantasmas(12, 7, 3)
	
    def iniciarFantasmasFase3(self, numero):
	if numero == -1 or numero == 0:
	    self.iniciarFantasmas(9, 7, 0)
	if numero == -1 or numero == 1:
	    self.iniciarFantasmas(10, 7, 1)
	if numero == -1 or numero == 2:
	    self.iniciarFantasmas(11, 7, 2)
	if numero == -1 or numero == 3:
	    self.iniciarFantasmas(12, 7, 3)
	
	
    def chamarFase1(self, reiniciando):
	# funcoes estao no criarFases.py
	if not reiniciando:
	    self.blocos = criarFase1()
	    self.imagemFase = imagemFase1()
	    self.pontosDecisao = criarPontosDecisaoFase1()
	    self.energias = criarEnergiasFase1()
	    self.pontinhos = criarPontinhosFase1(self.blocos)
	    #self.olhinhos = Personagens(self.blocos)
	    #self.pontoInicialFantasma = Personagens(self.blocos)
	
	self.pacs = Personagens(self.blocos)
	self.iniciarNovaVida(11, 10)

	self.fantasmas = Personagens(self.blocos)
	self.iniciarFantasmasFase1(-1)
	
	
    def chamarFase2(self, reiniciando):
	# funcoes estao no criarFases.py
	if not reiniciando:
	    self.blocos = criarFase2()
	    self.imagemFase = imagemFase2()
	    self.pontosDecisao = criarPontosDecisaoFase2()
	    self.energias = criarEnergiasFase2()
	    self.pontinhos = criarPontinhosFase2(self.blocos)
	
	self.pacs = Personagens(self.blocos)
	
	self.iniciarNovaVida(11, 11)

	self.fantasmas = Personagens(self.blocos)
	self.iniciarFantasmasFase2(-1)
    

    def chamarFase3(self, reiniciando):
	# funcoes estao no criarFases.py
	if not reiniciando:
	    self.blocos = criarFase3()
	    self.imagemFase = imagemFase3()
	    self.pontosDecisao = criarPontosDecisaoFase3()
	    self.energias = criarEnergiasFase3()
	    self.pontinhos = criarPontinhosFase3(self.blocos)

	self.pacs = Personagens(self.blocos)	
	self.iniciarNovaVida(11, 13)

	self.fantasmas = Personagens(self.blocos)
	self.iniciarFantasmasFase3(-1)
	
	
    def __init__(self):
	
        pygame.init()
	pygame.display.set_caption("PacMan")

	self.vg = VariaveisGlobais()
	
	self.tela = (1080, 718)
	self.screen = pygame.display.set_mode(self.tela, 0, 32)
	
	self.vidas = Personagens()
	self.pacs = None
	self.fantasmas = None
	self.energias = None
        self.pontinhos = None
	#self.pontoInicialFantasma = None
	#self.olhinhos = None
	
	self.fase = 1
	self.pontos = 0

	self.entrou_1 = False
	self.entrou_2 = False
	self.entrou_3 = False
	self.entrou_4 = False
	
        self.Inicio()
    
	
    def iniciarContagemVida(self, x, y):
        self.vidas.criarImagemcXcY(x, y, 1, 1, self.vg.lista_imagens_pac)
        
        #pega o numero desse ultimo elemento criado na lista 
        numero = len(self.vidas.lista_personagens)-1
	self.vidas.lista_personagens[numero].tempo_troca_imagem = 50

    
    def iniciarNovaVida(self, x, y, zerar = True):
        #pacs = Personagens(blocos)
	if zerar:
            self.pacs.apagarTodos()
            
        self.pacs.criarImagemcXcY(x, y, 1, 1, self.vg.lista_imagens_pac)
        
        #pega o numero desse ultimo elemento criado na lista 
        numero = len(self.pacs.lista_personagens)-1
        self.pacs.lista_personagens[numero].velocidade = 10
	self.pacs.lista_personagens[numero].tempo_troca_imagem = 50
	self.pacs.lista_personagens[numero].alterarImagemMesmoParado = False
	return self.pacs
    
    
    def iniciarFantasmas(self, x, y, numero = -1):
	ident = numero
	
        ##fantasmas = Personagens(blocos)
        self.fantasmas.criarImagemcXcY(x, y, 1, 1, self.vg.lista_imagens_fantasmas_acima[ident])
        	
	#pega o numero desse ultimo elemento criado na lista 
        numero = len(self.fantasmas.lista_personagens)-1

	self.fantasmas.lista_personagens[numero].ident = ident
        self.fantasmas.lista_personagens[numero].velocidade = 6 + numero * .2
        self.fantasmas.lista_personagens[numero].movx = self.fantasmas.lista_personagens[numero].velocidade
        self.fantasmas.lista_personagens[numero].tempo_troca_imagem = 90
        self.fantasmas.lista_personagens[numero].alterarImagemMesmoParado = True
        ##self.fantasmas.lista_personagens[numero].ciclo_imagem = True	
	
	#self.pontoInicialFantasma.criarImagemcXcY(x, y, 1, 1, self.vg.lista_imagens_olhinhos)
	

    def iniciarOlhinhos(self, x, y):
        self.olhinhos.criarImagemcXcY(x, y, 1, 1, self.vg.lista_imagens_olhinhos)
        
        #pega o numero desse ultimo elemento criado na lista
        numero = len(self.olhinhos.lista_personagens)-1
	
	self.olhinhos.lista_personagens[numero].velocidade = 6 + numero * .2
        self.olhinhos.lista_personagens[numero].movx = self.olhinhos.lista_personagens[numero].velocidade
	self.olhinhos.lista_personagens[numero].tempo_troca_imagem = 50

    
    ###########################################################
    
    def iniciarFase(self, UsarVida = True, com_musica_abertura = True):
	self.entrou_1 = False
	self.entrou_2 = False
	self.entrou_3 = False
	self.entrou_4 = False
	    
        if com_musica_abertura:
            self.vg.tocar(self.vg.som_iniciar_fase, 1)

	if self.fase == 1:
	    self.chamarFase1(False)
	elif self.fase == 2:
	    self.chamarFase2(False)
	elif self.fase == 3:
	    self.chamarFase3(False)
    
        self.redesenharTudo()
        
        time.sleep(self.vg.tempo_iniciar_fase)
	if UsarVida:
	    self.vidas.lista_personagens.remove(self.vidas.lista_personagens[len(self.vidas.lista_personagens)-1])
	
    #################################################################
    
    def ReIniciarFase(self):
        self.pacs.alterarImagensTodos(self.vg.lista_imagens_pac, False)
        #self.vg.tocar(som_reiniciar_fase, 1)

	if self.fase == 1:
	    self.chamarFase1(True)
	elif self.fase == 2:
	    self.chamarFase2(True)
	elif self.fase == 3:
	    self.chamarFase3(True)
	
        self.redesenharTudo()
        
        time.sleep(self.vg.tempo_reiniciar_fase)
	self.vidas.lista_personagens.remove(self.vidas.lista_personagens[len(self.vidas.lista_personagens)-1])
	
    ###########################################################
    
    def redesenharPersonagens(self):
        self.pontinhos.mostrarTodos()
        self.energias.mostrarTodos()
        
        ##redesenha os pontos de escolha
        #self.pontosDecisao.mostrarTodos()
    
        self.pacs.mostrarTodos()
        self.fantasmas.mostrarTodos()
	#self.olhinhos.mostrarTodos()
	
        pygame.display.flip()
    
        
    def redesenharTudo(self):
	
	self.screen.fill((0,0,0))
        self.screen.blit(self.imagemFase, (0,0))

	#self.blocos.mostrarTodos()
	self.vidas.moverTodos()
	self.vidas.mostrarTodos()
	
        self.redesenharPersonagens()

	pygame.display.flip() 
    

    def VerificarFecharFase(self):
        self.vg.tempo_passado = 0
        self.relogio.tick()
	
        while self.vg.tempo_passado < self.vg.tempo_piscar_fase * 1000:
            self.screen.fill((0, 0, 0))
            self.redesenharPersonagens()
            #pygame.display.update()
            time.sleep(.2)
            self.screen.blit(self.imagemFase, (0,0))
            self.redesenharPersonagens()
            #pygame.display.update()
            time.sleep(.2)
            self.vg.tempo_passado += self.relogio.tick()
	
	self.fase += 1
	#if self.fase == 3:
	#    self.chamarFase2()
	
        self.iniciarFase(False, True)
        
        
    #----------------------------------------------------------------------
    # INICIO DO PROGRAMA - PYGAME
    #----------------------------------------------------------------------

    def Inicio(self):
	
	self.iniciarContagemVida(21, 2)
	self.iniciarContagemVida(21, 3)
	self.iniciarContagemVida(21, 4)
	
	self.iniciarFase(True, True)	
	
	self.relogio = pygame.time.Clock()
	self.vg.tempo_passado = 0
	
	sair = False
	while not sair:
	    for evento in pygame.event.get():
		if evento.type == QUIT or evento.type == K_ESCAPE:
		    exit()

	    self.pacs.verificarEventoTodos()
	    
	    self.energias.moverTodos()
	    self.pacs.moverTodos()
		

	    #####################################################################################
	    self.fantasmas.verificarMudancaDirecao(self.pacs, self.pontosDecisao, 3)
	    self.fantasmas.gerarNovasPosicoes(self.pacs)

	    #self.olhinhos.verificarMudancaDirecao(self.pontoInicialFantasma, self.pontosDecisao, 1)
	    #self.olhinhos.gerarNovasPosicoes(self.pontoInicialFantasma)
	    #####################################################################################
	    
	    
	    if self.pacs.lista_personagens[0].poder == 0:
		self.fantasmas.ajustarImagens(self.vg.lista_imagens_fantasmas)
	
	    self.fantasmas.moverTodos()
	    #self.olhinhos.moverTodos()
	    
	    #####################################################################################
	
	    self.energias.verificarColisoes(self.pacs)
	    
	    if len(self.energias.lista_personagens_colididos) > 0:
		self.relogio.tick()
		self.vg.tempo_passado = 0
		guardar_imagens_anteriores = self.pacs.lista_personagens[0].poder == 0
		self.pacs.lista_personagens[0].poder = 1
		
		self.fantasmas.alterarVelocidadeTodos(1.5, 500, guardar_imagens_anteriores)
		self.fantasmas.alterarImagensTodos(self.vg.lista_imagens_fantasma_comer, guardar_imagens_anteriores, 0)
		
		
	    self.energias.apagarColididos(self.vg.som_comer_energia)
	
	    #####################################################################################
	
	    self.pontinhos.verificarColisoes(self.pacs)
	    self.pontinhos.apagarColididos(self.vg.som_pontinho)
	    
	    if len(self.pontinhos.lista_personagens) > 120:
		x=1
	    elif len(self.pontinhos.lista_personagens) > 70:
		self.entrou_3 = True
		self.pacs.lista_personagens[0].velocidade = 8
		for numero in range(len(self.fantasmas.lista_personagens)):
		    if self.fantasmas.lista_personagens[numero].revivido:
			self.fantasmas.lista_personagens[numero].velocidade = 6 + numero * .2
	    elif len(self.pontinhos.lista_personagens) > 40:
		self.entrou_2 = True
		self.pacs.lista_personagens[0].velocidade = 7
		for numero in range(len(self.fantasmas.lista_personagens)):
		    self.fantasmas.lista_personagens[numero].velocidade = 4 + numero * .2
	    elif len(self.pontinhos.lista_personagens) > 10:
		self.entrou_1 = True
		self.pacs.lista_personagens[0].velocidade = 5
		for numero in range(len(self.fantasmas.lista_personagens)):
		    self.fantasmas.lista_personagens[numero].velocidade = 3 + numero * .2
		    
		    
	    
	    if len(self.pontinhos.lista_personagens) + len(self.energias.lista_personagens) == 0:
		self.VerificarFecharFase()
		
	    else:
		
		self.fantasmas.verificarColisoes(self.pacs)
		if len(self.fantasmas.lista_personagens_colididos) > 0:

		    fantasma_colidido = self.fantasmas.lista_personagens_colididos
		    
		    # se energia estah ativa ou acabando
		    if not fantasma_colidido[0].revivido and (self.pacs.lista_personagens[0].poder == 1) or (self.pacs.lista_personagens[0].poder == 2) or (self.pacs.lista_personagens[0].poder == 3):

			#self.iniciarOlhinhos(fantasma_colidido[0].casaX, fantasma_colidido[0].casaY)
			self.fantasmas.apagarColididos(self.vg.som_comer_fantasma, .2)

			if self.fase == 1:
			    self.iniciarFantasmasFase1(fantasma_colidido[0].ident)
			elif self.fase == 2:
			    self.iniciarFantasmasFase2(fantasma_colidido[0].ident)
			elif self.fase == 3:
			    self.iniciarFantasmasFase3(fantasma_colidido[0].ident)
			
			
		    else:
			if len(self.pacs.lista_personagens) > 1:
			    self.pacs.lista_personagens.remove(self.pacs.lista_personagens[0])
			else:
			    self.pacs.alterarImagensTodos(self.vg.lista_imagens_pac_morrer, False)
			    self.vg.tocar(self.vg.som_pacman_morrer, 1)
			    
			    self.vg.tempo_passado = 0
			    self.relogio.tick()
			    
			    self.pacs.lista_personagens[0].angulo_giro = 0
			    self.pacs.lista_personagens[0].movx = 0
			    self.pacs.lista_personagens[0].movy = 0
			    self.pacs.lista_personagens[0].tempo_troca_imagem = 150
			    self.pacs.lista_personagens[0].alterarImagemMesmoParado = True
			    
			    while self.vg.tempo_passado < self.vg.tempo_morte_pac * 1000:
				self.pacs.moverTodos()
				self.redesenharTudo()
				self.vg.tempo_passado += self.relogio.tick()
			    
			    self.pacs.apagarTodos()
			    
			    if len(self.vidas.lista_personagens) > 0:
				self.ReIniciarFase()
			    else:
				sair = True
			    
		if not sair:	    
		    if (self.pacs.lista_personagens[0].poder == 1):
			self.vg.tempo_passado += self.relogio.tick()
			if self.vg.tempo_passado > self.vg.tempo_efeito_energia * 1000:
			    self.fantasmas.piscarImagens(self.vg.lista_imagens_fantasma_piscando)
			    #a energia vai acabar..
			    self.pacs.lista_personagens[0].poder = 2
			    
		    if (self.pacs.lista_personagens[0].poder == 2):
			self.vg.tempo_passado += self.relogio.tick()
			if self.vg.tempo_passado > self.vg.tempo_efeito_energia * 1000 + 3000:
			    self.fantasmas.piscarImagens(self.vg.lista_imagens_fantasma_piscando, 50)
			    #a energia ta quase acabando..
			    self.pacs.lista_personagens[0].poder = 3
    
		    if (self.pacs.lista_personagens[0].poder == 3):
			self.vg.tempo_passado += self.relogio.tick()
			if self.vg.tempo_passado > self.vg.tempo_efeito_energia * 1000 + 5000:
			    self.vg.tempo_passado = 0
			    #energia acabou!
			    self.pacs.lista_personagens[0].poder = 0
			    self.fantasmas.voltarVelocidadeAnteriorTodos()
			    #self.fantasmas.voltarImagensAnteriores(1)
			    
		    self.redesenharTudo()
		    