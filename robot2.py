import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (255, 255, 255)

# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
INACTIVE_COLOR = (100, 100, 100)
ACTIVE_COLOR = (0, 150, 0)

class Robot:
    def __init__(self, x, y, color, name):
        self.x = x
        self.y = y
        self.color = color
        self.name = name
        self.energy = 100.0
        self.octant = 0
        self.commands = []
        self.current_command_index = 0

    # [All your Robot methods here]

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 50, 50))
        # This just draws the robot as a rectangle. You can enhance this to represent direction, energy, etc.

class TextBox:
    def __init__(self, x, y, w, h, font, robot):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = INACTIVE_COLOR
        self.font = font
        self.text = ''
        self.txt_surface = font.render(self.text, True, self.color)
        self.active = False
        self.robot = robot

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = ACTIVE_COLOR if self.active else INACTIVE_COLOR
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.robot.add_commands(self.text)
                    self.robot.execute_command()
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = self.font.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Robot Battle")
    clock = pygame.time.Clock()

    alpha = Robot(100, SCREEN_HEIGHT // 2 - 25, RED, "Alpha")
    omega = Robot(SCREEN_WIDTH - 150, SCREEN_HEIGHT // 2 - 25, BLUE, "Omega")

    font = pygame.font.Font(None, 32)
    input_box1 = TextBox(50, 500, 200, 40, font, alpha)
    input_box2 = TextBox(SCREEN_WIDTH - 250, 500, 200, 40, font, omega)
    boxes = [input_box1, input_box2]

    while True:
        screen.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            for box in boxes:
                box.handle_event(event)

        for box in boxes:
            box.update()
            box.draw(screen)

        alpha.draw(screen)
        omega.draw(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
