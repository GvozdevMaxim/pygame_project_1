import pygame


image_path = "data/data/com.MyfirstGame.myapp/files/app/"
clock = pygame.time.Clock()

# Initialisation
pygame.init()
screen = pygame.display.set_mode((700, 399))
pygame.display.set_caption("my first game")
icon = pygame.image.load("Pygame projects/first_game/icons/djostic.icon.png")
pygame.display.set_icon(icon)

# square = pygame.Surface((50, 170))
# square.fill('Blue')

myFont = pygame.font.Font("Pygame projects/first_game/fonts/Roboto-Black.ttf", 40)
# text_surface = myFont.render('Kitty_myau', True, 'orange')


player = pygame.image.load("Pygame projects/first_game/icons/characters/standing.png").convert_alpha()
bg = pygame.image.load("Pygame projects/first_game/icons/bg.jpg").convert()
# player = pygame.image.load("Pygame projects/first_game/icons/characters/standing.png")

# animation packs and coordination
walk_left = [
    pygame.image.load("Pygame projects/first_game/icons/characters/L1.png").convert_alpha(),
    pygame.image.load("Pygame projects/first_game/icons/characters/L2.png").convert_alpha(),
    pygame.image.load("Pygame projects/first_game/icons/characters/L3.png").convert_alpha(),
    pygame.image.load("Pygame projects/first_game/icons/characters/L4.png").convert_alpha(),
    pygame.image.load("Pygame projects/first_game/icons/characters/L5.png").convert_alpha(),
    pygame.image.load("Pygame projects/first_game/icons/characters/L6.png").convert_alpha(),
    pygame.image.load("Pygame projects/first_game/icons/characters/L7.png").convert_alpha(),
    pygame.image.load("Pygame projects/first_game/icons/characters/L8.png").convert_alpha(),
    pygame.image.load("Pygame projects/first_game/icons/characters/L9.png").convert_alpha()
]
walk_right = [
    pygame.image.load("Pygame projects/first_game/icons/characters/R1.png").convert_alpha(),
    pygame.image.load("Pygame projects/first_game/icons/characters/R2.png").convert_alpha(),
    pygame.image.load("Pygame projects/first_game/icons/characters/R3.png").convert_alpha(),
    pygame.image.load("Pygame projects/first_game/icons/characters/R4.png").convert_alpha(),
    pygame.image.load("Pygame projects/first_game/icons/characters/R5.png").convert_alpha(),
    pygame.image.load("Pygame projects/first_game/icons/characters/R6.png").convert_alpha(),
    pygame.image.load("Pygame projects/first_game/icons/characters/R7.png").convert_alpha(),
    pygame.image.load("Pygame projects/first_game/icons/characters/R8.png").convert_alpha(),
    pygame.image.load("Pygame projects/first_game/icons/characters/R9.png")
]
enemies_walk_left = [
    pygame.image.load("Pygame projects/first_game/icons/characters/L1E.png").convert_alpha(),
    pygame.image.load("Pygame projects/first_game/icons/characters/L2E.png").convert_alpha(),
    pygame.image.load("Pygame projects/first_game/icons/characters/L3E.png").convert_alpha(),
    pygame.image.load("Pygame projects/first_game/icons/characters/L4E.png").convert_alpha(),
    pygame.image.load("Pygame projects/first_game/icons/characters/L5E.png").convert_alpha(),
    pygame.image.load("Pygame projects/first_game/icons/characters/L6E.png").convert_alpha(),
    pygame.image.load("Pygame projects/first_game/icons/characters/L7E.png").convert_alpha(),
    pygame.image.load("Pygame projects/first_game/icons/characters/L8E.png").convert_alpha(),
    pygame.image.load("Pygame projects/first_game/icons/characters/L9E.png").convert_alpha(),
    pygame.image.load("Pygame projects/first_game/icons/characters/L10E.png").convert_alpha(),
]
enemies_dead_img = pygame.image.load("Pygame projects/first_game/icons/characters/deadbody_first.png").convert_alpha()


player_anim_count = 0
bg_x = 0

player_speed = 7
player_x = 150
player_y = 300
is_jump = False
jump_count = 9

enemy_anim_count = 0
enemy_speed = 10
enemy_x = 720
enemy_y = 300
enemies_list_in_game = []
enemies_deads = []

# sound
bg_sounds = pygame.mixer.Sound("Pygame projects/first_game/sounds/maincraft.mp3")
bg_sounds.play()
pistol_sound = pygame.mixer.Sound("Pygame projects/first_game/sounds/pistol_sound.mp3")
fallen_body_sound = pygame.mixer.Sound("Pygame projects/first_game/sounds/fallen_body_sound.mp3")
jump_sound = pygame.mixer.Sound("Pygame projects/first_game/sounds/jump_sound.mp3")

# Spawn timer
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 3000)

