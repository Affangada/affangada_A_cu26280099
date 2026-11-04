<?php require "00-db.php";if(empty($_SESSION["user_id"]))die("Login required.");
if(isset($_GET["add"]))$pdo->prepare("INSERT IGNORE INTO wishlist(user_id,book_id) VALUES(?,?)")->execute([$_SESSION["user_id"],(int)$_GET["add"]]);
$s=$pdo->prepare("SELECT books.* FROM wishlist JOIN books ON books.id=wishlist.book_id WHERE user_id=?");$s->execute([$_SESSION["user_id"]]);?>
<h1>My Wishlist</h1><?php foreach($s as $b):?><p><?=h($b["title"])?></p><?php endforeach;?>