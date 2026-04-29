package arreglos;
import java.util.Scanner;

public class notas {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int estudiantes=5;
		int num;
		System.out.println("cuantas notas va a ingresar por estudiante?");
		num=sc.nextInt();

		double[][] notas= new double[estudiantes][num];
		for (int i=0;i<estudiantes;i++) {
			System.out.println("estudiante"+(i+1));
			for (int j=0;j<num;j++) {
				do {
					System.out.println("nota "+(j+1)+":");
					notas[i][j]=sc.nextDouble();
				}while (notas[i][j]<0 || notas[i][j]>5 );
			}
		}
		for (int i = 0; i < estudiantes; i++) {
            double suma = 0;
            double mayor = notas[i][0];
            double menor = notas[i][0];

            for (int j = 0; j < num; j++) {
                suma += notas[i][j];

                if (notas[i][j] > mayor) {
                    mayor = notas[i][j];
                }

                if (notas[i][j] < menor) {
                    menor = notas[i][j];
                }
            }

            double promedio = suma / num;

            System.out.println("\nResultados Estudiante " + (i + 1));
            System.out.println("Promedio: " + promedio);
            System.out.println("Mayor: " + mayor);
            System.out.println("Menor: " + menor);
		}
	}
}
