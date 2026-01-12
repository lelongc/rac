public class Circle extends Shape {
    private double radius;

    // Constructor
    public Circle(double radius) {
        this.radius = radius;
    }

    @Override
    public double calculateArea() {
        // Math.PI is a built-in constant for PI in Java
        return Math.PI * radius * radius;
    }
}
