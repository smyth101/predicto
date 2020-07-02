<?php 
session_start();
$con= new mysqli("localhost","root","","users");
$_SESSION['message'] = "";
if(!isset($_SESSION['user_ID'])){
    header("location:sign_in.php");
}
$uid = $_SESSION['user_ID'];
if ($_SERVER["REQUEST_METHOD"] == "POST"){
    if($_POST['oldpswd'] == $_POST['oldpswdc']){
        if($_POST['newpswd'] == $_POST['newpswdc']){
            $password = md5($_POST['oldpswd']);
            $sql = "SELECT * FROM users WHERE user_ID='$uid'";
            $user_details = mysqli_query($con,$sql);
            if(mysqli_num_rows($user_details) == 1){
                $result = mysqli_fetch_assoc($user_details);
                if($password == $result['password'] ){
                        $new_password = md5($_POST['newpswd']);
                        $update_query = mysqli_query($con,"UPDATE users
                        SET password = '$new_password' WHERE user_ID='$uid'");
                }
                    if(isset($update_query)){
                        $_SESSION['message']= "password successfully updated";
                    }
                    
                else{
                    $_SESSION['message'] = "old password entered is incorrect ";
                }
            }    
        
        }
        else{
            $_SESSION['message'] = "new password entered did not match";
        }
    }
    else{
        $_SESSION['message'] = "old passwords entered did not match";
    }

}

$con = mysqli_connect("localhost","root","","users");
?>

<!DOCTYPE html>
<head>
    <script type="text/javascript">
        function status_changer(){
            window.location.href="prediction.php?status=change";
        }
    </script>
    <title>
        Predicto
    </title>
    <script src="functions.js"></script>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <link rel="stylesheet" href="style_main.css?<?php echo time(); ?>"/>
    <link rel="stylesheet" href="style1.php" media="screen"/>
</head>
<body>
    <div id="header"><div id="logo">Predicto</div><div id="profile">
        <div id = "profile_title" onclick="show_account_options()">Account</div>
        <div id="profile_options">
            <ul>
                <li><a id="account_change_link">change password</a></li>
                <li onclick="show_signout()">sign out</li>
            </ul>
        </div>
    </div><div id="username"><div><?= $_SESSION['username'] ?></div>
</div></div>
    <div id="nav_bar"><ul id="nav_bar_content"><li><a href="index.php" class="nav_item">Home</a></li><li><a href="site_prediction.php" class="nav_item">Predictions</a></li><li> <a href="fixtures.php" class="nav_item"> Fixtures</a> </li><li> <a href="results.php" class="nav_item">Results</a></li> <li><a class="nav_item" href="table.php"> Table</a></li><li><a class="nav_item" href="prediction.php">My Predictions</a></li></ul></div></div>
    <div id ="content_container">
        <h2>Change Password</h2>
        <p>To change your password, please enter and confirm your old password. Then enter and confirm your new password.</p>
        <br>
        <div id="form_container">
<form method='post' action='account_change.php' >
              old password <input name='oldpswd' type='password' required/><br><br>
     confirm old password <input name='oldpswdc' type='password' required/><br><br><br>
new password <input name='newpswd' type='password' required/><br><br>
        confirm new password <input name='newpswdc' type='password' required/><br><br>
<input type='submit'>


</form>
</div><br><br><b>
<?= $_SESSION['message'] ?></b>


</div>

<div id="signout"><p>Are you sure you want to sign out?</p>
    <div id = "signout_buttons">
<form action="signout.php" method="post"><input type="submit" value="Sign out" id="signout_button"/></form><button onclick="cancel_signout()" id="cancel_button">cancel</button>
</div>
</div>
</body>
</html>