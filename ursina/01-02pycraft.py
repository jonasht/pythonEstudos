from ursina import *


app = Ursina()



window.color = color.rgb(100, 255, 1)

window.exit_button.visible = False

def input(key):
    if key == 'q' or 'escape':
        quit()



jeff = Entity(model='cube', color=color.green)

app.run()
