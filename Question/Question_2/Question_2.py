import numpy as np
import pandas as pd
# import dataframe_image as dfi
# import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

#https://cduvallet.github.io/posts/2018/03/slopegraphs-in-python

def preparing_the_data(df):
    relavent_years = np.arange(1990, 2021, 5)

    filter_data_by_month= df.loc[df['Month'] == 1, :]
    filter_data_by_month_year = filter_data_by_month[filter_data_by_month['Year'].isin(relavent_years)]

    relevant_items = ['Chicken Breast (1 kg)',
                      'bananas (1 kg)',
                      'lemons (1 kg)',
                      'Avocado (1 kg)',
                      'Apples - Granny Smith (1 kg)',
                      'Potatoes (1 kg)']

    column_indices = [df.columns.get_loc(col) for col in relevant_items]
    full_relevant_data = filter_data_by_month_year.iloc[:, column_indices]
    full_relevant_data = pd.DataFrame(full_relevant_data).set_index([relavent_years])
    print('*')
    full_relevant_data = full_relevant_data.reset_index()
    full_relevant_df =full_relevant_data.rename(columns={full_relevant_data.columns[0]: 'Year'},inplace=True)
    print('*')

    return full_relevant_data


def creating_the_line_chart(final_data ,my_list_colors):


    years = list(final_data.loc[:,'Year']) # 'years=x_values' line represents X- axis values
    chicken_breast = list(pd.to_numeric(final_data.loc[:,'Chicken Breast (1 kg)']))
    bananas = list(pd.to_numeric(final_data.loc[:,'bananas (1 kg)']))
    #lemons = list(pd.to_numeric(final_data.loc[:, 'lemons (1 kg)']))
    avocado = list(pd.to_numeric(final_data.loc[:, 'Avocado (1 kg)']))
    # apples = list(final_data.iloc[:, 'Apples - Granny Smith (1 kg)'])

    list_items = [chicken_breast ,bananas,avocado ]#,apples] ,lemons,
    print('*')
    # plt.style.use('seaborn')  # this time we add this labrary
    for specific_item,specific_color in zip( list_items,my_list_colors):
        plt.plot(years,
                 specific_item,
                 color=specific_color,
                 linestyle='-',
                 linewidth=1,
                 marker='o',
                 markersize=10,
                 label='Alice')

    plt.title('Prices of six items over the years')
    plt.xlabel('Years')
    plt.ylabel('Price')
    # plt.legend()
    plt.show()


if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/home/shay_diy/PycharmProjects/digging_deep_into_Israel_prices/Data/israel_prices.csv')
    df = df.replace(np.nan, '', regex=True)

    column_headers = list(df.columns.values)
    print("The Column Header :", column_headers)

    list_of_colors = ['Green', 'Blue' , 'lightblue']#, 'lightgreen' ] ,'Navy',
    # #1) What are the top 5 items that experienced a more significant decrease in prices compared to increases during the 90s and 2000s?
    #
    res = preparing_the_data(df)
    creating_the_line_chart(res,list_of_colors)
    print('*')
