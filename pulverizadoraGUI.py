from pulverizadora_ui import *
import formulasPulverizadora


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self) 
        
        

        self.boton_calcular.clicked.connect(self.calcular)



     # funcion de prueba para ver si se puede sacar el valor de una caja y meterlo en un objeto: FUNCIONA!
     # cambia el valor de cosito por ojete de mono y lo imprime en la consola
    def prueba(self):
        caudal_campo = int(self.caja_caudal_campo.text())
        variables["caudal_campo"] = "ojete de mono"        



    # Función para obtener los valores de las cajas:    
    def obtener_valores(self):    
        caudal_campo = int(self.caja_caudal_campo.text()) #lineEdit es el nombre que se le dio al diseñar la interfaz. Se puede cambiar.
        
        caudal_boquilla = int(self.caja_caudal_boquilla.text())

        velocidad_de_avance = int(self.caja_velocidad_avance.text())

        ancho_labor_boquilla = int(self.caja_ancho_labor_boquilla.text())   


    def calcular(self):
        self.prueba()
        
        print(variables["caudal_campo"])

        formulasPulverizadora.saludo(variables["Q"]) #otra prueba: usé una función del módulo con un valor del objeto de acá !!

        


        
        # Etiqueta que muestra el resultado final: exito! imprime lo del diccionario: "ojete de mono" en la etiqueta y en la consola.
        self.resultados.setText(variables["caudal_campo"]) #recordar pasarlo int a string, porque el método setText() solo trabaja con strings.
    




# Objeto con las variables:        
variables = {
    "Q": "esto vino del objeto en el archivo principal",
    "q": 0,
    "v": 0,
    "a": 0 
}



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()