<?php require "00-db.php";$id=(int)($_GET["id"]??0);$qty=max(1,(int)($_GET["qty"]??1));
$s=$pdo->prepare("SELECT title,stock FROM books WHERE id=?");$s->execute([$id]);$b=$s->fetch();
if(!$b)echo "Book not found.";elseif($qty<=$b["stock"])echo "Stock available. You can add ".$qty." copies of ".h($b["title"]).".";
else echo "Only ".$b["stock"]." copies available."; ?>