from ursina import *
from ursina.prefabs.first_person_controller import *
app = Ursina()

maze = Entity(model='maze', texture='brick', color=color.gray,
              scale=20,
              collider='mesh'
              )

player = FirstPersonController(y=100)

EditorCamera()
app.run()
