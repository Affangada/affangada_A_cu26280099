<?php
session_start(); require_once "Q02_db.php";
$error = "";
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $email = trim($_POST["email"] ?? ""); $password = $_POST["password"] ?? "";
    $stmt = $conn->prepare("SELECT id,name,password FROM users WHERE email=?");
    $stmt->bind_param("s", $email); $stmt->execute();
    $user = $stmt->get_result()->fetch_assoc();
    if ($user && password_verify($password, $user["password"])) {
        session_regenerate_id(true); $_SESSION["user_id"] = $user["id"];
        $_SESSION["name"] = $user["name"]; header("Location: Q05_dashboard.php"); exit;
    }
    $error = "Invalid email or password.";
}
?>
<form method="post"><input name="email" type="email" required>
<input name="password" type="password" required><button>Login</button></form>
<p><?= htmlspecialchars($error) ?></p>
