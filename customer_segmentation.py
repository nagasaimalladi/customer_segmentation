import json
import csv

def calculate_segment(amount):
    if amount < 100:
        return 'Low'
    elif 100 <= amount <= 500:
        return 'Medium'
    else:
        return 'High'

def process_data(input_file, output_file):
    with open(input_file) as f:
        data = json.load(f)

    segmented_data = []
    for customer in data:
        customer_id = customer['customer_id']
        name = customer['name']
        email = customer['email']
        purchase_amount = customer['purchase_amount']
        segment = calculate_segment(purchase_amount)
        segmented_data.append([customer_id, name, email, purchase_amount, segment])

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['customer_id', 'name', 'email', 'purchase_amount', 'segment'])
        writer.writerows(segmented_data)

    return segmented_data


if __name__ == '__main__':
    # The paths of your input and output files
    input_file = 'input_file.json'
    output_file = 'output_file.csv'

    # Call the process_data() function with the input and output file paths
    segmented_data = process_data(input_file, output_file)