<?php
require_once "Q02_db.php";
$name = "%".($_GET["name"] ?? "")."%"; $category = "%".($_GET["category"] ?? "")."%";
$min = (float)($_GET["min"] ?? 0); $max = (float)($_GET["max"] ?? 999999);
$stmt = $conn->prepare("SELECT name,category,price FROM products WHERE name LIKE ? AND category LIKE ? AND price BETWEEN ? AND ?");
$stmt->bind_param("ssdd", $name, $category, $min, $max); $stmt->execute(); $rows=$stmt->get_result();
?>
<form><input name="name" placeholder="Name"><input name="category" placeholder="Category">
<input name="min" type="number" placeholder="Min price"><input name="max" type="number" placeholder="Max price"><button>Search</button></form>
<?php while($r=$rows->fetch_assoc()) echo htmlspecialchars($r["name"])." - ".htmlspecialchars($r["category"]??"")." - ".$r["price"]."<br>"; ?>
