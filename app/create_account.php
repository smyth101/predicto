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
$con= new mysqli("localhost","root","","users");

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if ($_POST['password'] == $_POST['confirmpassword']) {
    	$username = $con->real_escape_string($_POST['username']);
    	$email = $con->real_escape_string($_POST['email']);
    	$username_check = mysqli_query($con,"SELECT email FROM users WHERE email='$email'" );
    	$row_count = mysqli_num_rows($username_check);
    	if($row_count == 0){ 
	        $password = md5($_POST['password']);
	                $_SESSION['username'] = $username;

	                $sql = 
	                "INSERT INTO users (name, email, password) "
	                . "VALUES ('$username', '$email', '$password')";
	               
	                if ($con->query($sql) == true){
						$_SESSION['message'] = "<div id='success_box'><div id='error_padding'>account successfully created</div></div>";
	                	header("location:sign_in.php");
                }
			}
		else{
			$_SESSION['message'] = 'email entered is already registered to an account';
		}

    }
    else{
    	$_SESSION['message'] = "passwords dont match";
    }


}
?>
	<div id = "content_container" style="margin-top:6%">
	<H2>Create Account</h2>
		<div id="form_container">	
	 <form class="create_account" action="create_account.php" method="post" enctype="multipart/form-data" autocomplete="off">
      
      Username: <input type="text" placeholder="User Name" name="username" required /><br><br>
      Email: <input type="email" placeholder="Email" name="email" required /><br><br>
      Password: <input type="password" placeholder="Password" name="password"  required /><br><br>
      Confirm Password: <input type="password" placeholder="Confirm Password" name="confirmpassword"  required /><br><br>
      <input type="submit" value="Register" name="register" /><br><br>
	</form>
<?php echo $_SESSION['message']; ?>
</div>
</div>	
</body>
<html>