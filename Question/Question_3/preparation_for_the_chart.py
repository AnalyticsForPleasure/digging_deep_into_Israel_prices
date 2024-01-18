import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

data = np.random.uniform(-0.193, 0.082, size=(14, 6)) # very nice - I didn't know that!


fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 9))
sns.set_style('white')

sns.heatmap(data, linewidth=3.5, annot=True,square=False, ax=ax1, cmap = 'Grays',fmt=".1%",cbar_kws={'label': 'Percentage'},annot_kws={'weight': 'bold', 'size': 10})
for ind, row in enumerate(data):
    min_col = np.argmin(row)
    ax1.add_patch(plt.Rectangle((min_col, ind), 1, 1, fc='none', ec='limegreen', lw=3.5, clip_on=False))

sns.heatmap(data, mask=data != data.min(axis=1, keepdims=True), annot=True, lw=2, linecolor='black', clip_on=False,
            cmap=ListedColormap(['limegreen']), cbar=False, ax=ax2,fmt=".1%",cbar_kws={'label': 'Percentage'},annot_kws={'weight': 'bold', 'size': 10})

#for idx in len(np.arange(0,2,1)):
ax2.set_xticklabels(["Hard yellow cheese\n(100 g)", 'Leben\n(200 ml)', "Cottage cheese'\n(250 grams)", 'Soft white cheese\n(250 grams)', 'Margarine\n(250 grams)', 'Natural yogurt\n(200 ml)'],
                    rotation=45, ha='right',weight='bold',color = 'darkgreen')
ax2.set_yticklabels(['Year {}'.format(i) for i in range(2009, 2023)], rotation=0,weight='bold',color = 'darkgreen')  # Customize y-axis labels


ax1.set_xticklabels(["Hard yellow cheese\n(100 g)", 'Leben\n(200 ml)', "Cottage cheese'\n(250 grams)", 'Soft white cheese\n(250 grams)', 'Margarine\n(250 grams)', 'Natural yogurt\n(200 ml)'],
                    rotation=45, ha='right', weight='bold',color = 'darkgreen')
ax1.set_yticklabels(['Year {}'.format(i) for i in range(2009, 2023)], rotation=0,weight='bold',color = 'darkgreen')  # Customize y-axis labels


ax1.set_title('Variation in Dairy Product Prices\nOver the Past 15 Years', fontsize=20, fontname='Franklin Gothic Medium Cond')
ax2.set_title('Upward Shift in Dairy Product Prices', fontsize=20, fontname='Franklin Gothic Medium Cond')

plt.tight_layout()

plt.savefig('heatmap_Advance_chart.jpg', dpi=250, bbox_inches='tight')
plt.show()

