from inputs import get_gamepad
import mouse
import win32api, win32gui

# https://docs.microsoft.com/uk-ua/windows/win32/inputdev/virtual-key-codes

sensitivity = 800
reactivity = 4000

def moveMouce(x,y):
    ax, ay = int(x), int(y)

    if ax > reactivity or ax < -reactivity or ay > reactivity or ay < -reactivity :
        print("AX " + str(ax))
    
        x, y = win32api.GetCursorPos()
        x  = x + ax / int(sensitivity)
        y = y + -ay / int(sensitivity)

        win32api.SetCursorPos((int(x),int(y)))



def Media_PLAY_PAUSE():
    from win32con import VK_MEDIA_PLAY_PAUSE, KEYEVENTF_EXTENDEDKEY
    win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)

def VOLUME_UP():
    from win32con import VK_VOLUME_UP, KEYEVENTF_EXTENDEDKEY
    win32api.keybd_event(VK_VOLUME_UP, 0, KEYEVENTF_EXTENDEDKEY, 0)

def VOLUME_DOWN():
    from win32con import VK_VOLUME_DOWN, KEYEVENTF_EXTENDEDKEY
    win32api.keybd_event(VK_VOLUME_DOWN, 0, KEYEVENTF_EXTENDEDKEY, 0)