<?php
include 'initialize.php';
$connection = mysqli_connect('localhost','root','1234','user');
?>
<!doctype html>
<html lang="en">
 <head>
  <meta charset="UTF-8">
  <meta name="Generator" content="EditPlus®">
  <meta name="Author" content="">
  <meta name="Keywords" content="">
  <meta name="Description" content="">
  <title>Music Preference</title>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">

  <style>
  body{
  margin-left:auto;
  margin-right:auto;
  margin-TOP:100PX;
  width:20em;
  }
  </style>

 </head>

 <body>

 <h1 style="font-size:80PX;">Music Preference</h1>
 <br>
 <h5 style="text-align:center">Jingyi Qian<br> Qianqian Zhang<br> Lixujing Pei</h5>
 <br>
  <div class="input-group">
  
  <form action = "lgi.php" method="post">
  <span class="input-group-addon" id="basic-addon1">@</span>
  <input id="userName" name = "userName" style="width:320px" type="text"  placeholder="Username" aria-describedby="basic-addon1">
  <br>
  <span class="input-group-addon" id="basic-addon1">@</span>
  <input id="passWord" name = "passWord" style="width:320px" type="password"  placeholder="Password" aria-describedby="basic-addon1">
  <br>
  <input type="submit" value = "Login" style="width:320px">
  </form>
</div>

<button type="button" style="width:320px"  onclick="Trans()">Sign Up</button>

<script>
function Trans()
{
	window.location.assign("./Signup.php");
}
</script>

 </body>
</html>
