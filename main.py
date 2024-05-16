from selenium import webdriver
from pyautogui import keyDown, keyUp, press, screenshot
import time

# Note: size of img is (2560, 1600)
for_bg = (600, 400)
middle_x, middle_y = (565, 870)
bottom_x, bottom_y = (565, 995)


dinosaur_url = "https://elgoog.im/dinosaur-game/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(dinosaur_url)
driver.maximize_window()
time.sleep(2)

# Presses up arrow key to start game
press("up")
time.sleep(2)

while True:
    pixel_set = set()
    opened_img = screenshot()

    # All these are RGB colours represented as tuples:
    bg_colour = opened_img.getpixel(for_bg)

    for bot_y_value in range(bottom_y - 50, bottom_y + 51, 50):
        pixel_set.add(opened_img.getpixel((bottom_x, bot_y_value)))

    for bot_x_value in range(bottom_x - 180, bottom_x + 101, 20):
        pixel_set.add(opened_img.getpixel((bot_x_value, bottom_y)))

    for mid_y_value in range(middle_y - 50, middle_y + 51, 50):
        pixel_set.add(opened_img.getpixel((middle_x, mid_y_value)))

    for mid_x_value in range(middle_x - 180, middle_x + 101, 20):
        pixel_set.add(opened_img.getpixel((mid_x_value, bottom_y)))

    # Checks if there are obstacles in the middle and bottom regions
    for pixel in pixel_set:
        if pixel != bg_colour:
            press("up")
            time.sleep(0.001)
            break
