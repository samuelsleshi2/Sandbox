import OOP.Person
import OOP.Employee
import OOP.Student

fun main() {
    val name = "kotlin"
    val language : String? = "java"
//     println("Hello, ${1+2}")
    val arr = arrayOf(1, 2, 3)
//    println(arr[0])
    val ia : IntArray = intArrayOf(2, 4, 6, 8, 10)
//    print("Please tell us your age: ")
//    val age = Integer.valueOf(readLine())
//    val result = if (age >= 21) "You are allowed to drink!" else "You are not allowed to drink!"
//    println(result)
//    print("What day is today? ")
//    val day = readLine();
//    val food = when (day) {
//        "Monday", "Wednesday" -> "Chicken"
//        "Friday", "Tuesday" -> "Salmon"
//        "Sunday", -> "Steak"
//        else -> "Bacon"
//    }
//    val food = when {
//        day == "Monday" -> "Chicken"
//        day == "Friday" -> "Salmon"
//        day == "Sunday" -> "Steak"
//        else -> "Bacon"
//    }
//    println(food)
    val list = listOf<String>("Kotlin", "Java", "Python", "C++")
    val map = mapOf(1 to "Kotlin", 2 to "Java", 3 to "Python", 4 to "C++")

//    for ((key, value) in map) {
//        println("$key => $value")
//    }
//
//    for (i in 9 downTo 1) {
//        print(i)
//    }
//    fun String.getEmotion(): String {
//        return when {
//            last() == '!' -> "Exciting"
//            last() == '?' -> "Curious"
//            last() == '.' -> "Calm"
//            else -> "Unidentified"
//        }
//    }
//    val s = "How are you"
//    println(s.getEmotion())

//    val p1 = Person()
//    p1.age = 10
//    println("My name is ${p1.firstName} ${p1.lastName}, and I am ${p1.age} years old.")
//    val p2 = Person(firstName = "Peter", lastName = "Jackson", age = 29)
//    println(p2.fullName)
//
//    val p3 = Person(year = 3)
//    println("My name is ${p3.firstName} ${p3.lastName}, and I am ${p3.age} years old.")
//    println("P3's id is ${p3.id}")

    val e1 = Employee(company = "XYZ")
    println("e1's id is: ${e1.id}")
    val s1 = Student(school = "ABC")
    println("s1's id is: ${s1.id}")
    e1.wearClothes()
    s1.wearClothes()
}