<?php
require_once "Q02_db.php";
$message = "";
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $name = trim($_POST["name"] ?? "");
    $email = trim($_POST["email"] ?? "");
    $password = $_POST["password"] ?? "";
    if ($name === "" || !filter_var($email, FILTER_VALIDATE_EMAIL) || strlen($password) < 6) {
        $message = "Enter valid details. Password must be 6 characters.";
    } else {
        $hash = password_hash($password, PASSWORD_DEFAULT);
        $stmt = $conn->prepare("INSERT INTO users(name,email,password) VALUES(?,?,?)");
        $stmt->bind_param("sss", $name, $email, $hash);
        $message = $stmt->execute() ? "Registration successful." : "Email may already exist.";
        $stmt->close();
    }
}
?>
<form method="post"><input name="name" placeholder="Name" required>
<input name="email" type="email" placeholder="Email" required>
<input name="password" type="password" required><button>Register</button></form>
<p><?= htmlspecialchars($message) ?></p>
