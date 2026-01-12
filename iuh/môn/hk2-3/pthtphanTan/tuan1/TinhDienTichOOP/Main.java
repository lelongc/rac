import java.util.ArrayList; // Library for dynamic arrays

public class Main {

    public static void main(String[] args) {
        // 1. Test Rectangle (Question 1)
        Rectangle rectangle = new Rectangle(5, 10);
        System.out.println("Area of Rectangle (5x10) = " + rectangle.calculateArea());

        // 2. Test Circle (Question 2)
        Circle circle = new Circle(3);
        System.out.println("Area of Circle (r=3) = " + circle.calculateArea());

        System.out.println("--------------------------");

        // 3. Using Polymorphism for shape list (Question 3)
        // Create a list containing different types of shapes
        ArrayList<Shape> shapeList = new ArrayList<>();
        
        shapeList.add(new Rectangle(4, 5));
        shapeList.add(new Circle(2.5));
        shapeList.add(new Rectangle(2, 8));

        // Iterate through the list and calculate areas
        System.out.println("--- Calculating areas for shape list ---");
        for (Shape shape : shapeList) {
            // Java automatically knows if shape is Circle or Rectangle to call the correct method
            System.out.println("Area of this shape is: " + shape.calculateArea());
        }
    }
}