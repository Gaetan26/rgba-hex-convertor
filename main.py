from widgets import Widgets
from os.path import exists
from json import load
import customtkinter as ctk
import convertions



if exists('config.json'):
    with open('config.json','rb+') as f:
        config = load(f); f.close()
else: raise FileNotFoundError()


    
class Main(ctk.CTk):
    
    ctk.set_appearance_mode(config["appearance_mode"])
    ctk.set_default_color_theme(config['default_color_theme'])

    def __init__(self):
        super().__init__()
        self.title(config['window_title'])
        self.iconbitmap(config['iconbitmap'])
        self.geometry(config['window_geometry'])
        self.resizable(width=False, height=False)                

        self.widgets = Widgets(self)
        self.widgets.render()

        def any_key_pressed(e):
            ksy = (e.keysym).lower()
            if ksy == 'delete':
                self.widgets.clear_all_fields()
            elif ksy == 'return':
                self.start_convert()
        
        self.bind('<Key>', any_key_pressed)


    def start_convert(self):
        r,g,b,a = self.widgets.R.get(), self.widgets.G.get(), self.widgets.B.get(), self.widgets.A.get()
        hex_ = self.widgets.HEX.get()

        if len(r) > 0 and len(g) > 0 and len(b) > 0 and len(hex_) == 0:
            r,g,b = int(r), int(g), int(b)
            if len(a) > 0: a = int(a)
            else: a = 255
            hex__ = convertions.switch_to_hex((r,g,b,a))
            self.widgets.clear_all_fields()
            self.widgets.HEX.insert(0, hex__)
        elif len(r) == 0 and len(g) == 0 and len(b) == 0 and len(hex_) > 0:
            r,g,b,a = convertions.switch_to_rgba(hex_)
            self.widgets.clear_all_fields()
            self.widgets.R.insert(0, r); self.widgets.G.insert(0, g)
            self.widgets.B.insert(0, b); self.widgets.A.insert(0, a)
        else:
            self.widgets.clear_all_fields()



if __name__ == '__main__':
    app = Main()
    app.mainloop()