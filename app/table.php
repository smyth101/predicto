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
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <link rel="stylesheet" href="style_main.css?<?php echo time(); ?>" type='text/css' type='text/css'/>
    <link rel="stylesheet" href="style1.php" media="screen"/>
</head>
<body>
   <div id="header">
    <div id="logo">Predicto</div>
    <div id="profile">
        <div id = "profile_title" onclick="show_account_options()">Account</div>
        <div id="profile_options">
            <ul>
                <li ><a id="account_change_link" href="account_change.php">change password</a></li>
                <li onclick="show_signout()">sign out</li>
            </ul>
        </div>
    </div>
    <div id="username"><div><?= $_SESSION['username'] ?></div></div>
    </div>
    <div id="nav_bar"><ul id="nav_bar_content"><li><a href="index.php" class="nav_item">Home</a></li><li><a href="site_prediction.php" class="nav_item">Predictions</a></li><li> <a href="fixtures.php" class="nav_item"> Fixtures</a> </li><li> <a href="results.php" class="nav_item">Results</a></li> <li><a class="nav_item" href="table.php"> Table</a></li><li><a class="nav_item" href="prediction.php">My Predictions</a></li></ul></div>

        <div id="content_container">
            <h2>Premier League Table</h2>
            <?php

// Check connection
if (mysqli_connect_errno())
{
echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

$result = mysqli_query($con,"SELECT position,team_name,played,won,drawn,lost,GF,GA,GD,points FROM pl_table ORDER BY position" );

echo "<table border='1' id='solo_table'>
<tr>
<th>Pos</th>
<th>Team</th>
<th>Played</th>
<th>Won</th>
<th>Drew</th>
<th>Lost</th>
<th>GF</th>
<th>GA</th>
<th>GD</th>
<th>Points</th>
</tr>";

while($row = mysqli_fetch_array($result))
{
echo "<tr>";
echo "<td>" . $row['position'] . "</td>";
echo "<td>" . $row['team_name'] . "</td>";
echo "<td>" . $row['played'] . "</td>";
echo "<td>" . $row['won'] . "</td>";
echo "<td>" . $row['drawn'] . "</td>";
echo "<td>" . $row['lost'] . "</td>";
echo "<td>" . $row['GF'] . "</td>";
echo "<td>" . $row['GA'] . "</td>";
echo "<td>" . $row['GD'] . "</td>";
echo "<td>" . $row['points'] . "</td>";
echo "</tr>";
}
echo "</table>";

mysqli_close($con);

?>
        </div></div>
        <div id="signout"><p>Are you sure you want to sign out?</p>
    <div id = "signout_buttons">
<form action="signout.php" method="post"><input type="submit" value="Sign out" id="signout_button"/></form><button onclick="cancel_signout()" id="cancel_button">cancel</button>
</div>
</div>
</body>
</html>