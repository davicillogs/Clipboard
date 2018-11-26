import win32con
from ctypes import wintypes, byref, windll
import pyperclip as clipboard

#creamos la clase principal del modulo 
class Portapapeles :
    #varible  que almacenara los valores
    clip = ["","","","",""]

    def __init__(self):
        pass
      


    #Funcion que registra la combinacion de teclas en windows
    def register_hotkey(self,key,valor):
        key = key.split('-')
        mod = 0
        if 'Ctrl' in key:
            mod |= win32con.MOD_CONTROL
        if 'Shift' in key:
            mod |= win32con.MOD_SHIFT
        if 'Alt' in key:
            mod |= win32con.MOD_ALT
        key = key[-1].upper()
        assert key in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        if windll.user32.RegisterHotKey(None, valor, mod, ord(key)) != 0:
            print("Hotkey registered!")
            


    
    

    #Funcion que copia el ultimo valor que hay en el portapapeles en la var clip
    def copy (self):
        self.clip.reverse()
        self.clip.pop()
        self.clip.reverse()
        self.clip.append(clipboard.paste())
        print (self.clip)
    #Funciones para seleccionar el indice de la array en el cual queremos posicionarnos
    def val_1(self):
        clipboard.copy (self.clip[0])
        print (self.clip)

    def val_2(self):
        clipboard.copy (self.clip[1])
        print (self.clip)

    def val_3(self):
        clipboard.copy (self.clip[2])
        print (self.clip)

    def val_4(self):
        clipboard.copy (self.clip[3])
        print (self.clip)

    def val_5(self):
        clipboard.copy (self.clip[4])
        print (self.clip)
    #funcion que detecta cuando se ha pulsado la combinacion registrada
    def handle_hotkey(self):
       
        msg = wintypes.MSG()
            
        if windll.user32.GetMessageA(byref(msg), None, 0, 0) != 0:
            if msg.message == win32con.WM_HOTKEY:
                if msg.wParam == 1:
                    print ('Hotkey triggered!')
                    self.copy()
                elif msg.wParam == 2:
                    self.val_1()
                elif msg.wParam == 3:
                    self.val_2()
                elif msg.wParam == 4:
                    self.val_3()
                elif msg.wParam == 5:
                    self.val_4()
                elif msg.wParam == 6:
                    self.val_5()


            windll.user32.TranslateMessage(byref(msg))
            windll.user32.DispatchMessageA(byref(msg))
            
    #funcion bucle que captura continuamente para ver si se pulsa la combinación
    def loop_clipboard (self):

        while True:
            
            self.register_hotkey('Ctrl-0', 1 )
            self.register_hotkey('Ctrl-1', 2 )
            self.register_hotkey('Ctrl-2', 3 )
            self.register_hotkey('Ctrl-3', 4 )
            self.register_hotkey('Ctrl-4', 5 )
            self.register_hotkey('Ctrl-5', 6 )
            self.handle_hotkey()
        
   
    
   