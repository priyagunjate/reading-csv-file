import matplotlib.pyplot as plt
from pandas import read_csv
from pandas.plotting import scatter_matrix

url = "https://goo.gl/vhm1eU"
names = ['preg' ,'plas', 'pres' , 'skin' , 'test' , 'mass' , 'pedi' ,' age' ,'class']
data = read_csv(url, names=names)
##print(data.shape)
##print(data)
##description = data.describe()
##print(description)
scatter_matrix(data)
plt.show()
