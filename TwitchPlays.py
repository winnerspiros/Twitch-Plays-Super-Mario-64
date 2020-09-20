import time, subprocess, ctypes, random, string, re, sys, TwitchPlays_Connection, pyautogui, pydirectinput, pynput
from TwitchPlays_AccountInfo import TWITCH_USERNAME, TWITCH_OAUTH_TOKEN
from pynput.mouse import Button, Controller
SendInput = ctypes.windll.user32.SendInput
def PressKeyPynput(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.ki = pynput._util.win32.KEYBDINPUT(0, hexKeyCode, 0x0008, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x = pynput._util.win32.INPUT(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
def ReleaseKeyPynput(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.ki = pynput._util.win32.KEYBDINPUT(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x = pynput._util.win32.INPUT(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
def PressAndHoldKey(hexKeyCode, seconds):
    PressKeyPynput(hexKeyCode)
    time.sleep(seconds)
    ReleaseKeyPynput(hexKeyCode)
mouse = Controller()
Q = 0x10
W = 0x11
E = 0x12
R = 0x13
T = 0x14
Y = 0x15
U = 0x16
I = 0x17
O = 0x18
P = 0x19
A = 0x1E
S = 0x1F
D = 0x20
F = 0x21
G = 0x22
H = 0x23
J = 0x24
K = 0x25
L = 0x26
Z = 0x2C
X = 0x2D
C = 0x2E
V = 0x2F
B = 0x30
N = 0x31
M = 0x32
ESC = 0x01
ONE = 0x02
TWO = 0x03
THREE = 0x04
FOUR = 0x05
FIVE = 0x06
SIX = 0x07
SEVEN = 0x08
EIGHT = 0x09
NINE = 0x0A
ZERO = 0x0B
MINUS = 0x0C
EQUALS = 0x0D
BACKSPACE = 0x0E
SEMICOLON = 0x27
TAB = 0x0F
CAPS = 0x3A
ENTER = 0x1C
LEFT_CONTROL = 0x1D
LEFT_ALT = 0x38
LEFT_SHIFT = 0x2A
SPACE = 0x39
DELETE = 0x53
COMMA = 0x33
PERIOD = 0x34
BACKSLASH = 0x35
NUMPAD_0 = 0x52
NUMPAD_1 = 0x4F
NUMPAD_2 = 0x50
NUMPAD_3 = 0x51
NUMPAD_4 = 0x4B
NUMPAD_5 = 0x4C
NUMPAD_6 = 0x4D
NUMPAD_7 = 0x47
NUMPAD_8 = 0x48
NUMPAD_9 = 0x49
NUMPAD_PLUS = 0x4E
NUMPAD_MINUS = 0x4A
LEFT_ARROW = 0xCB
RIGHT_ARROW = 0xCD
UP_ARROW = 0xC8
DOWN_ARROW = 0xD0
LEFT_MOUSE = 0x100
RIGHT_MOUSE = 0x101
MIDDLE_MOUSE = 0x102
MOUSE3 = 0x103
MOUSE4 = 0x104
MOUSE5 = 0x105
MOUSE6 = 0x106
MOUSE7 = 0x107
MOUSE_WHEEL_UP = 0x108
MOUSE_WHEEL_DOWN = 0x109
COMA = 0x33
RIGHT_SHIFT = 0x36
t = TwitchPlays_Connection.Twitch();
t.twitch_connect(TWITCH_USERNAME, TWITCH_OAUTH_TOKEN);
while True:
    new_messages = t.twitch_recieve_messages();
    if not new_messages:
        continue
    else:
        try:  
            for message in new_messages:
                msg = message['message'].lower()
                username = message['username'].lower()
                usr = username.decode()
                if msg in ['up', 'u', 'forward', 'go up']:
                    PressKeyPynput(W)
                    time.sleep(1.0)
                    ReleaseKeyPynput(W)         
                if msg in ['tap up', 'micro up', 'tap u', 'micro u']:
                    PressKeyPynput(W)
                    time.sleep(0.1)
                    ReleaseKeyPynput(W)  
                if msg in ['tap up left', 'micro up left', 'tap ul', 'micro ul', 'tap left up', 'micro left up', 'tap lu', 'micro lu']:
                    PressKeyPynput(W)
                    PressKeyPynput(A)
                    time.sleep(0.1)
                    ReleaseKeyPynput(W)
                    ReleaseKeyPynput(A)
                if msg in ['tap down left', 'micro down left', 'tap dl', 'micro dl', 'tap left down', 'micro left down', 'tap ld', 'micro ld']:
                    PressKeyPynput(S)
                    PressKeyPynput(A)
                    time.sleep(0.1)
                    ReleaseKeyPynput(S)
                    ReleaseKeyPynput(A)
                if msg in ['tap down right', 'micro down right', 'tap dr', 'micro dr', 'tap right down', 'micro right down', 'tap rd', 'micro rd']:
                    PressKeyPynput(S)
                    PressKeyPynput(D)
                    time.sleep(0.1)
                    ReleaseKeyPynput(S)
                    ReleaseKeyPynput(D)
                if msg in ['tap up right', 'micro up right', 'tap ur', 'micro ur', 'tap right up', 'micro right up', 'tap ru', 'micro ru']:
                    PressKeyPynput(W)
                    PressKeyPynput(D)
                    time.sleep(0.1)
                    ReleaseKeyPynput(W)
                    ReleaseKeyPynput(D)
                if msg in ['light up', 'soft up', 'mini up', 'mini u', 'soft u', 'light u']:
                    PressKeyPynput(W)
                    time.sleep(0.3)
                    ReleaseKeyPynput(W)
                if msg in ['light up left', 'soft up left', 'mini up left', 'mini ul', 'soft ul', 'light left up', 'soft left up', 'mini left up', 'light lu', 'soft lu', 'mini lu', 'light ul']:
                    PressKeyPynput(W)
                    PressKeyPynput(A)
                    time.sleep(0.3)
                    ReleaseKeyPynput(W)
                    ReleaseKeyPynput(A)
                if msg in ['light down left', 'soft down left', 'mini down left', 'mini dl', 'soft dl', 'light left down', 'soft left down', 'mini left down', 'light ld', 'soft ld', 'mini ld', 'light dl']:
                    PressKeyPynput(S)
                    PressKeyPynput(A)
                    time.sleep(0.3)
                    ReleaseKeyPynput(A)
                    ReleaseKeyPynput(S)
                if msg in ['light down right', 'soft down right', 'mini down right', 'mini dr', 'soft dr', 'light right down', 'soft right down', 'mini right down', 'light rd', 'soft rd', 'mini rd', 'light dr']:
                    PressKeyPynput(S)
                    PressKeyPynput(D)
                    time.sleep(0.3)
                    ReleaseKeyPynput(S)
                    ReleaseKeyPynput(D)
                if msg in ['light up right', 'soft up right', 'mini up right', 'mini ur', 'soft ur', 'light right up', 'soft right up', 'mini right up', 'light ru', 'soft ru', 'mini ru', 'light ur']:
                    PressKeyPynput(W)
                    PressKeyPynput(D)
                    time.sleep(0.3)
                    ReleaseKeyPynput(W)
                    ReleaseKeyPynput(D)
                if msg in ['hard up', 'aggresive up', 'hard u', 'aggresive u']:
                    PressKeyPynput(W)
                    time.sleep(2.0)
                    ReleaseKeyPynput(W)
                if msg in ['hard up left', 'aggresive up left', 'hard ul', 'aggresive ul', 'hard left up', 'aggresive left up', 'hard lu', 'aggresive lu']:
                    PressKeyPynput(W)
                    PressKeyPynput(A)
                    time.sleep(2.0)
                    ReleaseKeyPynput(W)
                    ReleaseKeyPynput(A)
                if msg in ['hard down left', 'aggresive down left', 'hard dl', 'aggresive dl', 'hard left down', 'aggresive left down', 'hard ld', 'aggresive ld']:
                    PressKeyPynput(S)
                    PressKeyPynput(A)
                    time.sleep(2.0)
                    ReleaseKeyPynput(S)
                    ReleaseKeyPynput(A)
                if msg in ['hard down right', 'aggresive down right', 'hard dr', 'aggresive dr', 'hard right down', 'aggresive right down', 'hard rd', 'aggresive rd']:
                    PressKeyPynput(S)
                    PressKeyPynput(D)
                    time.sleep(2.0)
                    ReleaseKeyPynput(S)
                    ReleaseKeyPynput(D)
                if msg in ['hard up right', 'aggresive up right', 'hard ur', 'aggresive ur', 'hard right up', 'aggresive right up', 'hard ru', 'aggresive ru']:
                    PressKeyPynput(W)
                    PressKeyPynput(D)
                    time.sleep(2.0)
                    ReleaseKeyPynput(W)
                    ReleaseKeyPynput(D)
                if msg in ['tap left', 'micro left', 'tap l', 'micro l']:
                    PressKeyPynput(A)
                    time.sleep(0.1)
                    ReleaseKeyPynput(A)    
                if msg in ['left', 'turn left', 'l', 'go left']:
                    PressKeyPynput(A)
                    time.sleep(1.0)
                    ReleaseKeyPynput(A)
                if msg in ['light left', 'soft left', 'mini left', 'light l', 'soft l' 'mini l']:
                    PressKeyPynput(A)
                    time.sleep(0.3)
                    ReleaseKeyPynput(A)
                if msg in ['hard left', 'aggresive left', 'hard l', 'aggresive l']:
                    PressKeyPynput(A)
                    time.sleep(2.0)
                    ReleaseKeyPynput(A)
                if msg in ['tap right', 'micro right', 'tap r', 'micro r']:
                    PressKeyPynput(D)
                    time.sleep(0.1)
                    ReleaseKeyPynput(D)    
                if msg in ['right', 'r', 'go right', 'turn right']:
                    PressKeyPynput(D)
                    time.sleep(1.0)
                    ReleaseKeyPynput(D)
                if msg in ['light right', 'soft right', 'mini right', 'light r', 'soft r', 'mini r']:
                    PressKeyPynput(D)
                    time.sleep(0.3)
                    ReleaseKeyPynput(D)
                if msg in ['hard right', 'aggresive right', 'hard r', 'aggresive r']:
                    PressKeyPynput(D)
                    time.sleep(2.0)
                    ReleaseKeyPynput(D)
                if msg in ['tap down', 'micro down', 'tap d', 'micro d', 'tap back', 'micro back']:
                    PressKeyPynput(S)
                    time.sleep(0.1)
                    ReleaseKeyPynput(S)    
                if msg in ['down', 'd', 'go down', 'back']:
                    PressKeyPynput(S)
                    time.sleep(1.0)
                    ReleaseKeyPynput(S)
                if msg in ['light down', 'soft down', 'mini down', 'light d', 'mini d', 'soft d', 'mini back', 'soft back', 'light back']:
                    PressKeyPynput(S)
                    time.sleep(0.3)
                    ReleaseKeyPynput(S)
                if msg in ['hard down', 'aggresive down', 'hard d', 'aggresive d', 'hard back', 'aggresive back']:
                    PressKeyPynput(S)
                    time.sleep(2.0)
                    ReleaseKeyPynput(S)
                if msg in ['ul', 'up left', 'forward left']: 
                    PressKeyPynput(W)
                    PressKeyPynput(A)
                    time.sleep(1.0)
                    ReleaseKeyPynput(W)
                    ReleaseKeyPynput(A)
                if msg in ['lu', 'left up', 'left forward']: 
                    PressKeyPynput(A)
                    PressKeyPynput(W)
                    time.sleep(1.0)
                    ReleaseKeyPynput(A)
                    ReleaseKeyPynput(W)  
                if msg in ['ur', 'up right', 'forward right']: 
                    PressKeyPynput(W)
                    PressKeyPynput(D)
                    time.sleep(1.0)
                    ReleaseKeyPynput(W)
                    ReleaseKeyPynput(D)
                if msg in ['ru', 'right up', 'right forward']: 
                    PressKeyPynput(D)
                    PressKeyPynput(W)
                    time.sleep(1.0)
                    ReleaseKeyPynput(D)
                    ReleaseKeyPynput(W)
                if msg in ['dl', 'down left']: 
                    PressKeyPynput(S)
                    PressKeyPynput(A)
                    time.sleep(1.0)
                    ReleaseKeyPynput(S)
                    ReleaseKeyPynput(A)
                if msg in ['ld', 'left down']: 
                    PressKeyPynput(A)
                    PressKeyPynput(S)
                    time.sleep(1.0)
                    ReleaseKeyPynput(A)
                    ReleaseKeyPynput(S)
                if msg in ['dr', 'down right']: 
                    PressKeyPynput(S)
                    PressKeyPynput(D)
                    time.sleep(1.0)
                    ReleaseKeyPynput(S)
                    ReleaseKeyPynput(D)
                if msg in ['rd', 'right down']: 
                    PressKeyPynput(D)
                    PressKeyPynput(S)
                    time.sleep(1.0)
                    ReleaseKeyPynput(D)
                    ReleaseKeyPynput(S)
                if msg in ['hu', 'hold up', 'hold forward', 'long up', 'long forward', 'long l', 'hold u']:
                    PressKeyPynput(W)
                    time.sleep(3.0)
                    ReleaseKeyPynput(W)                 
                if msg in ['hd', 'hold down', 'hold back', 'long down', 'long back', 'long d', 'hold d']:
                    PressKeyPynput(S)
                    time.sleep(3.0)
                    ReleaseKeyPynput(S)                   
                if msg in ['hl', 'hold left', 'long left', 'long l']:
                    PressKeyPynput(A)
                    time.sleep(3.0)
                    ReleaseKeyPynput(A)
                if msg in ['hr', 'hold right', 'hold r', 'long r', 'long right']:
                    PressKeyPynput(D)
                    time.sleep(3.0)
                    ReleaseKeyPynput(D)                                   
                if msg in ['hul', 'hold up left', 'hold forward left', 'long up left', 'hold ul', 'long ul', 'long forward left']: 
                    PressKeyPynput(W)
                    PressKeyPynput(A)
                    time.sleep(3.0)
                    ReleaseKeyPynput(W)
                    ReleaseKeyPynput(A)                   
                if msg in ['hlu', 'hold left up', 'hold left forward', 'long left forward', 'long lu', 'hold lu', 'long left up']: 
                    PressKeyPynput(A)
                    PressKeyPynput(W)
                    time.sleep(3.0)
                    ReleaseKeyPynput(A)
                    ReleaseKeyPynput(W)                    
                if msg in ['hur', 'hold up right', 'hold forward right', 'long up right', 'long forward right', 'hold ur']: 
                    PressKeyPynput(W)
                    PressKeyPynput(D)
                    time.sleep(3.0)
                    ReleaseKeyPynput(W)
                    ReleaseKeyPynput(D)               
                if msg in ['hru', 'hold right up', 'hold right forward', 'long right forward', 'long right up', 'long ru', 'hold ru']: 
                    PressKeyPynput(D)
                    PressKeyPynput(W)
                    time.sleep(3.0)
                    ReleaseKeyPynput(D)
                    ReleaseKeyPynput(W)               
                if msg in ['hdl', 'hold down left', 'hold back left', 'hold dl', 'long down left', 'long back left', 'long dl']: 
                    PressKeyPynput(S)
                    PressKeyPynput(A)
                    time.sleep(3.0)
                    ReleaseKeyPynput(S)
                    ReleaseKeyPynput(A)               
                if msg in ['hld', 'hold left down', 'hold left back', 'long left back', 'long left down', 'long ld', 'hold ld']: 
                    PressKeyPynput(A)
                    PressKeyPynput(S)
                    time.sleep(3.0)
                    ReleaseKeyPynput(A)
                    ReleaseKeyPynput(S)               
                if msg in ['hdr', 'hold down right', 'hold back right', 'hold dr', 'long dr', 'long down right', 'long back right']: 
                    PressKeyPynput(S)
                    PressKeyPynput(D)
                    time.sleep(3.0)
                    ReleaseKeyPynput(S)
                    ReleaseKeyPynput(D)
                if msg in ['select', 'start']: 
                    PressAndHoldKey(SPACE, 0.1)  
                if msg in ['duck', 'ground', 'c', 'crouch', 'crowl']: 
                    PressKeyPynput(K)
                    time.sleep(1.3)
                    ReleaseKeyPynput(K)             
                if msg in ['left jump', 'jump left', 'l jump', 'jump l', 'l a', 'a l']:
                    PressAndHoldKey(A, 0.2)
                    PressKeyPynput(A)
                    PressAndHoldKey(L, 0.7)
                    ReleaseKeyPynput(A)                  
                if msg in ['down jump', 'jump down', 'back jump', 'jump back', 'backwards jump', 'jump backwards', 'jump d', 'd jump', 'd a', 'a d']:
                    PressAndHoldKey(S, 0.2)
                    PressKeyPynput(S)
                    PressAndHoldKey(L, 0.7)
                    ReleaseKeyPynput(S)               
                if msg in ['right jump', 'jump right', 'r jump', 'jump r', 'r a', 'a r']:
                    PressAndHoldKey(D, 0.2)
                    PressKeyPynput(D)
                    PressAndHoldKey(L, 0.7)
                    ReleaseKeyPynput(D)              
                if msg in ['forward jump', 'jump up', 'jump forward', 'up jump', 'jump u', 'a u', 'u a']: 
                    PressKeyPynput(W)
                    time.sleep(0.2)
                    PressKeyPynput(L)
                    time.sleep(0.7)
                    ReleaseKeyPynput(W)
                    ReleaseKeyPynput(L)                   
                if msg in ['long jump', 'longjump', 'longjump up', 'long jump up', 'longjump u', 'long jump u', 'longjump forward', 'long jump forward', 'u longjump', 'up longjump', 'u long jump']:
                    PressKeyPynput(W)
                    time.sleep(0.28)
                    PressKeyPynput(K)
                    time.sleep(0.2)
                    PressAndHoldKey(L, 0.45)
                    ReleaseKeyPynput(K)
                    ReleaseKeyPynput(W)                   
                if msg in ['bowser spin', 'spin', 'spin bowser']:
                    PressAndHoldKey(D, 0.4)
                    PressAndHoldKey(W, 0.4)
                    PressAndHoldKey(A, 0.3)
                    PressAndHoldKey(S, 0.3)
                    spin=0
                    while spin<=10:
                        spin+=1
                        PressAndHoldKey(D, 0.2)
                        PressAndHoldKey(W, 0.2)
                        PressAndHoldKey(A, 0.2)
                        PressAndHoldKey(S, 0.2)
                    PressAndHoldKey(COMA, 0.4)                                
                if msg in ['long jump left', 'longjump left', 'left long jump', 'left longjump', 'l longjump', 'longjump l', 'l long jump', 'long jump l']:
                    PressKeyPynput(A)
                    time.sleep(0.28)
                    PressKeyPynput(K)
                    time.sleep(0.2)
                    PressAndHoldKey(L, 0.45)
                    ReleaseKeyPynput(K)
                    ReleaseKeyPynput(A)                   
                if msg in ['long jump right', 'longjump right', 'right long jump', 'right longjump', 'r longjump', 'longjump r', 'r long jump', 'long jump r']:
                    PressKeyPynput(D)
                    time.sleep(0.28)
                    PressKeyPynput(K)
                    time.sleep(0.2)
                    PressAndHoldKey(L, 0.45)
                    ReleaseKeyPynput(K)
                    ReleaseKeyPynput(D)                   
                if msg in ['long jump back', 'longjump back', 'back long jump', 'back longjump', 'longjump d', 'long jump d', 'longjump down', 'd long jump', 'd longjump', 'down longjump']:
                    PressKeyPynput(S)
                    time.sleep(0.28)
                    PressKeyPynput(K)
                    time.sleep(0.2)
                    PressAndHoldKey(L, 0.45)
                    ReleaseKeyPynput(K)
                    ReleaseKeyPynput(S)                  
                if msg in ['blj', 'backwards longjump', 'backwards long jump']:
                    PressKeyPynput(W)
                    time.sleep(0.25)
                    ReleaseKeyPynput(W)
                    PressAndHoldKey(K, 0.1)
                    PressKeyPynput(S)
                    PressAndHoldKey(L, 0.4)
                    time.sleep(0.3)
                    ReleaseKeyPynput(S)                   
                if msg in ['bljx250 up', 'backwards longjump x250 up', 'backwards long jump x250 up', 'x250 backwards longjump up', 'x250 backwards long jump up', 'blj x250 forward', 'blj x 250 forward', 'bljx250 forward', 'up blj x 250', 'up blj x250']:
                    PressKeyPynput(W)
                    time.sleep(0.26)
                    PressKeyPynput(K)
                    time.sleep(0.1)
                    PressKeyPynput(L)
                    time.sleep(0.1)
                    ReleaseKeyPynput(W)
                    PressKeyPynput(S)
                    time.sleep(0.1)
                    ReleaseKeyPynput(L)
                    time.sleep(0.08)
                    timer=0
                    while timer<=40:
                        timer+=1
                        PressAndHoldKey(L, 0.01854)
                        time.sleep(0.01874)
                    timer=0  
                    while timer<=210:
                        timer+=1
                        PressAndHoldKey(L, 0.0109) 
                        time.sleep(0.0084)
                    ReleaseKeyPynput(K)
                    ReleaseKeyPynput(S)                     
                if msg in ['bljx250 left', 'backwards longjump x250 left', 'backwards long jump x250 left', 'x250 backwards longjump left', 'x250 backwards long jump left', 'blj x250 left', 'blj x 250 left', 'bljx250 left', 'blj x 250 left', 'blj x250 left']:
                    PressKeyPynput(A)
                    time.sleep(0.26)
                    PressKeyPynput(K)
                    time.sleep(0.1)
                    PressKeyPynput(L)
                    time.sleep(0.1)
                    ReleaseKeyPynput(A)
                    PressKeyPynput(D)
                    time.sleep(0.1)
                    ReleaseKeyPynput(L)
                    time.sleep(0.08)
                    timer=0
                    while timer<=40:
                        timer+=1
                        PressAndHoldKey(L, 0.01854)
                        time.sleep(0.01874)
                    timer=0  
                    while timer<=210:
                        timer+=1
                        PressAndHoldKey(L, 0.0109) 
                        time.sleep(0.0084)
                    ReleaseKeyPynput(K)
                    ReleaseKeyPynput(D) 
                if msg in ['bljx250 right', 'backwards longjump x250 right', 'backwards long jump x250 right', 'x250 backwards longjump right', 'x250 backwards long jump right', 'blj x250 right', 'blj x 250 right', 'bljx250 right', 'blj x 250 right', 'blj x250 right']:
                    PressKeyPynput(D)
                    time.sleep(0.26)
                    PressKeyPynput(K)
                    time.sleep(0.1)
                    PressKeyPynput(L)
                    time.sleep(0.1)
                    ReleaseKeyPynput(D)
                    PressKeyPynput(A)
                    time.sleep(0.1)
                    ReleaseKeyPynput(L)
                    time.sleep(0.08)
                    timer=0
                    while timer<=40:
                        timer+=1
                        PressAndHoldKey(L, 0.01854)
                        time.sleep(0.01874)
                    timer=0  
                    while timer<=210:
                        timer+=1
                        PressAndHoldKey(L, 0.0109) 
                        time.sleep(0.0084)
                    ReleaseKeyPynput(K)
                    ReleaseKeyPynput(A)  
                if msg in ['bljx250 down', 'backwards longjump x250 down', 'backwards long jump x250 down', 'x250 backwards longjump down', 'x250 backwards long jump down', 'blj x250 down', 'blj x 250 down', 'bljx250 down', 'blj x 250 down', 'blj x250 down']:
                    PressKeyPynput(S)
                    time.sleep(0.26)
                    PressKeyPynput(K)
                    time.sleep(0.1)
                    PressKeyPynput(L)
                    time.sleep(0.1)
                    ReleaseKeyPynput(S)
                    PressKeyPynput(W)
                    time.sleep(0.1)
                    ReleaseKeyPynput(L)
                    time.sleep(0.08)
                    timer=0
                    while timer<=40:
                        timer+=1
                        PressAndHoldKey(L, 0.01854)
                        time.sleep(0.01874)
                    timer=0  
                    while timer<=210:
                        timer+=1
                        PressAndHoldKey(L, 0.0109) 
                        time.sleep(0.0084)                 
                    ReleaseKeyPynput(K)
                    ReleaseKeyPynput(W)                                                      
                if msg in ['hold forward forever', 'run forever up', 'hold up forever', 'up forever',  'run up forever', 'u forever']:
                    PressKeyPynput(W)                    
                if msg in ['hold down forever', 'run forever down', 'hold back forever', 'down forever', 'run forever down', 'd forever']:
                    PressKeyPynput(S)                    
                if msg in ['hold left forever', 'run forever left', 'left forever', 'run forever left', 'l forever']:
                    PressKeyPynput(A)                  
                if msg in ['hold right forever', 'run forever right', 'right forever', 'run forever right', 'r forever']:
                    PressKeyPynput(D)            
                if msg in ['!stop', 'stop', 'release', 'end', 'release key', 'release keys', 's', '!end', '!s']:
                    ReleaseKeyPynput(W)
                    ReleaseKeyPynput(A)
                    ReleaseKeyPynput(S)
                    ReleaseKeyPynput(D)
                    ReleaseKeyPynput(L)
                    ReleaseKeyPynput(COMA)
                    ReleaseKeyPynput(K)                   
                if msg in ['jump up left', 'jump left forward', 'jump forward left', 'forward jump left', 'jump ul', 'jump lu', 'ul jump', 'lu jump', 'up left left', 'left up jump']: 
                    PressKeyPynput(W)
                    PressKeyPynput(A)
                    time.sleep(0.3)
                    PressKeyPynput(L)
                    time.sleep(0.5)
                    ReleaseKeyPynput(W)
                    ReleaseKeyPynput(A)
                    ReleaseKeyPynput(L)     
                if msg in ['jump up right', 'jump right forward', 'jump forward right', 'forward jump right', 'jump ur', 'jump ru', 'ur jump', 'ru jump', 'up right jump', 'right up jump']: 
                    PressKeyPynput(W)
                    PressKeyPynput(D)
                    time.sleep(0.3)
                    PressKeyPynput(L)
                    time.sleep(0.5)
                    ReleaseKeyPynput(W)
                    ReleaseKeyPynput(D)
                    ReleaseKeyPynput(L)                    
                if msg in ['jump down left', 'jump left down', 'jump back left', 'back jump left', 'jump dl', 'jump ld', 'ld jump', 'dl jump', 'left down jump', 'down left jump']: 
                    PressKeyPynput(S)
                    PressKeyPynput(A)
                    time.sleep(0.3)
                    PressKeyPynput(L)
                    time.sleep(0.5)
                    ReleaseKeyPynput(S)
                    ReleaseKeyPynput(A)
                    ReleaseKeyPynput(L)     
                if msg in ['jump down right', 'jump right down', 'jump back right', 'back jump right', 'jump dr', 'jump rd', 'rd jump', 'dr jump', 'right down jump', 'down right jump']: 
                    PressKeyPynput(S)
                    PressKeyPynput(D)
                    time.sleep(0.3)
                    PressKeyPynput(L)
                    time.sleep(0.5)
                    ReleaseKeyPynput(S)
                    ReleaseKeyPynput(D)
                    ReleaseKeyPynput(L)                            
                if msg in ['back flip', 'backflip']: 
                    PressKeyPynput(K)
                    time.sleep(0.3)
                    PressKeyPynput(L)
                    time.sleep(0.3)
                    ReleaseKeyPynput(L)
                    ReleaseKeyPynput(K)                                                         
                if msg in ['mini stomp', 'short stomp', 'mini ground pound', 'short ground pound', 'mini groundpound', 'short groundpound', 'fast stomp']: 
                    PressKeyPynput(K)
                    PressKeyPynput(L)
                    time.sleep(0.2)
                    ReleaseKeyPynput(L)
                    ReleaseKeyPynput(K)                   
                if msg in ['jump stomp', 'stomp', 'ground pound', 'groundpound']:
                    PressKeyPynput(L)
                    time.sleep(0.5)
                    PressKeyPynput(K)
                    time.sleep(0.1)
                    ReleaseKeyPynput(L)
                    ReleaseKeyPynput(K)                  
                if msg in ['forward jump stomp', 'forward stomp', 'up stomp', 'forward ground pound', 'forward groundpound', 'up ground pound', 'up grounpound', 'ground pound forward', 'ground pound up', 'groundpound forward', 'groundpound up', 'u stomp', 'u groundpound', 'stomp u', 'groundpound u']:
                    PressAndHoldKey(W, 0.3) 
                    PressKeyPynput(W)
                    PressAndHoldKey(L, 0.5)
                    PressAndHoldKey(K, 0.2)
                    ReleaseKeyPynput(L)
                    ReleaseKeyPynput(W)                   
                if msg in ['left jump stomp', 'left stomp', 'stomp left', 'jump left stomp', 'left ground pound', 'left groundpound', 'jump left ground pound', 'jump left groundpound', 'ground pound left', 'groundpound left', 'l stomp', 'stomp l', 'l groundpound', 'groundpound l']:
                    PressAndHoldKey(A, 0.3) 
                    PressKeyPynput(A)
                    PressAndHoldKey(L, 0.5)
                    PressAndHoldKey(K, 0.2)
                    ReleaseKeyPynput(L)
                    ReleaseKeyPynput(A)                  
                if msg in ['right jump stomp', 'right stomp', 'stomp right', 'jump right stomp', 'jump right ground pound', 'jump right groundpound', 'right groundpound', 'right ground pound', 'ground pound right', 'groundpound right', 'r stomp', 'stomp r', 'r groundpound', 'groundpound r']:
                    PressAndHoldKey(D, 0.3) 
                    PressKeyPynput(D)
                    PressAndHoldKey(L, 0.5)
                    PressAndHoldKey(K, 0.2)
                    ReleaseKeyPynput(L)
                    ReleaseKeyPynput(D)                   
                if msg in ['down jump stomp', 'down stomp', 'stomp down', 'back stomp', 'stomp back', 'jump back stomp', 'jump down stomp', 'back jump stomp', 'jump down ground pound', 'jump down groundpound', 'jump back ground pound', 'jump back groundpound', 'back ground pound', 'back groundpound', 'down ground pound', 'down groundpound', 'd stomp', 'stomp d', 'd groundpound', 'groundpound d']:
                    PressAndHoldKey(S, 0.3) 
                    PressKeyPynput(S)
                    PressAndHoldKey(L, 0.5)
                    PressAndHoldKey(K, 0.2)
                    ReleaseKeyPynput(L)
                    ReleaseKeyPynput(S)           
                if msg in ['punch', 'b', 'grab']: 
                    PressAndHoldKey(COMA, 0.1)
                if msg in ['punch punch', 'b b', 'bb']:
                    PressAndHoldKey(COMA, 0.2)
                    time.sleep(0.2)
                    PressAndHoldKey(COMA, 0.2)
                    time.sleep(0.2)
                if msg in ['punch punch punch', 'b b b', 'bbb', 'punch punch kick', 'triplepunch', 'triplehit', 'triple b', 'triple punch', 'triple hit']: 
                    PressAndHoldKey(COMA, 0.2)
                    time.sleep(0.2)
                    PressAndHoldKey(COMA, 0.2)
                    time.sleep(0.2)
                    PressAndHoldKey(COMA, 0.2)                 
                if msg in ['kick']:
                    PressKeyPynput(L)
                    PressAndHoldKey(COMA, 0.2)
                    ReleaseKeyPynput(L)              
                if msg in ['down kick', 'kick down']:
                    PressKeyPynput(K)
                    time.sleep(0.25)
                    PressAndHoldKey(COMA, 0.2)
                    ReleaseKeyPynput(K)
                if msg in ['jump', 'a', 'read', 'talk']: 
                    PressAndHoldKey(L, 0.73)                  
                if msg in ['soft jump', ' soft a', 'light jump', 'light a']: 
                    PressAndHoldKey(L, 0.05)                  
                if msg in ['cl', 'camera left', 'left camera', 'look left', 'look l', 'camera l']:
                    PressKeyPynput(G)
                    time.sleep(0.3)
                    ReleaseKeyPynput(G)                   
                if msg in ['cr', 'camera right', 'right camera', 'look right', 'look r', 'camera r']:
                    PressKeyPynput(J)
                    time.sleep(0.3)
                    ReleaseKeyPynput(J)                  
                if msg in ['cu', 'camera forward', 'forward camera', 'up camera', 'camera up', 'zoom camera', 'camera zoom', 'zoom', 'look up', 'camera u', 'look u']:
                    PressKeyPynput(Y)
                    time.sleep(0.3)
                    ReleaseKeyPynput(Y)                
                if msg in ['cd', 'camera down', 'down camera', 'back camera', 'camera back', 'unzoom', 'camera d', 'look down', 'look d']:
                    PressKeyPynput(H)
                    time.sleep(0.3)
                    ReleaseKeyPynput(H)                
                if msg in ['change camera', 'mario camera', 'camera change', 'lattitude camera']:
                    PressAndHoldKey(B,0.4)              
                if msg in ['slide kick up', 'kick slide up', 'slide kick forward', 'kick slide forward', 'up kick slide', 'forward kick slide', 'up slide kick', 'forward slide kick', 'u kick slide', 'u slide kick']:
                    PressKeyPynput(W)
                    time.sleep(0.2)
                    PressAndHoldKey(K,0.1)
                    PressKeyPynput(COMA)
                    time.sleep(0.3)
                    ReleaseKeyPynput(COMA)
                    ReleaseKeyPynput(W)                   
                if msg in ['slide kick down', 'kick slide down', 'slide kick back', 'kick slide back', 'back kick slide', 'down kick slide', 'backwards slide kick', 'back slide kick', 'down slide kick', 'd slide kick', 'd kick slide']:
                    PressKeyPynput(S)
                    time.sleep(0.2)
                    PressAndHoldKey(K,0.1)
                    PressKeyPynput(COMA)
                    time.sleep(0.3)
                    ReleaseKeyPynput(COMA)
                    ReleaseKeyPynput(S)                    
                if msg in ['slide kick left', 'kick slide left', 'left kick slide', 'left slide kick', 'l slide kick', 'l kick slide']:
                    PressKeyPynput(A)
                    time.sleep(0.2)
                    PressAndHoldKey(K,0.1)
                    PressKeyPynput(COMA)
                    time.sleep(0.3)
                    ReleaseKeyPynput(COMA)
                    ReleaseKeyPynput(A)                   
                if msg in ['slide kick right', 'kick slide right', 'right kick slide', 'right slide kick', 'r slide kick', 'r kick slide']:
                    PressKeyPynput(D)
                    time.sleep(0.2)
                    PressAndHoldKey(K,0.1)
                    PressKeyPynput(COMA)
                    time.sleep(0.3)
                    ReleaseKeyPynput(COMA)
                    ReleaseKeyPynput(D)               
                if msg in ['jump kick', 'kick jump', 'a kick', 'a b']:
                    PressKeyPynput(L)
                    time.sleep(0.5)
                    PressAndHoldKey(COMA, 0.1) 
                    ReleaseKeyPynput(L)                   
                if msg in ['jump up kick', 'kick up jump', 'up jump kick', 'kick jump up', 'jump kick up', 'jump forward kick', 'kick jump forward', 'forward jump kick', 'kick jump forward', 'jump u kick', 'jump kick u', 'u jump kick']: 
                    PressKeyPynput(W)
                    time.sleep(0.1)
                    PressKeyPynput(L)
                    time.sleep(0.5)
                    ReleaseKeyPynput(W)
                    ReleaseKeyPynput(L)
                    PressAndHoldKey(COMA, 0.1)                     
                if msg in ['jump down kick', 'kick down jump', 'down jump kick', 'kick jump down', 'jump kick down', 'jump back kick', 'kick back jump', 'back jump kick', 'kick jump back', 'jump kick back', 'jump d kick', 'jump kick d', 'd jump kick']:
                    PressKeyPynput(S)
                    time.sleep(0.1)
                    PressKeyPynput(L)
                    time.sleep(0.5)
                    ReleaseKeyPynput(S)
                    ReleaseKeyPynput(L)
                    PressAndHoldKey(COMA, 0.1)                    
                if msg in ['jump left kick', 'kick left jump', 'left jump kick', 'kick jump left', 'jump kick left', 'l jump kick', 'l kick jump', 'jump l kick', 'jump kick l']:
                    PressKeyPynput(A)
                    time.sleep(0.1)
                    PressKeyPynput(L)
                    time.sleep(0.5)
                    ReleaseKeyPynput(A)
                    PressAndHoldKey(COMA, 0.1) 
                    ReleaseKeyPynput(L)                    
                if msg in ['jump right kick', 'kick right jump', 'right jump kick', 'kick jump right', 'jump kick right', 'r jump kick', 'r kick jump', 'jump r kick', 'jump kick r']:
                    PressKeyPynput(D)
                    time.sleep(0.1)
                    PressKeyPynput(L)
                    time.sleep(0.5)
                    ReleaseKeyPynput(D)
                    PressAndHoldKey(COMA, 0.1) 
                    ReleaseKeyPynput(L)                
                if msg in ['double jump', 'doublejump', 'aa', 'a a']:
                    jumpp=0
                    while jumpp<=5:
                        jumpp+=1
                        PressAndHoldKey(L,0.1)
                        time.sleep(0.2)           
                if msg in ['double jump forward', 'doublejump forward', 'double jump up', 'doublejump up', 'up double jump', 'up doublejump', 'forward double jump', 'forward doublejump', 'doublejump u', 'double jump u', 'u double jump', 'u doublejump']:
                    PressKeyPynput(W)
                    time.sleep(0.3)
                    jumpp=0
                    while jumpp<=5:
                        jumpp+=1
                        PressAndHoldKey(L,0.1)
                        time.sleep(0.2)
                    PressAndHoldKey(L,0.1)
                    time.sleep(0.2)
                    ReleaseKeyPynput(W)
                if msg in ['double jump left', 'doublejump left', 'left double jump', 'left doublejump', 'doublejump l', 'double jump l', 'l doublejump', 'l double jump']:
                    PressKeyPynput(A)
                    time.sleep(0.3)
                    jumpp=0
                    while jumpp<=5:
                        jumpp+=1
                        PressAndHoldKey(L,0.1)
                        time.sleep(0.2)
                    ReleaseKeyPynput(A)
                if msg in ['double jump right', 'doublejump right', 'right double jump', 'right doublejump', 'doublejump r', 'double jump r', 'r double jump', 'r doublejump']:
                    PressKeyPynput(D)
                    time.sleep(0.3)
                    jumpp=0
                    while jumpp<=5:
                        jump+=1
                        PressAndHoldKey(L,0.1)
                        time.sleep(0.2)
                    ReleaseKeyPynput(D)
                if msg in ['double jump down', 'doublejump down', 'down double jump', 'down doublejump', 'double jump back', 'doublejump back', 'back double jump', 'back doublejump', 'doublejump d', 'double jump d', 'd doublejump', 'd double jump']:
                    PressKeyPynput(S)
                    time.sleep(0.3)
                    jumppp=0
                    while jumpp<=5:
                        jumpp+=1
                        PressAndHoldKey(L,0.1)
                        time.sleep(0.2)
                    ReleaseKeyPynput(S)
                if msg in ['triple jump', 'triplejump', 'a a a', 'aaa']:
                    jumpp=0
                    while jumpp<=9:
                        jumpp+=1
                        PressAndHoldKey(L,0.1)
                        time.sleep(0.2)
                if msg in ['triple jump forward', 'triplejump forward', 'triple jump up', 'triplejump up', 'up triple jump', 'up triplejump', 'forward triple jump', 'forward triplejump', 'triplejump u', 'triple jump u', 'u triple jump', 'u triplejump']:
                    PressKeyPynput(W)
                    time.sleep(0.3)
                    jumpp=0
                    while jumpp<=9:
                        jumpp+=1
                        PressAndHoldKey(L,0.1)
                        time.sleep(0.2)
                    ReleaseKeyPynput(W)
                if msg in ['triple jump left', 'triplejump left', 'left triple jump', 'left triplejump', 'triplejump l', 'triple jump l', 'l triple jump', 'l triplejump']:
                    PressKeyPynput(A)
                    time.sleep(0.3)
                    jumpp=0
                    while jumpp<=9:
                        jumpp+=1
                        PressAndHoldKey(L,0.1)
                        time.sleep(0.2)
                    ReleaseKeyPynput(A)
                if msg in ['triple jump right', 'triplejump right', 'right triple jump', 'right triplejump', 'triplejump r', 'triple jump r', 'r triple jump', 'r triplejump']:
                    PressKeyPynput(D)
                    time.sleep(0.3)
                    jumpp=0
                    while jumpp<=9:
                        jumpp+=1
                        PressAndHoldKey(L,0.1)
                        time.sleep(0.2)
                    ReleaseKeyPynput(D)
                if msg in ['triple jump down', 'triplejump down', 'down triple jump', 'down triplejump', 'triple jump back', 'triplejump back', 'back triple jump', 'back triplejump', 'triplejump d', 'triple jump d', 'd triplejump', 'd triple jump']:
                    PressKeyPynput(S)
                    time.sleep(0.3)
                    jumpp=0
                    while jumpp<=9:
                        jumpp+=1
                        PressAndHoldKey(L,0.1)
                        time.sleep(0.2)
                    ReleaseKeyPynput(S)
                if msg in ['breakdance', 'break dance', 'do the mario', 'do the mario dance']:
                    PressKeyPynput(K)
                    time.sleep(0.25)
                    dancee=0
                    while dancee<=8:
                        dancee+=1
                        PressAndHoldKey(COMA,0.18)
                        time.sleep(0.13)
                    ReleaseKeyPynput(K)
                if msg in ['poop', 'poopoo', 'shit']:
                    PressAndHoldKey(K,2.0)
                if msg in ['wake', 'wake up']:
                    PressAndHoldKey(W,0.04)
                if msg in ['dive up', 'up dive', 'dive', 'jump dive', 'forward dive', 'dive forward', 'air dive', 'jump up dive', 'jump dive up', 'dive u', 'u dive']:
                    PressKeyPynput(W)
                    time.sleep(0.4)
                    PressAndHoldKey(L,0.33)
                    time.sleep(0.25)
                    PressAndHoldKey(COMA,0.1)
                    ReleaseKeyPynput(W)
                if msg in ['dive up jump', 'up dive jump', 'dive recover up', 'forward dive jump', 'dive forward jump', 'dive u jump', 'u dive jump', 'u jump dive']:
                    PressKeyPynput(W)
                    time.sleep(0.4)
                    PressAndHoldKey(L,0.33)
                    time.sleep(0.25)
                    PressAndHoldKey(COMA,0.1)
                    ReleaseKeyPynput(W)
                    PressAndHoldKey(L,0.2)
                if msg in ['dive left jump', 'left dive jump', 'dive recover left', 'dive jump left', 'dive l jump', 'l jump dive', 'left jump dive']:
                    PressKeyPynput(A)
                    time.sleep(0.4)
                    PressAndHoldKey(L,0.33)
                    time.sleep(0.25)
                    PressAndHoldKey(COMA,0.1)
                    ReleaseKeyPynput(A)
                    PressAndHoldKey(L,0.2)
                if msg in ['dive right jump', 'right dive jump', 'dive recover right', 'dive jump right', 'dive r jump', 'r jump dive', 'right jump dive']:
                    PressKeyPynput(D)
                    time.sleep(0.4)
                    PressAndHoldKey(L,0.33)
                    time.sleep(0.25)
                    PressAndHoldKey(COMA,0.1)
                    ReleaseKeyPynput(D)
                    PressAndHoldKey(L,0.2)
                if msg in ['dive down jump', 'down dive jump', 'dive recover down', 'back dive jump', 'dive back jump', 'dive d jump', 'd dive jump', 'd jump dive']:
                    PressKeyPynput(S)
                    time.sleep(0.4)
                    PressAndHoldKey(L,0.33)
                    time.sleep(0.25)
                    PressAndHoldKey(COMA,0.1)
                    ReleaseKeyPynput(S)
                    PressAndHoldKey(L,0.2)
                if msg in ['dive left', 'left dive', 'jump left dive', 'left jump dive', 'left dive jump', 'dive l', 'l dive']:
                    PressKeyPynput(A)
                    time.sleep(0.4)
                    PressAndHoldKey(L,0.33)
                    time.sleep(0.25)
                    PressAndHoldKey(COMA,0.1)
                    ReleaseKeyPynput(A)
                if msg in ['dive right', 'right dive', 'jump right dive', 'right jump dive', 'right dive jump', 'dive r', 'r dive']:
                    PressKeyPynput(D)
                    time.sleep(0.4)
                    PressAndHoldKey(L,0.33)
                    time.sleep(0.25)
                    PressAndHoldKey(COMA,0.1)
                    ReleaseKeyPynput(D)
                if msg in ['dive down', 'dive back', 'down dive', 'jump down dive', 'down jump dive', 'down dive jump', 'back dive', 'jump back dive', 'back jump dive', 'down dive jump', 'dive d', 'd dive']:
                    PressKeyPynput(S)
                    time.sleep(0.4)
                    PressAndHoldKey(L,0.33)
                    time.sleep(0.25)
                    PressAndHoldKey(COMA,0.1)
                    ReleaseKeyPynput(S)
                if msg in ['d backflip', 'down backflip', 'back backflip', 'backflip down', 'backflip d', 'backflip back', 'd back flip', 'back flip d']:
                    PressAndHoldKey(W,0.43)
                    time.sleep(0.01)
                    PressKeyPynput(S)
                    time.sleep(0.01)
                    PressKeyPynput(L)
                    time.sleep(0.4)
                    ReleaseKeyPynput(L)
                    ReleaseKeyPynput(S)
                if msg in ['up backflip', 'u backflip', 'forward backflip', 'backflip up', 'backflip u', 'backflip forward', 'u back flip', 'back flip u']:
                    PressAndHoldKey(S,0.43)
                    time.sleep(0.01)
                    PressKeyPynput(W)
                    time.sleep(0.01)
                    PressKeyPynput(L)
                    time.sleep(0.4)
                    ReleaseKeyPynput(L)
                    ReleaseKeyPynput(W)
                if msg in ['l backflip', 'left backflip', 'backflip left', 'backflip l', 'back flip l', 'l back flip']:
                    PressAndHoldKey(D,0.43)
                    time.sleep(0.01)
                    PressKeyPynput(A)
                    time.sleep(0.01)
                    PressKeyPynput(L)
                    time.sleep(0.4)
                    ReleaseKeyPynput(L)
                    ReleaseKeyPynput(A)
                if msg in ['r backflip', 'right backflip', 'backflip right', 'backflip r', 'r back flip', 'back flip r']:
                    PressAndHoldKey(A,0.43)
                    time.sleep(0.01)
                    PressKeyPynput(D)
                    time.sleep(0.01)
                    PressKeyPynput(L)
                    time.sleep(0.4)
                    ReleaseKeyPynput(L)
                    ReleaseKeyPynput(D)
                if msg in ['crowl up', 'crowl forward', 'baby steps up', 'baby steps u', 'baby steps forward', 'crowl u', 'baby step u', 'baby step up', 'baby step forward']:
                    PressKeyPynput(K)
                    time.sleep(0.3)
                    PressAndHoldKey(W,1.0)
                    ReleaseKeyPynput(K)
                if msg in ['crowl down', 'crowl back', 'baby steps down', 'baby steps d', 'baby steps back', 'crowl d', 'baby step d', 'baby step down', 'baby step back']:
                    PressKeyPynput(K)
                    time.sleep(0.3)
                    PressAndHoldKey(S,1.0)
                    ReleaseKeyPynput(K)
                if msg in ['crowl left', 'crowl l', 'baby steps left', 'baby steps left', 'baby steps l', 'baby step l', 'baby step left']:
                    PressKeyPynput(K)
                    time.sleep(0.3)
                    PressAndHoldKey(A,1.0)
                    ReleaseKeyPynput(K)
                if msg in ['crowl right', 'crowl r', 'baby steps right', 'baby steps right', 'baby steps r', 'baby step r', 'baby step r']:
                    PressKeyPynput(K)
                    time.sleep(0.3)
                    PressAndHoldKey(D,1.0)
                    ReleaseKeyPynput(K)
                if msg in ['go underwater', 'dive underwater', 'go under water', 'dive under water', 'down swim', 'swim down', 'downwards swim', 'swim downwards', 'swim d', 'd swim']:
                    PressKeyPynput(W)
                    time.sleep(0.2)
                    PressAndHoldKey(L,1.5)
                    ReleaseKeyPynput(W)
                if msg in ['swim forever', '!swim', 'forever swim', 'jump and grab', 'grab and jump', 'grab forever', 'jump and grab forever', 'grab and jump forever']:
                    PressKeyPynput(L)
                if msg in ['swim']:
                    PressAndHoldKey(L,1.5)
                if msg in ['up swim', 'swim up', 'upwards swim', 'swim upwards', 'u swim', 'swim u']:
                    PressKeyPynput(S)
                    time.sleep(0.2)
                    PressAndHoldKey(L,1.5)
                    ReleaseKeyPynput(S)
                if msg in ['left swim', 'swim left', 'l swim', 'swim l']:
                    PressKeyPynput(A)
                    time.sleep(0.2)
                    PressAndHoldKey(L,1.5)
                    ReleaseKeyPynput(A)
                if msg in ['right swim', 'swim right', 'r swim', 'swim r']:
                    PressKeyPynput(D)
                    time.sleep(0.2)
                    PressAndHoldKey(L,1.5)
                    ReleaseKeyPynput(D)
                if msg in ['short up slope', 'short kick up slope', 'short up kick slope', 'short slope up kick', 'short slope kick up', 'short up slope kick']:
                    PressKeyPynput(L)
                    time.sleep(0.2)
                    PressKeyPynput(W)
                    time.sleep(0.3)
                    sloped=0
                    while sloped<=7:
                        sloped+=1
                        PressAndHoldKey(COMA,0.1)
                        time.sleep(0.5)
                    ReleaseKeyPynput(W)
                    ReleaseKeyPynput(L)
                if msg in ['short left slope', 'short kick left slope', 'short left kick slope', 'short slope left kick', 'short slope kick left', 'short left slope kick']:
                    PressKeyPynput(L)
                    time.sleep(0.2)
                    PressKeyPynput(A)
                    time.sleep(0.3)
                    sloped=0
                    while sloped<=7:
                        sloped+=1
                        PressAndHoldKey(COMA,0.1)
                        time.sleep(0.5)
                    ReleaseKeyPynput(A)
                    ReleaseKeyPynput(L)
                if msg in ['short right slope', 'short kick right slope', 'short right kick slope', 'short slope right kick', 'short slope kick right', 'short right slope kick']:
                    PressKeyPynput(L)
                    time.sleep(0.2)
                    PressKeyPynput(D)
                    time.sleep(0.3)
                    sloped=0
                    while sloped<=7:
                        sloped+=1
                        PressAndHoldKey(COMA,0.1)
                        time.sleep(0.5)
                    ReleaseKeyPynput(D)
                    ReleaseKeyPynput(L)
                if msg in ['short down slope', 'short kick down slope', 'short down kick slope', 'short slope down kick', 'short slope kick down', 'short down slope kick']:
                    PressKeyPynput(L)
                    time.sleep(0.2)
                    PressKeyPynput(S)
                    time.sleep(0.3)
                    sloped=0
                    while sloped<=7:
                        sloped+=1
                        PressAndHoldKey(COMA,0.1)
                        time.sleep(0.5)
                    ReleaseKeyPynput(S)
                    ReleaseKeyPynput(L) 
                if msg in ['up slope', 'slope up', 'u slope', 'slope u', 'kick up slope', 'up kick slope', 'slope up kick', 'slope kick up', 'up slope kick']:
                    PressKeyPynput(L)
                    time.sleep(0.2)
                    PressKeyPynput(W)
                    time.sleep(0.3)
                    sloped=0
                    while sloped<=15:
                        sloped+=1
                        PressAndHoldKey(COMA,0.1)
                        time.sleep(0.5)
                    ReleaseKeyPynput(W)
                    ReleaseKeyPynput(L)
                if msg in ['left slope', 'l slope', 'slope left', 'slope l', 'kick left slope', 'left kick slope', 'slope left kick', 'slope kick left', 'left slope kick']:
                    PressKeyPynput(L)
                    time.sleep(0.2)
                    PressKeyPynput(A)
                    time.sleep(0.3)
                    sloped=0
                    while sloped<=15:
                        sloped+=1
                        PressAndHoldKey(COMA,0.1)
                        time.sleep(0.5)
                    ReleaseKeyPynput(A)
                    ReleaseKeyPynput(L)
                if msg in ['right slope', 'r slope', 'slope r', 'slope right', 'kick right slope', 'right kick slope', 'slope right kick', 'slope kick right', 'right slope kick']:
                    PressKeyPynput(L)
                    time.sleep(0.2)
                    PressKeyPynput(D)
                    time.sleep(0.3)
                    sloped=0
                    while sloped<=15:
                        sloped+=1
                        PressAndHoldKey(COMA,0.1)
                        time.sleep(0.5)
                    ReleaseKeyPynput(D)
                    ReleaseKeyPynput(L)
                if msg in ['down slope', 'd slope', 'slope d', 'slope down', 'kick down slope', 'down kick slope', 'slope down kick', 'slope kick down', 'down slope kick']:
                    PressKeyPynput(L)
                    time.sleep(0.2)
                    PressKeyPynput(S)
                    time.sleep(0.3)
                    sloped=0
                    while sloped<=15:
                        sloped+=1
                        PressAndHoldKey(COMA,0.1)
                        time.sleep(0.5)
                    ReleaseKeyPynput(S)
                    ReleaseKeyPynput(L)
                if msg in ['long up slope', 'long kick up slope', 'long up kick slope', 'long slope up kick', 'long slope kick up', 'long up slope kick']:
                    PressKeyPynput(L)
                    time.sleep(0.2)
                    PressKeyPynput(W)
                    time.sleep(0.3)
                    sloped=0
                    while sloped<=20:
                        sloped+=1
                        PressAndHoldKey(COMA,0.1)
                        time.sleep(0.5)
                    ReleaseKeyPynput(W)
                    ReleaseKeyPynput(L)
                if msg in ['long left slope', 'long kick left slope', 'long left kick slope', 'long slope left kick', 'long slope kick left', 'long left slope kick']:
                    PressKeyPynput(L)
                    time.sleep(0.2)
                    PressKeyPynput(A)
                    time.sleep(0.3)
                    sloped=0
                    while sloped<=20:
                        sloped+=1
                        PressAndHoldKey(COMA,0.1)
                        time.sleep(0.5)
                    ReleaseKeyPynput(A)
                    ReleaseKeyPynput(L)
                if msg in ['long right slope', 'long kick right slope', 'long right kick slope', 'long slope right kick', 'long slope kick right', 'long right slope kick']:
                    PressKeyPynput(L)
                    time.sleep(0.2)
                    PressKeyPynput(D)
                    time.sleep(0.3)
                    sloped=0
                    while sloped<=20:
                        sloped+=1
                        PressAndHoldKey(COMA,0.1)
                        time.sleep(0.5)
                    ReleaseKeyPynput(D)
                    ReleaseKeyPynput(L)
                if msg in ['long down slope', 'long kick down slope', 'long down kick slope', 'long slope down kick', 'long slope kick down', 'long down slope kick']:
                    PressKeyPynput(L)
                    time.sleep(0.2)
                    PressKeyPynput(S)
                    time.sleep(0.3)
                    sloped=0
                    while sloped<=20:
                        sloped+=1
                        PressAndHoldKey(COMA,0.1)
                        time.sleep(0.5)
                    ReleaseKeyPynput(S)
                    ReleaseKeyPynput(L)
                if msg in ['fast up slope', 'fast kick up slope', 'fast up kick slope', 'fast slope up kick', 'fast slope kick up', 'fast up slope kick']:
                    PressKeyPynput(L)
                    time.sleep(0.2)
                    PressKeyPynput(W)
                    time.sleep(0.3)
                    sloped=0
                    while sloped<=30:
                        sloped+=1
                        PressAndHoldKey(COMA,0.1)
                        time.sleep(0.1)
                    ReleaseKeyPynput(W)
                    ReleaseKeyPynput(L)
                if msg in ['fast left slope', 'fast kick left slope', 'fast left kick slope', 'fast slope left kick', 'fast slope kick left', 'fast left slope kick']:
                    PressKeyPynput(L)
                    time.sleep(0.2)
                    PressKeyPynput(A)
                    time.sleep(0.3)
                    sloped=0
                    while sloped<=30:
                        sloped+=1
                        PressAndHoldKey(COMA,0.1)
                        time.sleep(0.1)
                    ReleaseKeyPynput(A)
                    ReleaseKeyPynput(L)
                if msg in ['fast right slope', 'fast kick right slope', 'fast right kick slope', 'fast slope right kick', 'fast slope kick right', 'fast right slope kick']:
                    PressKeyPynput(L)
                    time.sleep(0.2)
                    PressKeyPynput(D)
                    time.sleep(0.3)
                    sloped=0
                    while sloped<=30:
                        sloped+=1
                        PressAndHoldKey(COMA,0.1)
                        time.sleep(0.1)
                    ReleaseKeyPynput(D)
                    ReleaseKeyPynput(L)
                if msg in ['fast down slope', 'fast kick down slope', 'fast down kick slope', 'fast slope down kick', 'fast slope kick down', 'fast down slope kick']:
                    PressKeyPynput(L)
                    time.sleep(0.2)
                    PressKeyPynput(S)
                    time.sleep(0.3)
                    sloped=0
                    while sloped<=30:
                        sloped+=1
                        PressAndHoldKey(COMA,0.1)
                        time.sleep(0.1)
                    ReleaseKeyPynput(S)
                    ReleaseKeyPynput(L)
                if msg in ['c forever', 'crouch forever', 'forever crouch', 'forever c', 'crowl forever', 'forever crowl']:
                    PressKeyPynput(K)
                if msg.startswith('up for '): 
                    try:
                        timee = msg[7:]
                        timee = float(timee)
                        if timee<=10 and timee>=0:
                            PressAndHoldKey(W,timee)
                    except:
                        print('er')
                if msg.startswith('left for '): 
                    try:
                        timee = msg[9:]
                        timee = float(timee)
                        if timee<=10 and timee>=0:
                            PressAndHoldKey(A,timee)
                    except:
                        print('er')
                if msg.startswith('right for '): 
                    try:
                        timee = msg[10:]
                        timee = float(timee)
                        if timee<=10 and timee>=0:
                            PressAndHoldKey(D,timee)
                    except:
                        print('er')
                if msg.startswith('down for '): 
                    try:
                        timee = msg[9:]
                        timee = float(timee)
                        if timee<=10 and timee>=0:
                            PressAndHoldKey(S,timee)
                    except:
                        print('er')
        except:
            print('Encountered an exception while reading chat.')
