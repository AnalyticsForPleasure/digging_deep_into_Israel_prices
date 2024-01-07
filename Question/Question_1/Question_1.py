import numpy as np
import pandas as pd
# import dataframe_image as dfi
# import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines



if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/home/shay_diy/PycharmProjects/digging_deep_into_Israel_prices/Data/israel_prices.csv')
    df = df.replace(np.nan, '', regex=True)

    # In order to concanate the 2 column of the "Year" and "Month" we need to convert to string if needed
    df['Year'] = df['Year'].astype(str)
    df['Month'] = df['Month'].astype(str)

    # very important - # Combine 'Year' and 'Month' columns to create a datetime index
    df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(DAY=1))

    # In order to rearrange columns (move last column to the first position)
    df = df[[df.columns[-1]] + list(df.columns[:-1])]
    column_headers = list(df.columns.values)
    print("The Column Header :", column_headers)


    data = df.filter(regex='Cottage|Soft white|Date') # 'Soft white cheese (250 grams)', Cottage cheese' (250 grams)'
    data_before_presenting = data.loc[276:480, :]
    #data_before_presenting['Soft white cheese (250 grams)'] = data_before_presenting['Soft white cheese (250 grams)'].apply(lambda x: f"{x:.2f}")
    data_before_presenting.loc[:, 'Soft white cheese (250 grams)'] = data_before_presenting['Soft white cheese (250 grams)'].apply(lambda x: f"{x:.2f}")

    print('*')

    # Plotting the line chart
    plt.plot(data_before_presenting['Date'], data_before_presenting['Soft white cheese (250 grams)'] , label='Line Chart')
#
    # Adding labels and title
    plt.xlabel('Year')
    plt.ylabel('Price')
    plt.title('Simple Line Chart')

    # Adding a legend
    plt.legend()

    plt.show()


    # 'Milk substitutes for babies(400 grams)', 'Milk substitutes for babies (450 grams)', 'Milk substitutes for babies (700 grams)'
    # 'Margarine in a package (200 grams)'
    # 'Margarine for spreading in a cup (250 grams)', 'Margarine in a package (200 grams)'
    # 'Soft white cheese (250 grams)'
    # 'Cottage cheese (250 grams)'