<?php require "00-db.php";if(empty($_SESSION["user_id"]))die("Login to review.");
if($_SERVER["REQUEST_METHOD"]==="POST"){$rating=(int)$_POST["rating"];
 if($rating>=1 && $rating<=5)$pdo->prepare("INSERT INTO reviews(user_id,book_id,rating,comment) VALUES(?,?,?,?)")->execute([$_SESSION["user_id"],(int)$_POST["book_id"],$rating,trim($_POST["comment"])]);
}
$id=(int)($_GET["book_id"]??$_POST["book_id"]??0);$s=$pdo->prepare("SELECT rating,comment FROM reviews WHERE book_id=?");$s->execute([$id]);?>
<h2>Book Reviews</h2><?php foreach($s as $r):?><p><?=str_repeat("★",$r["rating"])?> <?=h($r["comment"])?></p><?php endforeach;?>