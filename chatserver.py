import csv
import json

# 定義 CSV 檔案和 JSON 檔案的路徑
csv_file_path = 'data.csv'
json_file_path = 'data.json'

# 讀取 CSV 檔案
with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = [row for row in csv_reader]

# 將資料寫入 JSON 檔案
with open(json_file_path, mode='w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print(f"CSV 檔案已成功轉換為 JSON 檔案：{json_file_path}")