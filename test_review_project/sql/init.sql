-- 无索引、低效查询
SELECT * FROM users WHERE name = '$input';

-- 字段无注释
CREATE TABLE orders (
    id INT,
    user_id INT,
    amount FLOAT
);

-- 低效全表扫描
SELECT * FROM orders WHERE amount > 100;