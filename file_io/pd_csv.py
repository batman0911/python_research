import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('Result_59.csv')
    df['root_id'] = None
    print(df.head())

    df = df.reset_index()
    df.iloc[0]['root_id'] = df.iloc[0]['id']
    for i in range(10):
        prev = df.iloc[i]
        curr = df.iloc[i + 1]

        print(curr['card_id'], curr['id'])
        if curr['card_id'] == prev['card_id']:
            tmp = prev['card_id']
            curr['root_id'] = tmp
        else:
            tmp = curr['id']
            curr['root_id'] = tmp

    df.head()

