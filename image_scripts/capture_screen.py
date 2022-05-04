#TODO: Write script to capture screen
import numpy as np
import cv2
from mss import mss
import mss.tools
from PIL import Image
from win32api import GetSystemMetrics
from dataclasses import dataclass, field
import time



@dataclass
class ScreenCapture:
    top: int = field(default=0)
    left: int = field(default=0)
    width: int = field(default=GetSystemMetrics(0))
    height: int = field(default=GetSystemMetrics(1))


    def run_capture(self):
        #create section of screen to be recorded
        bounding_box = {'top': self.top, 'left': self.left, 'width': self.width, 'height': self.height}

        with mss.mss() as sct:

            while True:
                last_time = time.time()

                sct_img = np.array(sct.grab(bounding_box))
                cv2.imshow('screen', sct_img)

                print("fps: {}".format(1 / (time.time() - last_time)))
                if (cv2.waitKey(1) & 0xFF) == ord('q'):
                    cv2.destroyAllWindows()
                    break

    def take_screenshot(self, sct_num = 1):
        top = 300
        left = 700
        width = 500
        height = 500

        with mss.mss() as sct:
            sct_area = {'top': top, 'left': left, 'width': width, 'height': height}
            output = "pos_base_images/pos_{sct_num}.png".format(sct_num = sct_num)

            sct_img = sct.grab(sct_area)

            mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

    def get_screen_data(self):
        return [self.width, self.height]

    def menu(self):
        while True:
            print("0. Exit")
            print("1. Run screen capture")
            print("2. Take screenshot")
            response = int(input("Select an Option "))
            if response == 1:
                self.run_capture()
            if response == 2:
                self.take_screenshot()
            if response == 0:
                break
if __name__ == "__main__":
    screen = ScreenCapture()
    screen.menu()


