import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# **************************************************************************************************************
# Function  name: creating_the_data_food_item_prices_by_percentage_change_range_of_years
# input:
# return value:
# ****************************************************************************************************************
def creating_the_data_food_item_prices_by_percentage_change_range_of_years(df,starting_year , ending_year ):

    filter_data_by_year = df.loc[(df['Year'] <= ending_year) & (df['Year'] > starting_year)]
    food_items_filter = [ 'Year', 'Apples - Golden Delicious (1 kg)', 'Apples - Granny Smith (1 kg)', 'Oranges - smutty (1 kg)', 'Green bins (1 kg)', 'mango (1 kg)', 'Carrot (1 kg)']
    column_indices = [filter_data_by_year.columns.get_loc(col) for col in food_items_filter]  # filter_vegi_and_fruits
    full_relevant_data = filter_data_by_year.iloc[:, column_indices]
    print('*')

    table_stat_price = pd.DataFrame({'Year': [],
                                     'Apples - Golden Delicious (1 kg)': [],
                                     'Apples - Granny Smith (1 kg)': [],
                                     'Oranges - smutty (1 kg)': [],
                                     'Green bins (1 kg)': [],
                                     'mango (1 kg)': [],
                                     'Carrot (1 kg)': []})

    groups_by_year = full_relevant_data.groupby('Year')
    for current_year, mini_df_year in groups_by_year:
        print("The current year is: ", current_year)
        print(mini_df_year)
        mini_df_year = mini_df_year.apply(pd.to_numeric)
        avg_row = pd.DataFrame(mini_df_year.apply(np.mean)).T
        # Now, let's add each year to a dataframe:
        table_stat_price = pd.concat([table_stat_price, avg_row], axis=0)
    table_stat_price = table_stat_price.apply(lambda x: x.apply(lambda y: f'{y:.2f}'))
    table_stat_price = table_stat_price.apply(pd.to_numeric)
    percentage_changes = table_stat_price.pct_change()
    percentage_changes.drop('Year', axis=1, inplace=True)  # drop a column
    percentage_changes.drop(0, inplace=True) # drop first row
    percentage_changes_format = percentage_changes.applymap(lambda x: f'{x * 100:.1f}')
    # table_stat_price['Year'] = pd.to_numeric(table_stat_price['Year'])
    # Create a DataFrame from the range of years
    list_of_years = pd.DataFrame(np.arange(2013, 2023, 1), columns=['Year'])
    # Concatenate along the columns
    result_df = pd.concat([percentage_changes_format, list_of_years], axis=1)

    return result_df


if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/home/shay_diy/PycharmProjects/digging_deep_into_Israel_prices/Data/israel_prices.csv')
    df = df.replace(np.nan, '', regex=True)

    creating_the_data_Food_Item_Prices_by_Percentage_Change_Range_of_Years(df, starting_year=2012, ending_year=2022)


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


    # # Reshape the DataFrame for heatmap
    # heatmap_data = result_df.melt(id_vars='Year', var_name='Food_Item', value_name='Percentage_Change')
    #
    # # Define the percentage change categories for color mapping
    # categories = ['<-10%', '-10%-<-8%', '-8%-<-6%', '-6%-<-4%', '-4%-<-2%', '-2%-0%', '0%-2%', '2%-4%', '4%-6%',
    #               '6%-8%', '8%-10%', '>10%']
    #
    # # Create a heatmap
    # plt.figure(figsize=(12, 8))
    # sns.heatmap(heatmap_data.pivot('Year', 'Food_Item', 'Percentage_Change'),
    #             cmap='RdYlBu_r',
    #             annot=True,
    #             fmt=".1f",
    #             cbar_kws={'label': 'Percentage Change'},
    #             vmin=-10, vmax=10,  # Adjust these values based on your data range
    #             yticklabels=categories,
    #             linewidths=.5)
    # plt.title('Heatmap of Food Item Prices by Percentage Change Range Over 10 Years')
    # plt.xlabel('Food Item')
    # plt.ylabel('Percentage Change Range')
    # plt.show()

