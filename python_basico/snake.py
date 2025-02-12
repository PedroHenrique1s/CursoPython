#Para o funcionamento correto instalar 
#  python -m pip install windows-curses

import curses
import random
import time

#função do jogo
def game_loop(window, game_speed):
    # Setup inicial
    curses.curs_set(0)
    snake = [
        [10,15],
        [9,15],
        [8,15],
        [7,15],
    ]
    fruit = get_new_fruit(window=window)
    current_direction = curses.KEY_DOWN
    snake_eat_fruit = False
    score = 0

    while True:
        draw_screen(window=window)
        draw_snake(snake=snake, window=window)
        draw_actor(actor=fruit, window=window, char= curses.ACS_DIAMOND)
        direction = get_new_direction(window=window, timeout=game_speed)
        
        if direction is None:
            direction = current_direction
        if direction_is_opposite(direction=direction, current_direction=current_direction):
            direction = current_direction

        move_snake(snake=snake, direction=direction, snake_eat_fruit=snake_eat_fruit)
        if snake_hit_border(snake=snake, window=window):
            break
        if snake_hit_itself(snake=snake):
            break
        if snake_hit_fruit(snake=snake, fruit=fruit):
            snake_eat_fruit = True
            fruit = get_new_fruit(window=window)
            score += 1
        else:
            snake_eat_fruit = False
        current_direction = direction
    
    finish_game(score=score,window=window)


#finalização do jogo
def finish_game(score,window):
    height, width = window.getmaxyx()
    s = f"Você perdeu! Coletou {score} frutas!"
    y = int(height/2)
    x = int((width - len(s)) /2)
    window.addstr(y,x,s)
    window.refresh()
    time.sleep(5)

    
#usando a direnção ao contraria da snake 
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


#gerando a nova fruta de forma aleatoria 
def get_new_fruit(window):
    height, width = window.getmaxyx()
    return [random.randint(1, height-2), random.randint(1,width-2) ]


#validação quando a snake relar nas bordas
def snake_hit_border(snake,window):
    head = snake[0]
    return actor_hit_border(actor=head, window=window)


#validação para quando a snake relar na fruta
def snake_hit_fruit(snake,fruit):
    return fruit in snake


#validação quando a snake relar nela
def snake_hit_itself(snake):
    head = snake[0]
    body = snake[1:]
    return head in body

#Desenhando o ambiente deixando tudo preto e com borda em volta
def draw_screen(window):
    window.clear()
    window.border(0)

#desenhando a snake
def draw_snake(snake, window):
    head = snake[0]
    draw_actor(actor=head, window=window, char="@")
    body = snake[1:]
    for body_part in body:
        draw_actor(actor=body_part, window=window, char="s")


#Desenhando o ator tanto a snake quanto a fruta
def draw_actor(actor, window, char):
    window.addch(actor[0], actor[1], char)


#Verificação da direção com as setas 
def get_new_direction(window, timeout):
    window.timeout(timeout)
    direction = window.getch() 
    if direction in [curses.KEY_UP, curses.KEY_LEFT,curses.KEY_RIGHT, curses.KEY_DOWN]:
        return direction
    return None

#Movendo a Snake
def move_snake(snake,direction, snake_eat_fruit):
    head = snake[0].copy()
    move_actor(actor=head, direction=direction)
    snake.insert(0,head)
    if not snake_eat_fruit:
        snake.pop()

#movimentação com as setas
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

#validação de relar na borda snake/fruit
def actor_hit_border(actor, window):
    height, width = window.getmaxyx()
    if (actor[0] <= 0) or (actor[0] >= height-1):
        return True
    if (actor[1] <= 0) or (actor[1] >= width-1):
        return True
    return False

#Nivel de dificuldade do jogo 
def select_difficulty():
    difficulty = {
        '1':1000,
        '2':500,
        '3':150,
        '4':90,
        '5':35,
    }
    while True:
        answer = input("Selecione a dificuldade de 1 a 5: ")
        game_speeed = difficulty.get(answer)
        if game_speeed is not None:
            return game_speeed
        print('Escolha a dificuldade de 1 a 5!')

if __name__ == '__main__':
    curses.wrapper(game_loop, game_speed=select_difficulty())
