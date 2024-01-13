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



    column_headers = list(df.columns.values)
    print("The Column Header :", column_headers)


    #step 1: filtering the years
    new_data_by_years = df.loc[df['Year'] >= 1987]
    #df.loc[df['player_name'] == 'Chris Paul', :]
    print('*')




    filter_vegi_and_fruits = ['Apples - Golden Delicious (1 kg)',
                    'Apples - Granny Smith (1 kg)',
                    'Apples - Jonathan (1 kg)',
                    'Avocado (1 kg)',
                    'Oranges - Valencia (1 kg)',
                    'Oranges - smutty (1 kg)',
                    'Light green pepper (1 kg)',
                    'Dark green pepper (1 kg)',
                    'Melons - Galia (1 kg)',
                    'Green bins (1 kg)',
                    'Carrot (1 kg)',
                    'Green grapes without pits (1 kg)',
                    'lemons (1 kg)',
                    'Cucumbers (1 kg)']
                    #'Tomatoes'

    # Step 2: filtering the data by specific data I need
    column_indices = [new_data_by_years.columns.get_loc(col) for col in filter_vegi_and_fruits]
    full_relevant_data = new_data_by_years.iloc[:, column_indices]
    print('*')







