import pygame
import random 

pygame.init()

WIDTH, HEIGHT = 960, 720
TILE_SIZE = 24
MAXWIDTH, MAXHEIGHT = 1920 , 1440 
encounter = 0.1
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
battle = False
menu = False
in_grass = False
in_heal = False
battle_options = "attack", "switch","catch", "run", 


running = True
selected_switch = 0
selected = 0  # Track the currently selected Pokémon in the menu
selected_move = 0 # Track the currently selected move in battle
selected_option = 0
in_option = True
in_attack = False
in_switch = False
def whole_team_fainted(team):
    for pokemon in team:
        if pokemon.current_hp > 0:
            return False
    return True
def reset():
    global in_attack, in_switch, in_option
    in_attack = False
    in_switch = False
    in_option = True


# Function to switch Pokémon between boxes
def switch_pokemon(from_box, to_box, index):
    if len(to_box) < 6:  # Only allow switch if party size is under 6
        pokemon = from_box.pop(index)
        to_box.append(pokemon)
        if to_box == box1:
            print("Switched " + pokemon.name + " to the party!")
        else:
            print("Moved " + pokemon.name + " to the box.")
    else:
        print("Party is full. Can't add more Pokémon!")

# Pokemon class
class Pokemon:
    def __init__(self, name, poke_type, level, hp, power, defense, speed, maxxp):
        self.name = name                
        self.poke_type = poke_type      
        self.level = level              
        self.hp = hp                    
        self.max_hp = hp               
        self.power = power           
        self.defense = defense          
        self.speed = speed              
        self.current_hp = hp  
        self.xp = 0
        self.maxxp = maxxp
        self.status = "NA"
        self.charging = False
        self.turn = True
        self.actual_attack = self.power
        self.last_move = ""
        if name == "Charmander":
            self.moveset = "ember", "tackle", "rest", "will-o-wisp"
        elif name == "Bulbasaur":
            self.moveset = "vinewhip", "tackle", "synthesis", "solar beam"
        elif name == "Squirtle":
            self.moveset = "watergun", "tackle", "yawn", "rest"
        elif name == "Pikachu":
            self.moveset = "thunderbolt", "tackle", "synthesis", "takedown"
        elif name == "Gardivoir":
            self.moveset = "moonblast", "draining kiss", "lifedew", "hypnosis"
    
    def getmoveset(self):
        return list(self.moveset)

    def get_type(self):
        return self.poke_type
    def take_damage(self, damage):
        self.current_hp -= damage
        if self.current_hp < 0:
            self.current_hp = 0

    def apply_status(self):
        self.actual_attack = self.power
        if self.status == "burn":
            actual_attack = self.power/1.5
            self.take_damage(maxhp/12)
            print("burn effect happened")
        elif self.status == "sleep":
            wake = random.randrange(2)
            if wake == 1:
                self.status_effect_clear()
                print("woken up!")
            else:
                self.turn = False
        elif self.status == "confusion":
            smart = random.randrange(6)
            if smart == 1:
                self.status_effect_clear
                print("confusion cleared")
            elif smart % 2 == 0:
                self.take_damage(maxhp/8)
                self.turn = False
                print("hurt itself in confusion")
    def status_effect_clear(self):
        self.status = "NA"
    def status_effect(self,status):
        self.status = status

    def heal(self, amount):
        self.current_hp += amount
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp

    # Enemy attack feature
    def enemy_attack(self, enemy):
        enemy_choice = random.randrange(4)
        enemy_usable_moves = self.getmoveset()
        if enemy_choice == 0:
            self.attack(player_pokemon, enemy_usable_moves[0])
        elif enemy_choice == 1:
            self.attack(player_pokemon, enemy_usable_moves[1])
        elif enemy_choice == 2:
            self.attack(player_pokemon, enemy_usable_moves[2])
        elif enemy_choice == 3:
            self.attack(player_pokemon, enemy_usable_moves[3])

    def attack(self, enemy, move):
        print("move was used")
        if self.turn == True:
            self.last_move = move
            if self.charging == True:
                damage = self.actual_attack - enemy.defense
                if damage < 1:
                    damage = 1
                enemy.take_damage(damage * 2.5)
                print("solarbeam used")
            elif move == "tackle" or move == "moonblast":
                damage = self.actual_attack - enemy.defense
                if damage < 1:
                    damage = 1
                enemy.take_damage(damage)
                print("tackle was used")
                
            elif move == "ember":
                damage = self.actual_attack - enemy.defense
                if damage < 1:
                    damage = 1
                if enemy.get_type == "Grass":
                    damage *= 1.5
                enemy.take_damage(damage)
                print("ember used")
            elif move == "vinewhip":
                damage = self.actual_attack - enemy.defense
                if damage < 1:
                    damage = 1
                if enemy.get_type == "Water":
                    damage *= 1.5
                enemy.take_damage(damage)
                print("vinewhip used")
            elif move == "watergun":
                damage = self.actual_attack - enemy.defense
                if damage < 1:
                    damage = 1
                if enemy.get_type == "Fire":
                    damage *= 1.5
                enemy.take_damage(damage)
                print("watergun used")
            elif move == "thunderbolt":
                damage = self.actual_attack - enemy.defense
                if damage < 1:
                    damage = 1
                if enemy.get_type == "Water":
                    damage *= 1.5
                enemy.take_damage(damage)
                print("thunderbolt used")
            elif move == "rest":
                self.status_effect("sleep")
                self.heal(maxhp)
                print("rest was used")
            elif move == "will-o-wisp":
                enemy.status_effect("burn")
                print("will-o-wisp used")
            elif move == "synthesis" or move == "lifedew":
                self.heal(self.max_hp/2)
                print("synthesis was used / lifedew")
            elif move == "solar beam":
                self.charging = True
                print("solar beam charging")
            elif move == "yawn":
                enemy.status_effect("sleep")
                print("used yawn")
            elif move == "takedown":
                damage = self.actual_attack - enemy.defense
                if damage < 1:
                    damage = 1
                enemy.take_damage(damage * 1.5)
                self.take_damage(self.max_hp/8)
                print("used takedown")
            elif move == "draining kiss":
                damage = self.actual_attack - enemy.defense
                if damage < 1:
                    damage = 1
                enemy.take_damage(damage)
                self.heal(damage/2)
                print("used draining kiss")
            elif move == "hypnosis":
                enemy.status_effect("confusion") 
                print("used hypnosis")
            else:
                print("oh shit the code broke somehow")
        else:
            print( self.name + " turn was skipped")
        self.turn = True
        
    def level_up(self):
        self.level += 1
        self.max_hp += 3
        self.power += 2
        self.defense += 1
        self.speed += 1
        self.current_hp = self.max_hp
        self.xp = 0
        self.maxxp += 2 * level


    def full_recovery(self):
        self.heal(self.max_hp)
        self.status_effect = "NA"
    

