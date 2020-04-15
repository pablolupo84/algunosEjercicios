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
#define FILAS 8
#define ASIENTOS 12


/*Declaracion de estructuras*/
typedef struct butaca {
	char disponibilidad;
	int ubicacion;
	char nombre [80];
} BUTACA; //completar definición de la estructura

/*Declaracion de variables globales*/
BUTACA localidades[FILAS][ASIENTOS];
int numeracion[ASIENTOS]={1,3,5,7,9,11,12,10,8,6,4,2};

/*Declaracion de funciones*/
void inicializoLocalidades(BUTACA localidades[][ASIENTOS]);
void ImprimirvisualizarTeatro(BUTACA localidades[][ASIENTOS]);
int menuPrincipal();
int obtenerButacasDisponibles(BUTACA localidades[][ASIENTOS]);
void visualizarTeatro(BUTACA localidades[][ASIENTOS]);
int reservaButaca(BUTACA localidades[][ASIENTOS]);


int main(void)
{
	int opcion,cantidad,reservas;
	inicializoLocalidades(localidades);
	ImprimirvisualizarTeatro(localidades);
	cantidad=obtenerButacasDisponibles(localidades);
	printf("%d\n",cantidad);
	visualizarTeatro(localidades);
	reservas=reservaButaca(localidades);
	opcion=menuPrincipal();
	printf("%d\n",opcion);
	return 0;
}

/*
Funcion: inicializoLocalidades
Descripcion: Funcion para cargar los valores inciales de la estructura butaca
*/

void inicializoLocalidades(BUTACA localidades[][ASIENTOS])
{
	int i, j;
	for(i=0;i<FILAS;i++)
	{
		for(j=0;j<ASIENTOS;j++)
		{
			localidades[i][j].disponibilidad='D';
			localidades[i][j].ubicacion=numeracion[i];
			strcpy(localidades[i][j].nombre,"");
		}
	}
}


/*
Funcion: VisualizarTeatro
Descripcion: Funcion para sacar por pantalla la ocupacion del teatro
*/

void ImprimirvisualizarTeatro(BUTACA localidades[][ASIENTOS])
{
	int i,j;
	
	printf("\nHas seleccionado consultar las butacas libres.\n\n");
	//printf("Actualmente hay %d localidades disponibles para reservar\n", ...);
	printf("      ");
	for(i=0;i<ASIENTOS;i++){
		printf(" %d ",numeracion[i]);	
	}
	printf("\n");
	for(i=0;i<FILAS;i++)
	{
		printf("Fila %c:",i+65);
		for(j=0;j<ASIENTOS;j++){		
			printf(" %c ",localidades[i][j].disponibilidad);
		}
		printf("\n");
	}
}

/*
Funcion: VisualizarTeatro
Descripcion: Funcion para sacar por pantalla la ocupacion del teatro
*/

void visualizarTeatro(BUTACA localidades[][ASIENTOS])
{
	int i=0;
	int j=0;
	
	printf("\nHas seleccionado consultar las butacas libres.\n\n");
	printf("Actualmente hay %d localidades disponibles para reservar\n",obtenerButacasDisponibles(localidades));
	printf("A continuacion se presentara un esquema de las butacas libres.\n");
	printf("Leyenda [D]= disponible, [R]=Reservada\n\n");
	
	printf("      ");
	for(i=0;i<ASIENTOS;i++){
		printf(" %d ",numeracion[i]);	
	}
	printf("\n");
	for(i=0;i<FILAS;i++)
	{
		printf("Fila %c:",i+65);
		for(j=0;j<ASIENTOS;j++){		
			printf(" %c ",localidades[i][j].disponibilidad);
		}
		printf("\n");
	}
}


/*
Funcion: menuPrincipal
Descripcion: Funcion para sacar por pantalla las opciones de menu y recoger la opcion seleccionada por el usuario
*/

int menuPrincipal()
{	int opc=0;
	while(opc!=4)
	{ //Bucle de menu
		printf("\nSelecciona la opcion que deseas realizar:\n");
		printf("1. Consultar butacas disponibles\n");
		printf("2. Reservar una butaca\n");
		printf("3. Cancelar una reserva\n");
		printf("4. Salir\n");
		fflush(stdin);
		scanf("%d", &opc);
	}
	return opc;
}

/*
Funcion: obtenerButacasDisponibles
Descripcion: Funcion para obtener la cantidad de butacas disponibles.
*/
int obtenerButacasDisponibles(BUTACA localidades[][ASIENTOS])
{ 
	int i,j,cantidadDisponibles=0;
	for(i=0;i<FILAS;i++)
	{
		for(j=0;j<ASIENTOS;j++)
		{
			if(localidades[i][j].disponibilidad=='D')
				cantidadDisponibles+=1;
		}
	}
	return cantidadDisponibles;
}

/*
Funcion: reservaButaca
Descripcion: Funcion para hacer reserva con seguridad para que no se pueda hacer sobre butacas ya ocupados o posiciones incorrectas
*/

int reservaButaca(BUTACA localidades[][ASIENTOS])
{
	int i, j, k= 0;
	int disponibles[ASIENTOS];
	char letraFila;
	
	printf("Has seleccionado reservar una butaca libre\n");
	printf("Introduce la letra de la fila en la que te quieres sentar.\n");
	fflush(stdin);
	letraFila=getchar();
	if(letraFila>='A' || letraFila<='A'+ASIENTOS){
		k++;
		printf("entramooos\n");		
	}
	
	//printf("Quieres seguir reservando? [S/N] ");
	// fflush(stdin);
	// if('S' == getchar()) return(...);
	// else return(...);
	return k;
}
