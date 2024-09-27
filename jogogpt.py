import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minecraft em Pygame")

# Cores
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
SKY_BLUE = (135, 206, 235)
GRAY = (169, 169, 169)

# Configurações do bloco
BLOCK_SIZE = 40
ROWS = HEIGHT // BLOCK_SIZE
COLS = WIDTH // BLOCK_SIZE

# Classe para o mundo
class World:
    def __init__(self):
        self.blocks = [[self.random_block() for _ in range(COLS)] for _ in range(ROWS)]

    def random_block(self):
        return random.choice(['grass', 'dirt', 'stone'])

    def draw(self, surface):
        for y in range(ROWS):
            for x in range(COLS):
                block = self.blocks[y][x]
                color = self.get_block_color(block)
                pygame.draw.rect(surface, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def get_block_color(self, block):
        if block == 'grass':
            return GREEN
        elif block == 'dirt':
            return BROWN
        elif block == 'stone':
            return GRAY
        return (255, 255, 255)

    def get_block_at_mouse(self, mouse_pos):
        x, y = mouse_pos
        return x // BLOCK_SIZE, y // BLOCK_SIZE

    def add_block(self, position, block_type):
        x, y = position
        if 0 <= x < COLS and 0 <= y < ROWS:
            self.blocks[y][x] = block_type

    def remove_block(self, position):
        x, y = position
        if 0 <= x < COLS and 0 <= y < ROWS:
            self.blocks[y][x] = self.random_block()  # Troca para um bloco aleatório

# Inicialização do mundo
world = World()
clock = pygame.time.Clock()
running = True
selected_block = 'grass'  # Bloco padrão a ser adicionado

# Loop principal do jogo
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            x, y = world.get_block_at_mouse(mouse_pos)

            if event.button == 1:  # Botão esquerdo do mouse para adicionar bloco
                world.add_block((x, y), selected_block)
            elif event.button == 3:  # Botão direito do mouse para remover bloco
                world.remove_block((x, y))

    screen.fill(SKY_BLUE)
    world.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
