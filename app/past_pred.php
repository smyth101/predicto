<?php 
// session_start();

function sign( $number ) { 
    return ( $number > 0 ) ? 1 : ( ( $number < 0 ) ? -1 : 0 );
}


function score_system($rhs,$ras,$phs,$pas){
	$points = 0;
	if($rhs == $phs && $ras == $pas){
		$points = 5;
	}
	elseif($rhs == $phs xor $ras == $pas ){
		$points = 2;
	}
	elseif(sign(($rhs - $ras)) == sign(($phs - $pas))){
		$points = 1;
	}

	return $points;
}

$usr_ID = $_SESSION['user_ID'];
$con=mysqli_connect("localhost","root","","results");
$con2 = mysqli_connect("localhost","root","","users");
// $query = "SELECT results.*, preds.* 
//               FROM results AS results
//               INNER JOIN users.user_predictions as preds ON ( results.LinkKey = preds.LinkKey ) WHERE user_ID = '$usr_ID' ORDER BY match_date";

$query = "SELECT pred.pred_home_score as phs,pred.pred_away_score as pas,upred.*,results.* FROM user_predictions as upred JOIN fixtures.predictions as pred ON pred.LinkKey = upred.LinkKey JOIN results.results as results ON results.LinkKey = upred.LinkKey WHERE upred.user_ID = $_SESSION[user_ID] ORDER BY match_date DESC";
$usr_preds = mysqli_query($con2,$query);
// while($row = mysqli_fetch_assoc($usr_preds)){
// 	echo $row['home_team'];
// 	echo $row['phs'];
// 	echo $row['away_team'];
// 	echo $row['ahs'];
// }



?>
<form method="get" action="prediction.php">
	<div id='pred_filter'>
  show results<input type="checkbox" name="results" value="result_check" <?php if(isset($_GET['results'])) echo "checked='checked'"; ?>>
  show site predictions<input type="checkbox" name="preds" value="pred_check"<?php if(isset($_GET['preds'])) echo "checked='checked'"; ?>>
	<input type="submit" value="Apply"  name='filter' value='1'>
</div>
</form>

<?php
// echo "<script type='text/javascript'>overall_score('user_score_container','site_game_score')</script>";
echo "<div id='user_score_container'>Overall Points: </div>";

echo "<div id='site_score_container'>Site Points: </div><br>";
// echo "<script type='text/javascript'>overall_score('user_score_container','game_score')</script><br>";

if(mysqli_num_rows($usr_preds) == 0){
	echo "<table id='solo_table'><tr><td>No predictions have been made yet</td></tr></table>";
}


