import numpy as np
import pandas as pd
# import dataframe_image as dfi
# import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
#import seaborn as sys
import seaborn as sns


def creating_the_relavent_data(df):

    # step 1: filtering the years
    relavent_years = np.arange(1990, 2021, 5)
    filter_data_by_month = df.loc[df['Month'] == 1, :]
    filter_data_by_month_year = filter_data_by_month[filter_data_by_month['Year'].isin(relavent_years)]
    print('*')
    filter_vegi_and_fruits = ['Apples - Golden Delicious (1 kg)',
                              'Apples - Granny Smith (1 kg)',
                              # 'Apples - Jonathan (1 kg)',
                              'Avocado (1 kg)',
                              # 'Oranges - Valencia (1 kg)',
                              # 'Oranges - smutty (1 kg)',
                              # 'Light green pepper (1 kg)',
                              # 'Dark green pepper (1 kg)',
                              # 'Melons - Galia (1 kg)',
                              # 'Green bins (1 kg)',
                              'Carrot (1 kg)',
                              # 'Green grapes without pits (1 kg)',
                              'lemons (1 kg)',
                              'Cucumbers (1 kg)']
    # 'Tomatoes'
    # Step 2: filtering the data by specific data I need
    column_indices = [filter_data_by_month_year.columns.get_loc(col) for col in filter_vegi_and_fruits]
    full_relevant_data = filter_data_by_month_year.iloc[:, column_indices]
    full_relevant_data = full_relevant_data.apply(pd.to_numeric)
    percentage_changes = full_relevant_data.pct_change()
    # formatted_percentage_changes = percentage_changes.applymap(lambda x: f"{x * 100:.2f}")
    traspose_data = percentage_changes.T
    # rename_columns
    old_names = [84, 144, 204, 264, 324, 384, 444]
    new_names = ['Price_change_1990', 'Price_change_1995', 'Price_change_2000', 'Price_change_2005',
                 'Price_change_2010', 'Price_change_2015', 'Price_change_2020']
    res = traspose_data.rename(columns=dict(zip(old_names, new_names)), inplace=False)
    res = res.reset_index()
    res = res.rename(columns={res.columns[0]: 'Item_Name'})
    relevant_data = res.loc[:, ['Item_Name', 'Price_change_2020']]

    relevant_data_sorted = relevant_data.sort_values(by='Price_change_2020', ascending=False)
    relevant_data_sorted =relevant_data_sorted.reset_index()
    relevant_data_sorted = relevant_data_sorted.drop('index', axis=1)

    return relevant_data_sorted


def plotting_advance_bar_plot(relevant_data_sorted):
    plt.figure(figsize=(6, 6))
    ax = sns.barplot(data=relevant_data_sorted, y='Item_Name', x=[1] * len(relevant_data_sorted), color='lightgrey',
                     saturation=1)
    sns.barplot(data=relevant_data_sorted, y='Item_Name', x='Price_change_2020', color='skyblue', saturation=1, ax=ax)
    for lbl in ax.get_yticklabels():
        # add the y tick labels as right aligned text into the plot
        ax.text(0.985, lbl.get_position()[1], lbl.get_text(), transform=ax.get_yaxis_transform(), ha='right',
                va='center', fontname='Franklin Gothic Medium Cond', fontsize=16, fontweight='bold')
    ax.bar_label(ax.containers[1], fmt='%.2f %%', fontname='Franklin Gothic Medium Cond', fontsize=14,
                 fontweight='bold')  # label the bars ' %.2f %%'
    ax.set_xticks([])  # remove the x ticks
    ax.set_yticks([])  # remove the y ticks
    ax.xaxis.set_label_position('top')
    ax.xaxis.label.set_size(20)
    ax.set_ylabel('')  # remove the y label
    ax.margins(x=0)  # remove the spacing at the right
    sns.despine(left=True, bottom=True)  # remove the spines
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/home/shay_diy/PycharmProjects/digging_deep_into_Israel_prices/Data/israel_prices.csv')
    df = df.replace(np.nan, '', regex=True)



    column_headers = list(df.columns.values)
    print("The Column Header :", column_headers)

    res = creating_the_relavent_data(df)
    plotting_advance_bar_plot(res)
    print('*')





