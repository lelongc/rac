package OOP_IOStream;

public class Meo extends DongVat {
    public Meo(String ten, int tuoi) { 
        super("Meo", ten, tuoi); 
    }

    public void leoTuong() { 
        System.out.println(ten + " dang leo tuong..."); 
    }

    @Override
    public void taoAmThanh() { 
        System.out.println(ten + " keu: Meo Meo!"); 
    }
}
