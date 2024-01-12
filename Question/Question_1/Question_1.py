import numpy as np
import pandas as pd
# import dataframe_image as dfi
# import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import seaborn as sys



if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/home/shay_diy/PycharmProjects/digging_deep_into_Israel_prices/Data/israel_prices.csv')
    df = df.replace(np.nan, '', regex=True)

    plt.subplot(1, 2, 1)

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
    data_before_presenting.loc[:,'price'] = data_before_presenting['Soft white cheese (250 grams)'].apply(lambda x: f"{x:.2f}")
    data_before_presenting['price'] = pd.to_numeric(df['Soft white cheese (250 grams)'], errors='coerce')
    print('*')

    # Plotting the line chart
    x_values = data_before_presenting['Date']
    # First line :
    plt.subplot(1, 2, 1)
    #plt.style.use('fivethirtyeight')
    plt.plot(x_values, data_before_presenting['price'] , label='Soft white cheese ',linewidth=3.5 , color='navy' )
    plt.fill_between(x_values, data_before_presenting['price'], color='skyblue', alpha=0.4, label='Filled Area')

    plt.title('Soft white cheese price over the years',fontname='Franklin Gothic Medium Cond', color= 'gray', fontsize=21)

    # Second line :

    plt.subplot(1, 2, 2)
    plt.plot(x_values, data_before_presenting["Cottage cheese' (250 grams)"], label='Cottage_cheese', linewidth=4 ,color='green')
    plt.fill_between(x_values, data_before_presenting['price'], color='lightgreen', alpha=0.4, label='Filled Area')
    plt.title('Cottage cheese price over the years',fontname='Franklin Gothic Medium Cond', color= 'gray',fontsize=21)

    plt.tick_params(bottom=False, top=False,
                   left=False, right=False)

    # Remove the frame (spines) from the second subplot
    plt[0,1].spines['top'].set_visible(False)
    # ax2.spines['right'].set_visible(False)
    # ax2.spines['bottom'].set_visible(False)
    ax2.spines['left'].set_visible(False)

    # Adding labels and title

    plt.xlabel('Year')
    plt.ylabel('Price')
    plt.suptitle('Comparison between 2 alternative dairy products' ,fontsize=29,weight='bold',fontname='Franklin Gothic Medium Cond')


    # Adding a legend
    #plt.legend()

    plt.show()


    # 'Milk substitutes for babies(400 grams)', 'Milk substitutes for babies (450 grams)', 'Milk substitutes for babies (700 grams)'
    # 'Margarine in a package (200 grams)'
    # 'Margarine for spreading in a cup (250 grams)', 'Margarine in a package (200 grams)'
    # 'Soft white cheese (250 grams)'
    # 'Cottage cheese (250 grams)'