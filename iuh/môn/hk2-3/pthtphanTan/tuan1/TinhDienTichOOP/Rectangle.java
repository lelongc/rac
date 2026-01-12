public class Rectangle extends Shape {
    private double length;
    private double width;

    // Constructor
    public Rectangle(double length, double width) {
        this.length = length;
        this.width = width;
    }

    // Override the area calculation method from parent class
    @Override
    public double calculateArea() {
        return length * width;
    }
}
