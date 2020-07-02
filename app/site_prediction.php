<?php 
session_start();



$usr_ID = $_SESSION['user_ID'];
$con=mysqli_connect("localhost","root","","results");
$con2 = mysqli_connect("localhost","root","","fixtures");


$query = "SELECT pred.*,results.* FROM predictions as pred  JOIN results.results as results ON results.LinkKey = pred.LinkKey ORDER BY results.match_date DESC";
$usr_preds = mysqli_query($con2,$query);
?>
<!DOCTYPE html>
<head>
<link rel="stylesheet" href="style_main.css?<?php echo time(); ?>" type='text/css'/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<script src="functions.js??<?php echo time(); ?>"></script>

<title>
past predictions
</title>
</head>
<body>
    <div id="header"><div id="logo">Predicto</div><div id="profile">
        <div id = "profile_title" onclick="show_account_options()">Account</div>
        <div id="profile_options">
            <ul>
                <li><a id="account_change_link" href="account_change.php">change password</a></li>
                <li onclick="show_signout()">sign out</li>
            </ul>
        </div>
    </div><div id="username"><div><?= $_SESSION['username'] ?></div>
</div></div>
    <div id="nav_bar"><ul id="nav_bar_content"><li><a href="index.php" class="nav_item">Home</a></li><li><a href="site_prediction.php" class="nav_item">Predictions</a></li><li> <a href="fixtures.php" class="nav_item"> Fixtures</a> </li><li> <a href="results.php" class="nav_item">Results</a></li> <li><a class="nav_item" href="table.php"> Table</a></li><li><a class="nav_item" href="prediction.php">My Predictions</a></li></ul></div>
<div id="content_container">
<?php
$row_check = mysqli_query($con2,"SELECT * FROM fixtures ORDER BY match_date LIMIT 1"  );
$first_m_date = mysqli_fetch_array($row_check);
$first_m_date = $first_m_date["match_date"];
$first_m_date = date('Y-m-d', strtotime($first_m_date. '5 days'));


$predict = mysqli_query($con2,"SELECT fixtures.match_date,fixtures.home_team,fixtures.away_team,pred.pred_home_score,pred.pred_away_score FROM predictions as pred INNER JOIN fixtures.fixtures as fixtures ON fixtures.LinkKey = pred.LinkKey WHERE DATE(fixtures.match_date) < '$first_m_date' ORDER BY match_date"  );
$current = '';
echo "<h2> Weeks Predictions</h2>";
echo '<table id="solo_table">';
while($row = mysqli_fetch_array($predict))
{
if($current != $row['match_date']){
    echo '<tr id="row_date_break"><td><b>' . date("d F Y", strtotime($row['match_date'])) . '</b></td>';
}
else{
    echo '<tr><td></td>';
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
?>










<div id='content_container'>
<?php


        echo "<h2>Past Predictions</h2>";
		echo "<table id='solo_table'>";
		while($row = mysqli_fetch_assoc($usr_preds)){
			echo "<tr>";
			echo"<td><b>" .date("d F Y", strtotime($row['match_date'])) . "<b></td>";
			echo "<td>" . $row['home_team'] . "</td>";
			echo "<td>" . $row['pred_home_score'] . "</td>";
			echo "<td> - </td>";
			echo "<td>" . $row['pred_away_score'] . "</td>";
			echo "<td>" . $row['away_team'] . "</td>";

			
			echo "</tr>";
			echo "<tr id='row_break'>";
			echo"<td></td>";
			echo "<td class='result_row'>Result</td>";
			echo "<td class='result_row'>" . $row['home_score'] . "</td>";
			echo "<td> - </td>";
			echo "<td class='result_row'>" . $row['away_score'] . "</td>";
			echo "<td></td>";
			echo "</tr>";

	}
	echo "</table>";

?>
</div>
<div id="signout"><p>Are you sure you want to sign out?</p>
    <div id = "signout_buttons">
<form action="signout.php" method="post"><input type="submit" value="Sign out" id="signout_button"/></form><button onclick="cancel_signout()" id="cancel_button">cancel</button>
</div>
</div>
</body>
</html>
