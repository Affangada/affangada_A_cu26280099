<?php
require_once "Q02_db.php";
$perPage = 5; $page = max(1, (int)($_GET["page"] ?? 1)); $offset = ($page-1)*$perPage;
$total = $conn->query("SELECT COUNT(*) AS total FROM products")->fetch_assoc()["total"];
$stmt = $conn->prepare("SELECT id,name,price FROM products LIMIT ? OFFSET ?");
$stmt->bind_param("ii", $perPage, $offset); $stmt->execute(); $rows = $stmt->get_result();
while($r=$rows->fetch_assoc()) echo htmlspecialchars($r["name"])." - ₹".htmlspecialchars((string)$r["price"])."<br>";
$pages = max(1, (int)ceil($total/$perPage));
for($p=1;$p<=$pages;$p++) echo '<a href="?page='.$p.'">'.$p.'</a> ';
if($page>1) echo '<a href="?page='.($page-1).'">Previous</a> ';
if($page<$pages) echo '<a href="?page='.($page+1).'">Next</a>';
?>
