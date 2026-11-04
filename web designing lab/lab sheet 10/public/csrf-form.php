<?php require dirname(__DIR__).'/config/config.php';
if($_SERVER['REQUEST_METHOD']==='POST'){csrf_check();$message='Form token accepted.';} ?>
<h2>CSRF Protected Form</h2><p><?=e($message??'')?></p>
<form method="post"><input type="hidden" name="csrf" value="<?=e(csrf_token())?>">
<input name="comment" required><button>Submit</button></form>