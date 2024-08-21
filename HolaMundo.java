//import java.util.Scanner;
import javax.swing.JOptionPane;
public class HolaMundo{
    public static void main (String []args){
        //Scanner entrada = new Scanner(System.in);
        String nombre = "", apellido = "";
        nombre = JOptionPane.showInputDialog("Ingrese e; nombre");
        JOptionPane.showMessageDialog(null, "Tu nombre es " + nombre);
    }

}