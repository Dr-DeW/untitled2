import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

tips_df = sns.load_dataset('tips')
tips_df['tip_percentage'] = tips_df['tip']/tips_df['total_bill']
sns.lineplot(data=tips_df,x='total_bill',y='tip')
plt.xlabel('BILL')
plt.show()
