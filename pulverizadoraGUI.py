from pulverizadora_ui import *
import formulasPulverizadora


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self) 
        
        self.boton_calcular.clicked.connect(self.calcular)

       
        
        # Para que las cajan acepten solo números y que tengan decimales.
        self.caja_caudal_campo.setValidator(QtGui.QDoubleValidator()) 
        self.caja_caudal_boquilla.setValidator(QtGui.QDoubleValidator())
        self.caja_velocidad_avance.setValidator(QtGui.QDoubleValidator())
        self.caja_ancho_labor_boquilla.setValidator(QtGui.QDoubleValidator())


                
        # Un agregado al botón borrar: vaciar la lista mapeados:
        self.boton_borrar.clicked.connect(self.vaciar_valores)
        # Al resto de las "vaciadas" las hice desde el QT Designer.
        
        
        # Para que los resultados de la etiqueta no se corten:
        self.resultados.setWordWrap(True)

    #Esta función borra los valores de la lista "valores". El vaciado de las cajas se hizo desde el Qt Designer:   
    def vaciar_valores(self):
        valores.clear()


    
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

        
        
        # Esto usa map() para iterar por la lista valores y aplica la función convertir() a cada valor. Devuelve una nueva lista mapeados
        #con int en lugar de strings, si no no se pueden usar los valores para los cálculos:
        mapeados = list(map(convertir, valores))

        # Llamada para limpiar la lista así puede aceptar los nuevos valores:
        self.vaciar_valores()


        

        # CÁLCULOS:
        # Cálculo del caudal de campo (Q), el primer elemento de la lista "mapeados":
        if mapeados[0] == "x":
            caudalCampo = formulasPulverizadora.Q(mapeados[1], mapeados[2], mapeados[3])
            
            self.resultados.setText("El caudal de campo es: " + str(round(caudalCampo, 2)) + " litros por hectárea")
        
        
        # Cálculo del caudal de boquilla (q), el segundo elemento de la lista "mapeados":    
        elif mapeados[1] == "x":
            caudalBoquilla = formulasPulverizadora.q(mapeados[0], mapeados[2], mapeados[3])

            self.resultados.setText("El caudal de boquilla es: " + str(round(caudalBoquilla, 2)) + " litros por minuto.")


        # Cálculo de la velocidad de avance (v), el tercer elemento de la lista "mapeados":    
        elif mapeados[2] == "x":
            velocidadAvance = formulasPulverizadora.v(mapeados[0], mapeados[1], mapeados[3])

            self.resultados.setText("La velocidad de avance es de: " + str(round(velocidadAvance, 2)) + " kilómetros por hora") 



        # Cálculo del ancho de boquilla (a), el cuarto elemento de la lista "mapeados":    
        elif mapeados[3] == "x":
            anchoBoquilla = formulasPulverizadora.a(mapeados[0], mapeados[1], mapeados[2])

            self.resultados.setText("El ancho de labor de cada boquilla es de: " + str(round(anchoBoquilla, 2)) + " metros")           

            

    


# Función usada por el map(): si hay un "" mete una x, y si hay un número como string, lo pasa a un número con decimales:
def convertir(elemento):
    if elemento == "":
        return "x"
    else:
        return float(elemento) 




# Lista que recibe los valores de las cajas al apretar el botón calcular:       
valores = []

        

     



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()