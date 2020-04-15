/******************************************************************************************************************************************************
Programa: PROPUESTA PRACTICA 2

Descripcion: Se solicita diseñar y codificar un programa que simule una herramienta de gestión informatizada de taquilla de un teatro. 
Mediante un menú se podrá reservar (2), cancelar las reservas (3) de butacas de un teatro, así como mostrar qué butacas están ocupados y libres actualmente (1).
El teatro dispone de una planta donde se disponen de 8 filas, con 12 butacas cada una, haciendo un total de 96 localidades disponibles.

Se puede asimilar a una matriz 2-dimensional, en la cual cada posición será una estructura de nombre "butaca", donde se deberá incluir la siguiente información:
"	disponibilidad;    Si esta libre pondré 'D' / si está reservado 'R'
"	ubicacion;         numero par o impar que se corresponde con la localidad (ver mapa enunciado)
"	nombre [80];      nombre completo de la persona que la ha reservado
Si está disponible el campos de nombre no se tendrá en cuenta

Autor: AAAAAA BBBBBBB CCCCCCCC
DNI: XXXXXXXXA
******************************************************************************************************************************************************/
/*Declaracion de librerias y dependencias*/
#include <stdio.h>
#include <string.h>

#define DISPONIBLE	'D'
#define RESERVADO	'R'
...

/*Declaracion de estructuras*/
typedef struct butaca { ... } BUTACA; //completar definición de la estructura

/*Declaracion de variables globales*/
BUTACA localidades[FILAS][ASIENTOS];

/*Declaracion de funciones*/
... inicializoLocalidades(...);
... menuPrincipal(...);
... visualizarTeatro(...);
... reservaButaca(...);
... cancelacionReserva(...);

int main(void)
{
	int opcion, finalizar=0;
	
	/*inicializo mis butacas a todos libres usando una funcion para rellenar los miembros que me interesan*/
	...
	printf("Este es un programa para consultar disponibilidad y reservar butacas en un espectaculo de teatro\n");
		
	do
	{
		switch(...)
		{/*funcionalidad a ejecutar*/
			case 0:
				... menuPrincipal ...
				break;
			case 1: /*CONSULTAR ASIENTOS DISPONIBLES*/
				... visualizarTeatro ... 
				break;
			case 2: /*RESERVAR ASIENTOS DISPONIBLES*/
				... reservaButaca ... 
				break;
			case 3: /*ANULAR ASIENTOS OCUPADOS*/
				... cancelacionReserva ... 
				break;
			case 4: /*SALIR*/
				...
			default:
				...
		}
	}
	while(...);

/*	system ("PAUSE");*/
    getchar();
	return 0;
}

/*
Funcion: inicializoLocalidades
Descripcion: Funcion para cargar los valores inciales de la estructura butaca
*/

... inicializoLocalidades(...)
{
	int i, j;
	for(...)
	{
		for(...)
		{
		...
		}
	}
}

/*
Funcion: menuPrincipal
Descripcion: Funcion para sacar por pantalla las opciones de menu y recoger la opcion seleccionada por el usuario
*/

... menuPrincipal(...)
{
	...
	{ //Bucle de menu
		...
		fflush(stdin);
		scanf("%d", &opc);
	}
	...
}


/*
Funcion: VisualizarTeatro
Descripcion: Funcion para sacar por pantalla la ocupacion del teatro
*/

... visualizarTeatro(...)
{
	int i=0;
	int j=0;
	
	printf("\nHas seleccionado consultar las butacas libres.\n\n");
	printf("Actualmente hay %d localidades disponibles para reservar\n", ...);
	...
	
	//pintaremos las plazas libres
	...
	return ...;
}


/*
Funcion: reservaButaca
Descripcion: Funcion para hacer reserva con seguridad para que no se pueda hacer sobre butacas ya ocupados o posiciones incorrectas
*/

... reservaButaca(...)
{
	int i, j, k= 0;
	int disponibles[ASIENTOS];
	
	...
	...
	...
	
	printf("Quieres seguir reservando? [S/N] ");
	fflush(stdin);
	if('S' == getchar()) return(...);
	else return(...);
}

/*
Funcion: cancelacionReserva
Descripcion: Funcion para cancelar una reserva previamente hecha

*/

... cancelacionReserva(...)
{
	...
	char letra_asiento = 0;
	...

	printf("\nHas seleccionado cancelar una reserva ya existente.\n");
		
	do
	{ /*control de filas*/
		printf("Introduce la letra de la fila en la que tienes reserva.\n");
		fflush(stdin);
		letra_asiento = getchar();	
	}
	while(...);
		
	...
	...
	...
}