# Player class
class Player:
    def __init__(self):
        self.rect = pygame.Rect(320, 240, TILE_SIZE, TILE_SIZE)
        self.speed = TILE_SIZE  
        self.move_delay = 150
        self.last_move = pygame.time.get_ticks()
        self.image = pygame.image.load("miku_image")
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))  
    def move(self, dx, dy, barriers):
        time_now = pygame.time.get_ticks()
        if time_now - self.last_move >= self.move_delay:
            next_rect = self.rect.move(dx * self.speed, dy * self.speed)
            if not any(next_rect.colliderect(barrier) for barrier in barriers):
                self.rect = next_rect  
                if self.rect.right > camera_rect.right - 3 * TILE_SIZE:
                    camera_rect.x = min(camera_rect.x + self.speed, MAXWIDTH - WIDTH)
                elif self.rect.left < camera_rect.left + 3 * TILE_SIZE:
                    camera_rect.x = max(camera_rect.x - self.speed, 0)
                if self.rect.bottom > camera_rect.bottom - 3 * TILE_SIZE:
                    camera_rect.y = min(camera_rect.y + self.speed, MAXHEIGHT - HEIGHT)
                elif self.rect.top < camera_rect.top + 3 * TILE_SIZE:
                    camera_rect.y = max(camera_rect.y - self.speed, 0)
            self.last_move = time_now
        return camera_rect
    def draw_player(self, screen, camera_rect):
        # Calculate the player's position relative to the camera
        draw_position = (self.rect.x - camera_rect.x, self.rect.y - camera_rect.y)
        # Draw the player image at the adjusted position
        screen.blit(self.image, draw_position)
    def getposx(self):
        return self.rect.x

    def getposy(self):
        return self.rect.y

