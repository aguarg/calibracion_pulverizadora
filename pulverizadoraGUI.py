from pulverizadora_ui import *
import formulasPulverizadora


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self) 
        
        self.boton_calcular.clicked.connect(self.calcular)
        
        # Para que las cajan acepten solo números.
        self.caja_caudal_campo.setValidator(QtGui.QIntValidator()) 
        self.caja_caudal_boquilla.setValidator(QtGui.QIntValidator())
        self.caja_velocidad_avance.setValidator(QtGui.QIntValidator())
        self.caja_ancho_labor_boquilla.setValidator(QtGui.QIntValidator())



        #  PARECE QUE AUTOMATICAMENTE CONVIERTE LOS NUMEROS A INTEGERES. ME LA QUIERO CORTAR CON UNA PLANCHA.
        # Probar de sacar TODO lo que mapea y convierte a int.

        


    
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

        
        
        # Esto usa map() para iterar por la lista valores y aplica la función convertir() a cada valor. Devuelve una nueva lista mapeados:
        mapeados = list(map(convertir, valores))


        

        # CÁLCULOS:
        # Cálculo del caudal de campo (Q), el primer elemento de la lista "mapeados":
        if mapeados[0] == "x":
            caudalCampo = formulasPulverizadora.Q(mapeados[1], mapeados[2], mapeados[3])
            
            self.resultados.setText("El caudal de campo es: " + str(caudalCampo) + " litros por hectárea")
        
        
        # Cálculo del caudal de boquilla (q), el segundo elemento de la lista "mapeados":    
        elif mapeados[1] == "x":
            caudalBoquilla = formulasPulverizadora.q(mapeados[0], mapeados[2], mapeados[3])

            self.resultados.setText("El caudal de boquilla es: " + str(caudalBoquilla) + " liros por minuto.")


        # Cálculo de la velocidad de avance (v), el tercer elemento de la lista "mapeados":    
        elif mapeados[2] == "x":
            velocidadAvance = formulasPulverizadora.v(mapeados[0], mapeados[1], mapeados[3])

            self.resultados.setText("La velocidad de avance es de: " + str(velocidadAvance) + " kilómetros por hora") 



        # Cálculo del ancho de boquilla (a), el cuarto elemento de la lista "mapeados":    
        elif mapeados[3] == "x":
            anchoBoquilla = formulasPulverizadora.a(mapeados[0], mapeados[1], mapeados[2])

            self.resultados.setText("El ancho de labor de cada boquilla es de: " + str(anchoBoquilla) + " metros")           

            

    


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