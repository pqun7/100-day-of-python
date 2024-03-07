import json

# البيانات الأصلية في شكل JSON
json_data = '{"name": "John", "age": 30, "city": "New York"}'

# تحويل JSON إلى هيكل بيانات Python
data = json.loads(json_data)

# تحديث البيانات
data.update({"age": 31, "city": "San Francisco"})

# تحويل البيانات إلى JSON مرة أخرى
updated_json_data = json.dumps(data)

print(updated_json_data)