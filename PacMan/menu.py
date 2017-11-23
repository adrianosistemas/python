import sys, pygame, comenu
from pygame.locals import *
from personagens import *
from variaveis_globais import *

pygame.init()
pygame.display.set_caption("Menu PacMan")

def opcao1():
	from principal import *
	pr = Principal()
	main()


def opcao2():
	arquivo = open('auxiliares/ranking.txt', 'r')
	pontos = arquivo.read()
	arquivo.close()
	
	screen = pygame.display.set_mode((1024, 718))
	fundo = 'imagens/MENU/ranking.jpeg'
	plano = pygame.image.load(fundo).convert_alpha()
	screen.blit(plano, (0,0))
	
	fonte = pygame.font.Font("auxiliares/Broadway.ttf", 70)
	imagemDaFonte = fonte.render("Recorde:", True, (255,255,255))
	
	pontuacao = fonte.render(str(pontos), True, (211, 198, 20))
	
	screen.blit(imagemDaFonte, (300,100))
	screen.blit(pontuacao, (400,400))
	
	while True:		
		for event in pygame.event.get():
				event.type == pygame.KEYDOWN
				pygame.display.flip()
		pressed_keys = pygame.key.get_pressed()
		if pressed_keys[K_SPACE]:
			return main()
		if pressed_keys[K_ESCAPE]:
			return main()
		if pressed_keys[K_UP]:
			return main()
		if pressed_keys[K_DOWN]:
			return main()
def opcao3():
	creditos = 'imagens/MENU/creditos.jpeg'
	screen = pygame.display.set_mode((1024, 718))
	instrucoes = pygame.image.load(creditos).convert_alpha()
	while 1:
		for event in pygame.event.get():
				event.type == pygame.KEYDOWN
				screen.blit(instrucoes,(0,0))
				pygame.display.flip()
		pressed_keys = pygame.key.get_pressed()
		if pressed_keys[K_SPACE]:
			return main()
		if pressed_keys[K_ESCAPE]:
			return main()
		if pressed_keys[K_UP]:
			return main()
		if pressed_keys[K_DOWN]:
			return main()
		
def opcao4():
	instrucao = 'imagens/MENU/instrucoes.jpeg'
	screen = pygame.display.set_mode((1024, 718))
	instrucoes = pygame.image.load(instrucao).convert_alpha()
	while 1:
		for event in pygame.event.get():
			event.type == pygame.KEYDOWN
			screen.blit(instrucoes,(0,0))
			pygame.display.flip()
		
		pressed_keys = pygame.key.get_pressed()
		if pressed_keys[K_SPACE]:
			return main()
		if pressed_keys[K_ESCAPE]:
			return main()
		if pressed_keys[K_UP]:
			return main()
		if pressed_keys[K_DOWN]:
			return main()

def opcao5():
	about = 'imagens/MENU/sobre.jpeg'
	screen = pygame.display.set_mode((1024, 718))
	sobre = pygame.image.load(about).convert_alpha()
	while 1:
		for event in pygame.event.get():
			event.type == pygame.KEYDOWN
			screen.blit(sobre,(0,0))
			pygame.display.flip()

		pressed_keys = pygame.key.get_pressed()
		if pressed_keys[K_SPACE]:
			return main()
		if pressed_keys[K_ESCAPE]:
			return main()
		if pressed_keys[K_UP]:
			return main()
		if pressed_keys[K_DOWN]:
			return main()
		
def opcao6():
	exit()
	pygame.quit()

	
def iniciarFantasmas(fantasmas, x, y, numero = -1):
        fantasmas.criarImagemcXcY(x, y, 1, 1, vg.lista_imagens_fantasmas_direita[numero])
        
        #pega o numero desse ultimo elemento criado na lista 
        numero = len(fantasmas.lista_personagens)-1
        fantasmas.lista_personagens[numero].velocidade = 2.3
	fantasmas.lista_personagens[numero].ciclo_imagem = True
	
def main():
	
	global vg
	
	vg = VariaveisGlobais()
	vg.tocar("sons/menu.mp3", -1)

	menu = 'imagens/MENU/menu.jpeg'
	
	screen = pygame.display.set_mode((1024, 718))
	
	imagem_menu = pygame.image.load(menu).convert_alpha()

	menu = comenu.CoMenu(
		["Jogar", opcao1],	
		["Recordes",opcao2],
		["Creditos",opcao3],
		["Instrucoes",opcao4],
                ["Sobre",opcao5],
		["Sair", opcao6])

	menu.center_at(480, 460)
	menu.set_font(pygame.font.Font("auxiliares/Broadway.ttf", 40))
	menu.set_highlight_color((211, 198, 20))
	menu.set_normal_color((255, 255, 255))


	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
	linha = 7
	#dinamica no menu
	pacs = Personagens()

	pacs.criarImagemcXcY(0, linha, 1, 1, vg.lista_imagens_pac)
        pacs.lista_personagens[0].velocidade = 2
        pacs.lista_personagens[0].resolver_eventos = False
	pacs.lista_personagens[0].tempo_troca_imagem = 50

	fantasmas = Personagens()
 	iniciarFantasmas(fantasmas, -4, linha, 0)
	iniciarFantasmas(fantasmas, -5, linha, 1)
	iniciarFantasmas(fantasmas, -6, linha, 2)
	iniciarFantasmas(fantasmas, -7, linha, 3)
        
	energia = Personagens()
	energia.criarImagemcXcY(19, linha, 1, 1, vg.lista_imagens_energia)
        #self.energias.lista_personagens[0].alterarImagemMesmoParado = True
	
	# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	sinal = 1
	while 1:
		events = pygame.event.get()
		menu.update(events)

		for e in events:
			if e.type == pygame.QUIT:
				pygame.quit()
				return
		
		screen.blit(imagem_menu,(0,0))
		#screen.fill((0,0,0))
		menu.draw(screen)
		
		# ############################################################################
		
		energia.verificarColisoes(pacs)
		if len(energia.lista_personagens_colididos) > 0:
			energia.apagarColididos()
			sinal = -1
			pacs.lista_personagens[0].angulo_giro = 180
		
			fantasmas.alterarImagensTodos(vg.lista_imagens_fantasma_comer, False)
			fantasmas.alterarVelocidadeTodos(1.6)
			fantasmas.gerarNovasPosicoes(pacs)
		
		if len(fantasmas.lista_personagens) > 0 or pacs.lista_personagens[0].x < 500:
			pacs.lista_personagens[0].movx = pacs.lista_personagens[0].velocidade * sinal
		else:
			pacs.lista_personagens[0].movx = 0
		
		for x in range(len(fantasmas.lista_personagens)):
			fantasmas.lista_personagens[x].movx = fantasmas.lista_personagens[x].velocidade * sinal
		
		energia.moverTodos()
		energia.mostrarTodos()
		
		pacs.moverTodos()
		pacs.mostrarTodos()
		#fantasmas.gerarNovasPosicoes(pacs)
		fantasmas.moverTodos()
		#fantasmas.ajustarImagens(vg.lista_imagens_fantasmas)
		fantasmas.mostrarTodos()
		
		fantasmas.verificarColisoes(pacs)
		fantasmas.apagarColididos()
	
		if len(fantasmas.lista_personagens) == 0:
			sinal = 1
			pacs.lista_personagens[0].angulo_giro = 0
			
		# ############################################################################
		
		pygame.display.flip()
		#pygame.display.update()
		
		
if __name__ == "__main__":
	#pygame.mouse.set_visible(0)
	main()

	