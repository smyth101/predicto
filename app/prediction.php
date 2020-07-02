<?php 
session_start();

if(!isset($_SESSION['user_ID'])){
    header("location:sign_in.php");

}
$con=mysqli_connect("localhost","root","","fixtures");
$con2 = mysqli_connect("localhost","root","","users");

$row_check = mysqli_query($con,"SELECT * FROM fixtures ORDER BY match_date LIMIT 1"  );
$first_m_date = mysqli_fetch_array($row_check);
$first_m_date = $first_m_date["match_date"];
$first_m_date = date('Y-m-d', strtotime($first_m_date. '5 days'));
$usr_ID = $_SESSION['user_ID'];

$query = "SELECT fixt.*, preds.* 
              FROM fixtures AS fixt
              LEFT JOIN users.user_predictions as preds ON ( fixt.LinkKey = preds.LinkKey ) WHERE user_ID = '$usr_ID' AND DATE(match_date) < '$first_m_date' ORDER BY match_date,fixt.fixture_ID";


$usr_preds = mysqli_query($con,$query);
$usr_pred_count = mysqli_num_rows($usr_preds);

if(!isset($_SESSION["pred_status"])){
    header("location:prediction.php");
}

if(isset($_GET["status"])){
    $_SESSION['pred_status'] = "change";
}

else{
    if($_SESSION['pred_status'] == "change"){
        $_SESSION['pred_status'] = "change";
        
        

    }
    elseif($usr_pred_count >= 1){
        $_SESSION['pred_status'] = "current";
}
    else{
        $_SESSION['pred_status'] = "new";
}
}



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
    <script src="functions.js?<?php echo time(); ?>"></script>
    <link rel="stylesheet" href="style_main.css?<?php echo time(); ?>" type='text/css'/>
    <link rel="stylesheet" href="style1.php" media="screen"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
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
    <div id="nav_bar"><ul id="nav_bar_content"><li><a href="index.php" class="nav_item">Home</a></li><li><a href="site_prediction.php" class="nav_item">Predictions</a></li><li> <a href="fixtures.php" class="nav_item">Fixtures</a> </li><li> <a href="results.php" class="nav_item">Results</a></li> <li><a class="nav_item" href="table.php"> Table</a></li><li><a  class="nav_item" href="prediction.php">My Predictions</a></li></ul></div></div>
 
        <div id="content_container">
        <h2><?= $_SESSION['username'] ?>'s Predictions</h2>
            <form method="post" action="prediction.php">
 <?php

// Check connection
if (mysqli_connect_errno())
{
echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $fixt_id = $_SESSION['fixt'];
    $home_score = $_POST['home_score_value'];
    $away_score = $_POST['away_score_value'];
    if(sizeof($fixt_id) == sizeof($home_score) && sizeof($home_score) == sizeof($away_score)){
        if($_SESSION['pred_status'] == "new"){
            $link_query = mysqli_query($con,"SELECT * FROM fixtures WHERE DATE(match_date) < '$first_m_date' ORDER BY match_date,fixture_ID" );
            $link_keys = array();
            while($item = mysqli_fetch_array($link_query)){
                array_push($link_keys,$item['LinkKey']);
            }
            $i = 0;
            while($i < sizeof($fixt_id)){
                $id = $_SESSION['user_ID'];
                $stmt = $con2->prepare("INSERT INTO user_predictions (user_ID,LinkKey,fixture_ID,pred_home_score,pred_away_score) VALUES (?, ?, ?,?,?)");
                $stmt->bind_param("sssss", $id, $link_keys[$i], $fixt_id[$i], $home_score[$i],$away_score[$i] );
                $stmt->execute();
                // $sql = "INSERT INTO user_predictions (user_ID,LinkKey,fixture_ID,pred_home_score,pred_away_score) VALUES($id,$first_Name,$fixt_id[$i],$home_score[$i],$away_score[$i])";
                // $con2->query($sql);
                $i++;
            $_SESSION['pred_status'] = "current";
            // header("location:prediction.php");
            }
        }
        elseif($_SESSION['pred_status'] == "change"){
            $i = 0;
            while($i < sizeof($fixt_id)){
                $id = $_SESSION['user_ID'];
                // $sql = "UPDATE user_predictions SET pred_home_score = $home_score[$i],pred_away_score = $away_score[$i] WHERE user_ID = $id AND fixture_ID = $fixt_id[$i]";
                // $con2->query($sql);

                $link_query = mysqli_query($con,"SELECT * FROM fixtures WHERE DATE(match_date) < '$first_m_date'ORDER BY match_date,fixture_ID" );
                $link_keys = array();
                while($item = mysqli_fetch_array($link_query)){
                    array_push($link_keys,$item['LinkKey']);
                }

 $stmt = $con2->prepare("INSERT INTO user_predictions (user_ID,LinkKey,fixture_ID,pred_home_score,pred_away_score) VALUES (?, ?, ?,?,?) ON DUPLICATE KEY UPDATE pred_home_score = values(pred_home_score),pred_away_score = values(pred_away_score)");
                $stmt->bind_param("sssss", $id, $link_keys[$i], $fixt_id[$i], $home_score[$i],$away_score[$i] );
                $stmt->execute();

                $i++;
            $_SESSION['pred_status'] = 'current';
            // header("location:prediction.php");
        }
    }   


}
}


