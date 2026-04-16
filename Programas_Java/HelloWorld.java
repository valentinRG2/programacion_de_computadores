package pck;

public class HelloWorld {

	public static void main(String[] args) {
		//ejercicio de mayor o no de edad
		int edad = 18;
		
		if (edad>=18) {
			System.out.println("usted es mayor de edad");
		}else {
			System.out.println("usted es menor de edad");
		}
		//ejercicio de nums pos o nega
		int num= -22;
		if (num==0) {
			System.out.println("su numero es cero");
		}else if (num<0) {
			System.out.println("su numero es negativo");
		}else {
			System.out.println("su numero es positivo");
			
		}
		// num par o impar
		int nume = 0;
		
		if (nume==0) {
			System.out.println("su numero es 0");
	    }else if (nume%2 == 0) {
			System.out.println("el numero es par");
		}else {
			System.out.println("el numero es impar");
		}
		// mayor de 3 
		int a=2;
		int b=62;
		int c=44;
		int mayor=0;
		
		if (b>a) {
			mayor=b;
		}else {
			mayor=a;
		}if (c>mayor) {
			mayor=c;
		}System.out.println(mayor);
		//tabla del 5
		System.out.println("tabla de 5!");
		for (int i=0; i<11; i++) {
			System.out.println("5"+"*"+ i+"="+( i*5));
		}
		//suma del 1 al 10
		int suma=0;
		for(int e=1;e<11;e++) {
			suma=suma+e;
		}System.out.println(suma);
		
	}

}

















