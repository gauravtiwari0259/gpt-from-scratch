with open ('shakespear_dataset.txt', 'r' , encoding='utf-8') as f:
    text = f.read()

print(len(text))


chars = sorted(list(set(text)))
size = len(chars)
print(''.join(chars))
print(size)
