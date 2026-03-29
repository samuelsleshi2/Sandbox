<?php 
/* --- Object Oriented Programming -- */

/*
  From PHP5 onwards you can write PHP in either a procedural or object oriented way. OOP consists of classes that can hold "properties" and "methods". Objects can be created from classes.
*/

class User {
    // Properties are attributes that belong to a class
    public $name;
    public $email;
    public $password;


    public function __construct($name, $email, $password) {
        $this->name = $name;
        $this->email = $email;
        $this->password = $password;
    }

    function set_name($name) {
        $this->name = $name;
    }

    function get_name() {
        return $this->name;
    }
}

// Instantiate a user object
$user1 = new User('Sam', 'samuel@gmail.com', 'bro');
$user2 = new User('Cam', 'cam@gmail.com', 'ok');

// echo $user1->email;
// echo $user2->name;

class Employee extends User {
    public $title;

    public function __construct($name, $email, $password, $title) {
        parent::__construct($name, $email, $password);
        $this->title = $title;
    }

    public function getTitle() {
        return $this->title;
    }
}

$employee1 = new Employee('Sara', 'sara@gmail.com', '34343', 'Manager');

echo $employee1->getTitle();