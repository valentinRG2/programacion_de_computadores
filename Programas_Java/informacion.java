package pck;



import java.util.Scanner;



public class informacion {



	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		// TODO Auto-generated method stub

		System.out.println("Nombre: Valentin Rincon Garzon\n"

				+ "Edad:18\n"

				+ "Programa:Ing.Sistemas");

		//print("Nombre: Valentin Rincon Garzon\nEdad:18\nPrograma:Ing.Sistemas")

		String nombre= "Valentin Rincon Garzon";

		int edad=18 ;

		String programa="Ing.Sistemas";

		System.out.println(nombre+"\n" +edad+ "\n"+ programa);

		//----------------------------------------------------------------------

		System.out.println("cual es tu nombre: ");

		nombre=sc.nextLine();

		System.out.println("cual es tu edad: ");

		edad=sc.nextInt();

		sc.nextLine();

		System.out.println("cual es tu carrera: ");

		programa=sc.nextLine();
		
		System.out.println("------------------------------------");
		System.out.println(nombre+"\n" +edad+ "\n"+ programa);

		//-------------------------------------------------

		int opcion =menu();

		System.out.println("opcion seleccionada"+opcion);

	}

	public static int menu() {

		Scanner sc = new Scanner(System.in);

		int seleccion=0;
		
		System.out.println("--------------------------------------");
		System.out.println("1.saludar");

		System.out.println("2.despedir");

		System.out.println("3.ignorar");

		System.out.println("seleccione una opcion: ");

		seleccion = sc.nextInt();
		
		if (seleccion == 1) {
		    System.out.println("Holaa ");
		} else if (seleccion == 2) {
		    System.out.println("Adios ");
		} else if (seleccion == 3) {
		    System.out.println("..."); // ignorar
		} else {
		    System.out.println("Opción inválida");
		}
		
		return seleccion;



	}



}