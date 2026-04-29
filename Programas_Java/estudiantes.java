package arreglos;

import java.util.Scanner;

public class estudiantes {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int num;
		System.out.println("cuantas notas va a ingresar??????");
		num=sc.nextInt();

		double[] notas= new double[num];
		for(int i=0;i<num;i++) {
			do {
				System.out.println("nota: "+(i+1)+ ":");
				notas[i]=sc.nextDouble();
			}while (notas[i]<0 || notas[i]>5);
		}
		double suma=0;
		double mayor=notas[0];
		double menor=notas[0];
		for (int i = 0; i < num; i++) {
			suma += notas[i];

			if (notas[i] > mayor) {
				mayor = notas[i];
			}

			if (notas[i] < menor) {
				menor = notas[i];
			}
		}

		double promedio = suma / num;

		// Resultados
		System.out.println("Promedio: " + promedio);
		System.out.println("Mayor: " + mayor);
		System.out.println("Menor: " + menor);

	}

}