if($_SERVER["REQUEST_METHOD"] == "GET"){

	if(isset($_GET['filter']))
	{
		echo "<script>scroll_down()</script>";
	}

	if(isset($_GET['results']) && isset($_GET['preds'])){
		echo "<table id='solo_table' name='pred_scroll'>";
		if(mysqli_num_rows($usr_preds) != 0){
		echo "<tr ><td></td><td></td><td></td><td></td><td></td><td></td><td id='points_column' >Points</td></tr>";
		}
		while($row = mysqli_fetch_assoc($usr_preds)){
			echo "<tr>";
			echo"<td>" . date("d F Y", strtotime($row['match_date'])) . "</td>";
			echo "<td>" . $row['home_team'] . "</td>";
			echo "<td>" . $row['pred_home_score'] . "</td>";
			echo "<td> - </td>";
			echo "<td>" . $row['pred_away_score'] . "</td>";
			echo "<td>" . $row['away_team'] . "</td>";

			echo "<td name='game_score' class='points'>" . score_system($row['home_score'],$row['away_score'],$row['pred_home_score'],$row['pred_away_score']) . "</td>";
			echo "</tr>";
			echo "<tr>";
			echo"<td></td>";
			echo "<td class='result_row'>Result</td>";
			echo "<td class='result_row'>" . $row['home_score'] . "</td>";
			echo "<td> - </td>";
			echo "<td class='result_row'>" . $row['away_score'] . "</td>";
			echo "<td></td>";
			echo "</tr>";
			echo "<tr id='row_break'>";
			echo"<td></td>";
			echo "<td class='pred_row''>Site Prediction</td>";
			echo "<td class='pred_row'>" . $row['phs'] . "</td>";
			echo "<td> - </td>";
			echo "<td class='pred_row'>" . $row['pas'] . "</td>";
			echo "<td></td>";
			echo "<td name='site_game_score' class='points'>" . score_system($row['home_score'],$row['away_score'],$row['phs'],$row['pas']) . "</td>";
			echo "</tr>";
	}
	echo "</table>";
}
	else if(isset($_GET['results'])){
		echo "<table id='solo_table'>";
		if(mysqli_num_rows($usr_preds) != 0){
			echo "<tr ><td></td><td></td><td></td><td></td><td></td><td></td><td id='points_column' >Points</td></tr>";
			}
		while($row = mysqli_fetch_assoc($usr_preds)){
			echo "<tr>";
			echo"<td>" . date("d F Y", strtotime($row['match_date'])) . "</td>";
			echo "<td>" . $row['home_team'] . "</td>";
			echo "<td>" . $row['pred_home_score'] . "</td>";
			echo "<td> - </td>";
			echo "<td>" . $row['pred_away_score'] . "</td>";
			echo "<td>" . $row['away_team'] . "</td>";

			echo "<td name='game_score' class='points'>" . score_system($row['home_score'],$row['away_score'],$row['pred_home_score'],$row['pred_away_score']) . "</td>";
			echo "</tr>";
			echo "<tr id='row_break'>";
			echo"<td></td>";
			echo "<td class='result_row'>Result</td>";
			echo "<td class='result_row'>" . $row['home_score'] . "</td>";
			echo "<td> - </td>";
			echo "<td class='result_row'>" . $row['away_score'] . "</td>";
			echo "<td></td>";
			echo "</tr>";
			echo "<tr style='display:none'><td name='site_game_score' class='points'>" . score_system($row['home_score'],$row['away_score'],$row['phs'],$row['pas']) . "</td></tr>";
	}
	echo "</table>";

	}
		else if(isset($_GET['preds'])){
		echo "<table id='solo_table'>";
		if(mysqli_num_rows($usr_preds) != 0){
			echo "<tr ><td></td><td></td><td></td><td></td><td></td><td></td><td id='points_column' >Points</td></tr>";
			}
		while($row = mysqli_fetch_assoc($usr_preds)){
			echo "<tr>";
			echo"<td>" . date("d F Y", strtotime($row['match_date'])) . "</td>";
			echo "<td>" . $row['home_team'] . "</td>";
			echo "<td>" . $row['pred_home_score'] . "</td>";
			echo "<td> - </td>";
			echo "<td>" . $row['pred_away_score'] . "</td>";
			echo "<td>" . $row['away_team'] . "</td>";
			echo "<td name='game_score' class='points'>" . score_system($row['home_score'],$row['away_score'],$row['pred_home_score'],$row['pred_away_score']) . "</td>";
			echo "</tr>";
			echo "<tr id='row_break'>";
			echo"<td></td>";
			echo "<td class='pred_row'>Site Predictions</td>";
			echo "<td class='pred_row'>" . $row['phs'] . "</td>";
			echo "<td> - </td>";
			echo "<td class='pred_row'>" . $row['pas'] . "</td>";
			echo "<td></td>";
			echo "<td name='site_game_score' class='points'>" . score_system($row['home_score'],$row['away_score'],$row['phs'],$row['pas']) . "</td>";

			echo "</tr>";
	}
	echo "</table>";

	}
	else{
		echo "<table id='solo_table'>";
		if(mysqli_num_rows($usr_preds) != 0){
			echo "<tr ><td></td><td></td><td></td><td></td><td></td><td></td><td id='points_column' >Points</td></tr>";
			}
		while($row = mysqli_fetch_assoc($usr_preds)){
			echo "<tr id='row_break'>";
			echo"<td>" . date("d F Y", strtotime($row['match_date'])) . "</td>";
			echo "<td>" . $row['home_team'] . "</td>";
			echo "<td>" . $row['pred_home_score'] . "</td>";
			echo "<td> - </td>";
			echo "<td>" . $row['pred_away_score'] . "</td>";
			echo "<td>" . $row['away_team'] . "</td>";
			echo "<td name='game_score' class='points'>" . score_system($row['home_score'],$row['away_score'],$row['pred_home_score'],$row['pred_away_score']) . "</td>";
			echo "</tr>";
			echo "<tr style='display:none'><td name='site_game_score' class='points'>" . score_system($row['home_score'],$row['away_score'],$row['phs'],$row['pas']) . "</td></tr>";
	}
	echo "</table>";

	}

}
else{
	echo "<table id='solo_table'>";
	if(mysqli_num_rows($usr_preds) != 0){
		echo "<tr ><td></td><td></td><td></td><td></td><td></td><td></td><td id='points_column' >Points</td></tr>";
		}
	while($row = mysqli_fetch_assoc($usr_preds)){
		echo "<tr id='row_break'>";
		echo"<td>" . date("d F Y", strtotime($row['match_date'])) . "</td>";
		echo "<td>" . $row['home_team'] . "</td>";
		echo "<td>" . $row['pred_home_score'] . "</td>";
		echo "<td>" . $row['pred_away_score'] . "</td>";
		echo "<td>" . $row['away_team'] . "</td>";

		echo "<td name='game_score' class='points'>" . score_system($row['home_score'],$row['away_score'],$row['pred_home_score'],$row['pred_away_score']) . "</td>";
		echo "</tr>";
		echo "<tr style='display:none'><td name='site_game_score' class='points'>" . score_system($row['home_score'],$row['away_score'],$row['phs'],$row['pas']) . "</td></tr>";
	}
	echo "</table>";

	}
	echo "<script type='text/javascript'>overall_scores()</script>";
	// echo "<script type='text/javascript'>overall_score('user_score_container','game_score')</script>";
	
?>
