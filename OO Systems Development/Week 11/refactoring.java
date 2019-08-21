// Note: this example can't be compiled. Example only!

// Class refactoring example

public class Customer {
    private String name;
    private String workPhoneAreaCode;
    private String workPhoneNumber;
}

public class Customer {
    private String name;
    private Phone workPhone;
}

public class Phone {
    private String areaCode;
    private String number;
}

// Sub-class refactoring example

public class Person {
    private String name;
    private String jobTitle;
}

public class Person {
    protected String name;
}

public class Employee extends Person {
    private String jobTitle;
}

// Super-class refactoring example

public class Employee {
    private String name;
    private String jobTitle;
}

public class Student {
    private String name;
    private Course course;
}

public abstract class Person {
    protected String name;
}

public class Employee extends Person {
    private String jobTitle;
}

public class Student extends Person {
    private Course course;
}
