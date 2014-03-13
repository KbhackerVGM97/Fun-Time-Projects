import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Gui extends JFrame implements ActionListener {

    private Container pane;

    private class myKeyListener implements KeyListener {
	public void keyPressed(KeyEvent e){
	    
	}
	public void keyReleased(KeyEvent e){
	    
	}
	public void keyTyped(KeyEvent e){
	    
	}
    }
    public void actionPerformed(ActionEvent e){
	
    }
    public Gui(){
	setTitle("Awesome Title");
	setSize(700,500);
	setLocation(0,0);
	setDefaultCloseOperation(EXIT_ON_CLOSE);
	pane = this.getContentPane();
	pane.setLayout(new BorderLayout());
    }

    public static void main(String[] args){
	Gui g = new Gui();
	g.setVisible(true);
    }
    
}