// $row_check = mysqli_query($con,"SELECT * FROM fixtures ORDER BY match_date LIMIT 1"  );
// $first_m_date = mysqli_fetch_array($row_check);
// $first_m_date = $first_m_date["match_date"];
// $first_m_date = date('Y-m-d', strtotime($first_m_date. '5 days'));

// $row_check = mysqli_query($con,"SELECT * FROM fixtures ORDER BY fixture_ID DESC LIMIT 1"  );
// $first_fixt_id = mysqli_fetch_array($row_check);
// $first_fixt_id = $first_fixt_id[0];


// $usr_ID = $_SESSION['user_ID'];
// $usr_preds_check = mysqli_query($con2,"SELECT * FROM user_predictions WHERE fixture_ID = '$first_fixt_id' AND user_ID = '$usr_ID' ORDER BY fixture_ID DESC");
// $usr_pred_count = mysqli_num_rows($usr_preds_check);

$fixtures = mysqli_query($con,"SELECT * FROM fixtures WHERE DATE(match_date) < '$first_m_date'  ORDER BY match_date,fixture_ID" );

$query = "SELECT fixt.*, preds.* 
              FROM fixtures AS fixt
              LEFT JOIN users.user_predictions as preds ON ( fixt.LinkKey = preds.LinkKey ) WHERE user_ID = '$usr_ID' AND DATE(match_date) < '$first_m_date' ORDER BY match_date,fixt.fixture_ID";


$usr_preds = mysqli_query($con,$query);
$usr_pred_count = mysqli_num_rows($usr_preds);




echo "<table border='1' id='solo_table'>
<tr>
<th>Date</th>
<th>Home Team</th>
<th> Home Prediction</th>
<th>Away Team</th>
<th>Away Prediction</th>
</tr>";

$fixt_id = array();


while($row = mysqli_fetch_array($fixtures))
{
if($_SESSION['pred_status'] == "new" ){
echo "<tr id=".$row['fixture_ID'].">";
array_push($fixt_id,$row['fixture_ID']);
echo "<td>" . date("d F Y", strtotime($row['match_date'])) . "</td>";
echo "<td>" . $row['home_team'] . "</td>";
echo "<td><input type='number'value='0' min='0' name='home_score_value[]'/></td>";
echo "<td>" . $row['away_team'] . "</td>";
echo "<td><input type='number'value='0' min='0' name='away_score_value[]'/></td>";
}
elseif($_SESSION['pred_status'] == "change"){
 echo "<tr id=".$row['fixture_ID'].">";
array_push($fixt_id,$row['fixture_ID']);
echo "<td>" . date("d F Y", strtotime($row['match_date'])) . "</td>";
echo "<td>" . $row['home_team'] . "</td>";
$row_pred = mysqli_fetch_array($usr_preds);
if($row_pred['pred_home_score'] == ""){
    $row_pred['pred_home_score'] = 0;
    $row_pred['pred_away_score'] = 0;
}
echo "<td><input type='number' min='0' name='home_score_value[]' value='" . $row_pred['pred_home_score'] . "'/></td>";
echo "<td>" . $row['away_team'] . "</td>";
echo "<td><input type='number' min='0' name='away_score_value[]' value='" . $row_pred['pred_away_score'] . "'/></td>";   
}
else{
 echo "<tr id=".$row['fixture_ID'].">";
array_push($fixt_id,$row['fixture_ID']);
echo "<td>" . date("d F Y", strtotime($row['match_date'])) . "</td>";
echo "<td>" . $row['home_team'] . "</td>";
$row_pred = mysqli_fetch_array($usr_preds);
if("" == $row_pred['pred_home_score']){
echo "<td> - </td>";
echo "<td>" . $row['away_team'] . "</td>";
echo "<td> - </td>";
}
else{
echo "<td>" . $row_pred['pred_home_score'] . "</td>";
echo "<td>" . $row['away_team'] . "</td>";
echo "<td>" . $row_pred['pred_away_score'] . "</td>";
}   
}


}
$_SESSION['fixt'] = $fixt_id;
echo "</table>";

mysqli_close($con);

echo '<input type="submit" id="submit_'. $_SESSION['pred_status'] .'" />';
echo '</form>';
?>
<input type="button" onclick="status_changer()" value="Edit Predictions" id=<?= "change_".$_SESSION['pred_status']?>>

<br>
</div>
<div id="content_container">
<h2><?=$_SESSION['username']?>'s Past Predictions</h2> 
<?php
require('past_pred.php');
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