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
            #observa eventos de teclado e mouse
