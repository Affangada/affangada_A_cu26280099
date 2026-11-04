<?php require "00-db.php"; $msg="";
if($_SERVER["REQUEST_METHOD"]==="POST"){
 if(isset($_POST["register"])){
  $s=$pdo->prepare("INSERT INTO users(name,email,password) VALUES(?,?,?)");
  try{$s->execute([trim($_POST["name"]),trim($_POST["email"]),password_hash($_POST["password"],PASSWORD_DEFAULT)]);$msg="Registered. Please log in.";}
  catch(PDOException $e){$msg="Email may already be registered.";}
 } else {
  $s=$pdo->prepare("SELECT * FROM users WHERE email=?");$s->execute([trim($_POST["email"])]);
  $u=$s->fetch();
  if($u && password_verify($_POST["password"],$u["password"])){
   session_regenerate_id(true);$_SESSION["user_id"]=$u["id"];$_SESSION["role"]=$u["role"];$msg="Login successful.";
  } else $msg="Invalid email or password.";
 }
}
?><h2>Register / Login</h2><p><?=h($msg)?></p>
<form method="post"><h3>Register</h3><input name="name" placeholder="Name" required>
<input type="email" name="email" placeholder="Email" required><input type="password" name="password" required>
<button name="register">Register</button></form>
<form method="post"><h3>Login</h3><input type="email" name="email" required>
<input type="password" name="password" required><button>Login</button></form>
<a href="logout.php">Logout</a>