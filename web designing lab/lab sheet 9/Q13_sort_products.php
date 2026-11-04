<?php
require_once "Q02_db.php";
$allowed = ["name","category","price"]; $sort = $_GET["sort"] ?? "name";
$sort = in_array($sort,$allowed,true) ? $sort : "name";
$direction = strtoupper($_GET["dir"] ?? "ASC"); $direction = $direction==="DESC" ? "DESC" : "ASC";
$sql = "SELECT name,category,price FROM products ORDER BY $sort $direction";
$result = $conn->query($sql);
?>
<table border="1"><tr>
<?php foreach($allowed as $col): ?><th><a href="?sort=<?= $col ?>&dir=<?= $direction==='ASC'?'DESC':'ASC' ?>"><?= ucfirst($col) ?></a></th><?php endforeach; ?>
</tr><?php while($r=$result->fetch_assoc()): ?><tr>
<td><?= htmlspecialchars($r["name"]) ?></td><td><?= htmlspecialchars($r["category"]??"") ?></td><td><?= $r["price"] ?></td></tr><?php endwhile; ?></table>
