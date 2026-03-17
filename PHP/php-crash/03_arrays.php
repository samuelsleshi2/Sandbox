<?php
/* ----------- Arrrays ----------- */

/*
  Arrays hold multiple values. Each value in an array is called an "element"
*/

// two ways to make a simple array
$numbers = [1, 2, 3, 4];
$fruits = ['apple', 'orange', 'pear'];

// var_dump($numbers);
// echo $fruits[0];

// Associative Array (essentially key-value pairs)
$colors = [
    1 => 'red',
    4 => 'blue',
    6 => 'green'
];

// echo $colors[4];

$hex = [
    'red' => '#f00',
    'blue' => '#00f',
    'green' => '#0f0'
];

// echo $hex['blue'];

$person = [
    'first_name' => 'Brad',
    'last_name' => 'Traversy',
    'email' => 'brad@gmail.com'
];

// echo $person['first_name'];

// Multi-dimensional Array (array of associative arrays)
$people = [
    [
        'first_name' => 'Brad',
        'last_name' => 'Traversy',
        'email' => 'brad@gmail.com'
    ],
    [
        'first_name' => 'John',
        'last_name' => 'Doe',
        'email' => 'john@gmail.com'
    ],
    [
        'first_name' => 'Jane',
        'last_name' => 'Doe',
        'email' => 'jane@gmail.com'
    ]
];

// echo $people[1]['email'];
var_dump(json_encode($people));