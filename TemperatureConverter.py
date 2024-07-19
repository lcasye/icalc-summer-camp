from tkinter import *
from tkinter import ttk

class TemperatureConverter():
    def __init__(self):
        self.temperatures = ['Celsius','Fahrenheit','Kelvin']

    def convert(self, from_temp, to_temp, degree):

        if from_temp == 'Celsius':
            if to_temp == 'Fahrenheit':
                degree = degree * 9/5 + 32
            if to_temp == 'Kelvin':
                degree = degree + 273.15

        if from_temp == 'Fahrenheit':
            if to_temp == 'Celsius':
                degree = (degree - 32) * 5/9
            if to_temp == 'Kelvin':
                degree = (degree + 459.67) * 5/9

        if from_temp == 'Kelvin':
            if to_temp == 'Celsius':
                degree = degree - 273.15
            if to_temp == 'Fahrenheit':
                degree =  degree * 9/5 - 459.67

        degree = round(degree, 2)
        return degree

class App(Tk):
    def __init__(self, converter):
        Tk.__init__(self)
        self.my_converter = converter
        self.config(bg='lightblue')
        self.geometry('800x400')

        self.title = Label(self, text = 'Temperature Converter')
        self.title.config(font=('Courier',15,'bold'))
        self.title.place(x=300,y=5)

        self.entry_box = Entry(self, bd=3, justify = CENTER)
        self.entry_box.place(x=330,y=80)

        self.from_temperature_list = StringVar(self)
        self.from_temperature_list.set('Kelvin')
        self.to_temperature_list = StringVar(self)
        self.to_temperature_list.set('Celsius')
        font = ('Courier',12)
        self.option_add('*TCombobox*Listbox.font',font)
        self.from_temperature_dropdown = ttk.Combobox(self,textvariable=self.from_temperature_list,value=list(self.my_converter.temperatures))
        self.to_temperature_dropdown = ttk.Combobox(self,textvariable=self.to_temperature_list,value=list(self.my_converter.temperatures))
        self.from_temperature_dropdown.place(x=250,y=50)
        self.to_temperature_dropdown.place(x=400,y=50)

        self.result = Label(self,text='')
        self.result.config(font=('Arial',12,'bold'))
        self.result.place(x=380,y=200)

        self.convert_button = Button(self,text='Convert', bg='green', command=self.do_convert)
        self.convert_button.config(font=('Arial',10))
        self.convert_button.place(x=380,y=120)

    def do_convert(self):
        degree = float(self.entry_box.get())
        from_temp = self.from_temperature_dropdown.get()
        to_temp = self.to_temperature_dropdown.get()
        converted_degree = self.my_converter.convert(from_temp,to_temp,degree)
        self.result.config(text=str(converted_degree))

my_converter = TemperatureConverter()
App(my_converter)
mainloop()




