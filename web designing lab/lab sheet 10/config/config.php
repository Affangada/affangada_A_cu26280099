<?php
define('DB_HOST', 'localhost');
define('DB_NAME', 'lab10_app');
define('DB_USER', 'lab10_user'); // use the limited user created in Q20
define('DB_PASS', 'change_this_password');
define('APP_URL', 'http://localhost/MCA108P_AS10_Solutions/public');
define('UPLOAD_DIR', dirname(__DIR__) . '/storage/uploads/');
define('LOG_FILE', dirname(__DIR__) . '/storage/logs/app.log');

$isHttps = !empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off';
if (session_status() === PHP_SESSION_NONE) {
    session_set_cookie_params([
        'httponly' => true, 'secure' => $isHttps, 'samesite' => 'Lax',
        'path' => '/'
    ]);
    session_start();
}
ini_set('display_errors', '0');
ini_set('log_errors', '1');
ini_set('error_log', LOG_FILE);

function e($value) {
    return htmlspecialchars((string)$value, ENT_QUOTES, 'UTF-8');
}
function csrf_token() {
    if (empty($_SESSION['csrf'])) $_SESSION['csrf'] = bin2hex(random_bytes(32));
    return $_SESSION['csrf'];
}
function csrf_check() {
    $token = $_POST['csrf'] ?? '';
    if (!is_string($token) || !hash_equals($_SESSION['csrf'] ?? '', $token)) {
        http_response_code(419); exit('Invalid CSRF token');
    }
}
?>