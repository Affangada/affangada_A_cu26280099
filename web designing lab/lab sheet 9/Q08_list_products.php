<?php
require_once "Q02_db.php";
$result = $conn->query("SELECT id,name,category,price FROM products ORDER BY id");
?>
<table border="1" cellpadding="8"><tr><th>ID</th><th>Name</th><th>Category</th><th>Price</th></tr>
<?php while($row = $result->fetch_assoc()): ?>
<tr><td><?= (int)$row["id"] ?></td><td><?= htmlspecialchars($row["name"]) ?></td>
<td><?= htmlspecialchars($row["category"] ?? "") ?></td><td><?= number_format($row["price"],2) ?></td></tr>
<?php endwhile; ?></table>
