package OOP

abstract class Person (var firstName: String = "John", var lastName: String = "Smith", var age: Int = 19) {
    val fullName: String
        get() = "$firstName $lastName"

    constructor(year: Int) : this() {
        age =+ year
    }

    abstract val id : String
//    init {
//        id = fullName + age
//    }
}

class Employee(company: String) : Person(), PersonActions {
    override val id = fullName + company + age
    override fun wearClothes() {
        println("Employee wears suit and tie.")
    }
}

class Student (school : String) : Person(), PersonActions {
    override val id = fullName + school + age
    override fun wearClothes() {
        println("Student wears uniform.")
    }
}