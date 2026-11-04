<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $email = trim($_POST["email"] ?? "");
    if (!empty($_POST["remember"]) && filter_var($email,FILTER_VALIDATE_EMAIL)) {
        setcookie("remember_email",$email, time()+30*24*60*60, "/", "", false, true);
    } else {
        setcookie("remember_email","",time()-3600,"/");
    }
}
$remembered = htmlspecialchars($_COOKIE["remember_email"] ?? "", ENT_QUOTES, "UTF-8");
?>
<form method="post"><input name="email" type="email" value="<?= $remembered ?>" required>
<label><input type="checkbox" name="remember"> Remember Me</label><button>Save</button></form>
<?php if($remembered): ?><p>Welcome back, <?= $remembered ?>!</p><?php endif; ?>
