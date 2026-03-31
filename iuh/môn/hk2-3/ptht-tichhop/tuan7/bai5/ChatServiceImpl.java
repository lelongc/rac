package bai5;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class ChatServiceImpl extends UnicastRemoteObject implements ChatService {

    protected ChatServiceImpl() throws RemoteException {
        super();
    }

    @Override
    public String sendMessage(String message) throws RemoteException {
        System.out.println("Client: " + message);

        String msg = message == null ? "" : message.trim().toLowerCase();

        if (msg.equals("hello") || msg.equals("hi")) {
            return "Server: Xin chao ban!";
        } else if (msg.equals("bye")) {
            return "Server: Tam biet!";
        } else if (msg.isEmpty()) {
            return "Server: Ban chua nhap gi.";
        } else {
            return "Server: Da nhan -> " + message;
        }
    }
}