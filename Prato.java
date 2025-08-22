public class Prato {
    private String comida;
    private String tipo;
    public String valor;

    public Prato(String comida, String valor, String tipo) {
        this.comida = comida;
        this.tipo = tipo;
        this.valor = valor;
    }


    @Override
    public String toString() {
        return "Comida: " + comida +"\nTipo: " + tipo + "\nValor: R$" + valor;
    }

    public static void main(String[] args) {
        Prato prato = new Prato("Picanha", "220", "Prato Principal");
        System.out.println(prato); 
}
