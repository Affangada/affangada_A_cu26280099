<?php require "00-db.php";if(empty($_SESSION["user_id"]))die("Login required.");
$id=(int)($_GET["id"]??0);$s=$pdo->prepare("SELECT * FROM orders WHERE id=? AND user_id=?");$s->execute([$id,$_SESSION["user_id"]]);$o=$s->fetch();if(!$o)die("Invoice not found.");?>
<h1>BookNest – Invoice</h1><p>Invoice No: <?=$o["id"]?></p><p>Date: <?=$o["created_at"]?></p>
<p>Shipping: <?=h($o["shipping_address"])?></p><p>Total: ₹<?=$o["total"]?></p><p>Status: <?=h($o["status"])?></p>
<button onclick="window.print()">Print Invoice</button>