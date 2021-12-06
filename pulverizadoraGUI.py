from pulverizadora_ui import *
import formulasPulverizadora


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self) 
        
        self.boton_calcular.clicked.connect(self.calcular)


    
    def calcular(self):
        # Recibe los datos de las cajas y las agrega a la lista "valores":
        caudal_de_campo = self.caja_caudal_campo.text()
        valores.append(caudal_de_campo)
                
        caudal_de_boquilla = self.caja_caudal_boquilla.text()
        valores.append(caudal_de_boquilla)

        velocidad = self.caja_velocidad_avance.text()
        valores.append(velocidad)

        ancho_de_boquilla = self.caja_ancho_labor_boquilla.text()
        valores.append(ancho_de_boquilla)


        
        # esto usa map() para iterar por la lista valores y aplica la función convertir() a cada valor. Devuelve una nueva lista mapeados:
        mapeados = list(map(convertir, valores))

        print(mapeados)


# Función usada por el map(): si hay un "" mete una x, y si hay un número como string, lo pasa a integer:
def convertir(elemento):
    if elemento == "":
        return "x"
    else:
        return int(elemento)    







# Lista con los valores de las cajas        
valores = []
        

    # ERROR: ValueError: invalid literal for int() with base 10: ''
    # Esto pasa porque se quiere convertir a integer una cadena vacía. solo sucede si la caja está vacía.    

        
       #Imprime en la etiqueta:
        #self.resultados.setText() #recordar pasarlo int a string, porque el método setText() solo trabaja con strings.
    



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()