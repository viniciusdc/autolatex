#import csv
import pandas as pd
import locale
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

locale.setlocale(locale.LC_NUMERIC, "pt_BR.UTF-8")

df = pd.read_csv('notas.csv', sep=';', index_col=0)
df = df.applymap(lambda x: '0' if x in ['-'] else x)
df = df.applymap(locale.atof)

plt.figure(1)
n, bins, patches = plt.hist(df.values[:,0])
y = mlab.normpdf(bins)
l = plt.plot(bins, y, 'r--', linewidth=1)
plt.show()

plt.figure(2)
plt.hist(df.values[:,1])
plt.show()

plt.figure(3)
plt.hist(df.values[:,2])
plt.show()
