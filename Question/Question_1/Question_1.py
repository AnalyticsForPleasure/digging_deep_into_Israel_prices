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

    relavent_years = np.arange(2006, 2023, 2)

    filter_data_by_month= df.loc[df['Month'] == 1, :]
    filter_data_by_month_year = filter_data_by_month[filter_data_by_month['Year'].isin(relavent_years)]
    print('*')


    data = filter_data_by_month_year.filter(regex='Cottage|Soft white|Year') # 'Soft white cheese (250 grams)', Cottage cheese' (250 grams)'
    print('*')

    # Plotting the line chart
    x_values = list(data.loc[:,'Year'])
    y_values_white_cheese = list(data.loc[:,'Soft white cheese (250 grams)'])
    y_values_cottage = list(data.loc[:, "Cottage cheese' (250 grams)"])
    print('*')
    # First line :
    plt.subplot(1, 2, 1)
    #plt.style.use('fivethirtyeight')
    plt.plot(x_values, y_values_white_cheese , label='Soft white cheese ',linewidth=3.5 , color='navy' )
    plt.fill_between(x_values, y_values_white_cheese, color='skyblue', alpha=0.4, label='Filled Area')

    plt.title('Soft white cheese price over the years',fontname='Franklin Gothic Medium Cond', color= 'gray', fontsize=21)

    # Second line :

    plt.subplot(1, 2, 2)
    plt.plot(x_values,y_values_cottage , label='Cottage_cheese', linewidth=4 ,color='green')
    plt.fill_between(x_values, y_values_cottage, color='lightgreen', alpha=0.4, label='Filled Area')
    plt.title('Cottage cheese price over the years',fontname='Franklin Gothic Medium Cond', color= 'gray',fontsize=21)

    plt.tick_params(bottom=False, top=False,
                   left=False, right=False)

    # Remove the frame (spines) from the second subplot
    # plt[0,1].spines['top'].set_visible(False)
    # # ax2.spines['right'].set_visible(False)
    # # ax2.spines['bottom'].set_visible(False)
    # ax2.spines['left'].set_visible(False)

    # Adding labels and title

    plt.xlabel('Year')
    plt.ylabel('Price')
    plt.suptitle('Comparison between Cottage Cheese and Soft White Cheese as Substitute Products' ,fontsize=29,weight='bold',fontname='Franklin Gothic Medium Cond')


    # Adding a legend
    #plt.legend()

    plt.show()


    # 'Milk substitutes for babies(400 grams)', 'Milk substitutes for babies (450 grams)', 'Milk substitutes for babies (700 grams)'
    # 'Margarine in a package (200 grams)'
    # 'Margarine for spreading in a cup (250 grams)', 'Margarine in a package (200 grams)'
    # 'Soft white cheese (250 grams)'
    # 'Cottage cheese (250 grams)'