player = Player()
camera_rect = pygame.Rect(0, 0, WIDTH, HEIGHT)
enemy = [

]
box1 = [
    Pokemon("Charmander", "Fire", 4 ,21 ,10 , 8, 12, 50)
]
team = [
    Pokemon("Pikachu", "Electric", 4 ,18 ,8 , 5, 16, 1)
]
heal_tiles = [
    pygame.Rect(150, 200, TILE_SIZE, TILE_SIZE),
]
# Example barriers
barriers = [
    pygame.Rect(100, 100, TILE_SIZE, TILE_SIZE),
    pygame.Rect(200, 200, TILE_SIZE, TILE_SIZE),
    pygame.Rect(300, 400, TILE_SIZE, TILE_SIZE)
]

# Grass areas
grass = [
    pygame.Rect(1000, 200, TILE_SIZE, TILE_SIZE),
    pygame.Rect(500, 700, TILE_SIZE, TILE_SIZE),
    pygame.Rect(300, 300, TILE_SIZE, TILE_SIZE)
]


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.getposx() > 0:
        player.move(-1, 0, barriers)
    if keys[pygame.K_RIGHT] and player.getposx() < MAXWIDTH - player.rect.width:
        player.move(1, 0, barriers)
    if keys[pygame.K_UP] and player.getposy() > 0:
        player.move(0, -1, barriers)
    if keys[pygame.K_DOWN] and player.getposy() < MAXHEIGHT - player.rect.height:
        player.move(0, 1, barriers)
    if keys[pygame.K_m]:
        menu = True

    screen.fill((118, 198, 161))

    # Draw player and barriers
    player_on_screen = player.rect.move(-camera_rect.x, -camera_rect.y)
    
    player.draw_player(screen,camera_rect)
    tree_image = pygame.image.load("tree_image.png")
    tree_image = pygame.transform.scale(tree_image, (TILE_SIZE, TILE_SIZE))
    for barrier in barriers:
        barrier_on_screen = barrier.move(-camera_rect.x, -camera_rect.y)
        screen.blit(tree_image, barrier_on_screen)

    for heal_tile in heal_tiles:
        heal_on_screen = heal_tile.move(-camera_rect.x, -camera_rect.y)
        pygame.draw.rect(screen, (0, 0, 255), heal_on_screen)
        if in_heal == False:
            if player.rect.colliderect(heal_tile):
                for pokemon in team:
                    font = pygame.font.Font(None, 72)
                    pokemon.full_recovery()
                    screen.fill((255,255,255))
                    text = font.render("Team healed fully!", True, (255, 0, 0))
                    text_centre = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                    screen.blit(text,text_centre)
                    pygame.display.flip()
                    pygame.time.delay(1000)
    in_heal = any(player.rect.colliderect(heal_tile) for heal_tile in heal_tiles)

    grass_image = pygame.image.load("grass_image.jpeg")
    grass_image = pygame.transform.scale(grass_image, (TILE_SIZE, TILE_SIZE))
    for grass_tile in grass:
    # Adjust grass tile position relative to camera
        grass_on_screen = grass_tile.move(-camera_rect.x, -camera_rect.y)
        # Draw the grass image at the adjusted position
        screen.blit(grass_image, grass_on_screen)
        # Check for player collision with grass tile to start battle
        if not in_grass:
            if player.rect.colliderect(grass_tile) and not whole_team_fainted(team):
                battle = True
    # Update in_grass status for any collision with grass tiles
    in_grass = any(player.rect.colliderect(grass_tile) for grass_tile in grass)
    #Menu function
    while menu:
        screen.fill((200, 200, 200))  # Background color for the menu
        font = pygame.font.Font(None, 24)  # Font for displaying text
        y_pos = 50  # Starting position for rendering Pokémon names

        # Display Pokémon in the team
        screen.blit(font.render("Your Team:", True, (255, 255, 255)), (50, y_pos))
        y_pos += 30
        for idx, poke in enumerate(team):
            # Highlight only the selected Pokémon in the team
            color = (20, 200, 35) if idx == selected and selected < len(team) else (255, 255, 255)
            text = font.render(poke.name + " - Lv " + str(poke.level), True, color)
            screen.blit(text, (50, y_pos))
            y_pos += 30

        y_pos += 30  # Add some space between team and box1

        # Display Pokémon in box1
        screen.blit(font.render("Storage Box:", True, (255, 255, 255)), (50, y_pos))
        y_pos += 30
        if box1:
            for idx, poke in enumerate(box1):
                # Highlight only the selected Pokémon in the box1
                color = (20, 200, 35) if idx == selected - len(team) and selected >= len(team) else (255, 255, 255)
                text = font.render(poke.name + " - Lv " + str(poke.level), True, color)
                screen.blit(text, (50, y_pos))
                y_pos += 30
        else:
            empty_text = font.render("No Pokémon in box!", True, (255, 0, 0))
            screen.blit(empty_text, (50, y_pos))

        # Handle menu navigation and selection
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    # Move down the list, but don't go past the last Pokémon in either team or box1
                    if selected < len(team) + len(box1) - 1:
                        selected += 1
                elif event.key == pygame.K_UP:
                    # Move up the list, but don't go before the first Pokémon
                    if selected > 0:
                        selected -= 1
                elif event.key == pygame.K_RETURN:
                    # Switch Pokémon between the team and box1
                    if selected < len(team):  # Selected Pokémon is in the team
                        switch_pokemon(team, box1, selected)
                    else:  # Selected Pokémon is in the box1
                        switch_pokemon(box1, team, selected - len(team))  # Adjust index for box1
                    if selected >= len(team) + len(box1):  # Prevent index overflow
                        selected = len(team) + len(box1) - 1
                elif event.key == pygame.K_ESCAPE:
                    menu = False

        pygame.display.flip()  # Update the screen
 
    #Battle function
    while battle:
        #Get random pokemon at rand level
        pokemon = random.randrange(1,14)
        if pokemon == 1 or pokemon == 5 or pokemon == 9:
            namez = "Charmander"
            type = "Fire"
            level = random.randrange(1,10)
            maxhp = 12 + (3*level)
            power = 6 + (2*level)
            defense = 2 + level
            speed = 9 + level
            maxxp = 50

        elif pokemon == 2 or pokemon == 6 or pokemon == 10:
            namez = "Bulbasaur"
            type = "Grass"
            level = random.randrange(1,10)
            maxhp = 15 + (3*level)
            power = 6 + (2*level)
            defense = 2 + level
            speed = 7 + level
            maxxp = 50
        elif pokemon == 3 or pokemon == 7 or pokemon == 11:
            namez = "Squirtle"
            type = "Water"
            level = random.randrange(1,10)
            maxhp = 14 + (3*level)
            power = 5 + (2*level)
            defense = 2 + level
            speed = 7 + level
            maxxp = 50
        elif pokemon == 4 or pokemon == 8 or pokemon == 12:
            namez = "Pikachu"
            Type = "Electric"
            level = random.randrange(1,10)
            maxhp = 11 + (3*level)
            power = 5 + (2*level)
            defense = 0 + level
            speed = 13 + level
            maxxp = 50
        else:
            namez = "Gardivoir"
            type = "Fairy/Phycic"
            level = random.randrange(5,15)
            maxhp = 21 + (3*level)
            power = 12 + (2*level)
            defense = 2 + level
            speed = 11 + level
            maxxp = 80
        # Add pokemon to enemy list
        enemy.append(Pokemon(namez, type, level, maxhp, power, defense, speed, maxxp))
        font = pygame.font.Font(None, 24)
        player_pokemon = team[0]
        enemy_pokemon = enemy[0]
        screen.fill((255, 255, 255))

        # Draw active Pokémon and their health bars
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(50, 100, 100, 10))  # Enemy HP bar border
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(50, 100, int(100 * enemy_pokemon.current_hp / enemy_pokemon.max_hp), 10))
        enemy_text = font.render("Enemy: " + enemy_pokemon.name + " Lv " + str(enemy_pokemon.level), True, (0, 0, 0))
        screen.blit(enemy_text, (50, 70))
        enemy_status_text = font.render("status:" +
        str(enemy_pokemon.status) , True, (0, 0, 0))
        screen.blit(enemy_status_text, (155, 98))
        enemy_last_move_text = font.render("Used:" + enemy_pokemon.last_move, True, (0, 0, 0))
        screen.blit(enemy_last_move_text, (50, 130))

        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(650, 500, 100, 10))  # Player HP bar border
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(650, 500, int(100 * player_pokemon.current_hp / player_pokemon.max_hp), 10))
        player_text = font.render("Your: " + player_pokemon.name + " Lv " + str(player_pokemon.level), True, (0, 0, 0))
        screen.blit(player_text, (650, 470))
        status_text = font.render("status:" + player_pokemon.status , True, (0, 0, 0))
        screen.blit(status_text, (755, 498))
        last_move_text = font.render("Used:" + player_pokemon.last_move, True, (0, 0, 0))
        screen.blit(last_move_text, (650, 530))
        if player_pokemon.charging:
            player_pokemon.attack(enemy_pokemon," ")
            player_pokemon.charging = False
        if in_option:
            y_offset = 500
            for i, option in enumerate(battle_options):
                color = (255, 0, 0) if i == selected_option else (0, 0, 0)
                option_text = font.render(option, True, color)
                screen.blit(option_text, (50, y_offset))
                y_offset += 40
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        selected_option = (selected_option + 1)  % len(battle_options)
                    elif event.key == pygame.K_UP:
                        selected_option = (selected_option - 1) % len(battle_options)
                    elif event.key == pygame.K_RETURN:
                        # Execute selected move effect
                        choice = battle_options[selected_option]
                        if choice == "attack":
                            in_option = False
                            in_attack = True
                        elif choice == "switch":
                            in_option = False
                            in_switch = True
                        elif choice == "run":
                            yas = random.randrange(1,5)
                            if yas > 1:
                                battle = False
                                enemy.clear()
                            else:
                                text = font.render("Can't run!", True, (255, 0, 0))
                                text_centre = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                                screen.blit(text,text_centre)
                                pygame.display.flip()
                                pygame.time.delay(500)
                                if enemy_pokemon.current_hp > 0:
                                    enemy_pokemon.enemy_attack(player_pokemon)
                            reset()
                        elif choice == "catch":
                            yas = random.randrange(1,10)
                            if yas > 1:
                                battle = False
                                caught = enemy.pop()
                                box1.append(caught)
                            else:
                                text = font.render("Failed to catch!!", True, (255, 0, 0))
                                text_centre = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                                screen.blit(text,text_centre)
                                pygame.display.flip()
                                pygame.time.delay(500)
                                if enemy_pokemon.current_hp > 0:
                                    enemy_pokemon.enemy_attack(player_pokemon)
                            reset()
        elif in_attack:# Display moveset options
            moves = player_pokemon.moveset
            y_offset = 500
            for i, move in enumerate(moves):
                color = (255, 0, 0) if i == selected_move else (0, 0, 0)
                move_text = font.render(move, True, color)
                screen.blit(move_text, (50, y_offset))
                y_offset += 40
            # Handle move selection and attack execution
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        selected_move = (selected_move + 1) % len(moves)
                    elif event.key == pygame.K_UP:
                        selected_move = (selected_move - 1) % len(moves)
                    elif event.key == pygame.K_RETURN:
                        # Execute selected move effect
                        move = moves[selected_move]
                        if player_pokemon.speed > enemy_pokemon.speed:
                            player_pokemon.apply_status()
                            player_pokemon.attack(enemy_pokemon, move)
                            
                            if enemy_pokemon.current_hp > 0:
                                enemy_pokemon.apply_status()
                                enemy_pokemon.enemy_attack(player_pokemon)
                        elif enemy_pokemon.current_hp > 0:
                            enemy_pokemon.apply_status()
                            enemy_pokemon.enemy_attack(player_pokemon)
                            
                            if player_pokemon.current_hp > 0:
                                player_pokemon.apply_status()
                                player_pokemon.attack(enemy_pokemon, move)
                                
                        reset()
                    elif event.key == pygame.K_ESCAPE:
                        reset()
    
        elif in_switch:
            screen.fill((200, 200, 200))  # Background color for the menu
            font = pygame.font.Font(None, 24)  # Font for displaying text
            y_pos = 50  # Starting position for rendering Pokémon names

            # Display Pokémon in the team
            screen.blit(font.render("Your Team:", True, (255, 255, 255)), (50, y_pos))
            y_pos += 30
            for idx, poke in enumerate(team):
                # Highlight only the selected Pokémon in the team
                color = (20, 200, 35) if idx == selected_switch and selected_switch < len(team) else (255, 255, 255)
                text = font.render(poke.name + " - Lv " + str(poke.level), True, color)
                screen.blit(text, (50, y_pos))
                y_pos += 30

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        selected_switch = (selected_switch + 1) % len(team)
                    elif event.key == pygame.K_UP:
                        selected_switch = (selected_switch - 1) % len(team)
                    elif event.key == pygame.K_RETURN:
                        if selected_switch == 0:
                            text = font.render("This pokemon is already battling!!", True, (255, 0, 0))
                            text_centre = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                            screen.blit(text,text_centre)
                            pygame.display.flip()
                            pygame.time.delay(1000)
                        else:
                            switch_pokemon = team.pop(selected_switch)
                            team.insert(0, switch_pokemon)
                            player_pokemon = team[0]
                            if enemy_pokemon.current_hp > 0:
                                enemy_pokemon.enemy_attack(player_pokemon)
                            reset()
                    elif event.key == pygame.K_ESCAPE:
                        reset()


            
        if player_pokemon.current_hp<= 0:
            if whole_team_fainted(team):
                screen.fill((255,255,255))
                text = font.render("You Lost!!!", True, (255, 0, 0))
                text_centre = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                screen.blit(text,text_centre)
                pygame.display.flip()
                pygame.time.delay(1000)
                enemy.remove(enemy_pokemon)
                reset()
                battle = False
            else:
                screen.fill((200, 200, 200))  # Background color for the menu
                font = pygame.font.Font(None, 24)  # Font for displaying text
                y_pos = 50  # Starting position for rendering Pokémon names

                # Display Pokémon in the team
                screen.blit(font.render("Your Team:", True, (255, 255, 255)), (50, y_pos))
                y_pos += 30
                for idx, poke in enumerate(team):
                    # Highlight only the selected Pokémon in the team
                    color = (20, 200, 35) if idx == selected_switch and selected_switch < len(team) else (255, 255, 255)
                    text = font.render(poke.name + " - Lv " + str(poke.level), True, color)
                    screen.blit(text, (50, y_pos))
                    y_pos += 30

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                            selected_switch = (selected_switch + 1) % len(team)
                        elif event.key == pygame.K_UP:
                            selected_switch = (selected_switch - 1) % len(team)
                        elif event.key == pygame.K_RETURN:
                            if selected_switch == 0 or team[selected_switch].current_hp <= 0:
                                text = font.render("This pokemon is fainted!!", True, (255, 0, 0))
                                text_centre = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                                screen.blit(text,text_centre)
                                pygame.display.flip()
                                pygame.time.delay(1000)
                            else:
                                switch_pokemon = team.pop(selected_switch)
                                team.insert(0, switch_pokemon)
                                player_pokemon = team[0]
                                
                        elif event.key == pygame.K_ESCAPE:
                            reset()

                
        pygame.display.flip()
        if enemy_pokemon.current_hp <= 0:
            screen.fill((255,255,255))
            text = font.render("You Win!!", True, (255, 0, 0))
            text_centre = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text,text_centre)
            pygame.display.flip()
            player_pokemon.xp += 3 * enemy_pokemon.level
            pygame.time.delay(1000)
            enemy.remove(enemy_pokemon)
            reset
            battle = False

    for pokemon in team:
        if pokemon.xp >= pokemon.maxxp:
            screen.fill((255,255,255))
            pokemon.level_up()
            text = font.render(pokemon.name + " leveled up!!!", True, (255, 0, 0))
            text_centre = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text,text_centre)
            pygame.display.flip()
            pygame.time.delay(1000)

    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
