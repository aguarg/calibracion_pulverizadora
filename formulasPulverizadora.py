#ECUACIONES DE PULVERIZADORA

# 1- ECUACIÓN Q = (q*600) / (*a) 
# Q: Caudal de campo; 
# q: caudal de pico; 
# a: ancho de pico; 
# v: velocidad de avance.





# ====================== Ecuaciones ==========================

# 1- Ecuación Q = (q*600) / (*a):
# Q, el caudal de campo:
def Q(q, v, a):
	return (q * 600) / (v * a)



# q, el caudal de boquilla:
def q(Q, v, a):
	return (Q * v * a) / 600



# v, la velocidad de avance:
def v(Q, q, a):
	return (q * 600) / (Q * a)


# a, el ancho de labor de cada boquilla o del botalón entero:
def a(Q, q, v):
	return (q * 600) / (v * Q)	






valores = ["67", " ", "5", "2"]


# Función del map(): si hay un espacio, lo reemplaza por una "x", si no, cambia el string por un integer:
def convertir(elemento):
	if elemento == " ":
		return "x"
	else:
		return int(elemento)	


# esto usa map() para iterar por la lista y aplica la función convertir() a cada valor. Devuelve una nueva lista mapeados:
mapeados = list(map(convertir, valores))

print(mapeados)



