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

        # Imprime lo que sea en la etiqueta "resultados". Le metí la lista para ver si funcionaba nomás.
        #self.resultados.setText(str(mapeados))


        print(mapeados)



# Función usada por el map(): si hay un "" mete una x, y si hay un número como string, lo pasa a integer:
def convertir(elemento):
    if elemento == "":
        return "x"
    else:
        return int(elemento)    



# Lista que recibe los valores de las cajas al apretar el botón calcular:       
valores = []
        

     



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()