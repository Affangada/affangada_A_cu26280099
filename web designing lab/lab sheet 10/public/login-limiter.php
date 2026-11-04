<?php
require dirname(__DIR__).'/config/config.php';
require dirname(__DIR__).'/app/Core/Database.php';
$msg='';
if($_SERVER['REQUEST_METHOD']==='POST'){
 csrf_check();$email=filter_var($_POST['email']??'',FILTER_VALIDATE_EMAIL);
 $s=Database::get()->prepare("SELECT * FROM users WHERE email=?");$s->execute([$email]);$u=$s->fetch();
 if($u && $u['locked_until'] && strtotime($u['locked_until'])>time()) $msg='Account locked. Try later.';
 elseif($u && password_verify($_POST['password']??'',$u['password'])){
  Database::get()->prepare("UPDATE users SET failed_attempts=0,locked_until=NULL WHERE id=?")->execute([$u['id']]);
  session_regenerate_id(true);$_SESSION['user_id']=$u['id'];$msg='Login successful.';
 } elseif($u){
  $n=$u['failed_attempts']+1;$until=$n>=5?date('Y-m-d H:i:s',time()+900):null;
  Database::get()->prepare("UPDATE users SET failed_attempts=?,locked_until=? WHERE id=?")->execute([$n,$until,$u['id']]);
  $msg=$until?'Too many attempts. Locked for 15 minutes.':'Invalid login.';
 } else $msg='Invalid login.';
} ?>
<h2>Login with Attempt Limiter</h2><p><?=e($msg)?></p><form method="post">
<input type="hidden" name="csrf" value="<?=e(csrf_token())?>">
<input name="email" type="email" required><input name="password" type="password" required><button>Login</button></form>