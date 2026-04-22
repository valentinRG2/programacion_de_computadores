package menuNumeros;
import java.util.Scanner;
public class menums {

	public static void main(String[] args) {
		int op = mostrarMenu();
		System.out.println(op);
	while (op!=4) {
		if (op==1) {
			mostrarNumeros();
		}else if(op==2) {
			sumarNumeros();
		}else if(op==3) {
			validarPassword();
		}
		op=mostrarMenu();
		
	}
		

	}
	public static int mostrarMenu() {
		Scanner sc = new Scanner(System.in);
		int op=0;
		
		System.out.println("===== MENÚ =====");
		System.out.println("1.mostar menu \n2.sumar numeros \n3.validar contraseña \n4.salir");
		System.out.println("elija una opcion: ");
		op= sc.nextInt();
		System.out.println("================");
		
		return op;
		
	}
	public static void mostrarNumeros() {
		Scanner sc = new Scanner(System.in);

		System.out.println("ingrese su numero: ");
		int num = sc.nextInt();
		for (int i=1;i<=num;i++) {
			System.out.println(i);
		}
		
	}
	public static void sumarNumeros() {
		Scanner sc = new Scanner(System.in);
		int resultado=0;
		int num=0;
		int bucle=1;
		while (bucle!=0) {
			System.out.println("ingrese el numero a sumar: ");
			num=sc.nextInt();
			if (num==0) {
				bucle=0;
			}else {
				resultado+=num;
			}
		}System.out.println("el resultado de su suma es: "+resultado);
		
		
	}
	public static void validarPassword() {
		Scanner sc = new Scanner(System.in);
		String contraseña="";
		String verificacion="";
		System.out.println("ingrese su contraseña: ");
		contraseña=sc.nextLine();
		do {
			System.out.println("verifique su contraseña: ");
			verificacion=sc.nextLine();
		}while (!contraseña.equals(verificacion));
		if (contraseña.equals(verificacion)) {
			System.out.println("acceso concedido...");
		}
	}
	

}









