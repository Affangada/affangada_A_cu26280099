<?php
require dirname(__DIR__).'/config/config.php';require dirname(__DIR__).'/app/Core/Database.php';
$msg='';
if($_SERVER['REQUEST_METHOD']==='POST'){
 csrf_check();$token=$_POST['token']??'';$hash=hash('sha256',$token);
 $s=Database::get()->prepare("SELECT id FROM users WHERE reset_hash=? AND reset_expires>NOW()");
 $s->execute([$hash]);$u=$s->fetch();
 if($u && strlen($_POST['password']??'')>=8){
  Database::get()->prepare("UPDATE users SET password=?,reset_hash=NULL,reset_expires=NULL WHERE id=?")
   ->execute([password_hash($_POST['password'],PASSWORD_DEFAULT),$u['id']]);$msg='Password updated.';
 } else $msg='Invalid/expired token or weak password.';
} ?>
<h2>Reset Password</h2><p><?=e($msg)?></p><form method="post">
<input type="hidden" name="csrf" value="<?=e(csrf_token())?>"><input name="token" required>
<input type="password" name="password" minlength="8" required><button>Reset</button></form>