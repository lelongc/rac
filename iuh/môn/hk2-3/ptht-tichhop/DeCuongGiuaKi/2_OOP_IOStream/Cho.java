package OOP_IOStream;

public class Cho extends DongVat {
    public Cho(String ten, int tuoi) { 
        super("Cho", ten, tuoi); 
    }

    public void chay() { 
        System.out.println(ten + " dang chay ton ton..."); 
    }
    
    @Override
    public void taoAmThanh() { 
        System.out.println(ten + " keu: Go Go!"); 
    }
}
