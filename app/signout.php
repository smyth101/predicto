<?php
if ($_SERVER["REQUEST_METHOD"] == "POST"){
    session_start();

    session_unset();

    session_destroy();

    header("location:sign_in.php");
}
else{
    header("location:index.php");
}
exit();

?>