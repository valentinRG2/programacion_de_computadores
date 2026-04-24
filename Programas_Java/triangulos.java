package figuras;

public class triangulos {

	public static void main(String[] args) {
		triangulo1();
		System.out.println("-------------------");
		triangulo2();
		System.out.println("-------------------");
		triangulo3();
		System.out.println("-------------------");
		triangulo4();

	}
	public static void triangulo1() {
        int h = 5;

        for (int i = 1; i <= h; i++) {
            String espacio = " ".repeat(h - i);
            String estrellas = "*".repeat(2 * i - 1);
            System.out.println(espacio + estrellas);
        }
    }
	public static void triangulo2() {
		int h=5;
		for (int i=0;i<h;i++) {
			String espacio = " ".repeat(i);
			String estrellas = "*".repeat(2*(h-i)-1);
            System.out.println(espacio + estrellas);

		}
	}
	public static void triangulo3() {
		int h=5;
		for (int i=1;i<=h;i++) {
			String espacio=" ".repeat(h-i);
			String estrellas="*".repeat(i);
            System.out.println(espacio + estrellas);
		}
	}
	public static void triangulo4() {
		int h=5;
		for (int i=0;i<=h;i++) {
			String espacio=" ".repeat(i);
			String estrellas="*".repeat(h-i);
			System.out.println(espacio + estrellas);
		}
	}
	
}
