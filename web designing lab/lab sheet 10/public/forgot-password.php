<?php
require dirname(__DIR__).'/config/config.php';require dirname(__DIR__).'/app/Core/Database.php';
$msg='';
if($_SERVER['REQUEST_METHOD']==='POST'){
 csrf_check();$email=filter_var($_POST['email']??'',FILTER_VALIDATE_EMAIL);
 $s=Database::get()->prepare("SELECT id FROM users WHERE email=?");$s->execute([$email]);$u=$s->fetch();
 if($u){$token=bin2hex(random_bytes(32));$hash=hash('sha256',$token);
  Database::get()->prepare("UPDATE users SET reset_hash=?,reset_expires=DATE_ADD(NOW(),INTERVAL 30 MINUTE) WHERE id=?")->execute([$hash,$u['id']]);
  // In production email this link; do not display token to visitors.
  $msg='If the account exists, a reset link will be sent. (Lab token: '.$token.')';
 } else $msg='If the account exists, a reset link will be sent.';
} ?>
<h2>Forgot Password</h2><p><?=e($msg)?></p><form method="post">
<input type="hidden" name="csrf" value="<?=e(csrf_token())?>"><input name="email" type="email" required><button>Request reset</button></form>