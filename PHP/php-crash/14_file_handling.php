<?php

/* ---------- File Handling --------- */

/* 
  File handling is the ability to read and write files on the server.
  PHP has built in functions for reading and writing files.
*/
$file = 'php-crash/extras/users.txt';

if (file_exists($file)) {
    $handle = fopen($file, 'r');
    $contents = fread($handle, filesize($file));
    fclose($handle);
    echo $contents;
} else {
    $handle = fopen($file, 'w');
    $contents = 'Sam' . PHP_EOL . 'Cam' . PHP_EOL . 'Ram';
    fwrite($handle, $contents);
    fclose($handle);
}