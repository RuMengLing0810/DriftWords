# 保存为 floating_text_pygame.py ，运行：python floating_text_pygame.py
import pygame
import random
import sys

# 配置
WIDTH, HEIGHT = 1280, 720
NUM_TEXTS = 120
TEXTS = ["Python", "飘字", "Hello", "2025", "✨", "加油"]
FONT_SIZES = [20, 24, 28, 32, 40]

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("满屏飘字 - pygame")
clock = pygame.time.Clock()

class FloatText:
    def __init__(self, text, x, y, vx, vy, font):
        self.text = text
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.font = font
        self.surf = self.font.render(self.text, True, (255,255,255))
        self.alpha = 255

    def update(self):
        self.x += self.vx
        self.y += self.vy
        # 缓慢淡出（可选）
        self.alpha = max(0, self.alpha - 0.1)
        self.surf.set_alpha(int(self.alpha))
        # 出底部则重置到顶部
        if self.y > HEIGHT + 50 or self.x < -200 or self.x > WIDTH + 200:
            self.reset()

    def reset(self):
        self.x = random.uniform(-100, WIDTH)
        self.y = random.uniform(-HEIGHT, -20)
        self.vx = random.uniform(-0.8, 0.8)
        self.vy = random.uniform(0.5, 3.0)
        self.alpha = 255

    def draw(self, surface):
        surface.blit(self.surf, (self.x, self.y))


# 生成文字对象
fonts = [pygame.font.SysFont("arial", s, bold=True) for s in FONT_SIZES]
items = []
for i in range(NUM_TEXTS):
    txt = random.choice(TEXTS)
    font = random.choice(fonts)
    x = random.uniform(0, WIDTH)
    y = random.uniform(-HEIGHT, HEIGHT)
    vx = random.uniform(-1.0, 1.0)
    vy = random.uniform(0.5, 3.0)
    items.append(FloatText(txt, x, y, vx, vy, font))

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    screen.fill((95, 111, 153))  # 背景色
    for it in items:
        it.update()
        it.draw(screen)

    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
sys.exit()
