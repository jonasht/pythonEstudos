from direct.showbase.ShowBase import ShowBase
from direct.task import Task

from math import pi, sin, cos

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.scene = self.loader.loadModel('models/environment')
        self.scene.reparentTo(self.render)

        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        self.task_mgr.add(self.spinCameraTask, 'SpinCameraTask' )

    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)


        
app = App()
app.run()