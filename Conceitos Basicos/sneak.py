import time
import curses
import random


def game_lop(windows, game_speed):
    #Setup inicial
    curses.curs_set(0)
    sneak = [
        [10,15],
        [9,15],
        [8,15],
        [7,15],
    ]

    fruit = get_new_fruit(window=windows)
    current_direction = curses.KEY_DOWN
    snake_ate_fruit = False
    score = 0


    while True:
        draw_screen(windows=windows)
        draw_snake(snake=sneak, window=windows)
        draw_actor(actor=fruit, windows=windows, char=curses.ACS_DIAMOND)
        direction = get_new_direction(windows=windows, timeout=game_speed)
        if direction is None:
            direction = current_direction

        if direction_is_opposite(direction=direction, current_direction=current_direction):
            direction = current_direction
        move_snake(snake=sneak, direction = direction, snake_ate_fruit=snake_ate_fruit)
        if snake_hit_border(snake = sneak, window=windows):
            break
        if snake_hit_itself(snake=sneak):
            break
        if snake_hit_fruit(snake=sneak, fruit=fruit):
            snake_ate_fruit = True
            fruit = get_new_fruit(window=windows)
            score += 1
        else:
            snake_ate_fruit = False
        current_direction = direction
    
    finish_game(score=score, window=windows)

def finish_game(score, window):
    height, width = window.getmaxyx()
    s = f'Você perdeu! Coletou {score} frutas!'
    y = int(height/2)
    x = int((width - len(s)) / 2)
    window.addstr(y,x,s)
    window.refresh()
    time.sleep(5)

def direction_is_opposite(direction, current_direction):
    match direction:
        case curses.KEY_UP:
            return current_direction == curses.KEY_DOWN
        case curses.KEY_LEFT:
            return current_direction == curses.KEY_RIGHT
        case curses.KEY_DOWN:
            return current_direction == curses.KEY_UP
        case curses.KEY_RIGHT:
            return current_direction == curses.KEY_LEFT

def snake_hit_itself(snake):
    head = snake[0]
    body = snake[1:]
    return head in body


def get_new_fruit(window):
    height, width = window.getmaxyx()
    return [random.randint(1, height-2), random.randint(1, width-2)]

def snake_hit_fruit(snake, fruit):
    return fruit in snake

def snake_hit_border(snake, window):
    head = snake[0]
    return actor_hit_border(actor=head, windows=window)

def draw_screen(windows):
    windows.clear()
    windows.border(0)

def draw_snake(snake, window):
    head = snake[0]
    draw_actor(actor=head, windows=window, char="@")
    body = snake[1:]
    for body_part in body:
        draw_actor(actor=body_part, windows=window, char="s")

def draw_actor(actor, windows, char):
    windows.addch(actor[0], actor[1], char)

def get_new_direction(windows, timeout):
    windows.timeout(timeout)
    direction = windows.getch()
    if direction in [curses.KEY_UP, curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_RIGHT]:
        return direction
    return None

def move_snake(snake, direction, snake_ate_fruit):
    head = snake[0].copy()
    move_actor(actor=head, direction=direction)
    snake.insert(0, head)
    if not snake_ate_fruit:
        snake.pop()


def move_actor(actor, direction):

    match direction:
        case curses.KEY_UP:
            actor[0] -= 1
        case curses.KEY_LEFT:
            actor[1] -= 1
        case curses.KEY_DOWN:
            actor[0] += 1
        case curses.KEY_RIGHT:
            actor[1] += 1

def actor_hit_border(actor, windows):

    height, width = windows.getmaxyx()
    if (actor[0] <= 0) or (actor[0] >= height-1):
        return True
    if (actor[1] <= 0) or (actor[1] >= width-1):
        return True
    return False

def select_difficulty():
    difficulty = {
        '1': 1000,
        '2': 500,
        '3': 150,
        '4': 90,
        '5': 35
    }
    while True:
        answer = input('Selecione a dificuldade de 1 a 5: ')
        game_speed = difficulty.get(answer)
        if game_speed is not None:
            return game_speed
        print('Escolha a dificuldade de 1 a 5:')

if __name__ == '__main__':
    curses.wrapper(game_lop, game_speed=select_difficulty())
