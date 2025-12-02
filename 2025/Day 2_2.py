def has_repeat_pattern(n):
    s = str(n)
    length = len(s)
    
    for repeat_count in range(2, length + 1):
        if length % repeat_count == 0:
            pattern_length = length // repeat_count
            pattern = s[:pattern_length]
            
            if pattern * repeat_count == s:
                return True
    
    return False


def find_repeats_in_range(start, end):
    return [num for num in range(start, end + 1) if has_repeat_pattern(num)]


def process_input(input_str):
    results = []
    parts = input_str.split(',')
    
    for part in parts:
        part = part.strip()
        if not part:
            continue
            
        if '-' in part:
            start, end = map(int, part.split('-'))
            results.extend(find_repeats_in_range(start, end))
        else:
            num = int(part)
            if has_repeat_pattern(num):
                results.append(num)
    
    return results


def main():
    with open("input.txt", 'r') as f:
        input_data = f.read()
    
    repeats = process_input(input_data)
    
    print("Invalid IDs:")
    for num in repeats:
        print(num)
    
    print(f"Total sum: {sum(repeats)}")


if __name__ == "__main__":
    main()
