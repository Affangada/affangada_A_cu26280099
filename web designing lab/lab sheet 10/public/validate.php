<?php
$email=filter_var($_POST['email']??'',FILTER_VALIDATE_EMAIL);
$url=filter_var($_POST['url']??'',FILTER_VALIDATE_URL);
$age=filter_var($_POST['age']??'',FILTER_VALIDATE_INT);
$name=filter_var(trim($_POST['name']??''),FILTER_SANITIZE_SPECIAL_CHARS);
?><form method="post"><input name="email" placeholder="Email"><input name="url" placeholder="URL">
<input name="age" placeholder="Integer"><input name="name" placeholder="Name"><button>Validate</button></form>
<?php if($_SERVER['REQUEST_METHOD']==='POST'): ?>
<p>Email: <?=e($email ?: 'Invalid')?></p><p>URL: <?=e($url ?: 'Invalid')?></p>
<p>Integer: <?=e($age===false ? 'Invalid' : $age)?></p><p>Name: <?=$name?></p><?php endif;?>