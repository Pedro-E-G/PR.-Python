import sys 
import pygame

class AlienInvasion:
    """classe geral para comportamento do jogo"""
    
    def init_(self):
        """inicializa o jogo e cria recursos do jogo"""
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_CAPTION("AlienInvasion")
        
    def run_game(self):
        """inicia o loop principal do jogo"""
        while True:
            #captura comandos do teclado
            for event in pygame.event.get():
                if event.type = pygame.QUIT
                    sys.exit()
            #deixa a tela desenhada mais recente visivel
            pygame.display.flip()
                if_name_==_maiu_:
                    #cria uma instancia do jogo
                    2i=AlienInvasion()
                    2i.run_game()
