<?php require "00-db.php";if(empty($_SESSION["user_id"]))die("Please login.");
$s=$pdo->prepare("SELECT id,total,status,created_at FROM orders WHERE user_id=? ORDER BY id DESC");$s->execute([$_SESSION["user_id"]]);?>
<h1>My Orders</h1><?php foreach($s as $o):?><p>Order #<?=$o["id"]?> | ₹<?=$o["total"]?> | <?=h($o["status"])?> | <?=$o["created_at"]?></p><?php endforeach;?>