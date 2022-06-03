import pandas as pd

if __name__ == '__main__':
    pd.set_option("display.max_columns", None)
    shop_df = pd.read_excel('Shop_C2C_HN.xlsx', sheet_name='Report')
    print(f'len of shop_df: {shop_df.shape[0]}')

    ekyc_df = pd.read_csv('Result_69.csv')
    print(f'len of ekyc_df: {ekyc_df.shape[0]}')

    shop_info = pd.merge(shop_df, ekyc_df, on='ekyc_id', how='left')
    print(shop_info.head())
    print(f'len of shop_info: {shop_info.shape[0]}')
    shop_info.to_csv('shop_info.csv', sep=',', index=False, encoding='utf-8')