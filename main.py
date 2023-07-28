from pynput import mouse
import threading
import time
Controller=mouse.Controller()
Button=mouse.Button

def right_click():
    Controller.click(Button.left, 1)

class auto_clicker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(10):
            # print('2')
            Controller.click(Button.right, 1)
            time.sleep(0.02)
ac=auto_clicker()
breaker=[]
with mouse.Events() as events:
    for event in events:
        if type(event) is mouse.Events.Click:
            if event.button==mouse.Button.middle and event.pressed:
                breaker.append(time.time())
                if(len(breaker)>=3 and breaker[-1]-breaker[0]<=2):
                    break
                elif len(breaker)>=3:
                    breaker=breaker[-2:]

        if type(event) is mouse.Events.Scroll and not ac.is_alive():
            try:
                ac.start()
            except:
                ac=auto_clicker()
                ac.start()
        

