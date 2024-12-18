package com.profzahnpasta;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;

public class Main {

    public static void main(String[] args) {
        openUI();
       /*  Scanner scanner = new Scanner(System.in);
        Integer number = ThreadLocalRandom.current().nextInt(0, 101);
        boolean guessedCorrectly = false;
        Integer attempts = 0;
        while (!guessedCorrectly) {
            System.out.print("Whats your guess? ");
            String strnumber = scanner.nextLine();
            attempts++;
            int usernumber = Integer.parseInt(strnumber);
            guessedCorrectly = guess(number, usernumber, attempts);
        }
        scanner.close(); */
    }

    public static void openUI() {
        JFrame frame = new JFrame("Guess the number!");
        frame.setSize(300,400);
        frame.setLocation(100,150);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setDefaultLookAndFeelDecorated(true);
        frame.setVisible(true);

        JLabel text = new JLabel("Guess a number:");
        text.setBounds(50,25,200,30);
        text.setHorizontalAlignment(JLabel.CENTER);
        frame.add(text);

        JTextField textField = new JTextField();
        textField.setBounds(50,100,200,30);
        frame.setLayout(null);
        frame.add(textField);

        JButton button = new JButton("Guess!");
        button.setBounds(50, 150, 200,30);
        frame.add(button);

        
    }

    public static boolean guess(Integer number, int usernumber, Integer attempts) {
        if (number.equals(usernumber)) {
            System.out.println("You have guessed correctly! Your attempts: " + attempts);
            return true;
        } else {
            System.out.println("That's sadly wrong :(");

            if (number > usernumber) {
                System.out.println("The number is too small!");
            } else {
                System.out.println("The number is too high!");
            }
            return false;
        }
    }
}
