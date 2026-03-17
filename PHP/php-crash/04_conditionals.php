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

$t = date("H");

if ($t < 12) {
    echo "Good Morning, time is {$t}";
}
else if ($t < 17) {
    echo "Good Afternoon, time is {$t}";
}
else {
    echo "Good Evening, time is {$t}";
}

