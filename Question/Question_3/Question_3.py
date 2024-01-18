import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# **************************************************************************************************************
# Function  name: creating_the_data_food_item_prices_by_percentage_change_range_of_years
# input:
# return value:
# ****************************************************************************************************************
def creating_the_data_food_item_prices_by_percentage_change_range_of_years_(df, ending_year, starting_year):

    filter_data_by_year = df.loc[(df['Year'] <= ending_year) & (df['Year'] > starting_year)]


    filter_Dairy_Product = ['Year',
                            "Hard yellow cheese from cow's milk (100 g)",
                            'Leben (200 ml)',
                            "Cottage cheese' (250 grams)",
                            'Soft white cheese (250 grams)',
                            'Margarine for spreading in a cup (250 grams)',
                            'Natural yogurt in a plastic container (200 ml)']

    column_indices = [filter_data_by_year.columns.get_loc(col) for col in filter_Dairy_Product]  # filter_vegi_and_fruits
    full_relevant_data = filter_data_by_year.iloc[:, column_indices]
    print('*')
    table_stat_price = pd.DataFrame({'Year':[],
                                     "Hard yellow cheese from cow's milk (100 g)": [],
                                     'Leben (200 ml)': [],
                                     "Cottage cheese' (250 grams)": [],
                                     'Soft white cheese (250 grams)': [],
                                     'Margarine for spreading in a cup (250 grams)': [],
                                     'Natural yogurt in a plastic container (200 ml)': []})



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
    #percentage_changes.drop(0, inplace=True)  # drop first row
    percentage_changes_format = percentage_changes.applymap(lambda x: f'{x * 100:.1f}')
    #table_stat_price['Year'] = pd.DataFrame(np.arange(2013, 2023, 1), columns=['Year'])
    # Create a DataFrame from the range of years
    year_df = pd.DataFrame(np.arange(2013, 2023, 1), columns=['Year'])
    # Concatenate along the columns - TODO: not working well!
    result_df = pd.merge(percentage_changes_format, year_df, on="Year")

    #result_df = pd.concat([percentage_changes_format, list_of_years], axis=1)
    print('*')

    return result_df


if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/home/shay_diy/PycharmProjects/digging_deep_into_Israel_prices/Data/israel_prices.csv')
    df = df.replace(np.nan, '', regex=True)

    column_headers = list(df.columns.values)
    print("The Column Header :", column_headers)

    ending_year = 2022
    starting_year = 2007

    result_df = creating_the_data_food_item_prices_by_percentage_change_range_of_years_(df, ending_year, starting_year)
    print('*')





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

