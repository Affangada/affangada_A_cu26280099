MCA108P – LAB SHEET 10: PHP MVC + SECURITY + DEPLOYMENT
20 questions solved with compact working examples.

SETUP
1. Put this folder inside XAMPP htdocs (or configure the Apache VirtualHost).
2. Create database `lab10_app` and import database.sql.
3. Edit config/config.php for your MySQL username/password and app URL.
4. Run locally through Apache. For HTTPS, follow docs/apache-https-vhost.txt.
5. Composer packages for email: composer require phpmailer/phpmailer
6. Create an API token and store its SHA-256 hash in api_tokens (see docs/API-SETUP.txt).

FOLDER MAP
app/Models, app/Controllers, app/Views, config, public, storage/uploads,
storage/logs, docs, database.sql, .gitignore

SECURITY NOTES
- Examples demonstrate the requested lab concepts and use PDO prepared statements,
  password hashing, CSRF tokens, MIME checks and hashed API/reset tokens.
- HTTPS secure cookies require HTTPS. The local self-signed certificate is for testing.
- Configure SMTP credentials via environment variables; never commit secrets.
- Production apps also need rate limiting at the network edge, CSRF coverage on every
  state-changing form, email verification, audit logs, backups and deployment hardening.
