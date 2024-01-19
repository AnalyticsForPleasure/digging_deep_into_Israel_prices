import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

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
    percentage_changes_format= percentage_changes_format.reset_index()
    percentage_changes_format = percentage_changes_format.drop(index=0).reset_index(drop=True)
    percentage_changes_format_table = percentage_changes_format.drop(columns=['index'])
    percentage_changes_format_table = percentage_changes_format_table.apply(pd.to_numeric)
    print('*')

    return percentage_changes_format_table

# **************************************************************************************************************
# Function  name: creating_advance_heatmap
# input:
# return value:
# ****************************************************************************************************************
def creating_advance_heatmap(data):

    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 9))

    sns.set_style('white')
    sns.heatmap(data, linewidth=3.5, annot=True, square=False, ax=ax1, cmap='Greens', fmt=".1%",
                    cbar_kws={'label': 'Percentage'}, annot_kws={'weight': 'bold', 'size': 10})

    min_columns = data.idxmin(axis=1)
    min_columns_colors = ['limegreen' if col == data.columns.get_loc(min_col) else 'none' for col, min_col in zip(range(len(data)), min_columns)]
    sns.heatmap(data, mask=data != data.min(axis=1, keepdims=True), annot=True, lw=2, linecolor='black',
                    clip_on=False,
                    cmap=ListedColormap(min_columns_colors), cbar=False, ax=ax2, fmt=".1%",
                    cbar_kws={'label': 'Percentage'},
                    annot_kws={'weight': 'bold', 'size': 10})

    # Customize x-axis and y-axis labels
    x_labels = ["Hard yellow cheese\n(100 g)", 'Leben\n(200 ml)', "Cottage cheese'\n(250 grams)",
                    'Soft white cheese\n(250 grams)', 'Margarine\n(250 grams)', 'Natural yogurt\n(200 ml)']
    y_labels = ['Year {}'.format(i) for i in range(2009, 2023)]

    ax2.set_xticklabels(x_labels, rotation=45, ha='right', weight='bold', color='darkgreen')
    ax2.set_yticklabels(y_labels, rotation=0, weight='bold', color='darkgreen')

    ax1.set_xticklabels(x_labels, rotation=45, ha='right', weight='bold', color='darkgreen')
    ax1.set_yticklabels(y_labels, rotation=0, weight='bold', color='darkgreen')

    ax1.set_title('Variation in Dairy Product Prices\nOver the Past 15 Years', fontsize=20, fontname='Franklin Gothic Medium Cond')
    plt.tight_layout()

    plt.savefig('heatmap_Advance_chart.jpg', dpi=250, bbox_inches='tight')
    plt.show()


    # fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 9))
    #
    # sns.set_style('white')
    # sns.heatmap(data, linewidth=3.5, annot=True, square=False, ax=ax1, cmap='Grays', fmt=".1%",
    #             cbar_kws={'label': 'Percentage'}, annot_kws={'weight': 'bold', 'size': 10})
    #
    # for ind, row in enumerate(data):
    #     min_col = np.argmin(row)
    #     ax1.add_patch(plt.Rectangle((min_col, ind), 1, 1, fc='none', ec='limegreen', lw=3.5, clip_on=False))
    # sns.heatmap(data, mask=data != data.min(axis=1, keepdims=True), annot=True, lw=2, linecolor='black', clip_on=False,
    #             cmap=ListedColormap(['limegreen']), cbar=False, ax=ax2, fmt=".1%", cbar_kws={'label': 'Percentage'},
    #             annot_kws={'weight': 'bold', 'size': 10})
    # # for idx in len(np.arange(0,2,1)):
    # ax2.set_xticklabels(["Hard yellow cheese\n(100 g)", 'Leben\n(200 ml)', "Cottage cheese'\n(250 grams)",
    #                      'Soft white cheese\n(250 grams)', 'Margarine\n(250 grams)', 'Natural yogurt\n(200 ml)'],
    #                     rotation=45, ha='right', weight='bold', color='darkgreen')
    # ax2.set_yticklabels(['Year {}'.format(i) for i in range(2009, 2023)], rotation=0, weight='bold',
    #                     color='darkgreen')  # Customize y-axis labels
    #
    # ax1.set_xticklabels(["Hard yellow cheese\n(100 g)", 'Leben\n(200 ml)', "Cottage cheese'\n(250 grams)",
    #                      'Soft white cheese\n(250 grams)', 'Margarine\n(250 grams)', 'Natural yogurt\n(200 ml)'],
    #                     rotation=45, ha='right', weight='bold', color='darkgreen')
    # ax1.set_yticklabels(['Year {}'.format(i) for i in range(2009, 2023)], rotation=0, weight='bold',
    #                     color='darkgreen')  # Customize y-axis labels
    # #
    # # # Adjust subplot layout to make room for upper labels
    # # plt.subplots_adjust(top=0.9)
    # ax1.set_title('Variation in Dairy Product Prices\nOver the Past 15 Years', fontsize=20,
    #               fontname='Franklin Gothic Medium Cond')
    # ax2.set_title('Upward Shift in Dairy Product Prices', fontsize=20, fontname='Franklin Gothic Medium Cond')
    # plt.tight_layout()
    # plt.savefig('heatmap_Advance_chart.jpg', dpi=250, bbox_inches='tight')
    # plt.show()


if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/home/shay_diy/PycharmProjects/digging_deep_into_Israel_prices/Data/israel_prices.csv')
    df = df.replace(np.nan, '', regex=True)

    column_headers = list(df.columns.values)
    print("The Column Header :", column_headers)

    ending_year = 2022
    starting_year = 2007

    result_df = creating_the_data_food_item_prices_by_percentage_change_range_of_years_(df, ending_year, starting_year)
    creating_advance_heatmap(result_df)
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

