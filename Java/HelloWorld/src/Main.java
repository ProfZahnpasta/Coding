import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        morning_or_evening(3874);
    }

    public static void morning_or_evening(Integer age) {
        String name = "Jonas";
        Scanner scanner = new Scanner(System.in);
        System.out.print("Wie viel Uhr ist es? ");
        String strhour = scanner.nextLine();
        int inthour = Integer.parseInt(strhour);
        if (inthour < 12) {
            System.out.println("Guten Morgen allerseits");
        }
        else {
            if (inthour > 12) {
                System.out.println("Guten Abend meine Herr*innen");
            }
        }
        System.out.println("Moin, ich bin " + name + " und ich bin " + age + " Jahre alt.");
    }
}
