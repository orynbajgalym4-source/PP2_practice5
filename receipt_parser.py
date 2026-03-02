import re
import json

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

prices = re.findall(r'\d{1,3}(?: \d{3})*,\d{2}', text)

products = re.findall(r'\n\d+\.\n([^\n]+)', text)

m_total = re.search(r'ИТОГО:\n\s*(\d{1,3}(?: \d{3})*,\d{2})', text)
total = m_total.group(1) if m_total else None

m_dt = re.search(r'Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})', text)
date = m_dt.group(1) if m_dt else None
time = m_dt.group(2) if m_dt else None

m_pay = re.search(r'(Банковская карта)', text)
payment_method = m_pay.group(1) if m_pay else None

result = {
    "prices": prices,
    "products": products,
    "total": total,
    "date": date,
    "time": time,
    "payment_method": payment_method
}

print(json.dumps(result, ensure_ascii=False, indent=2))