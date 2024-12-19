package com.profzahnpasta;
import java.awt.Font;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.concurrent.ThreadLocalRandom;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;

public class Main {

    static JLabel text = new JLabel("Guess a number:", JLabel.CENTER);
    static Integer number = ThreadLocalRandom.current().nextInt(0, 101);
    static Integer attempts = 0;

    public static void main(String[] args) {
        openUI();
    }

    public static void openUI() {
        JFrame frame = new JFrame("Guess the number! - Try guessing a random number between 1 and 100!");
        frame.setSize(600, 400);
        frame.setLocation(100, 150);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setDefaultLookAndFeelDecorated(true);
        
        frame.setLayout(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.fill = GridBagConstraints.HORIZONTAL;
        
        text.setFont(new Font("Tahoma", Font.PLAIN, 20));
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.gridwidth = 2;
        gbc.insets = new java.awt.Insets(10, 0, 20, 0);
        frame.add(text, gbc);
        
        final JTextField textField = new JTextField();
        gbc.gridx = 0;
        gbc.gridy = 1;
        gbc.gridwidth = 2;
        gbc.insets = new java.awt.Insets(0, 50, 20, 50);
        gbc.ipady = 10;
        frame.add(textField, gbc);
        
        JButton button = new JButton("Guess!");
        gbc.gridx = 0;
        gbc.gridy = 2;
        gbc.gridwidth = 2;
        gbc.insets = new java.awt.Insets(10, 50, 10, 50);
        gbc.ipady = 10;
        frame.add(button, gbc);

        frame.setVisible(true);

        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    String textFromTextField = textField.getText();
                Integer usernumber = Integer.parseInt(textFromTextField);
                attempts++;
                guess(number, usernumber, attempts);
                textField.setText("");
                } catch (Exception error) {
                    text.setText("You are such a Witzbold.");
                }
                
            }
        });
    }

    public static boolean guess(Integer number, int usernumber, Integer attempts) {
        if (number.equals(usernumber)) {
            text.setText("You have guessed correctly! Your attempts: " + attempts);
            return true;
        } else {
            text.setText("That's sadly wrong :(");

            if (number > usernumber) {
                text.setText("The number is too small!");
            } else {
                text.setText("The number is too high!");
            }
            return false;
        }
    }
}
