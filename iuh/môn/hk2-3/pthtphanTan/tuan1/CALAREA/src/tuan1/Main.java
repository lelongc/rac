package tuan1;

import java.util.ArrayList; 

public class Main {

    public static void main(String[] args) {
       
        Rectangle rectangle = new Rectangle(5, 10);
        System.out.println("Area of Rectangle (5x10) = " + rectangle.calculateArea());

      
        Circle circle = new Circle(3);
        System.out.println("Area of Circle (r=3) = " + circle.calculateArea());

        System.out.println("--------------------------");

        ArrayList<Shape> shapeList = new ArrayList<>();
        
        shapeList.add(new Rectangle(4, 5));
        shapeList.add(new Circle(2.5));
        shapeList.add(new Rectangle(2, 8));

        
        System.out.println("--- Calculating areas for shape list ---");
        for (Shape shape : shapeList) {
            System.out.println("Area of this shape is: " + shape.calculateArea());
        }
    }
}