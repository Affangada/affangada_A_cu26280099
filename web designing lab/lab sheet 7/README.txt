MCA108P – LAB SHEET 7: ONLINE BOOKSTORE
All 21 answers are included as short, practical programs.

SETUP
1. Install XAMPP and start Apache + MySQL.
2. Copy this folder into htdocs.
3. Open phpMyAdmin and import 02-database.sql.
4. Edit database credentials in 00-db.php if needed.
5. Open http://localhost/MCA108P_AS07_Solutions/01-homepage.html

NOTES
- PHP files use PDO prepared statements.
- Register a user using 05-auth.php? (Use the form in that file.)
- For admin features, create an admin user manually by setting users.role='admin'
  in phpMyAdmin after registering.
- These are compact lab-sheet examples; for a real store, add CSRF protection,
  payment-gateway verification, stronger authorization and production error handling.
