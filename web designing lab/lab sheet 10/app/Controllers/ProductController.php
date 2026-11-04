<?php
class ProductController {
    public function index() {
        $products=(new Product())->all();
        require dirname(__DIR__).'/Views/products.php';
    }
    public function show() {
        $p=(new Product())->find((int)($_GET['id'] ?? 0));
        if (!$p) { http_response_code(404); require dirname(__DIR__).'/Views/404.php'; return; }
        require dirname(__DIR__).'/Views/product.php';
    }
}
?>