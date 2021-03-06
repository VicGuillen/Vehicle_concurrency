import threading
from time import sleep

class RedLight(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.deactivate()

    def activate(self):
        self.activated=True

    def deactivate(self):
        self.pos=0  # number of lights on
        self.activated=False

    def get_activated(self):
        return self.activated

    def get_status(self):
        return self.pos


    def run(self):
        while True:
            if self.activated:
                for i in range(1,5):  # si ponemos range(0,5) no se queda la de abajo fija
                    self.pos = i
                    sleep(0.2)
            
            else:
                self.pos = 0
            

        
            sleep(0.2)
    
    
