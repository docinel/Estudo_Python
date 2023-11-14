import pyautogui as pa

pa.FAILSAFE = True

pa.sleep(5)

distance = 200
while distance > 0:
    pa.dragRel(distance, 0, 0.5)  # move right
    distance = distance - 5
    pa.dragRel(0, distance, 0.5)  # move down
    pa.dragRel(-distance, 0, 0.5)  # move left
    distance = distance - 5
    pa.dragRel(0, -distance, 0.5)  # move up