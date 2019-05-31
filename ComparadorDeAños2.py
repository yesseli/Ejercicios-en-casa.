from tkinter import ttk
from tkinter import *

class Desk:
    def __init__(self, window):
        # Initializations
        
        #ancho
        ancho = 500
        
        #alto
        alto = 300
        
        # asignamos la ventana a una variable de la clase llamada wind
        self.wind = window

        #le asignamos el ancho y el alto a la ventana con la propiedad geometry
        self.wind.geometry(str(ancho)+'x'+str(alto))

        #centramos el contenido 
        self.wind.columnconfigure(0, weight=1)
        
        #le damos un titulo a la ventana
        self.wind.title('Aplicación con interface gráfica Angel Vargas')
        
        # creamos un contenedor
        frame = LabelFrame(self.wind, text = 'Comparar de años')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 80)
        
        # creamos un etiqueta
        Label(frame, text = 'año actual: ').grid(row = 1, column = 0)
        
        #creamos un input donde ingresar valores
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 1, column = 1)
        
        # igual que arriba una etiqueta y un campo input para ingresar valores
        Label(frame, text = 'otro año: ').grid(row = 2, column = 0)
        
        #creamos un input donde ingresar valores
        self.var2 = Entry(frame)
        self.var2.focus()
        self.var2.grid(row = 2, column = 1)
        
        #Creamos un boton para ejecutar las operaciones       
        Button (frame, text = 'Comparar si es menor', command = self.dividir).grid(row = 6, columnspan = 5, sticky = W + E)
        
        #designamos un área para mensajes
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)
        
    # creamos una función para validar que los campos no esten en blanco
    
   
    # esta es la función que ejecuta la división
   
    def dividir(self):
            
           
            
            x=float(self.var1.get())
            y=float(self.var2.get())
               
            if  x>y:
                 resultado=float(x)-float(y)
                 r1=resultado
                 if r1 !=1:
                     self.message['text'] = 'ya pasaron {} años '.format(resultado)
                 if r1==1:
                     self.message['text'] = 'ya paso un año '
            elif y>x:
                    resultado=float(y)-float(x)
                    if resultado !=1:
                     self.message['text'] = 'faltan {} años '.format(resultado) 
                    else:
                     self.message['text'] = 'falta  un año'         
                
                   
                 
                    

                

           

    
    
    
#validamos si estamos en la aplicación inicial
if __name__ == '__main__':
    
    #asignamos la propiedad de tkinter a la variable window
    window = Tk()
    
    #en la variable app guardamos la clase Desk y le enviamos como parametro la ventana 
    app = Desk(window)

    #ejecutamos un mainloop para que se ejecute la ventana
    window.mainloop()
