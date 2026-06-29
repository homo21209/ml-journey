import csv

path = '/Users/mac/piton/src/cars.csv'
data = []

with open(path,newline='',encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)



def is_numeric_string(value):
    if not isinstance(value,str):
        return False

    try:
        float(value)
    except ValueError:
        return False
    return value    

def num_finder(data:dict)->list:
    num_keys = list()
    for key,value in data.items():
        if is_numeric_string(value) or isinstance(value,(int,float)) :
            num_keys.append(key)
    return num_keys

num_keys = num_finder(data[0])

sums = {key:0.0 for key in num_keys}
counts = {key:0 for key in num_keys}
max_val = {key:0 for key in num_keys}
min_val = {key:10**10 for key in num_keys}

for row in data:
    for key in num_keys:
        val = row.get(key)
        if float(val) > max_val[key]:
            max_val[key] = float(val)
            
        if float(val) < min_val[key]:
            min_val[key] = float(val)
            

        if row[key] is not None:
            sums[key] += float(val)
            counts[key] += 1

print(num_keys)

for key in num_keys:
    print(f'{key} минимум: {min_val[key]}, максимум:{max_val[key]}, среднее {sums[key]/counts[key]} ')


