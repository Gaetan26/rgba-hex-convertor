import customtkinter as ctk



class Widgets():

    def __init__(self, parent):
        self.parent = parent

    def clear_all_fields(self):
        for f in [self.R, self.G, self.B, self.A, self.HEX]:
            f.delete(0, 'end')    

    def render(self):
        self.parent.columnconfigure([0,1,2,3], weight=1)
        self.parent.rowconfigure([1,2], weight=1)

        #
        text = "contribute to project!\nwww.github.com/Gaetan26/hexrgbconvert"
        ctk.CTkLabel(self.parent, text=text, font=('', 14)).grid(column=0, row=0, columnspan=4, sticky='nwe', padx=10, pady=(5, 5), ipady=10, ipadx=5)
        
        # rgba - fields
        self.R, self.G = ctk.CTkEntry(self.parent, placeholder_text="R"), ctk.CTkEntry(self.parent, placeholder_text="G")
        self.B, self.A = ctk.CTkEntry(self.parent, placeholder_text="B"), ctk.CTkEntry(self.parent, placeholder_text="A")
        i = 0
        for f in [self.R,self.G,self.B,self.A]:
            f.configure(font=('', 18))             
            f.grid(column=i,row=1, padx=10, pady=10, ipady=10, ipadx=5, sticky='nwe')
            i+=1
       
        self.R.grid_configure(padx=(30, 10))
        self.A.grid_configure(padx=(10, 30))

        # hex - field
        self.HEX = ctk.CTkEntry(self.parent, placeholder_text="HEX", font=('', 18))
        self.HEX.grid(column=0, row=2, columnspan=4, sticky='nwe', padx=20, pady=10, ipady=10, ipadx=5)

        #
        text = "press `enter`: convert RGBA color to HEX color\nor convert HEX color to RGBA color"
        ctk.CTkLabel(self.parent, text=text, font=('', 14)).grid(column=0, row=3, columnspan=4, sticky='nwe', padx=10, pady=(5,15), ipady=10, ipadx=5)