# Main menu
lable = pygame.font.Font("Pygame projects/first_game/fonts/Roboto-Black.ttf", 40)
lose_lable = lable.render("YOU LOSE", True, (245, 239, 66))
restart_lable = lable.render("restart", True, (245, 239, 66))
restart_lable_rect = restart_lable.get_rect(topleft=(300, 100))
gameplay = True

# Bullets
bullet = pygame.image.load("Pygame projects/first_game/icons/Bullet__1.png").convert_alpha()
bullet = pygame.transform.scale(bullet, (16, 16))
bullets = []
bullets_left = 10

# Ammo boxes
ammo_box = pygame.image.load("Pygame projects/first_game/sounds/ammo_box_img.png").convert_alpha()
ammo_box = pygame.transform.scale(ammo_box, (30, 30))
ammo_boxes_in_game = []
# Ammo timer
ammo_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ammo_timer, 8000)


# ammo menu
ammo_image = pygame.image.load("Pygame projects/first_game/icons/ammo_img.png").convert_alpha()
ammo_image = pygame.transform.scale(ammo_image, (35, 35))


# The main loop
running = True
while running:
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 590, 0))
    screen.blit(ammo_image, (600, 10))

# Ammo_menu
    ammo = myFont.render(str(bullets_left), True, (255, 149, 0))
    screen.blit(ammo, (650, 5))

    if gameplay:
        # invisible rect around the models of the player and the enemy
        player_rect = walk_left[0].get_rect(topleft=[player_x, player_y])
        enemy_rect = walk_left[0].get_rect(topleft=[enemy_x, enemy_y])

 # enemy movement
        if enemies_list_in_game:
            for i,el in enumerate(enemies_list_in_game):
                screen.blit(enemies_walk_left[enemy_anim_count], el)
                el.x -= 5

                if el.x < - 30:
                    enemies_list_in_game.pop(i)

                if player_rect.colliderect(el):
                    gameplay = False
                    print("yoy lose")
# enemies
        if enemies_deads:
            for i, el in enumerate(enemies_deads):
                screen.blit(enemies_dead_img, el)
                el.x -= 2

                if el.x < - 30:
                    enemies_deads.pop(i)
# Ammo boxes movement
        if ammo_boxes_in_game:
            for i, el in enumerate(ammo_boxes_in_game):
                screen.blit(ammo_box, el)
                el.x -= 2
                if el.x < - 30:
                    ammo_boxes_in_game.pop(i)
                if el.colliderect(player_rect):
                    bullets_left += 3
                    ammo_boxes_in_game.pop(i)




# Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        elif keys[pygame.K_RIGHT]:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))
        else:
            screen.blit(player, (player_x, player_y))
            player_x -= 2

        if keys[pygame.K_LEFT] and player_x > 10:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 670:
            player_x += player_speed

        if not is_jump:
            if keys[pygame.K_UP]:
                is_jump = True

        else:
            if jump_count >= -9:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                jump_sound.play()
                is_jump = False
                jump_count = 9


        # Animation counter
        if player_anim_count == 8:
            player_anim_count = 0
        else:
            player_anim_count += 1

        if enemy_anim_count == 9:
            enemy_anim_count = 0
        else:
            enemy_anim_count += 1

        # background movement
        bg_x -= 2
        if bg_x == - 700:
            bg_x = 0



        if bullets:
            for i,el in enumerate(bullets):
                screen.blit(bullet, (el.x, el.y))
                el.x += 4

                if el.x > 700:
                    bullets.pop(i)

                if enemies_list_in_game:
                    for i, enemy in enumerate(enemies_list_in_game):
                        if el.colliderect(enemy):
                            fallen_body_sound.play()
                            enemies_deads.append(enemies_dead_img.get_rect(topleft=(el.x, el.y + 5)))
                            enemies_list_in_game.pop(i)
                            bullets.pop(i)

        # screen.blit(square, (10, 0))
        # screen.blit(text_surface, (300, 100))
        # screen.blit(player, (100, 30))
        # pygame.draw.circle(screen, 'Red', (10, 70), 5)
        # screen.fill((98, 153, 217))
    else:
        screen.fill((237, 192, 69))
        screen.blit(lose_lable, (270, 200))

        screen.blit(restart_lable, restart_lable_rect)

        mouth = pygame.mouse.get_pos()
        if restart_lable_rect.collidepoint(mouth) and pygame.mouse.get_pressed()[0]:
            player_x = 150
            enemies_list_in_game.clear()
            bullets.clear()
            ammo_boxes_in_game.clear()
            bullets_left = 10
            gameplay = True

    pygame.display.update()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == enemy_timer:
            enemies_list_in_game.append(enemies_walk_left[0].get_rect(topleft=(720, 300)))
        if event.type == ammo_timer:
            ammo_boxes_in_game.append(ammo_box.get_rect(topleft=(720, 310)))
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_SPACE and bullets_left > 0:
            bullets.append(bullet.get_rect(topleft=(player_x + 40, player_y + 20)))
            pistol_sound.play()
            bullets_left -= 1

    clock.tick(26)
