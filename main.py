import pygame
import math

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
        self.acceleration = 0
        self.acceleration_x = 0
        self.acceleration_y = 0
        self.velocity = 0
        self.velocity_x = 0
        self.velocity_y = 0
        self.angle = 0
        self.angular_velocity = 0
        self.angular_acceleration = 0

        self.image = car_img
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50

    def rotate(self):
        self.image = pygame.transform.rotate(car_img, -self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def set(self, acceleration, angular_acceleration):
        self.acceleration = acceleration
        self.angular_acceleration = angular_acceleration

    def run(self):
        self.velocity = self.velocity + self.acceleration
        if self.velocity > 20:
            self.velocity = 20

        self.velocity_x = self.velocity * math.cos(self.angle * math.pi / 180)
        self.velocity_y = self.velocity * math.sin(self.angle * math.pi / 180)
        self.rect.x = self.rect.x + self.velocity_x
        self.rect.y = self.rect.y + self.velocity_y
        self.angular_velocity = self.angular_velocity + self.angular_acceleration
        self.angle = self.angle + 0.03 * self.angular_velocity * self.velocity

        self.rotate()


# 小车加载
car_group = pygame.sprite.Group()
car = Car()
car_group.add(car)

# 游戏循环
running = True
while running:
    # 无事件参数
    car.angular_acceleration = -car.angular_velocity/abs(car.angular_velocity) if car.angular_velocity != 0 else 0
    car.acceleration = -car.velocity/abs(car.velocity) if car.velocity != 0 else 0

    print(car.velocity)

    # 事件处理
    for event in pygame.event.get():
        # 退出代码
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            running = False

    # 键盘处理
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_LEFT]:
        car.angular_velocity = -10
    if key_pressed[pygame.K_RIGHT]:
        car.angular_velocity = 10
    if key_pressed[pygame.K_UP]:
        car.acceleration = 1
    if key_pressed[pygame.K_DOWN]:
        car.acceleration = -1

    # 计算
    car.run()
    # 绘制
    screen.fill((130, 200, 235))
    car_group.draw(screen)

    pygame.display.update()
    clock.tick(60)
