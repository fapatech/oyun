# oyun
fruıt ninja mblock ve python kodlar
from mblock import event
import time
import random

blade_index = 0

@event.greenflag
def on_greenflag():
    global blade_index
    sprite.size = 100
    blade_index = 3
    sprite.set_variable('blade', 'Pixel Love')
    sprite.broadcast(str('refreshblade'))
    while True:
        sprite.clone('_myself_')



@event.received('refreshblade')
def on_received():
    global blade_index
    sprite.set_costume('sprite.get_variable('blade')')


@event.keypressed('right arrow')
def on_keypressed():
    global blade_index
    blade_index = ((blade_index + 1)) % #
    sprite.set_variable('blade', #)
    sprite.broadcast(str('refreshblade'))


@event.greenflag
def on_greenflag1():
    global blade_index
    sprite.set_variable('slicing?', 0)
    while True:
        while not (sprite.is_mousedown or sprite.is_keypressed('space')):
            pass

        sprite.set_variable('slicing?', 1)
        sprite.show()
        while not not (sprite.is_mousedown or sprite.is_keypressed('space')):
            pass

        sprite.set_variable('slicing?', 0)
        sprite.hide()



@event.keypressed('left arrow')
def on_keypressed1():
    global blade_index
    blade_index = ((blade_index - 1)) % #
    sprite.set_variable('blade', #)
    sprite.broadcast(str('refreshblade'))


@event.greenflag
def on_greenflag2():
    global blade_index
    while True:
        sprite.towards('mouse')
        sprite.goto('mouse')



@event.received('refreshblade')
def on_received1():
    global blade_index
    if sprite.get_variable('blade') == 'Butterfly':
        while not not sprite.get_variable('blade') == 'Butterfly':
            if sprite.get_variable('slicing?') == 1:
                for count3 in range(int(random.randint(1, 3))):
                    sprite.clone('Butterfly')


            time.sleep(0.2)







# not supported yet
if sprite.get_variable('slicing?') == 1:
    sprite.goto('mouse')
    time.sleep(0)
    sprite.towards('mouse')
    sprite.show()
    for count in range(10):
        sprite.size = sprite.size + -10

    # not supported yet

# not supported yet





# not supported yet
if sprite.get_variable('blade') == 'Rainbow':
    for count2 in range(10):
        sprite.change_effect_by('color', 20)



# not supported yet
if sprite.get_variable('blade') == 'Original':
    time.sleep(0)
    sprite.set_costume('Original Tail')


# not supported yet
if sprite.get_variable('blade') == 'Shiny Red':
    time.sleep(0)
    sprite.set_costume('Shiny Red Tail')



# not supported yet
if sprite.get_variable('blade') == 'Pixel Love':
    sprite.clone('Pixel')
