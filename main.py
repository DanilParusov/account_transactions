import json

with open("operations.json", 'r', encoding='utf-8') as f:
    data = json.load(f)


def last_operations():
    operations = sorted(data, key=lambda x: x['date'], reverse=True)[:5]
    return operations


def print_operations():
    for operation in last_operations():
        date = operation['date'][:10]
        description = operation['description']
        from_value = operation.get('from', '')
        to_value = operation.get('to', '')
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']

        masked_from = mask_number(from_value)
        masked_to = mask_number(to_value)

        print(f"{date} {description}")
        print(f"{masked_from} -> {masked_to}")
        print(f"{amount} {currency}")
        print()


def mask_number(number):
    if number.startswith('Счет'):
        return f"Счет **{number[-4:]}"
    elif number.startswith('Visa'):
        return mask_visa_number(number)
    elif number.startswith('Maestro'):
        return mask_maestro_number(number)


def mask_maestro_number(number):
    number = number.split()
    maestro_card = " ".join(number[:1])
    card_number = number[1]
    parts = [card_number[i:i + 4] for i in range(0, len(card_number), 4)]
    parts[2] = "****"
    result = " ".join(parts)
    return f"{maestro_card} {result}"


def mask_visa_number(number):
    number = number.split()
    visa_card = " ".join(number[:2])
    card_number = number[2]
    parts = [card_number[i:i + 4] for i in range(0, len(card_number), 4)]
    parts[2] = "****"
    result = " ".join(parts)
    return f"{visa_card} {result}"


print_operations()