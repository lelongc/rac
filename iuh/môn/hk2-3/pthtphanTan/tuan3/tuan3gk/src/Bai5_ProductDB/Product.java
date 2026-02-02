package Bai5_ProductDB;

import java.io.Serializable;

public class Product implements Serializable {
    public int id;
    public String name;
    public double price;
    public String desc;

    public Product(int i, String n, double p, String d) {
        id = i;
        name = n;
        price = p;
        desc = d;
    }

    public String toString() {
        return id + " | " + name + " | " + price + " | " + desc;
    }
}
