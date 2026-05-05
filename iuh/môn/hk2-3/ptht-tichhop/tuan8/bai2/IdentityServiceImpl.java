package bai2;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.HashMap;
import java.util.Map;

public class IdentityServiceImpl extends UnicastRemoteObject implements IdentityService {

    /**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private final Map<String, PersonInfo> db = new HashMap<>();

    protected IdentityServiceImpl() throws RemoteException {
        super();

       
        db.put("012345678901", new PersonInfo("Nguyen Van A", "Ha Noi"));
        db.put("079123456789", new PersonInfo("Tran Thi B", "TP Ho Chi Minh"));
        db.put("123456789",    new PersonInfo("Le Van C", "Da Nang")); 
    }

    @Override
    public String lookup(String idNumber) throws RemoteException {
        if (idNumber == null) return "ERROR: id rong";
        String id = idNumber.trim();

        if (id.isEmpty()) return "ERROR: id rong";
        if (!id.matches("\\d+")) return "ERROR: id chi duoc chua chu so";
        
        if (id.length() < 9 || id.length() > 12) return "ERROR: do dai id khong hop le (9-12 so)";

        PersonInfo info = db.get(id);
        if (info == null) return "ERROR: khong tim thay thong tin cho id " + id;

        return "Ho ten: " + info.fullName + " | Que quan: " + info.hometown;
    }

    private static class PersonInfo {
        final String fullName;
        final String hometown;

        PersonInfo(String fullName, String hometown) {
            this.fullName = fullName;
            this.hometown = hometown;
        }
    }
}