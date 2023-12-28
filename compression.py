def compress(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        return "Error file not found"    

    frequency = {}
    for char in text:
        if char not in frequency:
            frequency[char] = 1
        else:
            frequency[char] += 1
    for char, freq in frequency.items():
        print(f"{char}: {freq}")

compress("test.txt")