# 过度嵌套、低效循环 O(n²)
def find_duplicate_orders(orders):
    duplicates = []
    for o1 in orders:
        for o2 in orders:
            if o1["id"] == o2["id"] and o1 is not o2:
                duplicates.append(o1)
    return duplicates

# 除零风险、无类型提示
def calculate_avg_amount(orders):
    total = 0
    for o in orders:
        total += o["amount"]
    return total / len(orders)

# 重复代码、无注释
def create_order(data):
    if not data:
        return None
    sql = f"INSERT INTO orders (user_id, amount) VALUES ({data['user_id']}, {data['amount']})"
    from app.db import execute
    return execute(sql)

def update_order(data):
    if not data:
        return None
    sql = f"UPDATE orders SET amount={data['amount']} WHERE id={data['id']}"
    from app.db import execute
    return execute(sql)