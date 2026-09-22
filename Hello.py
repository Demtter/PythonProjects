import re

text = input()

# Шаблон: 3 группы «цифры + точка» и одна финальная группа цифр
pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

ips = re.findall(pattern, text)

for ip in ips:
    print(ip)

