from random import randint
import tkinter

for num in range(0,5):
    target = {'speed': randint(1, 100)}

    int = target['speed']

    if int <= 10:
        target['speed'] = 'very slow'

    elif int >= 11 and int <= 30:
        target['speed'] = 'slow'

    elif int >= 31 and int <= 80:
        target['speed'] = 'average'

    elif int >= 81 and int <= 95:
        target['speed'] = 'fast'

    elif int >= 96 and int <= 100:
        target['speed'] = 'very fast'


speed = target['speed']

print(speed)


if speed == 'very slow':
    spd = 1

if speed == 'slow':
    spd = 2

if speed == 'average':
    spd = 3

if speed == 'fast':
    spd = 4

if speed == 'very fast':
    spd = 5


boundary = 100

xboundary = (0, boundary)
yboundary = (0, boundary)

target = {'x_pos': randint(xboundary[0], xboundary[1]), 'y_pos': randint(yboundary[0], yboundary[1])}

for num in range(1, 5):
    psng = randint(1, 4)

    if psng == 1:
        target['x_pos'] = target['x_pos'] + randint(0, spd)
        target['y_pos'] = target['y_pos'] + randint(0, spd)

    elif psng == 2:
        target['x_pos'] = target['x_pos'] + randint(0, spd)
        target['y_pos'] = target['y_pos'] - randint(0 ,spd)

    elif psng == 3:
        target['x_pos'] = target['x_pos'] - randint(0, spd)
        target['y_pos'] = target['y_pos'] + randint(0, spd)

    elif psng == 4:
        target['x_pos'] = target['x_pos'] - randint(0, spd)
        target['y_pos'] = target['y_pos'] - randint(0, spd)

    else:
        print(':(')

    if target['x_pos'] >= boundary:
        target['x_pos'] = boundary

    if target['y_pos'] >= boundary:
        target['y_pos'] = boundary

    tarxy = (target['x_pos'], target['y_pos'])

    root = tkinter
    for r in range(boundary + 1):
        for c in range(boundary + 1):
            coordinate = (r, c)
            if tarxy == coordinate:
                tkinter(root, text='%s,%s,%s' (r, c, 'yaaay'),
                              borderwidth=5).grid(row=r, column=c)
                print(coordinate)

            else:
                tkinter(root, text='%s,%s' (r, c),
                              borderwidth=5).grid(row=r, column=c)

print(tarxy, 'qwerty')
root.mainloop(  )