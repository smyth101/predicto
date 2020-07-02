<!DOCTYPE html>

<head>
<title>
        Predicto
    </title>
    <script src="functions.js"></script>
    <link rel="stylesheet" href="style_main.css?<?php echo time(); ?>"/>
    <link rel="stylesheet" href="style1.php" media="screen"/>
</head>
<body>
    <div id="header"><div id="logo">Predicto</div>
</div>
	<?php
session_start();
$_SESSION['message'] = '';

?>
	<div id = "content_container" style="margin-top:6%">
	<H2>Password Recovery</h2>
	 <p>Forgot your password?<br>
     Just email recover@predicto.com with the email address you used to create your Predicto account and request for a password change</p>
</div>	
</body>
<html>