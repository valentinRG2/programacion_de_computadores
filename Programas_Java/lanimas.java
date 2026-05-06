package mundial;

public class lanimas {
	public class laminas{
		int numero;
		String jugador;
		double estatura;
		int peso;
		String posicion;
		String fecha;
		int cantidad;
		public laminas(int numero, String jugador, double estatura, int peso, String posicion, String fecha) {
			super();
			this.numero = numero;
			this.jugador = jugador;
			this.estatura = estatura;
			this.peso = peso;
			this.posicion = posicion;
			this.fecha = fecha;
			this.cantidad=0;
		}
		public int getNumero() {
			return numero;
		}
		public void setNumero(int numero) {
			this.numero = numero;
		}
		public String getJugador() {
			return jugador;
		}
		public void setJugador(String jugador) {
			this.jugador = jugador;
		}
		public double getEstatura() {
			return estatura;
		}
		public void setEstatura(double estatura) {
			this.estatura = estatura;
		}
		public int getPeso() {
			return peso;
		}
		public void setPeso(int peso) {
			this.peso = peso;
		}
		public String getPosicion() {
			return posicion;
		}
		public void setPosicion(String posicion) {
			this.posicion = posicion;
		}
		public String getFecha() {
			return fecha;
		}
		public void setFecha(String fecha) {
			this.fecha = fecha;
		}
		public void repetidas(int cantidad) { 
			if (cantidad == 1) {
				System.out.println("No está repetida");
			} 
			else if (cantidad > 1) { 
				System.out.println("La lámina está repetida " + cantidad + " veces");
			}
		}
	}
}
