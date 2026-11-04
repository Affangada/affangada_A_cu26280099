<?php
class Product {
    private PDO $db;
    public function __construct() { $this->db = Database::get(); }
    public function all(): array {
        return $this->db->query("SELECT * FROM products ORDER BY id DESC")->fetchAll();
    }
    public function find(int $id): ?array {
        $s=$this->db->prepare("SELECT * FROM products WHERE id=?");
        $s->execute([$id]); return $s->fetch() ?: null;
    }
    public function create(string $name, float $price): bool {
        return $this->db->prepare("INSERT INTO products(name,price) VALUES(?,?)")->execute([$name,$price]);
    }
    public function update(int $id,string $name,float $price): bool {
        return $this->db->prepare("UPDATE products SET name=?,price=? WHERE id=?")->execute([$name,$price,$id]);
    }
    public function delete(int $id): bool {
        return $this->db->prepare("DELETE FROM products WHERE id=?")->execute([$id]);
    }
}
?>