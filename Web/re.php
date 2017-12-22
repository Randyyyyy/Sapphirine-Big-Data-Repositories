<?php
$connection = mysqli_connect('localhost','root','1234','user');
$rate_1=isset($_POST['Rating_1']) ? $_POST['Rating_1'] : false;
$rate_2=isset($_POST['Rating_2']) ? $_POST['Rating_2'] : false;
$rate_3=isset($_POST['Rating_3']) ? $_POST['Rating_3'] : false;
$s1=$_POST['song1'];
$s2=$_POST['song2'];
$s3=$_POST['song3'];

if($rate_1!=false)
{
	$music_1=mysqli_fetch_assoc(mysqli_query($connection,"Select `song_id`,`song_titles`,`style` from (Select `song_id`,`song_titles`,`style` from `tmp` where `song_titles` = '$s1[1]') as a limit 1"));
	$music_2=mysqli_fetch_assoc(mysqli_query($connection,"Select `song_id`,`song_titles`,`style` from (Select `song_id`,`song_titles`,`style` from `tmp` where `song_titles` = '$s2[1]') as b limit 1"));
	$music_3=mysqli_fetch_assoc(mysqli_query($connection,"Select `song_id`,`song_titles`,`style` from (Select `song_id`,`song_titles`,`style` from `tmp` where `song_titles` = '$s3[1]') as c limit 1"));
	$user = mysqli_fetch_assoc(mysqli_query($connection,"Select `user` from `cur_user`"));

	$u = $user['user'];

	$id_1 = $music_1[`song_id`];
	$title_1 = $music_1[`song_titles`];
	$style_1 = $music_1[`style`];
	$id_2 = $music_2[`song_id`];
	$title_2 =$music_2[`song_titles`];
	$style_2 = $music_2[`style`];
	$id_3 = $music_3[`song_id`];
	$title_3 = $music_3[`song_titles`];
	$style_3 = $music_3[`style`];
	mysqli_query($connection,"insert into `user`.`music` (`user_id`,`song_id`,`song_title`,`rating`,`style`) values ('$u','$id_1','$title_1','$rate_1','$style_1')");
	mysqli_query($connection,"insert into `user`.`music` (`user_id`,`song_id`,`song_title`,`rating`,`style`) values ('$u','$id_2','$title_2','$rate_2','$style_2')");
	mysqli_query($connection,"insert into `user`.`music` (`user_id`,`song_id`,`song_title`,`rating`,`style`) values ('$u','$id_3','$title_3','$rate_3','$style_3')");
	header('Location:recommendation.php');
}
?>