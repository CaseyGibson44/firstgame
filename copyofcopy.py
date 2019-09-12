import pygame
import random
import sys

pygame.init()

WIDTH = 800
HEIGTH = 600

RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0,0,0)
YELLOW = (255,255,0)

player_size = 50
player_pos = [WIDTH/2, HEIGTH-2*player_size]

enemy_size = 25
enemy_pos = [random.randint(0,WIDTH-enemy_size), 0]
enemy_list = [enemy_pos]

enemy_size_two = 25
enemy_pos_two = [random.randint(0,WIDTH-enemy_size_two), 0]
enemy_list_two = [enemy_pos_two]

SPEED = 10
SPEED_two= 10

screen = pygame.display.set_mode((WIDTH, HEIGTH))

game_over = False

score = 0
score_two = 0

clock  = pygame.time.Clock()

myFont = pygame.font.SysFont("monospace", 35)

def set_level(score, SPEED):
    #if score < 20:
        #SPEED = 5
    #elif score < 40:
        #SPEED = 8
    #elif score < 60:
        #SPEED = 12
    #else:
        #SPEED = 15
    SPEED = score/5 + 2
    return SPEED

def set_level_two(score, SPEED_two):
    SPEED_two = score/5 + 2
    return SPEED_two
        
def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1:
        x_pos = random.randint(0,WIDTH-enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])

def drop_enemies_two(enemy_list_two):
    delay_two = random.random()
    if len(enemy_list_two) < 10 and delay_two < 0.1:
        x_pos_two = random.randint(0,WIDTH-enemy_size_two)
        y_pos_two = 0
        enemy_list_two.append([x_pos_two, y_pos_two])
        
def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def draw_enemies_two(enemy_list_two):
    for enemy_pos_two in enemy_list_two:
        pygame.draw.rect(screen, YELLOW, (enemy_pos_two[0], enemy_pos_two[1], enemy_size_two, enemy_size_two))

def update_enemy_positions(enemy_list, score):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGTH:
            enemy_pos[1] += SPEED
        
        else:
            enemy_list.pop(idx)
            score += 1
    return score

def update_enemy_positions_two(enemy_list_two, score_two):
    for idx, enemy_pos_two in enumerate(enemy_list_two):
        if enemy_pos_two[1] >= 0 and enemy_pos_two[1] < HEIGTH:
            enemy_pos_two[1] += SPEED_two

        else:
            enemy_list_two.pop(idx)
            score_two += 1
        return score_two

def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos, player_pos):
            return True
        return False

def collision_check_two(enemy_list_two, player_pos):
    for enemy_pos_two in enemy_list_two:
        if detect_collision_two(enemy_pos_two, player_pos):
            return True
        return False

def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x + player_size)) or p_x >= e_x and p_x < (e_x+enemy_size):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):
            return True
        return False

def detect_collision_two(player_pos, enemy_pos_two):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x_two = enemy_pos_two[0]
    e_y_two = enemy_pos_two[1]

    if (e_x_two >= p_x and e_x_two < (p_x + player_size)) or p_x >= e_x_two and p_x < (e_x_two+enemy_size_two):
        if (e_y_two >= p_y and e_y_two < (p_y + player_size)) or (p_y >= e_y_two and p_y < (e_y_two+enemy_size)):
            return True
        return False
    

while not game_over:
    for event in pygame.event.get():

        if event.type ==- pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            
            x = player_pos[0]
            y = player_pos[1]
            
            if event.key == pygame.K_LEFT:
                x -= player_size
            
            elif event.key == pygame.K_RIGHT:
                x += player_size

            player_pos = [x,y]
            
    screen.fill((BLACK))

    if detect_collision(player_pos, enemy_pos):
        game_over = True
        break

    if detect_collision_two(player_pos, enemy_pos_two):
        game_over = True
        break
    
    drop_enemies_two(enemy_list_two)
    drop_enemies(enemy_list)
    score_two = update_enemy_positions_two(enemy_list_two, score_two)
    score = update_enemy_positions(enemy_list, score)
    SPEED_two = set_level(score_two, SPEED_two)
    SPEED = set_level(score, SPEED)

    drop_enemies(enemy_list)
    score = update_enemy_positions(enemy_list, score)
    SPEED = set_level(score, SPEED)

    text = "score:" + str(score)
    label = myFont.render(text, 1, YELLOW)
    screen.blit(label, (WIDTH-200, HEIGTH-40))
   
    
    if collision_check(enemy_list, player_pos):
        game_over = True
        break

    if collision_check_two(enemy_list_two, player_pos):
        game_over = True
        break

    draw_enemies_two(enemy_list_two)
    draw_enemies(enemy_list)
    
    pygame.draw.rect(screen, (RED), (player_pos[0], player_pos[1], player_size, player_size))

    clock.tick(30)

    pygame.display.update()
    
