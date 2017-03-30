import webbrowser
import time

totalBreaks = 3
breakCount = 0

print('Program started')

while(breakCount < totalBreaks):
    time.sleep(5)
    webbrowser.open_new('https://www.youtube.com/watch?v=KfXIF2Mm2Kc')
    breakCount = breakCount + 1