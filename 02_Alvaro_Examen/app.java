package examen;


import java.text.DecimalFormat;

public class app {
	
	public static void main(String[] args) {
		int matriz[][] = new int[10][16];
		InicializarRandom(matriz);
		mostrarMatriz(matriz);
		ContagiosxDia(matriz);
		ContagiosxDiaPais(matriz);
		int a=regionConMasContagios(matriz);
		System.out.println("Region con mas contagios:\n" + a);
		
		for(int i=0;i<10;i++){
			System.out.println(regionConMayorTasaContagios(i,matriz));
		}
		System.out.println("diaConMayorTasaContagios:\n" + diaConMayorTasaContagios(matriz));
	}
	
	public static void InicializarRandom(int matriz[][]){
	for (int x=0; x < matriz.length; x++) {
		  for (int y=0; y < matriz[x].length; y++) {
		    matriz[x][y] = (int) (Math.random()*2500+1);
		  }
		}
	}
	
	public static void mostrarMatriz(int matriz[][]){
		for (int x=0; x < matriz.length; x++) {
			  for (int y=0; y < matriz[x].length; y++) {
				  System.out.println(matriz[x][y]);
			  }
			  System.out.println("\n");
			}
	}
	
	public static double sumaColumnas(int matriz[][], int numColumna) {
		DecimalFormat df = new DecimalFormat();
		double suma = 0;
		try {
			for (int i = 0; i < matriz.length; i++) {
				suma += matriz[i][numColumna];
			}
		return suma;
		} catch (Exception e) {
			return suma;
		}
	}
	
	public static double sumaFila(int matriz[][],int numFila){
		DecimalFormat df = new DecimalFormat();
		double suma = 0;
		try {
			for (int i = 0; i < matriz[0].length; i++) {
				suma += matriz[numFila][i];
			}
			return suma;
		} catch (Exception e) {
			return suma;
		}
	}
	
	public static void ContagiosxDia(int matriz[][]){
		/*
		int i,j;
		int suma[] = new int[10];
		for(int x=0;x<10;x++){
			suma[x]=0;
		}
		
		for (i = 0; i < matriz.length; i++) {
			for (j = 0; j < matriz[i].length; j++) {
				suma[i]=suma[i]+ matriz[i][j];
			}
			System.out.println("Dia " + i + ":" + suma[i]);
		}
		*/
		System.out.println("contagios por dia:");
		for ( int i = 0; i < 10; i++)
			System.out.println("\tDia " + i + ":" + sumaFila(matriz, i));
	}
	
	public static void ContagiosxDiaPais(int matriz[][]){
		int i,j;
		int suma=0;
		
		
		for (i = 0; i < matriz.length; i++) {
			suma=0;
			for (j = 0; j < matriz[i].length; j++) {
				suma=suma+ matriz[i][j];
			}
			System.out.println("Pais: " + suma);
		}	
	}
	
	public static int regionConMasContagios(int matriz[][]) {
		double totalRegiones[]=new double[16];
		int regionConMasContagios = 0;
		double totalContagiosRegionMax;

		//inicalizo array contagios por region
		for ( int i = 0; i < 16; i++) {
			totalRegiones[i] = sumaColumnas(matriz, i);
		}

		//asumo la region con mas contagios la 0
		totalContagiosRegionMax = totalRegiones[0];

		//busco region con mas contagios
		for ( int i = 1; i < 16; i++) {
		if ( totalContagiosRegionMax < totalRegiones[i] ) {
			regionConMasContagios = i;
			totalContagiosRegionMax = totalRegiones[i];
			}
		}

		return regionConMasContagios;
	}
	
	public static int regionConMayorTasaContagios(int diaActual,int matriz[][]) {
		int regionConMayorTasa = 0;
		int TasaContagiosRegionMax = 0;
		int totalDiarioAculado = 0;

		int totalTasaRegionesDiarios[][]=new int[10][16];
		//int totalRegionesTasaDia[MAX_REGIONES];

		for ( int dia = 0; dia < 10; dia++) {
			totalDiarioAculado += sumaFila(matriz, dia);
		for (int region = 0; region < 16; region++) {
			//tasa = diario region / total dia pais acumulado al dia
			totalTasaRegionesDiarios[dia][region] =  matriz[dia][region]/totalDiarioAculado;
			}
		}

		//asumo la region con mas contagios la 0
		TasaContagiosRegionMax = 0;

		//busco region con mas contagios
		for ( int region = 1; region < 16; region++) {
			if ( TasaContagiosRegionMax < totalTasaRegionesDiarios[diaActual][region] ) {
				regionConMayorTasa = region;
				TasaContagiosRegionMax = totalTasaRegionesDiarios[diaActual][region];
			}
		}
		return regionConMayorTasa;
		}
	
		public static int diaConMayorTasaContagios(int matriz[][]) {

		double totalTasaPaisDiario[] = new double[16];
		int totalDiarioAculado = 0;
		int diaConMayorTasa = 0;
		double TasaMax = 0;

		for ( int dia = 0; dia < 10; dia++) {
			totalDiarioAculado += sumaFila(matriz, dia);
			for (int region = 0; region < 169; region++) {
				//tasa = diario pais / total dia pais acumulado al dia
				totalTasaPaisDiario[dia] =  sumaFila(matriz, dia)/totalDiarioAculado;
			}
		}

		//busco region con mas contagios
		for ( int dia = 1; dia < 10; dia++) {
			if ( TasaMax < totalTasaPaisDiario[dia] ) {
				diaConMayorTasa = dia;
				TasaMax = totalTasaPaisDiario[dia];
			}
		}

		return diaConMayorTasa;
		} 
}
