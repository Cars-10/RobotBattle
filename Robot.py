import pygame
class Robot:
    def __init__(self, x_position, y_position):
        # Positions are given so we know where the robot is on the board
        self.x_position = x_position
        self.y_position = y_position
        # We initialize the robot's health to 100
        self.health = 100

class Turret:
    def __init__(self, belong_to):
        # Turret belongs to a robot
        self.belong_to = belong_to
        # We initialize the turret's ammo to 50
        self.ammo = 50

class Bullet:
    def __init__(self, fired_by):
        # Bullet is fired by a turret
        self.fired_by = fired_by

# Creating game state with two robots and their turrets
robot1 = Robot(0, 0)
turret1 = Turret(robot1)

robot2 = Robot(100, 100)
turret2 = Turret(robot2)

game_state = {
    'Robots': [robot1, robot2],
    'Turrets': [turret1, turret2],
    'Bullets': []
}

# Print the game state
for obj_type, obj_list in game_state.items():
    for obj in obj_list:
        if obj_type == 'Robots':
            pos_str = '({}, {})'.format(obj.x_position, obj.y_position)
            print('Robot at position {} with health {}'.format(pos_str, obj.health))
        elif obj_type == 'Turrets':
            print('Turret with ammo {} belong to Robot at position ({}, {})'.format(obj.ammo,
obj.belong_to.x_position, obj.belong_to.y_position))
        elif obj_type == 'Bullets':
            print('Bullet fired by Turret belong to Robot at position ({},{})'.format(obj.fired_by.belong_to.x_position, obj.fired_by.belong_to.y_position))
        else:
            print('Unknown object in game state')


class Robot:
    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position
        self.health = 100

    def move(self, direction):
        if direction == 'up' and self.y_position < 100:
            self.y_position += 1
        elif direction == 'down' and self.y_position > 0:
            self.y_position -= 1
        elif direction == 'left' and self.x_position > 0:
            self.x_position -= 1
        elif direction == 'right' and self.x_position < 100:
            self.x_position += 1

class Turret:
    def __init__(self, belong_to):
        self.belong_to = belong_to
        self.ammo = 50

    def rotate(self, angle):
        # In this simplified version, we don't need to do anything specific when rotating the turret.
        return

    def fire(self):
        if self.ammo > 0:
            bullet = Bullet(self)
            game_state['Bullets'].append(bullet)
            self.ammo -= 1
        else:
            print('The turret has no ammo left')

class Bullet:
    def __init__(self, fired_by):
        self.fired_by = fired_by

# We re-define the robots, turrets and game state
robot1 = Robot(0, 0)
turret1 = Turret(robot1)
robot2 = Robot(100, 100)
turret2 = Turret(robot2)
game_state = {'Robots': [robot1, robot2], 'Turrets': [turret1, turret2], 'Bullets': []}

def update_game_state():
    for bullet in game_state['Bullets']:
        hit_robot = next((robot for robot in game_state['Robots'] if
                          (x_pos := robot.x_position) == bullet.fired_by.belong_to.x_position and
                          (y_pos := robot.y_position) == bullet.fired_by.belong_to.y_position), None)
        if hit_robot:
            hit_robot.health -= 10
            if (health := hit_robot.health) <= 0:
                print(f'Robot at position ({x_pos}, {y_pos}) is destroyed')
                game_state['Robots'].remove(hit_robot)
            game_state['Bullets'].remove(bullet)

# Add some actions
robot1.move('up')
robot2.move('down')
turret1.fire()
turret2.fire()
update_game_state()

for obj_type, obj_list in game_state.items():
    for obj in obj_list:
        if obj_type == 'Robots':
            pos_str = '({}, {})'.format(obj.x_position, obj.y_position)
            print('Robot at position {} with health {}'.format(pos_str, obj.health))
        elif obj_type == 'Turrets':
            print('Turret with ammo {} belong to Robot at position ({}, {})'.format(obj.ammo,
                    obj.belong_to.x_position, obj.belong_to.y_position))
        elif obj_type == 'Bullets':
            print('Bullet fired by Turret belong to Robot at position ({},{})'
                  .format(obj.fired_by.belong_to.x_position, obj.fired_by.belong_to.y_position))
        else:
            print('Unknown object in game state')

def process_user_command(command):
    words = command.strip().split(' ')
    if len(words) >= 3:
        if words[0].lower() == 'move' and words[1].lower() == 'robot1':
            robot1.move(words[2].lower())
        if words[0].lower() == 'rotate' and words[1].lower() == 'turret1':
            try:
                turret1.rotate(int(words[2]))
            except ValueError:
                print('Invalid rotation angle')
        if words[0].lower() == 'fire' and words[1].lower() == 'turret1':
            turret1.fire()
    update_game_state()


for obj_type, obj_list in game_state.items():
    for obj in obj_list:
        if obj_type == 'Robots':
            pos_str = '({}, {})'.format(obj.x_position, obj.y_position)
            print('Robot at position {} with health {}'.format(pos_str, obj.health))
        elif obj_type == 'Turrets':
            print('Turret with ammo {} belong to Robot at position ({}, {})'.format(obj.ammo,
            obj.belong_to.x_position, obj.belong_to.y_position))
        elif obj_type == 'Bullets':
            print('Bullet fired by Turret belong to Robot at position ({},{})'
                  .format(obj.fired_by.belong_to.x_position, obj.fired_by.belong_to.y_position))
        else:
            print('Unknown object in game state')
def game_loop():
    commands = ['move robot1 up', 'fire turret1', 'move robot2 down', 'rotate turret1 180', 'fire turret2']
    for command in commands:
        process_user_command(command)
        for obj_type, obj_list in game_state.items():
            for obj in obj_list:
                if obj_type == 'Robots':
                    pos_str = '({}, {})'.format(obj.x_position, obj.y_position)
                    print('Robot at position {} with health {}'.format(pos_str, obj.health))
                elif obj_type == 'Turrets':
                    print('Turret with ammo {} belong to Robot at position ({}, {})'.format(obj.ammo,
                    obj.belong_to.x_position, obj.belong_to.y_position))
                elif obj_type == 'Bullets':
                    print('Bullet fired by Turret belong to Robot at position ({}, {})'
                    .format(obj.fired_by.belong_to.x_position, obj.fired_by.belong_to.y_position))
                else:
                    print('Unknown object in game state')
        print('------------------------------------------')
    print('Game over.')

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the size of the window
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
# Test our function
process_user_command('move robot1 up')
process_user_command('rotate turret1 90')
process_user_command('fire turret1')

# Invoke our game loop
game_loop()