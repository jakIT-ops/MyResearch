package ClassAndObjects;

class Student {

	  // Private fields
	  private String name;
	  private double mark1;
	  private double mark2;

	  // Default Constructor
	  public Student() {
	    name = "";
	    mark1 = 0;
	    mark2 = 0;
	  }

	  // Parameterized Constructor
	  public Student(String name, double mark1, double mark2) {
	    this.name = name;
	    this.mark1 = mark1;
	    this.mark2 = mark2;
	  }

	  // Getter Function
	  public double getMarks(int markNumber) {

		    if(markNumber == 1) return mark1;
		    else if(markNumber == 2) return mark2;
		    return 0;
	  }

	  public double calcTotal() {
		  // Write definition here
		  double totalMarks = mark1 + mark2;
		  return totalMarks;
	  }
}

class Demo {

	public static void main(String args[]) {
	    Student student = new Student("Jack", 60, 70);
	    System.out.println(student.calcTotal());
	 }

}
