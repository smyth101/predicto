<?php 
session_start();
if(!isset($_SESSION['user_ID'])){
    header("location:sign_in.php");

}
?>
<!DOCTYPE html>
<head>
    <title>
        Predicto
    </title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <script src="functions.js?<?php echo time(); ?>"></script>
    <link rel="stylesheet" href="style_main.css?<?php echo time(); ?>" type='text/css'/>
    <link rel="stylesheet" href="style1.php" media="screen"/>


</head>
<body>
    <div id="header"><div id="logo">Predicto</div><div id="profile">
        <div id = "profile_title" onclick="show_account_options()">Account</div>
        <div id="profile_options">
            <ul>
                <li><a href="account_change.php" id="account_change_link">change password</a></li>
                <li onclick="show_signout()">sign out</li>
            </ul>
        </div>
    </div><div id="username"><div><?= $_SESSION['username'] ?></div>
</div></div>
    <div id="nav_bar"><ul id="nav_bar_content"><li><a href="index.php" class="nav_item">Home</a></li><li><a href="site_prediction.php" class="nav_item">Predictions</a></li><li> <a href="fixtures.php" class="nav_item"> Fixtures</a> </li><li> <a href="results.php" class="nav_item">Results</a></li> <li><a class="nav_item" href="table.php"> Table</a></li><li><a class="nav_item" href="prediction.php">My Predictions</a></li></ul></div>
    <div id ="main_container">
    <div class="mid_container">
             <?php
$con=mysqli_connect("localhost","root","","results");
$con2=mysqli_connect("localhost","root","","fixtures");

if (mysqli_connect_errno())
{
echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

$predict = mysqli_query($con2,"SELECT fixtures.match_date,fixtures.home_team,fixtures.away_team,pred.pred_home_score,pred.pred_away_score FROM predictions as pred INNER JOIN fixtures.fixtures as fixtures ON fixtures.LinkKey = pred.LinkKey ORDER BY match_date LIMIT 5"  );


$current = '';
echo "<h3>Predictions</h3>";
echo '<table>';
while($row = mysqli_fetch_array($predict))
{
echo '<tr>';
if($current != $row['match_date']){
    echo '<td><b>' . date("d F Y", strtotime($row['match_date'])) . '<b></td>';
}
else{
    echo '<td></td>';
}

echo "<td>" . $row['home_team'] . "</td>";
echo "<td>" . $row['pred_home_score'] . "</td>";
echo "<td> - </td>";
echo "<td>" . $row['pred_away_score'] . "</td>";
echo "<td>" . $row['away_team'] . "</td>";
echo "</tr>";
$current = $row['match_date'];
}
echo '</table></div>';




$result = mysqli_query($con,"SELECT match_date,home_team,away_team,home_score,away_score FROM results WHERE YEAR(match_date) = 2018 OR YEAR(match_date) = 2019 ORDER BY match_date DESC LIMIT 5"  );


$current = '';
echo '<div class="mid_container">';
echo '<h3>Recent Results</h3>';
echo '<table>';
while($row = mysqli_fetch_array($result))
{
echo '<tr>';
if($current != $row['match_date']){
    echo '<td><b>' . date("d F Y", strtotime($row['match_date'])) . '<b></td>';
}
else{
    echo '<td></td>';
}

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
    <div class = "mid_container">
         <?php
$con=mysqli_connect("localhost","root","","results");

if (mysqli_connect_errno())
{
echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

$result = mysqli_query($con2,"SELECT match_date,home_team,away_team FROM fixtures ORDER BY match_date LIMIT 6" );
echo "<h3>Upcoming Fixtures</h3>";
echo "<table>";
$_current = "";
while($row = mysqli_fetch_array($result))
{
    if($current != $row['match_date']){
        echo '<tr id="row_date_break"><td><b>' . date("d F Y", strtotime($row['match_date'])) . '</b></td>';
    }
    else{
        echo '<tr><td></td>';
    }   
echo "<td>" . $row['home_team'] . "</td>";
echo "<td> v </td>";
echo "<td>" . $row['away_team'] . "</td>";
$current = $row['match_date'];

}
echo "</table>";

mysqli_close($con2);

?>
    </div>
    </div>
    <div id="right_side_container">
        <div id="sidebar">
            <h3>Table</h3>
            


<?php
$con=mysqli_connect("localhost","root","","results");

if (mysqli_connect_errno())
{
echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

$result = mysqli_query($con,"SELECT position,team_name,played,points FROM pl_table ORDER BY position" );

echo "<table border='1' id='side_table'>
<tr>
<th>Pos</th>
<th>Team</th>
<th>Played</th>
<th>Points</th>
</tr>";

while($row = mysqli_fetch_array($result))
{
echo "<tr>";
echo "<td>" . $row['position'] . "</td>";
echo "<td>" . $row['team_name'] . "</td>";
echo "<td>" . $row['played'] . "</td>";
echo "<td>" . $row['points'] . "</td>";
echo "</tr>";
}
echo "</table>";

mysqli_close($con);

?>
        </div>
    </div>
    <div id="signout"><p>Are you sure you want to sign out?</p>
    <div id = "signout_buttons">
<form action="signout.php" method="post"><input type="submit" value="Sign out" id="signout_button"/></form><button onclick="cancel_signout()" id="cancel_button">cancel</button>
</div>
</div>
</body>
</html>