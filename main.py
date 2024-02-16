import pygame
import cv2



# 初始化
pygame.init()
# 显示配置
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
pygame.display.set_caption("AI_racecar")
clock = pygame.time.Clock()

pygame.key.set_repeat(1, 1)

# 小车对象定义
car_img = pygame.image.load("source/picture/car.png").convert_alpha()

class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = car_img
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50

    def rotate(self, angle):
        # 选择机身
        self.image = pygame.transform.rotate(car_img, angle)
        self.rect = self.image.get_rect(center=self.rect.center)


# 小车加载
car_group = pygame.sprite.Group()
car = Car()
car_group.add(car)

# 游戏循环
running = True
while running:
    # 事件处理
    for event in pygame.event.get():
        # 退出代码
        if event.type == pygame.QUIT:
            running = False
        # 键鼠操作(如果有的话)直接写点击退出了
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("鼠标点击")
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car.rect.x -= 1
                car.rotate(90)
            elif event.key == pygame.K_RIGHT:
                car.rect.x += 1
                car.rotate(-90)

    # 绘制
    screen.fill((130, 200, 235))
    car_group.draw(screen)

    pygame.display.update()
    clock.tick(60)

