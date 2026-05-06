package mundial;

public class equipos {
	private String nombre;
	private String letras;
	private String grupo;

	public equipos(String nombre, String letras, String grupo, int nroPegatina) {
		super();
		this.nombre = nombre;
		this.letras = letras;
		this.grupo = grupo;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getLetras() {
		return letras;
	}

	public void setLetras(String letras) {
		this.letras = letras;
	}

	public String getGrupo() {
		return grupo;
	}

	public void setGrupo(String grupo) {
		this.grupo = grupo;
	}
}
