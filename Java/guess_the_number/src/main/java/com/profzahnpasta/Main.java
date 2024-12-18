package com.profzahnpasta;
import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
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
        scanner.close();
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
