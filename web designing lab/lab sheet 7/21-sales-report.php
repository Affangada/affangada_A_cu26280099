<?php require "00-db.php";if(($_SESSION["role"]??"")!=="admin")die("Admin access only.");
$totalOrders=$pdo->query("SELECT COUNT(*) FROM orders")->fetchColumn();
$revenue=$pdo->query("SELECT COALESCE(SUM(total),0) FROM orders")->fetchColumn();
$rows=$pdo->query("SELECT DATE(created_at) day,SUM(total) revenue FROM orders GROUP BY DATE(created_at) ORDER BY day DESC")->fetchAll();?>
<h1>Sales Summary</h1><p>Total orders: <?=$totalOrders?></p><p>Total revenue: ₹<?=$revenue?></p>
<h3>Daily sales</h3><?php foreach($rows as $r):?><p><?=h($r["day"])?> — ₹<?=$r["revenue"]?></p><?php endforeach;?>