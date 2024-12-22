package com.profzahnpasta;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("How many numbers of the fibonacci sequence do you want to display? ");
        String strinput = scanner.nextLine();
        Integer input = 0;
        try {
            input = Integer.parseInt(strinput);
        }
        catch(Exception error) {
            System.out.println("Type a valid number.");
            return;
        }
        fibonacci(input);
    }

    static void fibonacci(Integer times_of_displaying) {
        Integer first_number = 0;
        Integer sec_number = 1;
        System.out.println(first_number);
        System.out.println(sec_number);
        for (int i = 0; i < times_of_displaying - 2; i++) {
            Integer new_number = first_number + sec_number;
            if (new_number < first_number) {
                System.out.println("The number is higher than the Integer Limit. Sequence stopped.");
                break;
            }
            System.out.println(new_number);
            first_number = sec_number;
            sec_number = new_number;
            
        }
    }
}