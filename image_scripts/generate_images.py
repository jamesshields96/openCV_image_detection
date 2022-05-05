import capture_screen
import pyautogui

#TODO: Write script to cycle through FFXIV character creator and take screenshots
def main():
    screen = capture_screen.ScreenCapture()
    screenWidth, screenHeight = pyautogui.size()
    pyautogui.FAILSAFE = True
    while True:
        print(pyautogui.position())



if __name__ == "__main__":
    main()
