package taller_funciones;
import java.util.Scanner;
import java.util.Random;

public class funciones {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		edad();
		//-----------------------------------------------------
		suma();
		//-----------------------------------------------------
		numAleatorio();
		//-----------------------------------------------------
		contadorVocales();
		//-----------------------------------------------------
		boolean resultado=palindromo("oso");
		System.out.println(resultado);
		//-----------------------------------------------------
		calcularPotencia(2,3);
		//-----------------------------------------------------
		int[] lista= {1,2,3,3,4,2,2};
		calcularMedia(lista);
		String resu=invertirCadena("queso");
		System.out.println(resu);
		//-----------------------------------------------------
		int resul=mayorDeTres(15,8,13);
		System.out.println(resul);
		//-----------------------------------------------------
		double area = calcularArea(3, 6);
        System.out.println("Área: " + area);
		//-----------------------------------------------------
		boolean result = buscarPalabra("dijiste queso?", "queso");
        System.out.println(result);
		//-----------------------------------------------------
		double[] notas= {5,4.5,3,3.5,1};
		double resultad = promedio(notas);
		System.out.println("El promedio es: " + resultad);
		//-----------------------------------------------------
		 int[] list = {2, 3, 4, 4};
	        int numero = 4;
	        int[] re = multiplicarLista(list, numero);
	        for (int i = 0; i < re.length; i++) {
	            System.out.print(re[i] + " ");
	        }
	      //-----------------------------------------------------
	        lista =new int[] {2, 5, 1, 9, 3};
	        int mayor = mayorDeVarios(lista);
	        System.out.println("El mayor es: " + mayor);
	      //-----------------------------------------------------
	        int ocurrencias = contar_ocurrencias("hola hola mundo hola", "hola");
	        System.out.println("Aparece: " + ocurrencias + " veces");
	}
	public static void edad() {
		System.out.println("cual es tu edad: ");
		int e=sc.nextInt();
		System.out.println("Tu edad es: "+e+" años");
	}
	public static void suma() {
		System.out.println("ingrese el numero 1: ");
		int num1=sc.nextInt();
		System.out.println("ingrese el numero 2: ");
		int num2=sc.nextInt();
		System.out.println("la suma: "+num1+"+"+num2+"="+(num1+num2));
	}
	public static void numAleatorio() {
		Random rand = new Random();
		int numCorrecto = rand.nextInt(101)+1;
		int num=0;
		while(numCorrecto!=num) {
			System.out.println("ingrese un numero entre 1 y 100: ");
			num=sc.nextInt();
			if (num==numCorrecto) {
				System.out.println("¡Felicitaciones, adivinaste el número!");
			}else if(num<numCorrecto) {
				System.out.println("el numero es mas alto");
			}else {
				System.out.println("el numero es mas bajo");
			}	
		}
	}
	public static void contadorVocales() {
		System.out.println("ingrese su palabra/oracion: ");
		String cadena=sc.nextLine();
		cadena=cadena.toLowerCase();
		int contador=0;
		for (int i=0;i<cadena.length();i++) {
			char letra=cadena.charAt(i);
			if (letra=='a' || letra=='e'|| letra=='i' || letra=='o' || letra=='u') {
				contador++;
			}
		}
		System.out.println("cantidad de vocales: "+contador);
	}
	public static boolean palindromo(String palabra) {
		palabra=palabra.toLowerCase();
		int inicio=0;
		int fin=palabra.length()-1;
		while(inicio<fin) {
			if (palabra.charAt(inicio)!=palabra.charAt(fin)){
				return false;
			}
			inicio++;
			fin--;
		}
		return true;
	}
	public static void calcularPotencia(int base,int exponente) {
		int resultado=1;
		for (int i=0;i<exponente;i++) {
			resultado*=base;
		}
		System.out.println("Resultado: " + resultado);
	}
	public static void calcularMedia(int[] lista) {
		int suma=0;
		for (int i=0;i<lista.length;i++) {
			suma+=lista[i];
		}
		double media=(double) suma/lista.length;
		System.out.println("la media es: "+media);
	}
	public static String invertirCadena(String cadena) {
		String invertida="";
		for(int i=cadena.length()-1;i>=0;i--) {
			invertida+=cadena.charAt(i);
		}return invertida;
	}
	public static int mayorDeTres(int num1,int num2,int num3) {
		int mayor=0;
		if(num1>num2) {
			mayor=num1;
		}else {
			mayor=num2;
		}if(mayor<num3) {
			mayor=num3;
		}
		return mayor;
	}
	public static double calcularArea(double radio,double altura) {
		double area=2*Math.PI*radio*altura+2*Math.PI*radio*radio;
		return area;
	}
	public static Boolean buscarPalabra(String cadena,String palabra) {
		return cadena.contains(palabra);
	}
	public static double promedio(double[]notas) {
	double suma=0;
		for (int i=0;i<notas.length;i++) {
			suma+=notas[i];
		}
		double promedio=(double) suma/notas.length;
		return promedio;
	}
	public static int[] multiplicarLista(int[]lista,int num) {
		int[]nuevaLista=new int[lista.length];
		for(int i=0;i<lista.length;i++) {
			nuevaLista[i]=lista[i]*num;
		}return nuevaLista;	
	}
	public static int mayorDeVarios(int[]lista) {
		int mayor=lista[0];
		for(int i=0;i<lista.length;i++) {
			if(lista[i]>mayor) {
				mayor=lista[i];
			}
		}return mayor;
	}
	public static int contar_ocurrencias(String cadena, String palabra) {
        int contador = 0;
        int indice = 0;
        cadena = cadena.toLowerCase();
        palabra = palabra.toLowerCase();
        while ((indice = cadena.indexOf(palabra, indice)) != -1) {
            contador++;
            indice += palabra.length(); 
        }
        return contador;
    }
}
























