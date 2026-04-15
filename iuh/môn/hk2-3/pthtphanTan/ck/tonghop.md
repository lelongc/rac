[Giới thiệu về Java RMI(Remote Method Invocation)](https://viblo.asia/p/gioi-thieu-ve-java-rmiremote-method-invocation-XogBG2xrRxnL)

[Java RMI Phần 1 - Concept và exploit RMI Server](https://viblo.asia/p/java-rmi-phan-1-concept-va-exploit-rmi-server-obA46Mm0VKv)


**IAccount.java**

```Java
package com.rmi;

import java.rmi.Remote;
import java.rmi.RemoteException;

import com.bean.User;

/**
 * @author framgiavn
 */
public interface IAccount extends Remote {

    /**
     * @return
     * @throws RemoteException
     */
    public User getUser() throws RemoteException;
}
```


**AccountServiceImpl.java**

```Java
package com.sept.server.impl;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

import com.bean.User;
import com.rmi.IAccount;

/**
 *
 * @author framgiavn
 *
 */
public class AccountServiceImpl extends UnicastRemoteObject implements IAccount {
    private static final long serialVersionUID = 1L;

    public AccountServiceImpl() throws RemoteException {
    }

    public User getUser() {
        User u = new User();
        u.setId(23);
        u.setUname("framgia");
        u.setPasswd("222");
        return u;
    }
}

```

 **Xem thêm**

Cài đặt cho đối tượng trên Server: **RMIServer.java**

```Java
package com.sept.server.impl;

import java.net.MalformedURLException;
import java.rmi.AlreadyBoundException;
import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;

import com.rmi.IAccount;

/**
 * @author framgiavn
 */
public class RMIServer {
    public static void main(String args[]) {

        try {
            IAccount rAccount = new AccountServiceImpl();

            LocateRegistry.createRegistry(6789);

			// Đăng ký đối tượng này với rmiregistry
            Naming.bind("rmi://192.168.1.230:6789/SeptemberRMI", rAccount);

            System.out.println(">>>>>INFO: RMI Server started!!!!!!!!");
        } catch (RemoteException e) {
            e.printStackTrace();
        } catch (AlreadyBoundException e) {
            e.printStackTrace();
        } catch (MalformedURLException e) {
            e.printStackTrace();
        }
    }
}

```

5.3 Cài đặt đối tượng trên client: **RMIClient.java**

```Java
package com.sept.client.impl;

import java.net.MalformedURLException;
import java.rmi.Naming;
import java.rmi.NotBoundException;
import java.rmi.RemoteException;

import com.rmi.IAccount;

/**
 *
 * @author framgiavn
 *
 */
public class RMIClient {
    public static void main(String args[]) {
        try {
            //Xác định RMI máy chủ.
            IAccount iAccount = (IAccount) Naming.lookup("rmi://192.168.1.230:6789/SeptemberRMI");
            System.out.println("Name: " + iAccount.getUser().getUname());
        } catch (NotBoundException e) {
            e.printStackTrace();
        } catch (MalformedURLException e) {
            e.printStackTrace();
        } catch (RemoteException e) {
            e.printStackTrace();
        }
    }
}
```
