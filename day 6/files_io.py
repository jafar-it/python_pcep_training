
with open('assignment.txt', 'r', encoding='utf-8') as f:
    #content = f.read()
    content = f.readlines()
    print(content[:5])