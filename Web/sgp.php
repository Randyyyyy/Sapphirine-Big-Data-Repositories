<?php
$connection = mysqli_connect('localhost','root','1234','user');
$username = $_POST['userName'];
$pw_1 = $_POST['pw_1'];
$pw_2 = $_POST['pw_2'];
$r = mysqli_num_rows(mysqli_query($connection,"select user_id from `user_account` where `user_id`='$username';"));

if(empty($_POST['userName']) == true||empty($_POST['pw_1']) == true||empty($_POST['pw_2']) == true)
{
	$message = "Username and password can not be blank!";
	echo "<script type='text/javascript'>alert('$message');</script>";
	echo " <script type='text/javascript'>history.back();</script>";
}
else if($pw_1!=$pw_2)
{
	$message = "Different Password!";
	echo "<script type='text/javascript'>alert('$message');</script>";
	echo " <script type='text/javascript'>history.back();</script>";
}
else if(r!=0)
{
	$message = "Username exist!";
	echo "<script type='text/javascript'>alert('$message');</script>";
	echo " <script type='text/javascript'>history.back();</script>";
}
else
{
	mysqli_query($connection,"insert into `user_account` (`user_id`,`password`) values ('$username','$pw_1')");

	$message = "Sign Up Successed!";
	echo "<script type='text/javascript'>alert('$message');</script>";
	
	header('Location:login.php');
}
mysqli_free_result($result);

?>