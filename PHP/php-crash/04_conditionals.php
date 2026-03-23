<?php

/* ---- Conditionals & Operators ---- */

/* ------------ Operators ----------- */

/*
  < Less than
  > Greater than
  <= Less than or equal to
  >= Greater than or equal to
  == Equal to
  === Identical to
  != Not equal to
  !== Not identical to
*/

/* ---------- If & If-Else Statements --------- */

/*
** If Statement Syntax
if (condition) {
  // code to be executed if condition is true
}
*/

/* -------- Ternary Operator -------- */
/*
  The ternary operator is a shorthand if statement.
  Ternary Syntax:
    condition ? true : false;
*/


/* -------- Switch Statements ------- */

$age = 17;

// if ($age >= 18) {
//     echo 'You are old enough to vote';
// } 

// else {
//     echo 'Sorry, you are not old enough to vote';
// }

$t = date("H"); // current hour

// if ($t < 12) {
//     echo "Good Morning, time is {$t}";
// } else if ($t < 17) {
//     echo "Good Afternoon, time is {$t}";
// } else {
//     echo "Good Evening Chimdi, time is {$t}";
// }

// if (true) {
//   echo('123');
// }

$posts = [];

// if (!(empty($posts))) {
//   echo $posts[0];
// } else {
//   echo('No posts');
// }

// echo !empty($posts) ? $posts[0] : 'No Posts';

// $firstPost = !empty($posts) ? $posts[0] : 'No Posts';
// $firstPost = !empty($posts) ? $posts[0] : null;

// $firstPost = $posts[0] ?? null;

// echo $firstPost;

$favcolor = 'blue';

switch($favcolor) {
  case 'red':
    echo 'your favorite color is red';
    break;
  case 'green':
    echo 'your favorite color is green';
    break;
  case 'blue':
    echo 'your favorite color is blue';
    break;
  default:
    echo 'your favorite color is not red green or blue';
}