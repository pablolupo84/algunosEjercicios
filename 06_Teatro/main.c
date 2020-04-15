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
#include <stdlib.h>

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
int menuPrincipal();
int obtenerButacasDisponibles(BUTACA localidades[][ASIENTOS]);
void visualizarTeatro(BUTACA localidades[][ASIENTOS]);
int reservaButaca(BUTACA localidades[][ASIENTOS]);
void imprimirArray(int array[],int cantidad);
int arrayDispFila(int array[],BUTACA localidades[][ASIENTOS],int valueFila);
int pertenece(int array[],int valor,int cantidad);
int posicionDiccionario(int array[],int valor,int cantidad);
int arrayReservaFila(int array[],BUTACA localidades[][ASIENTOS],int valueFila);
int cancelacionReserva(BUTACA localidades[][ASIENTOS]);


int main(void)
{
	int opcion=0, cantCanceladas=0,cantReservas=0,finalizar=0;
	
	/*inicializo mis butacas a todos libres usando una funcion para rellenar los miembros que me interesan*/
	inicializoLocalidades(localidades);
	printf("Este es un programa para consultar disponibilidad y reservar butacas en un espectaculo de teatro\n");
		
	do
	{
		switch(opcion)
		{/*funcionalidad a ejecutar*/
			case 0:
				opcion=menuPrincipal();
				if(opcion==4)
					finalizar=-1;
				break;
			case 1: /*CONSULTAR ASIENTOS DISPONIBLES*/
				visualizarTeatro(localidades);
				opcion=0;
				break;
			case 2: /*RESERVAR ASIENTOS DISPONIBLES*/
				cantReservas+=reservaButaca(localidades);
				opcion=0;
				break;
			case 3: /*ANULAR ASIENTOS OCUPADOS*/
				cantCanceladas+=cancelacionReserva(localidades);
				opcion=0;
				break;
			case 4: /*SALIR*/
				finalizar=-1;
				break;
		}
	}
	while(finalizar==0);
	printf("Se ha finalizado\n");
	system ("PAUSE");
    getchar();
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
			localidades[i][j].ubicacion=numeracion[j];
			strcpy(localidades[i][j].nombre,"");
		}
	}
}


/*
Funcion: menuPrincipal
Descripcion: Funcion para sacar por pantalla las opciones de menu y recoger la opcion seleccionada por el usuario
*/

int menuPrincipal()
{	int opc=0;
	//while(opc!=4)
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
Funcion: reservaButaca
Descripcion: Funcion para hacer reserva con seguridad para que no se pueda hacer sobre butacas ya ocupados o posiciones incorrectas
*/

int reservaButaca(BUTACA localidades[][ASIENTOS])
{
	int i, j, k= 0,asientoReservar,posicionPertenece=-1;
	int disponibles[ASIENTOS],validarIngreso=0;
	char letraFila;
	
	do{
		printf("Has seleccionado reservar una butaca libre\n");
		while(validarIngreso==0){
			printf("Introduce la letra de la fila en la que te quieres sentar.\n");
			fflush(stdin);
			letraFila=getchar();
			if(letraFila>=65 && letraFila<=65+ ASIENTOS){
				validarIngreso=-1;
			}
		}
		i=letraFila-65;
		k=arrayDispFila(disponibles,localidades,i);
		if(k>0){
			printf("Las butacas disponibles en esa fila son:\n");
			imprimirArray(disponibles,k);
			printf("\nIntroduce la butaca que te gustaria reservar introduciendo el numero correspondiente de las [%d] disponibles.\n",k);
			fflush(stdin);
			scanf("%d", &asientoReservar);
			posicionPertenece=pertenece(disponibles,asientoReservar,k);
			if(posicionPertenece!=-1){
				printf("Quieres reservar la butaca %c%d en la fila %d.\n",letraFila,asientoReservar,i+1);
				printf("Introduce tu nombre\n");
				fflush(stdin);
				scanf("%s", &localidades[i][posicionPertenece].nombre);
				localidades[i][posicionPertenece].disponibilidad='R';
				printf("Has reservado esa butaca correctamente\n");
				printf("Quieres seguir reservando? [S/N] ");
				fflush(stdin);
			}
		}
	}while('S' == getchar());
	return k;
}

/*
Funcion: cancelacionReserva
Descripcion: Funcion para cancelar una reserva previamente hecha
*/

int cancelacionReserva(BUTACA localidades[][ASIENTOS])
{
	int i, j, k= 0,asientoCancelar,posicionPertenece=-1;
	int reservados[ASIENTOS],validarIngreso=0;
	char letra_asiento = 0;	
	printf("\nHas seleccionado cancelar una reserva ya existente.\n");
	do{
		while(validarIngreso==0){
			printf("Introduce la letra de la fila en la que tienes reserva.\n");
			fflush(stdin);
			letra_asiento=getchar();
			if(letra_asiento>=65 && letra_asiento<=65+ ASIENTOS){
				validarIngreso=-1;
			}
		}
		i=letra_asiento-65;
		k=arrayReservaFila(reservados,localidades,i);
		if(k>0){
			printf("Las butacas ya reservadas en esa fila son: :\n");
			imprimirArray(reservados,k);
			printf("\nntroduce la butaca que te gustaria anular introduciendo el numero correspondiente de las [%d] disponibles\n",k);
			fflush(stdin);
			scanf("%d", &asientoCancelar);
			posicionPertenece=pertenece(reservados,asientoCancelar,k);
			if(posicionPertenece!=-1){
				printf("Anulada la reserva de la butaca %c%d en la fila %d.\n",letra_asiento,asientoCancelar,i+1);
				printf("Has liberado esa butaca correctamente.\n");
				localidades[i][posicionPertenece].disponibilidad='D';
				strcpy(localidades[i][posicionPertenece].nombre,"");
				printf("Quieres seguir Anulando Reservas? [S/N] ");
				fflush(stdin);
			}
		}else{
			printf("No hay butacas disponibles\n");
		}
	}while('S' == getchar());
	return k;
}


/*
Funcion: imprimirArray
Descripcion: Funcion para mostrar por pantalla un array de enteros.
conociendo su cantidad de valores.
*/
void imprimirArray(int array[],int cantidad){
	int i;
	for(i=0;i<cantidad;i++){
		printf(" %d",array[i]);
	}
}

int arrayDispFila(int array[],BUTACA localidades[][ASIENTOS],int valueFila){
	int j,k=0;
	for(j=0;j<ASIENTOS;j++){
		if(localidades[valueFila][j].disponibilidad=='D'){
			array[k]=localidades[valueFila][j].ubicacion;
			k++;
		}
	}
	return k;
}

int pertenece(int array[],int valor,int cantidad){
	int i,posicion=-1;
	for(i=0;i<cantidad;i++){
		if(valor==array[i]){
			posicion=posicionDiccionario(numeracion,valor,ASIENTOS);
			//printf("Encontrado en Posicion i: %d",i);
			break;
		}
	}
	return posicion;
}

int posicionDiccionario(int array[],int valor,int cantidad){
	int i,posicion=-1;
	for(i=0;i<cantidad;i++){
		if(valor==array[i]){
			posicion=i;
			break;
		}
	}
	return posicion;	
}

int arrayReservaFila(int array[],BUTACA localidades[][ASIENTOS],int valueFila){
	int j,k=0;
	for(j=0;j<ASIENTOS;j++){
		if(localidades[valueFila][j].disponibilidad=='R'){
			array[k]=localidades[valueFila][j].ubicacion;
			k++;
		}
	}
	return k;
}