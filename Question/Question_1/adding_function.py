import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
#import seaborn as sys
import seaborn as sns

# **************************************************************************************************************
# Function  name: creating_the_relavent_data
# input:
# return value:
# ****************************************************************************************************************
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
                              'Oranges - smutty (1 kg)',
                              # 'Light green pepper (1 kg)',
                              # 'Dark green pepper (1 kg)',
                              # 'Melons - Galia (1 kg)',
                              'Green bins (1 kg)',
                              'Carrot (1 kg)',
                              # 'Green grapes without pits (1 kg)',
                              'lemons (1 kg)',
                              'Cucumbers (1 kg)']

    # Step 2: filtering the data by specific data I need
    column_indices = [filter_data_by_month_year.columns.get_loc(col) for col in filter_vegi_and_fruits]
    full_relevant_data = filter_data_by_month_year.iloc[:, column_indices]
    full_relevant_data = full_relevant_data.apply(pd.to_numeric)
    percentage_changes = full_relevant_data.pct_change()

    traspose_data = percentage_changes.T
    traspose_data = traspose_data.apply(lambda x: x * 100)

    # rename_columns
    old_names = [84, 144, 204, 264, 324, 384, 444]
    new_names = ['1990', '1995', '2000', '2005',
                 '2010', '2015', '2020']
    res = traspose_data.rename(columns=dict(zip(old_names, new_names)), inplace=False)
    res = res.reset_index()
    res = res.rename(columns={res.columns[0]: 'Item_Name'})
    res = res.reset_index()
    res = res.drop('index', axis=1)

    # Remove "(1 kg)" from the 'Item_Name' column
    res['Item_Name'] = res['Item_Name'].apply(lambda x: x.replace('(1 kg)', ''))

    return res

# **************************************************************************************************************
# Function  name: plotting_advance_bar_plot
# input:
# return value:
# ****************************************************************************************************************
def plotting_advance_bar_plot(res):

    fig, axes = plt.subplots(1, 2, figsize=(15, 4))
    list_of_colors = ['royalblue','deepskyblue']
    list_of_ranges_of_years = ['2015', '2020']

    for idx, (current_range_of_year, current_color) in enumerate(zip(list_of_ranges_of_years, list_of_colors)):
        new_df = res.loc[:, ['Item_Name', current_range_of_year]].sort_values(by=current_range_of_year,ascending=False)
        print('*')
        ax = sns.barplot(data=new_df,y=new_df.loc[:, 'Item_Name'], x=[100] * len(new_df),color='lightgrey', saturation=1, ax=axes[idx])
        sns.barplot(data=new_df, y=new_df.loc[:, 'Item_Name'],x=new_df.loc[:, current_range_of_year], color=current_color, saturation=1, ax=ax)
        for lbl in ax.get_yticklabels():
            ax.text(0.985, lbl.get_position()[1], lbl.get_text(), transform=ax.get_yaxis_transform(),
                    ha='right', va='center', fontname='Franklin Gothic Medium Cond', fontsize=14, fontweight='bold')
        ax.bar_label(ax.containers[1], fmt=' %.2f %%', fontname='Franklin Gothic Medium Cond', fontsize=14,
                         fontweight='bold')  # label the bars

        ax.set_xticks([])  # remove the x ticks
        ax.set_yticks([])  # remove the y ticks
        ax.set_xlabel('')
        ax.set_ylabel('')  # remove the y label
        ax.margins(x=0)  # remove the spacing at the right
        sns.despine(left=True, bottom=True)  # remove the spines

        # plt.title(f"Increase in vegetable & fruits prices\n from {int(current_range_of_year) - 5} to {current_range_of_year}",
        #           loc='center', fontproperties='Franklin Gothic Medium Cond', size=20, color='slategray', pad=10 )
        ax.set_title(f"Increase in prices\n{int(current_range_of_year) - 5} to {current_range_of_year}", loc='center',
                     size=14, color='slategray', pad=10,fontname='Franklin Gothic Medium Cond', fontsize=20)

    plt.tight_layout()
    fig.suptitle("Price Increase Over the Years", fontweight='bold',fontproperties='Franklin Gothic Medium Cond', size=20)

    #plt.title(f"Increase in vegetable & fruits prices",loc='center', fontproperties='Franklin Gothic Medium Cond', size=20, color='slategray', pad=10 )

    plt.savefig(f'plotting_advance_bar_plot_year.jpg', dpi=250, bbox_inches='tight')

    plt.show()

if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/home/shay_diy/PycharmProjects/digging_deep_into_Israel_prices/Data/israel_prices.csv')
    df = df.replace(np.nan, '', regex=True)

    list_of_ranges = [['2015', '2020'], ['2005','2010']]

    column_headers = list(df.columns.values)
    print("The Column Header :", column_headers)


    res = creating_the_relavent_data(df)
    plotting_advance_bar_plot(res)
    print('*')





