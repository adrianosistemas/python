from personagens import *
from ponto_decisao_direcao import *
from variaveis_globais import *

def iniciarCores():
    global amarelo
    global ciano
    global rosa
    global outro4
    
    global preto
    global branco
    global azul
    global verde
    global vermelho
    
    amarelo = (255, 255, 0)
    ciano = (0, 255, 255)
    rosa = (255, 0, 255)
    outro4 = (50, 100, 155)
    
    preto = (0,0,0)
    branco = (255, 255, 255)
    azul = (0, 0, 255)
    verde = (0, 255, 0)
    vermelho = (255, 0, 0)


    
def imagemFase3():
    return pygame.image.load(lista_imagens_labirintos[0]).convert_alpha()


def IniciarListaLab():
    global lista_imagens_labirintos
    global lista_imagens_blocos
    
    lista_imagens_labirintos = ["imagens/fases/labirinto3.jpg"]
    lista_imagens_blocos = ["Imagens/objetos/bloco1.jpg"]

    
def criarFase3():
    #Laterais
    IniciarListaLab()
    blocos = Personagens()
    blocos.criarImagemcXcY(1, 1, 1, 6, lista_imagens_blocos)
    blocos.criarImagemcXcY(1, 8, 1, 7, lista_imagens_blocos)
    blocos.criarImagemcXcY(2, 14, 19, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(2, 1, 19, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(20, 1, 1, 6, lista_imagens_blocos)
    blocos.criarImagemcXcY(20, 8, 1, 6, lista_imagens_blocos)
    #Lado esquerdo
    blocos.criarImagemcXcY(3, 2, 1, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(3, 4, 2, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(5, 3, 1, 4, lista_imagens_blocos)
    blocos.criarImagemcXcY(5, 8, 1, 3, lista_imagens_blocos)
    blocos.criarImagemcXcY(3, 10, 1, 3, lista_imagens_blocos)
    blocos.criarImagemcXcY(4, 12, 2, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(2, 6, 2, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(2, 8, 2, 1, lista_imagens_blocos)
    #Meio
    blocos.criarImagemcXcY(7, 3, 8, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(7, 5, 3, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(7, 6, 1, 3, lista_imagens_blocos)
    blocos.criarImagemcXcY(8, 8, 6, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(14, 5, 1, 4, lista_imagens_blocos)
    blocos.criarImagemcXcY(12, 5, 2, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(7, 10, 8, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(10, 11, 2, 2, lista_imagens_blocos)
    blocos.criarImagemcXcY(7, 12, 2, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(13, 12, 2, 1, lista_imagens_blocos)
    #Lado direito
    blocos.criarImagemcXcY(18, 2, 1, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(16, 3, 1, 4, lista_imagens_blocos)
    blocos.criarImagemcXcY(17, 4, 2, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(16, 8, 1, 3, lista_imagens_blocos)
    blocos.criarImagemcXcY(18, 10, 1, 3, lista_imagens_blocos)
    blocos.criarImagemcXcY(16, 12, 2, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(18, 6, 2, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(18, 8, 2, 1, lista_imagens_blocos)
    return blocos


def criarPontosDecisaoFase3():
    pontosDecisao = PontosDeDecisao()
    iniciarCores()
    
    pontosDecisao.criarPonto(3, 2, 1, 1, 50, 3, False, True, False, False, vermelho)
    pontosDecisao.criarPonto(8, 2, 1, 1, 50, 3, False, False, False, True, verde)
    
    pontosDecisao.criarPonto(13, 2, 1, 1, 50, 3, False, False, False, True, verde)
    
    pontosDecisao.criarPonto(8, 4, 1, 1, 50, 3, True, False, True, False, azul)
    pontosDecisao.criarPonto(9, 4, 1, 1, 50, 3, True, False, False, True, azul)
    pontosDecisao.criarPonto(12, 4, 1, 1, 50, 3, False, True, False, True, azul)
    pontosDecisao.criarPonto(13, 4, 1, 1, 50, 3, False, True, True, False, azul)
    
    pontosDecisao.criarPonto(7, 5, 1, 1, 50, 3, True, False, False, False, branco)
    pontosDecisao.criarPonto(14, 5, 1, 1, 50, 3, False, True, False, False, branco)
    
    pontosDecisao.criarPonto(2, 7, 1, 1, 50, 3, False, True, False, False, amarelo)
    pontosDecisao.criarPonto(2, 11, 1, 1, 50, 3, False, True, False, False, amarelo)
    
    pontosDecisao.criarPonto(5, 5, 1, 1, 50, 3, False, True, False, False, ciano)
    pontosDecisao.criarPonto(5, 7, 1, 1, 50, 3, True, False, False, False, ciano)
    pontosDecisao.criarPonto(5, 10, 1, 1, 50, 3, False, True, False, False, ciano)
    
    pontosDecisao.criarPonto(7, 10, 1, 1, 50, 3, False, False, True, False, vermelho)
    pontosDecisao.criarPonto(8, 10, 1, 1, 50, 3, False, False, False, True, vermelho)
    pontosDecisao.criarPonto(13, 10, 1, 1, 50, 3, False, False, False, True, vermelho)
    pontosDecisao.criarPonto(14, 10, 1, 1, 50, 3, False, False, True, False, vermelho)
    
    pontosDecisao.criarPonto(16, 5, 1, 1, 50, 3, True, False, False, False, rosa)
    pontosDecisao.criarPonto(16, 7, 1, 1, 50, 3, False, True, False, False, rosa)
    pontosDecisao.criarPonto(16, 10, 1, 1, 50, 3, True, False, False, False, rosa)
    
    pontosDecisao.criarPonto(19, 4, 1, 1, 50, 3, True, False, False, False, outro4)
    pontosDecisao.criarPonto(19, 7, 1, 1, 50, 3, True, False, False, False, outro4)
    pontosDecisao.criarPonto(19, 11, 1, 1, 50, 3, True, False, False, False, outro4)
    
    pontosDecisao.criarPonto(8, 13, 1, 1, 50, 3, False, False, True, False, amarelo)
    pontosDecisao.criarPonto(13, 13, 1, 1, 50, 3, False, False, True, False, amarelo)
    return pontosDecisao


def criarEnergiasFase3():
    energias = Personagens()
    vg = VariaveisGlobais()
    energias.criarImagemcXcY(2, 2, 1, 1, vg.lista_imagens_energia)
    energias.criarImagemcXcY(19, 2, 1, 1, vg.lista_imagens_energia)
    #energias.criarImagemcXcY(2, 13, 1, 1, vg.lista_imagens_energia)
    #energias.criarImagemcXcY(19, 13, 1, 1, vg.lista_imagens_energia)
    energias.criarImagemcXcY(9, 11, 1, 1, vg.lista_imagens_energia)
    energias.criarImagemcXcY(12, 11, 1, 1, vg.lista_imagens_energia)
    
    energias.lista_personagens[0].alterarImagemMesmoParado = True
    energias.lista_personagens[1].alterarImagemMesmoParado = True
    energias.lista_personagens[2].alterarImagemMesmoParado = True
    energias.lista_personagens[3].alterarImagemMesmoParado = True
    
    energias.lista_personagens[0].tempo_troca_imagem = 80
    energias.lista_personagens[1].tempo_troca_imagem = 80
    energias.lista_personagens[2].tempo_troca_imagem = 80
    energias.lista_personagens[3].tempo_troca_imagem = 80
    return energias
    

def criarPontinhosFase3(blocos):

    pontinhos = Personagens(blocos)
    vg = VariaveisGlobais()
    
    for x in range(18):
        for y in range(12):
            pontinhos.criarImagemcXcY(x+2, y+2, 1, 1, vg.lista_imagens_pontinhos)
            ponto = pontinhos.lista_personagens[len(pontinhos.lista_personagens)-1]
            if not blocos.verificarColisao_N_para_1(ponto) is None:
                pontinhos.lista_personagens.remove(ponto)
    return pontinhos

