package File_Folder;

public class QuanLyVuonThu {
    
    // ==================================================
    // 1. CLASS CHA (DONG VAT)
    // ==================================================
    static abstract class DongVat {
        protected String name;
        protected double weight;

        public DongVat(String name, double weight) {
            this.name = name;
            this.weight = weight;
        }
        
        public abstract void inThongTin();
    }

    // ==================================================
    // 2. CLASS SU TU
    // ==================================================
    static class SuTu extends DongVat {
        private double eatAmount;

        public SuTu(String name, double weight, double eatAmount) {
            super(name, weight);
            this.eatAmount = eatAmount;
        }

        @Override
        public void inThongTin() {
            System.out.println("Su tu " + name + " nang " + weight + " can va an " + eatAmount + " can thit moi ngay.");
        }
    }

    // ==================================================
    // 3. CLASS RAN
    // ==================================================
    static class Ran extends DongVat {
        private double length;

        public Ran(String name, double weight, double length) {
            super(name, weight);
            this.length = length;
        }

        @Override
        public void inThongTin() {
            System.out.println("Con ran " + name + " nang " + weight + " can va dai " + length + " met.");
        }
    }

    // ==================================================
    // 4. CLASS KHI
    // ==================================================
    static class Khi extends DongVat {
        private String favoriteFood;

        public Khi(String name, double weight, String favoriteFood) {
            super(name, weight);
            this.favoriteFood = favoriteFood;
        }

        @Override
        public void inThongTin() {
            System.out.println("Con khi " + name + " nang " + weight + " can va thich an " + favoriteFood);
        }
    }

    // ==================================================
    // CHUONG TRINH CHINH
    // ==================================================
    public static void main(String[] args) {
        DongVat sutu = new SuTu("Leo", 300, 5);
        DongVat ran = new Ran("Boa", 50, 5);
        DongVat khi = new Khi("George", 150, "chuoi");

        sutu.inThongTin();
        ran.inThongTin();
        khi.inThongTin();
    }
}
