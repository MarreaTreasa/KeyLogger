from pynput.mouse import Listener

def writeToFile(x,y):
    with open("mouse_log.txt","a") as f:
        f.write(f"Mouse moved to:({x},{y})\n")


def start_mouse_logger():
    with Listener(on_move=writeToFile) as listener:
        listener.join()

if __name__=="__main__":
    start_mouse_logger()
