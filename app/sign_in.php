<?php
session_start();
if(!isset($_SESSION['message'])){
	$_SESSION['message'] = "";
}
else{
		if($_SESSION['message'] != "<div id='success_box'><div id='error_padding'>account successfully created</div></div>"){
			$_SESSION['message'] = "";
}
}

$con= new mysqli("localhost","root","","users");
if ($_SERVER["REQUEST_METHOD"] == "POST") {
	$email = $con->real_escape_string($_POST['email']);
	$password = md5($_POST['password']);
	$sql = "SELECT * FROM users WHERE email='$email'";
	$user_details = mysqli_query($con,$sql);
	if(mysqli_num_rows($user_details) == 1){
		$result = mysqli_fetch_assoc($user_details);
		if($password == $result['password'] ){
			$_SESSION['username'] = $result['name'];
			$_SESSION['user_ID'] = $result['user_ID'];
			header("location: index.php");}
		else{
			$_SESSION['message'] = "<div id='error_box'><div id='error_padding'>Incorrect email and/or password entered.</div></div>";
		}
	}
	else{
		$_SESSION['message'] = "<div id='error_box'><div id='error_padding'>Incorrect email and/or password entered</div></div>";
	}
}
?>
<!DOCTYPE html>
<head>
	<title>sign-in</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
	<link rel="stylesheet" href="style.css?<?php echo time(); ?>" type="text/css"/>
</head>
<body>
	<form class="signin" action="sign_in.php" method="post" enctype="multipart/form-data" autocomplete="off">
	<img src = "login.jpg" class = "image" alt = "avatar">
			<div id = "heading">
				<h1>Login Here</h1>
			</div>
			<?php echo $_SESSION['message'] ?><br>
			<div id="details">
			<p>Email</p>	
      <input type="email" placeholder="Email" name="email" required />
			<p>Password</p>
			<input type="password" placeholder="Password" name="password"  required />
</div>
<div id="button">
			<input type="submit" value="Sign in" name="signin" />
</div>
<div id = "links">
				<!-- <a href = "#passwordreset">Forgot your password?</a><br> -->
				Dont have an account? <br><a href = "create_account.php">click here to Register</a><br><br>
				Forgot your password? <br><a href = "forgot_password.php">click here to Recover</a>
			</div>
    </form>
</body>
<html>