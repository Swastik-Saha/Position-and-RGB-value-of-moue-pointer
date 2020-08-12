import pyautogui, time

import tkinter as tk


root = tk.Tk()
root.title('Mouse Now')
root.geometry('350x170')
root.maxsize(350,170)
root.minsize(350,170)

positionStr = tk.StringVar()
x, y = pyautogui.position()
screenshot_obj = pyautogui.screenshot()
pixelColor = screenshot_obj.getpixel((x, y))
positionStr.set(f'X: {x}\nY: {y}\nRGB: {pixelColor}')
label = tk.Label(textvariable = positionStr, padx = 20, pady = 20, font = 'calibri 30 bold')
label.pack()


try:
    while True:
        time.sleep(0.5)
        x, y = pyautogui.position()
        screenshot_obj = pyautogui.screenshot()
        pixelColor = screenshot_obj.getpixel((x, y))
        positionStr.set(f'X: {x}\nY: {y}\nRGB: {pixelColor}')
        label.update()        
except:
    pass

root.mainloop()
