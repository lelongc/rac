package codetuan3.StudentManagement;

public class Student {
	private int id;
	private String name;
	private double result;

	public Student(int id, String name, double result) {
		super();
		this.id = id;
		this.name = name;
		this.result = result;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public double getResult() {
		return result;
	}

	public void setResult(double result) {
		this.result = result;
	}

	@Override
	public String toString() {
		return "sinh viên : id=" + id + ", name=" + name + ", result=" + result;
	}

}