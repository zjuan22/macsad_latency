import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
from matplotlib.patches import Polygon
import matplotlib

matplotlib.rc('xtick', labelsize=8)
matplotlib.rc('ytick', labelsize=8)


#file to read in
#infile = '/Users/suneetsingh/Desktop/Boxplot/l3/l3_latency_boxplot.csv'
infile = '/home/lion/workspace/macsad_latency/eps_figures/l3_boxplot/l3_latency_boxplot.csv'


#pull data into NumPy dataframe
df = pd.read_csv(infile, sep=',', na_values='.')

#plt.labels('128', '256', '512', '1024')
plt.title('Latency')
plt.xlabel('Packet Size (Bytes)')
plt.ylabel('Latency (ns)')



x = np.array([64,128,156,512,1024,1280,1518,64,128,156,512,1024,1280,1518,64,128,156,512,1024,1280,1518,64,128,156,512,1024,1280,1518,64,128,156,512,1024,1280,1518,64,128,156,512,1024,1280,1518])

#x=range(len(x_axis))


#plt.legend(["64","","","","","",""])
#myplot = df.plot.bar()
#for item in myplot.get_xticklabels():
#   item.set_rotation(90)

bp= df.boxplot(whis=[1,99], showfliers=True, showmeans=True,)
plt.xticks(rotation=90)
#df.drop(['7','8','16', '17', '25', '26', '34', '35' ], axis=1, inplace=True)
#df
#df.loc[:, ~df.columns.str.contains('^Unnamed')]
#df.drop(df.columns[[7, 8, 16, 17,25,26,34,35]], axis=1, inplace=True)
#df = pd.DataFrame(columns=['a','Unnamed: 7', 'Unnamed: 8','foo'])
plt.legend()
plt.xlabel('x')
plt.show()



