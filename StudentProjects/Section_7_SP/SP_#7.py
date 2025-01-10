from datetime import datetime

dairy_items = []

while True:
    dairy = input("Enter your notes for today. Type 'exit' to save and exit: ")
    if dairy == 'exit':
        break
    dairy_items.append(dairy)


content = "\n".join(dairy_items)

day = datetime.now().strftime("%A")
filename = f'{day}.txt'
with open(filename, 'w') as file:
    file.write(content)

print(f"Your dairy for {day} has been saved as {filename}")  # <---