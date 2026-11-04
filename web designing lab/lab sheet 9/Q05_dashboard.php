<?php
session_start();
if (!isset($_SESSION["user_id"])) { header("Location: Q04_login.php"); exit; }
?>
<h2>Welcome, <?= htmlspecialchars($_SESSION["name"]) ?></h2>
<a href="Q06_logout.php">Logout</a>
