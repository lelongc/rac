package tuan2b;

public class Main {
    public static void main(String[] args) {
       
        XeMay xm = new XeMay("Honda", 2026, 40000000, 125);
        System.out.println("thong tin xe may");
        xm.hienThiThongTin();
        System.out.println("tax: " + xm.tinhThue());

        System.out.println("\n------------------------\n");

        
        Oto ot = new Oto("Toyota", 2028, 800000000, 5);
        System.out.println("thong tin oto");
        ot.hienThiThongTin();
        System.out.println("tax: " + ot.tinhThue());
    }
}