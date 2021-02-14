import pywhatkit as kit
from pynput.keyboard import Key, Controller
#kit.add_driver_path('chromedriver.exe')
#kit.load_QRcode()
kit.sendwhatmsg('+91mobile number', 'you`s message', 21,6)
keyboard = Controller()
keyboard.press(Key.enter)
keyboard.release(Key.enter)
