from threading import Thread 
from mouse_logger import start_mouse_logger
from keyboard_logger import start_keyboard_logger

def main():
    mouse_thread=Thread(target=start_mouse_logger)
    keyboard_thread=Thread(target=start_keyboard_logger)

    mouse_thread.start()
    keyboard_thread.start()

    mouse_thread.join()
    keyboard_thread.join()

if __name__ == "__main__":
    main()