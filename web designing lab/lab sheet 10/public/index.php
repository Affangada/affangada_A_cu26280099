<?php
require dirname(__DIR__).'/config/config.php';
require dirname(__DIR__).'/app/Core/Database.php';
require dirname(__DIR__).'/app/Models/Product.php';
require dirname(__DIR__).'/app/Controllers/ProductController.php';

$route = $_GET['r'] ?? 'products';
try {
    $controller = new ProductController();
    switch ($route) {
        case 'products': $controller->index(); break;
        case 'product': $controller->show(); break;
        default: http_response_code(404); require dirname(__DIR__).'/app/Views/404.php';
    }
} catch (Throwable $ex) {
    error_log($ex->getMessage());
    http_response_code(500); require dirname(__DIR__).'/app/Views/500.php';
}
?>