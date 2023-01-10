from ursina import *

app = Ursina()

def update():
    firstEntity.rotation_y += 50 *time.dt
    # firstEntity.position += Vec3(1,0,0) * time.dt
    firstEntity.position += firstEntity.forward * time.dt
    
# firstEntity = Entity(model='cube',
#                      color=color.green,
#                      texture='brick',
#                      x=0,
#                      y=0,
#                      z=0
#                      )
firstEntity = Entity(model='cube',
                    color=color.green,
                    texture='brick',

                    position=(0,0,0),
                    rotation=(0,0,0),
                    scale=2,
                    )

EditorCamera()
app.run()
