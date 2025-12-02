def has_double_repeat(n):
    s = str(n)
    length = len(s)
    
    if length % 2 != 0:
        return False
    
    mid = length // 2
    return s[:mid] == s[mid:]


def find_double_repeats_in_range(start, end):
    return [num for num in range(start, end + 1) if has_double_repeat(num)]


def process_input(input_str):
    results = []
    parts = input_str.split(',')
    
    for part in parts:
        part = part.strip()
        if not part:
            continue
            
        if '-' in part:
            start, end = map(int, part.split('-'))
            results.extend(find_double_repeats_in_range(start, end))
        else:
            num = int(part)
            if has_double_repeat(num):
                results.append(num)
    return results


def main():
    with open(r"C:\Users\lukas.han\Downloads\input.txt", 'r') as f:
        input_data = f.read()
    
    repeats = process_input(input_data)
    
    print("Invalid IDs:")
    for num in repeats:
        print(num)
    
    print(f"Total sum: {sum(repeats)}")


if __name__ == "__main__":
    main()
