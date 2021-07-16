import json

with open('File.txt', 'w') as fl:
    fl.write("""{"name": "samsung", "price": 500, "quantity": 10}
{"name": "iphone", "price": 600, "quantity": 5}""")

with open('File.txt', 'r') as fl:
    final_file = []
    for item in fl:
        item = item.strip()[1:-1].replace('"', '').replace(':', '').replace(',', '').split()
        count = int(len(item) / 2)
        final_file.append({item[2 * i]: item[2 * i + 1] for i in range(count)})
    print(final_file)
total_price = (int(final_file[0]['price']) * int(final_file[0]['quantity']) +
               int(final_file[1]['price']) * int(final_file[1]['quantity']))

print(f"the total price is {total_price}")

with open("File1.json", "w") as json_file:
    json.dump(final_file, json_file, indent=2)
