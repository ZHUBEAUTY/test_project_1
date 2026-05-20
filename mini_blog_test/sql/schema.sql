-- 无主键、无索引（低效查询）
CREATE TABLE users (
    username TEXT,
    password TEXT
);

CREATE TABLE articles (
    title TEXT,
    content TEXT
);

-- 低效全表扫描
SELECT * FROM articles WHERE title LIKE '%test%';

-- 语法错误：少分号
INSERT INTO users (username) VALUES ('admin')