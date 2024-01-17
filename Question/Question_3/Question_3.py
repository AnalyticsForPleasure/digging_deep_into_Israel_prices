import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/home/shay_diy/PycharmProjects/digging_deep_into_Israel_prices/Data/israel_prices.csv')
    df = df.replace(np.nan, '', regex=True)

    filter_data_by_year = df.loc [(df['Year'] <= 2022) & (df['Year'] > 2012)]

    food_items = [ 'Year',
        'Apples - Golden Delicious (1 kg)',
                              'Apples - Granny Smith (1 kg)',
                              'Oranges - smutty (1 kg)',
                              'Green bins (1 kg)',
                              'mango (1 kg)',
                              'Carrot (1 kg)'],
                             #  'Zucchini (1 kg)',
                             #  'Tomatoes - Cherry (1 kg)',
                             #  'lemons (1 kg)',
                             #  'Potatoes (1 kg)',
                             #  'Cucumbers (1 kg)',
                             # 'Chicken Breast (1 kg)',
                             # 'Chicken meat with toppings (1 portion)',starting to create the data for the matrix chart heatmap
                             # 'Fresh beef for steak - shoulder (1 kg)',
                             # 'Frozen beef for roasting (1 kg)',
                             # 'Fresh tilapia fish (1 kg)',
                             # 'Frozen beef - ribs (1 kg)',
                             # 'Frozen beef liver (1 kg)',
                             # 'Packaged frozen chicken (1 kg)',
                             # 'Frozen salmon fish (Ilatit). (1 kg)',
                             # 'Frozen tilapia fillet fish (Mosht). (1 kg)',
                             # 'Nile princess fillet fish, frozen (1 kg)']
                             #

    table_stat_price =  pd.DataFrame({'Year':[],
                         'Apples - Golden Delicious (1 kg)':[],
                         'Apples - Granny Smith (1 kg)':[],
                         'Oranges - smutty (1 kg)':[],
                         'Green bins (1 kg)':[],
                         'mango (1 kg)':[],
                         'Carrot (1 kg)':[]})


    column_indices = [filter_data_by_year.columns.get_loc(col) for col in food_items]  # filter_vegi_and_fruits
    full_relevant_data = filter_data_by_year.iloc[:, column_indices]
    print('*')

    groups_by_year = full_relevant_data.groupby('Year')
    for current_year, mini_df_year in groups_by_year:
        print("The current year is: ", current_year)
        print(mini_df_year)
        mini_df_year = mini_df_year.apply(pd.to_numeric)
        for idx in np.arange(1, mini_df_year.shape[1]):
            #res = mini_df_year.loc[:,'lemons (1 kg)'].mean()
            res = mini_df_year.loc[:, idx].mean()

            avg_price_calulation = pd.concat([avg_price_calulation, res], axis=0)
        print('*')
