#!/usr/bin/env python

#Matriz de datos Definidas Globalmente -> TARIFAS METRO 
matrizTarifas=[[740,660,610],[210,210,210],[210,210,210]]

#Variables Globales
saldo=[25000,25000,25000]
viajesGratisBajo=[0,0,5]
saldoCargaSuperior=15000


def main():
	viajesGratisparaTodos=0
	contadorViajes=0
	retenido=False
	tipoUsuario=input("Ingrese tipo de Usuario (A,E o M): ")
	fila=-1
	columna=-1
	if(tipoUsuario =='A'):
		print("TIPO A")
		fila=0
		while(retenido !=True):
			horarioViaje = input("Ingrese Horario de Viaje (P,V o B): ")
			#retenido=True
			if(horarioViaje == 'P'):
				print("TIPO P")
				columna=0
				if(saldo[fila]>matrizTarifas[fila][columna]):
					saldo[fila]=saldo[fila]-matrizTarifas[fila][columna]
					print ("Boleto Comprado, Saldo Restante: ",saldo[fila])
				else:
					recargar=input("Saldo No disponible, Desea Recargar? (S,N): ")
					if (recargar == 'S'):
						value=int(input("Valor a cargar: "))
						saldo[fila]+=value
						if (value >=saldoCargaSuperior):
							print("Obtiene un viaje gratis en Horario Bajo")
							viajesGratisBajo[fila]+=1
					else:
						print("Saliendo.....Boleto Retenido")
						retenido=True
			elif(horarioViaje == 'V'):
				print("TIPO V")
				columna=1
				if(saldo[fila]>matrizTarifas[fila][columna]):
					saldo[fila]=saldo[fila]-matrizTarifas[fila][columna]
					print ("Boleto Comprado, Saldo Restante: ",saldo[fila])
				else:
					recargar=input("Saldo No disponible, Desea Recargar? (S,N): ")
					if (recargar == 'S'):
						value=int(input("Valor a cargar: "))
						saldo[fila]+=value
						if (value >=saldoCargaSuperior):
							print("Obtiene un viaje gratis en Horario Bajo")
							viajesGratisBajo[fila]+=1
					else:
						print("Saliendo.....Boleto Retenido")
						retenido=True
			elif(horarioViaje == 'B'):
				print("TIPO B")
				columna=2
				if(viajesGratisBajo[fila]>0):
					viajesGratisBajo[fila]-=1
					print("Utiliza viaje gratis, restan: ",viajesGratisBajo[fila])
				elif(saldo[fila]>matrizTarifas[fila][columna]):
					saldo[fila]=saldo[fila]-matrizTarifas[fila][columna]
					print ("Boleto Comprado, Saldo Restante: ",saldo[fila])
				else:
					recargar=input("Saldo No disponible, Desea Recargar? (S,N): ")
					if (recargar == 'S'):
						value=int(input("Valor a cargar: "))
						saldo[fila]+=value
						if (value >=saldoCargaSuperior):
							print("Obtiene un viaje gratis en Horario Bajo")
							viajesGratisBajo[fila]+=1
					else:
						print("Saliendo.....Boleto Retenido")
						retenido=True
			else:
				print("Horario Invalido")
	elif (tipoUsuario == 'E'):
		print("TIPO E")
		fila=1
		while(retenido !=True):
			horarioViaje = input("Ingrese Horario de Viaje (P,V o B): ")
			#retenido=True
			if(horarioViaje == 'P'):
				print("TIPO P")
				columna=0
				if(saldo[fila]>matrizTarifas[fila][columna]):
					saldo[fila]=saldo[fila]-matrizTarifas[fila][columna]
					print ("Boleto Comprado, Saldo Restante: ",saldo[fila])
				else:
					recargar=input("Saldo No disponible, Desea Recargar? (S,N): ")
					if (recargar == 'S'):
						value=int(input("Valor a cargar: "))
						saldo[fila]+=value
						if (value >=saldoCargaSuperior):
							print("Obtiene un viaje gratis en Horario Bajo")
							viajesGratisBajo[fila]+=1
					else:
						print("Saliendo.....Boleto Retenido")
						retenido=True
			elif(horarioViaje == 'V'):
				print("TIPO V")
				columna=1
				if(saldo[fila]>matrizTarifas[fila][columna]):
					saldo[fila]=saldo[fila]-matrizTarifas[fila][columna]
					print ("Boleto Comprado, Saldo Restante: ",saldo[fila])
				else:
					recargar=input("Saldo No disponible, Desea Recargar? (S,N): ")
					if (recargar == 'S'):
						value=int(input("Valor a cargar: "))
						saldo[fila]+=value
						if (value >=saldoCargaSuperior):
							print("Obtiene un viaje gratis en Horario Bajo")
							viajesGratisBajo[fila]+=1
					else:
						print("Saliendo.....Boleto Retenido")
						retenido=True
			elif(horarioViaje == 'B'):
				print("TIPO B")
				columna=2
				if(viajesGratisBajo[fila]>0):
					viajesGratisBajo[fila]-=1
					print("Utiliza viaje gratis, restan: ",viajesGratisBajo[fila])
				elif(saldo[fila]>matrizTarifas[fila][columna]):
					saldo[fila]=saldo[fila]-matrizTarifas[fila][columna]
					print ("Boleto Comprado, Saldo Restante: ",saldo[fila])
				else:
					recargar=input("Saldo No disponible, Desea Recargar? (S,N): ")
					if (recargar == 'S'):
						value=int(input("Valor a cargar: "))
						saldo[fila]+=value
						if (value >=saldoCargaSuperior):
							print("Obtiene un viaje gratis en Horario Bajo")
							viajesGratisBajo[fila]+=1
					else:
						print("Saliendo.....Boleto Retenido")
						retenido=True
			else:
				print("Horario Invalido")
	elif (tipoUsuario == 'M'):
		print("TIPO M")
		fila=2
		while(retenido !=True):
			horarioViaje = input("Ingrese Horario de Viaje (P,V o B): ")
			#retenido=True
			if(horarioViaje == 'P'):
				print("TIPO P")
				columna=0
				if(saldo[fila]>matrizTarifas[fila][columna]):
					saldo[fila]=saldo[fila]-matrizTarifas[fila][columna]
					print ("Boleto Comprado, Saldo Restante: ",saldo[fila])
				else:
					recargar=input("Saldo No disponible, Desea Recargar? (S,N): ")
					if (recargar == 'S'):
						value=int(input("Valor a cargar: "))
						saldo[fila]+=value
						if (value >=saldoCargaSuperior):
							print("Obtiene un viaje gratis en Horario Bajo")
							viajesGratisBajo[fila]+=1
					else:
						print("Saliendo.....Boleto Retenido")
						retenido=True
			elif(horarioViaje == 'V'):
				print("TIPO V")
				columna=1
				if(saldo[fila]>matrizTarifas[fila][columna]):
					saldo[fila]=saldo[fila]-matrizTarifas[fila][columna]
					print ("Boleto Comprado, Saldo Restante: ",saldo[fila])
				else:
					recargar=input("Saldo No disponible, Desea Recargar? (S,N): ")
					if (recargar == 'S'):
						value=int(input("Valor a cargar: "))
						saldo[fila]+=value
						if (value >=saldoCargaSuperior):
							print("Obtiene un viaje gratis en Horario Bajo")
							viajesGratisBajo[fila]+=1
					else:
						print("Saliendo.....Boleto Retenido")
						retenido=True
			elif(horarioViaje == 'B'):
				print("TIPO B")
				columna=2
				if(viajesGratisBajo[fila]>0):
					viajesGratisBajo[fila]-=1
					print("Utiliza viaje gratis, restan: ",viajesGratisBajo[fila])
				elif(saldo[fila]>matrizTarifas[fila][columna]):
					saldo[fila]=saldo[fila]-matrizTarifas[fila][columna]
					print ("Boleto Comprado, Saldo Restante: ",saldo[fila])
				else:
					recargar=input("Saldo No disponible, Desea Recargar? (S,N): ")
					if (recargar == 'S'):
						value=int(input("Valor a cargar: "))
						saldo[fila]+=value
						if (value >=saldoCargaSuperior):
							print("Obtiene un viaje gratis en Horario Bajo")
							viajesGratisBajo[fila]+=1
					else:
						print("Saliendo.....Boleto Retenido")
						retenido=True
			else:
				print("Horario Invalido")
	else:
		print("Usuario Invalido")




main()




