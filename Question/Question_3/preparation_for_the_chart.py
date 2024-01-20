import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

data = np.random.uniform(-0.193, 0.082, size=(14, 6)) # very nice - I didn't know that!


#data = np.random.uniform(-0.193, 0.082, size=(10, 6))

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 9))
sns.set_style('dark')

# Heatmap number 1 :
sns.heatmap(data, linewidth=3.5, annot=True,square=False, ax=ax1, cmap = 'Grays',fmt=".2%",cbar_kws={'label': 'Percentage'},annot_kws={'weight': 'bold', 'size': 10})

# Creating the squares for heatmap 1
for ind, row in enumerate(data):
    min_col = np.argmax(row)
    ax1.add_patch(plt.Rectangle((min_col, ind), 1, 1, fc='none', ec='limegreen', lw=3.5, clip_on=False))


# Name: Explanation for heatmap 2
# input: This this code is creating a heatmap where each row is highlighted, showing the minimum value in each row
#        and masking (hiding) the other values. The purpose of the mask is to emphasize the minimum/ maximun value in each row.
# ***************************************************************************************************************
sns.heatmap(data, mask=data != data.max(axis=1, keepdims=True), annot=True, lw=2, linecolor='black', clip_on=False,
            cmap=ListedColormap(['limegreen']), cbar=False, ax=ax2,fmt=".2%",cbar_kws={'label': 'Percentage'},annot_kws={'weight': 'bold', 'size': 10})

x_labels = ["Hard yellow cheese\n(100 g)", 'Leben\n(200 ml)', "Cottage cheese'\n(250 grams)", 'Soft white cheese\n(250 grams)', 'Margarine\n(250 grams)', 'Natural yogurt\n(200 ml)']
y_labels = ['Year {}'.format(i) for i in range(2009, 2023)]


# loop iterates over the two subplots (ax1 and ax2)
for ax in [ax1, ax2]:
    ax.set_xticklabels(x_labels, rotation=45, ha='right', weight='bold', color='darkgreen')
    ax.set_yticklabels(y_labels, rotation=0, weight='bold', color='darkgreen')





ax1.set_title('Variation in Dairy Product Prices\nOver the Past 15 Years', fontsize=20, fontname='Franklin Gothic Medium Cond')
ax2.set_title('Upward Shift in Dairy Product Prices', fontsize=20, fontname='Franklin Gothic Medium Cond')

plt.tight_layout()

plt.savefig('heatmap_Advance_chart.jpg', dpi=250, bbox_inches='tight')


# Adding picture - https://www.kaggle.com/code/andradaolteanu/bitcoin-dogecoin-on-rapids-and-elon-musk
#path='../input/all-elon-musks-tweets/images/images/elon_rocket.png'
#offset_png(x=6.9, y=2000, path=path, ax=ax, zoom=0.27, offset=0)
plt.show()

