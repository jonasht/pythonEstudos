from direct.showbase.ShowBase import ShowBase


class MyApp(ShowBase):
    def __ini__(self):
        ShowBase.__init__(self)

        
app = MyApp()
app.run()




# ----
