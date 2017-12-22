<?php
$connection = mysqli_connect('localhost','root','1234','user');

$option = isset($_POST['Style']) ? $_POST['Style'] : false;
if ($option) 
{
	$con="Insert into user.tmp SELECT * FROM user.music where";
	$s="";
	foreach ($option as $t)
	{
		$s=$s." style="."'".$t."'"." "."or";
	}
	mysqli_query($connection,"drop table if exists tmp");
	mysqli_query($connection,"CREATE TABLE `user`.`tmp` (`user_id` VARCHAR(45) NOT NULL,`song_id` VARCHAR(45) NULL,`song_titles` VARCHAR(45) NULL,`rating` VARCHAR(45) NULL,`style` VARCHAR(45) NULL,PRIMARY KEY (`user_id`));");
	$query=$con.$s;
	$query=substr($query,0,strlen($query)-3);
	mysqli_query($connection,$query);
	header('Location:recommendation.php');

} 
else 
{
     echo "task option is required";
     $message = "Please select something!";
     echo "<script type='text/javascript'>alert('$message');</script>";
     echo " <script type='text/javascript'>history.back();</script>";
     exit; 
}
?>