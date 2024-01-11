import numpy as np
import pandas as pd
import seaborn as sns
# import dataframe_image as dfi
# import numpy as np
import matplotlib.pyplot as plt
import style


def preparing_the_data(df):
    relavent_years = np.arange(1990, 2021, 5)

    filter_data_by_month= df.loc[df['Month'] == 1, :]
    filter_data_by_month_year = filter_data_by_month[filter_data_by_month['Year'].isin(relavent_years)]

    relevant_items = ['Chicken Breast (1 kg)',
                      'Instant coffee (200 grams)',
                      'lemons (1 kg)',
                      #'Avocado (1 kg)',
                      #'Apples - Granny Smith (1 kg)',
                      #'Fresh beef for steak - shoulder (1 kg)',
                      'Frozen beef - ribs (1 kg)']# Fresh # Potatoes

    column_indices = [df.columns.get_loc(col) for col in relevant_items]
    full_relevant_data = filter_data_by_month_year.iloc[:, column_indices]
    full_relevant_data = pd.DataFrame(full_relevant_data).set_index([relavent_years])
    print('*')
    full_relevant_data = full_relevant_data.reset_index()
    full_relevant_df =full_relevant_data.rename(columns={full_relevant_data.columns[0]: 'Year'},inplace=True)
    print('*')

    return full_relevant_data


def creating_the_line_chart(final_data ,my_list_colors):
    plt.style.available
    plt.style.use('fivethirtyeight')
    #plt.style.use('Solarize_Light2')
    #plt.style.use('seaborn-dark')

    fig, ax = plt.subplots(figsize=(18, 9))
    d_slope = list(pd.to_numeric(final_data.loc[0, :]))
    #d_slope = [15.3 ,2.8 ,2.3, 3.3 , 3 ,15]#final_data.loc[0,:]
    print('*')

    years = list(final_data.loc[:,'Year']) # 'years=x_values' line represents X- axis values
    chicken_breast = list(pd.to_numeric(final_data.loc[:,'Chicken Breast (1 kg)']))
    coffee = list(pd.to_numeric(final_data.loc[:,'Instant coffee (200 grams)']))
    lemons = list(pd.to_numeric(final_data.loc[:, 'lemons (1 kg)']))
    #avocado = list(pd.to_numeric(final_data.loc[:,Fresh beef for steak - shoulder (1 kg)]))
    frozenbeef = list(pd.to_numeric(final_data.loc[:, 'Frozen beef - ribs (1 kg)']))

    #apples = list(final_data.iloc[:, 'Apples - Granny Smith (1 kg)'])

    list_items = [chicken_breast ,coffee,lemons,frozenbeef ]#,apples] ,lemons, avocado
    #print('*')

    for specific_item,specific_color in zip( list_items,my_list_colors):
        plt.plot(years,
                 specific_item,
                 color=specific_color,
                 linestyle='-',
                 linewidth=2.5,
                 marker='o', # (5, 0)
                 markersize=14,
                 label='Alice')

        # Display values on the data points
        for year, value in zip(years, specific_item):
            plt.text(year, value+1, f'{value:.1f}', ha='left', va='bottom', fontsize=10,weight='bold' )

    ax.tick_params(bottom=False, top=False,
                   left=False, right=False)


    for key, spine in ax.spines.items():
        spine.set_visible(False)

    plt.text(1990+1, d_slope[1]+1.5, "Chicken Breast", rotation=19,fontname='Franklin Gothic Medium Cond') #Frozen beef
    plt.text(1990+3, d_slope[2] + 6, "Coffee", rotation=25,fontname='Franklin Gothic Medium Cond')
    plt.text(1990+1, d_slope[3]+0.5, "Lemons", rotation=6,fontname='Franklin Gothic Medium Cond')
    # plt.text(1990, d_slope[3], "Potatoes", rotation=45)
    #plt.text(1990+2, d_slope[4]+1, "Avocado", rotation=28.5)
    #plt.text(1990+1, d_slope[5]+1.5, "Chicken Breast", rotation=19,fontname='Franklin Gothic Medium Cond')
    plt.text(1990 + 5.5, d_slope[4] + 5.25, "Frozen beef - ribs (1 kg)", rotation=28, fontname='Franklin Gothic Medium Cond')
    #plt.text(1990, 31, "Frozen beef", rotation=-15, va='bottom', ha='right')


    ax.set_yticks([0, 5,10, 15,20,25,30,35])

    plt.title('Chicken Breast | Coffee | Lemons | Tomatoes | Frozen beef - ribs', fontsize=14, fontweight='bold',color ='Gray', fontname='Franklin Gothic Medium Cond')
    plt.suptitle('The progression of individual food item prices\nover the course of 40 years in Israel',fontsize=28, fontweight='bold', fontname='Franklin Gothic Medium Cond')
    plt.xlabel('Years',fontsize=19, fontweight='bold', fontname='Franklin Gothic Medium Cond')
    plt.ylabel('Price',fontsize=19, fontweight='bold', fontname='Franklin Gothic Medium Cond')

    plt.savefig('Evolution_of_the_costs.png')
    plt.show()


if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/home/shay_diy/PycharmProjects/digging_deep_into_Israel_prices/Data/israel_prices.csv')
    df = df.replace(np.nan, '', regex=True)

    column_headers = list(df.columns.values)
    print("The Column Header :", column_headers)

    list_of_colors = ['Green', 'Blue' , 'lightblue', 'lightgreen'  ,'Navy', 'orchid']
    # #1) What are the top 5 items that experienced a more significant decrease in prices compared to increases during the 90s and 2000s?
    #
    res= preparing_the_data(df)
    creating_the_line_chart(res,list_of_colors)
    print('*')
