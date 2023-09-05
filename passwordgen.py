import random
import pyautogui
#defining array
arr = [1,2,3,4,5]
randomindexofarr = random.randint(0, len(arr) - 1)
if randomindexofarr == 2:
 pyautogui.moveTo(-50 , 50)
print(randomindexofarr)