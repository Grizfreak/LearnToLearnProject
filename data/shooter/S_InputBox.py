import pygame


class S_InputBox:

    def __init__(self, x, y, w, h, interpreter, text=''):
        self.interpreter = interpreter
        self.rect = pygame.Rect(x, y, w, h)
        self.color = pygame.Color('lightskyblue3')
        self.text = text
        self.FONT = pygame.font.Font(None, 32)
        self.txt_surface = self.FONT.render(str(text), True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_k and not self.active:
            # Toggle the active variable.
            self.active = not self.active
            return
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.interpreter.interprete_command(self.text)
                    self.text = ''
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = pygame.font.Font(None, 32).render(self.text, True, self.color)

    def update(self):
        # Change the current color of the input box.
        self.color = pygame.Color('dodgerblue2') if self.active else self.color
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)