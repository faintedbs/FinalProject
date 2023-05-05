WIDTH = 800
HEIGHT = 600
PLAYER_ACC = 2
PLAYER_FRICTION = -0.3
PLAYER_JUMP = 20
PLAYER_GRAV = 0.8
MOB_ACC = 2
MOB_FRICTION = -0.3
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
RED = (255,50,50)
FPS = 60
RUNNING = True
SCORE = 0
PAUSED = False

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, (64, 57, 29), "normal"),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, (64, 100, 29), "normal"),
                 (125, HEIGHT - 350, 100, 5, (64, 150, 29), "bouncy "),
                 (350, 200, 100, 20, (64, 100, 29), "normal"),
                 (550, 400, 50, 20, (64, 150, 29), "bouncy")]