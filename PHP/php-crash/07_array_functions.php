<?php
/* --------- Array Functions -------- */

/*
  Functions to work with arrays
  https://www.php.net/manual/en/ref.array.php
*/

$fruits = ['apple', 'orange', 'pear'];

echo count($fruits);

// var_dump(in_array('apples', $fruits));

// Adding to array
$fruits[] = 'grape';
array_push($fruits, 'blueberry', 'strawberry');
array_unshift($fruits, 'mango');

// Removing from array
array_pop($fruits);
array_shift($fruits);
// unset($fruits[2]);



print_r($fruits);