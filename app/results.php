<?php 
session_start();
if(!isset($_SESSION['user_ID'])){
    header("location:sign_in.php");

}
$con=mysqli_connect("localhost","root","","results");

?>
<!DOCTYPE html>
<head>
    <title>
        Predicto
    </title>
    <script src="functions.js"></script>
    <link rel="stylesheet" href="style_main.css?<?php echo time(); ?>" type='text/css'/>
    <link rel="stylesheet" href="style1.php" media="screen"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
</head>
<body>
    <div id="header"><div id="logo">Predicto</div><div id="profile">
        <div id = "profile_title" onclick="show_account_options()">Account</div>
        <div id="profile_options">
            <ul>
                <li><a  id="account_change_link" href="account_change.php">change password</a></li>
                <li onclick="show_signout()">sign out</li>
            </ul>
        </div>
    </div><div id="username"><div><?= $_SESSION['username'] ?></div>
</div></div>
    <div id="nav_bar"><ul id="nav_bar_content"><li><a href="index.php" class="nav_item">Home</a></li><li><a href="site_prediction.php" class="nav_item">Predictions</a></li><li> <a href="fixtures.php" class="nav_item"> Fixtures</a> </li><li> <a href="results.php" class="nav_item">Results</a></li> <li><a class="nav_item" href="table.php"> Table</a></li><li><a class="nav_item" href="prediction.php">My Predictions</a></li></ul></div>
        
        <div id="content_container">
        <h2>Results</h2>
            <?php

// Check connection
if (mysqli_connect_errno())
{
echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

$result = mysqli_query($con,"SELECT match_date,home_team,away_team,home_score,away_score FROM results WHERE YEAR(match_date) = 2018 OR YEAR(match_date) = 2019 ORDER BY match_date DESC"  );


$current = '';
echo '<table id = "solo_table">';
while($row = mysqli_fetch_array($result))
{

if($current != $row['match_date']){
    echo '<tr id="row_date_break"><td><b>' . date("d F Y", strtotime($row['match_date'])) . '</b></td>';
}
else{
    echo '<tr><td></td>';
}
// echo "<td> HOME TEAM HERE</td>";
echo "<td>" . $row['home_team'] . "</td>";
echo "<td>" . $row['home_score'] . "</td>";
echo "<td> - </td>";
echo "<td>" . $row['away_score'] . "</td>";
echo "<td>" . $row['away_team'] . "</td>";
echo "</tr>";
$current = $row['match_date'];
}
echo '</table>';

mysqli_close($con);

?>
</div>
<div id="signout"><p>Are you sure you want to sign out?</p>
    <div id = "signout_buttons">
<form action="signout.php" method="post"><input type="submit" value="Sign out" id="signout_button"/></form><button onclick="cancel_signout()" id="cancel_button">cancel</button>
</div>
</div>
</body>
</html>