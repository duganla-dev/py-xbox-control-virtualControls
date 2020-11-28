from inputs import get_gamepad
import mouse


from virtualControls import *

while True:
    if win32api.GetAsyncKeyState(ord('Q')):
        exit()
    
    events = get_gamepad()
    for event in events:
        if event.ev_type == "Key":
            if event.state == 1:
                down = True
            if event.state == 0:
                down = False


            if event.code == 'BTN_EAST':
                print("B")
                if down:
                    mouse.press('right')
                else:
                    mouse.release('right')


            if event.code == 'BTN_NORTH':
                print("Y")
                if down:LBUTTON()
            if event.code == 'BTN_WEST':
                print("X")

         
            if event.code == 'BTN_SOUTH':
                print("A")
                if down:
                    mouse.press('left')
                else:
                    mouse.release('left')
                

            if event.code == "BTN_TL":
                print("Left Bumper")
                if down:
                    VOLUME_UP()

            if event.code == "BTN_TR":
                print("Right Bumper")
                if down:
                    VOLUME_DOWN()

            if event.code == 'BTN_START':
                print('START')
            if event.code == 'BTN_SELECT':
                print('SELECT')


            if event.code == 'BTN_THUMBL':
                print('Left Thumb')
            if event.code == 'BTN_THUMBR':
                print('Right Thumb')
                if down:
                    Media_PLAY_PAUSE()
            

            if down:
                print("Down")
            if down:
                print("UP")

        if event.ev_type == 'Absolute':
            if event.code == 'ABS_HAT0Y':
                if event.state == -1:
                    print('D-Pad UP')
                if event.state == 1:
                    print('D-Pad Down')
                if event.state == 0:
                    print('D-Pad Release')

            if event.code == 'ABS_HAT0X':
                if event.state == -1:
                    print('D-Pad Left')
                if event.state == 1:
                    print('D-Pad Right')
                if event.state == 0:
                    print('D-Pad Release')
                    
            if event.code == 'ABS_Z':
                print('Left Trigger')
                print(event.state)
                
            if event.code == 'ABS_RZ':
                print('Right Trigger')
                print(event.state)

            if event.code == 'ABS_X':
                #print('Right Stick X: ')
                #print(event.state)
                moveMouce(event.state, 0)
            
            if event.code == 'ABS_Y':
                #print('Right Stick Y: ')
                #print(event.state)
                moveMouce(0, event.state)

            
            if not event.code == 'ABS_X' and not event.code == 'ABS_Y' and not event.code == 'ABS_RX' and not event.code == 'ABS_RY':
                print("Event Type: " + event.ev_type)
                print("Event Code: " + event.code)
                print("Event State: " + str(event.state))
                print("------------------------")
