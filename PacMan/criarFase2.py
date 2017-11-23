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


def imagemFase2():
    return pygame.image.load(lista_imagens_labirintos[0]).convert_alpha()


def IniciarListaLab():
    global lista_imagens_labirintos
    global lista_imagens_blocos
    
    lista_imagens_labirintos = ["imagens/fases/labirinto2.jpg"]
    lista_imagens_blocos = ["Imagens/objetos/bloco1.jpg"]

    
def criarFase2():
    IniciarListaLab()
    blocos = Personagens()
    #laterais
    blocos.criarImagemcXcY(1, 1, 1, 14, lista_imagens_blocos)
    blocos.criarImagemcXcY(2, 14, 19, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(2, 1, 19, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(20, 1, 1, 14, lista_imagens_blocos)
    #Lado esquerdo
    blocos.criarImagemcXcY(3, 3, 1, 3, lista_imagens_blocos)
    blocos.criarImagemcXcY(4, 5, 2, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(5, 3, 3, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(3, 7, 3, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(3, 8, 1, 3, lista_imagens_blocos)
    blocos.criarImagemcXcY(3, 12, 5, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(5, 9, 1, 3, lista_imagens_blocos)
    #MEIO
    blocos.criarImagemcXcY(10, 2, 2, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(9, 3, 4, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(7, 5, 3, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(7, 6, 1, 3, lista_imagens_blocos)
    blocos.criarImagemcXcY(8, 8, 6, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(14, 5, 1, 4, lista_imagens_blocos)
    blocos.criarImagemcXcY(12, 5, 2, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(7, 10, 8, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(9, 12, 4, 2, lista_imagens_blocos)
    #LADO DIREITO
    blocos.criarImagemcXcY(14, 3, 3, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(18, 3, 1, 3, lista_imagens_blocos)
    blocos.criarImagemcXcY(16, 5, 2, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(16, 7, 3, 1, lista_imagens_blocos)
    blocos.criarImagemcXcY(18, 8, 1, 3, lista_imagens_blocos)
    blocos.criarImagemcXcY(16, 9, 1, 3, lista_imagens_blocos)
    blocos.criarImagemcXcY(14, 12, 5, 1, lista_imagens_blocos)
    return blocos


def criarPontosDecisaoFase2():
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


def criarEnergiasFase2():
    energias = Personagens()
    vg = VariaveisGlobais()
    energias.criarImagemcXcY(9, 2, 1, 1, vg.lista_imagens_energia)
    energias.criarImagemcXcY(12, 2, 1, 1, vg.lista_imagens_energia)
    #energias.criarImagemcXcY(8, 7, 1, 1, vg.lista_imagens_energia)
    #energias.criarImagemcXcY(13, 7, 1, 1, vg.lista_imagens_energia)
    energias.criarImagemcXcY(2, 13, 1, 1, vg.lista_imagens_energia)
    energias.criarImagemcXcY(19, 13, 1, 1, vg.lista_imagens_energia)
    
    energias.lista_personagens[0].alterarImagemMesmoParado = True
    energias.lista_personagens[1].alterarImagemMesmoParado = True
    energias.lista_personagens[2].alterarImagemMesmoParado = True
    energias.lista_personagens[3].alterarImagemMesmoParado = True
    
    energias.lista_personagens[0].tempo_troca_imagem = 80
    energias.lista_personagens[1].tempo_troca_imagem = 80
    energias.lista_personagens[2].tempo_troca_imagem = 80
    energias.lista_personagens[3].tempo_troca_imagem = 80
    return energias
    

def criarPontinhosFase2(blocos):
    
    pontinhos = Personagens(blocos)
    vg = VariaveisGlobais()
    
    for x in range(18):
        for y in range(12):
            pontinhos.criarImagemcXcY(x+2, y+2, 1, 1, vg.lista_imagens_pontinhos)
            ponto = pontinhos.lista_personagens[len(pontinhos.lista_personagens)-1]
            if not blocos.verificarColisao_N_para_1(ponto) is None:
                pontinhos.lista_personagens.remove(ponto)
    return pontinhos

