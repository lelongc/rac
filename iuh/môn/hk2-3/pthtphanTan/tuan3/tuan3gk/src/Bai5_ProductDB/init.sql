USE productdb;

DROP TABLE IF EXISTS products;

CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    price DOUBLE,
    description TEXT
);

INSERT INTO products (name, price, description) VALUES 
('Laptop Dell XPS', 1500.0, 'High-end laptop'),
('iPhone 15 Pro', 1200.0, 'Apple smartphone'),
('Samsung Monitor', 300.0, '4K UHD Monitor'),
('Logitech Mouse', 50.0, 'Wireless gaming mouse'),
('Sony Headphones', 200.0, 'Noise cancelling headphones');
