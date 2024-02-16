import pygame

# 初始化
pygame.init()
# 显示配置
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
pygame.display.set_caption("AI_racecar")
clock = pygame.time.Clock()


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

    # 绘制
    screen.fill((255, 255, 255))

    pygame.display.update()
    clock.tick(60)
