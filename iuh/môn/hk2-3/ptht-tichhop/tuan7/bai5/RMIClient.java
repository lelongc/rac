package bai5;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class RMIClient {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            ChatService service = (ChatService) registry.lookup("ChatService");

            System.out.println("Chat voi server (go 'exit' de thoat)");

            while (true) {
                System.out.print("Ban: ");
                String message = sc.nextLine();

                if ("exit".equalsIgnoreCase(message)) {
                    System.out.println("Thoat chat.");
                    break;
                }

                String reply = service.sendMessage(message);
                System.out.println(reply);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}