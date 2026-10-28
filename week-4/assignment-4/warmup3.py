# week-4/assignment-4
# Warmup 3: Set Operations

data_eng_lang = ["python", "sql", "java", "go"]
web_dev_lang = ["javascript", "python", "php", "ruby"]

data_eng_lang = set(data_eng_lang)
web_dev_lang = set(web_dev_lang)

print(data_eng_lang.union(web_dev_lang))
print(data_eng_lang.intersection(web_dev_lang))
print(data_eng_lang.difference(web_dev_lang))
