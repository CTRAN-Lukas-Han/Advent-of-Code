import pandas as pd

def process_to_dataframe(file_path, start=50):
    current = start
    data = []
    click = 0
    pre_val = start

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            value = int(line[1:])
            
            if value >= 100:
                click = click + (value // 100) 
                value = value % 100
                
            if direction == 'L':
                current -= value
            elif direction == 'R':
                current += value

            if current < 0:
                if pre_val != 0:
                    click = click + 1   
                current += 100
            if current == 0:
                click = click + 1                
            elif current >= 100:
                current -= 100  
                click = click + 1                            

            data.append({'origin': line, 'result': current, 'click': click})
            pre_val = current

    return pd.DataFrame(data)

df = process_to_dataframe("input.txt")
print(df)

zero_count = (df['result'] == 0).sum()
max_value = df['click'].max()

print(f"\n num of zero: {zero_count}")
print(f"\n num of clicks: {max_value}")
