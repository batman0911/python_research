import csv
import pandas as pd

if __name__ == '__main__':
    pd.set_option("display.max_columns", None)

    file = open('ref_ekyc.csv')
    type(file)
    csvreader = csv.reader(file)
    header = next(csvreader)

    content = []
    for row in csvreader:
        content.append(row)

    print(len(content))

    ref = content[0][2]
    content[0].append(ref)
    for i in range(len(content) - 1):
        prev = content[i]
        curr = content[i + 1]
        if curr[0] == prev[0]:
            curr.append(prev[5])
        else:
            curr.append(curr[2])

    df = pd.DataFrame(content, columns=['card_id', 'card_type', 'ekyc_id', 'iam_client_id', 'status', 'root_ekyc_id'])
    ref_ekyc_table = df[['ekyc_id', 'root_ekyc_id']]

    print(ref_ekyc_table.head())

    ref_ekyc_table.to_csv('ref_ekyc_table.csv', sep=',', index=False)
