<?php
//print("hello world")
$str = 'This is Main String';
 
if (strpos($str, 'This') !== false) {
    echo 'true';
}else{
	echo 'false';
}

//$obj= new ReflectionObject("str");
//$obj= new ReflectionClass($str).getMethods();
print_r($GLOBALS);
?>
