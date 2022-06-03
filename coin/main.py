import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

if __name__ == '__main__':
    pd.set_option("display.max_columns", None)
    coin_data = pd.read_csv('coin_Aave.csv')
    print(coin_data.head())

    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    ax.plot(coin_data['Date'], coin_data['Volume'])
