<?php
require_once "Q02_db.php";
$email = $_GET["email"] ?? "";
// Vulnerable example - never use this:
$vulnerable = "SELECT * FROM users WHERE email='$email'";
// Secure prepared statement:
$stmt = $conn->prepare("SELECT id,name,email FROM users WHERE email=?");
$stmt->bind_param("s", $email); $stmt->execute();
$result = $stmt->get_result();
echo "Secure query returned ".$result->num_rows." record(s).";
?>
