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

    # Convert DataFrame to NumPy array - inorder to countinue running with the chart
    numpy_array_data = data.values

    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 9))

    sns.set_style('white')

    # Heatmap number 1 :
    sns.heatmap(numpy_array_data, linewidth=3.5, annot=True, square=False, ax=ax1, cmap='Greens', fmt=".1%",
                    cbar_kws={'label': 'Percentage'}, annot_kws={'weight': 'bold', 'size': 10})

    # Creating the squares for heatmap 1
    for ind, row in enumerate(numpy_array_data):
        min_col = np.argmax(row)
        ax1.add_patch(plt.Rectangle((min_col, ind), 1, 1, fc='none', ec='limegreen', lw=3.5, clip_on=False))

    # Explanation for heatmap 2 :
    # This this code is creating a heatmap where each row is highlighted, showing the minimum value in each row
    # and masking (hiding) the other values. The purpose of the mask is to emphasize the minimum/ maximun value in each row.

    sns.heatmap(numpy_array_data, mask=numpy_array_data != numpy_array_data.max(axis=1, keepdims=True), annot=True, lw=2, linecolor='black', clip_on=False,
                cmap=ListedColormap(['limegreen']), cbar=False, ax=ax2, fmt=".1%",
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




