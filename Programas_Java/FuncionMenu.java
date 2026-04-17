package menu;

import java.util.Scanner;


public class FuncionMenu {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
				
		int opcion = mostrarMenu();
		System.out.println(opcion);
	}
	public static int mostrarMenu() {
		Scanner sc = new Scanner(System.in);
		int opcion = 0;
		
		System.out.println("===== MENÚ =====");
		System.out.println("1.ingresar datos \n2.mostrar datos \n3.salir");
		System.out.println("elija una opcion: ");
		opcion= sc.nextInt();
		System.out.println("--------------------");
		return opcion;
		
	}

}
