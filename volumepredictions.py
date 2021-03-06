# -*- coding: utf-8 -*-
"""AramexVolumePredictions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JaSbX9F6XadN1mgBsCGvgEtzCYuErsH8

# **Importing Relevant Packages**
"""

pip install pmdarima

pip install statsmodels

import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.arima.model import ARIMA 
import seaborn as sns
import warnings
import matplotlib.pyplot as plt
import statsmodels.graphics.tsaplots as sgt
import statsmodels.tsa.stattools as sts
from statsmodels.tsa.arima_model import ARIMA
from scipy.stats.distributions import chi2 
from math import sqrt
import seaborn as sns
import warnings

sns.set()

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.api import qqplot

"""# **Loading and Transforming the Data**"""

df_predictions  = pd.DataFrame()

#dfs = pd.read_excel("Arax.xlsx", sheet_name="Forecast")
dfs = pd.read_csv("222.csv")
df_comp=dfs.copy()

from datetime import datetime
df_comp['Date'] = pd.to_datetime(df_comp['Date'])
df_comp= df_comp.set_index("Date")

df_comp.head()
df_comp.plot()

#df_comp["Fullmonth"] = df_comp['Fullmonth'].str.replace('[A-Za-z]', '').str.replace(',', '.').astype(float)

size = int(len(df_comp)*0.8)
df_train, df_test = df_comp.iloc[:size], df_comp.iloc[size:]

df_train

df_test

"""# **simple AR model**"""

model_ar = ARIMA(df_train.fullmonth , order = (1,0,0))
results_ar = model_ar.fit()

start_date = df_test.index[0]
end_date=df_test.index[-1]
print(start_date , end_date)

df_pred_AR= results_ar.predict(start=start_date, end = end_date)

df_comp["AR-predictions"] = df_pred_AR
df_predictions["AR-predictions"] = df_pred_AR
print(df_pred_AR)

df_pred_AR[start_date:end_date].plot(figsize = (20,5), color = "red")
try:
     df_test.fullmonth[start_date:end_date].plot(color = "blue")
except ValueError:  
    pass
plt.title("Predictions vs Actual", size = 24)
plt.show()

model_ar2 = ARIMA(df_train.fullmonth , order = (2,0,0))
results_ar2 = model_ar.fit()

df_pred_AR2= results_ar.predict(start=start_date, end = end_date)

df_pred_AR2[start_date:end_date].plot(figsize = (20,5), color = "red")
try:
     df_test.fullmonth[start_date:end_date].plot(color = "blue")
except ValueError:  
    pass
plt.title("Predictions vs Actual", size = 24)
plt.show()

model_ar3 = ARIMA(df_train.fullmonth , order = (3,0,0))
results_ar3 = model_ar.fit()

df_pred_AR3= results_ar.predict(start=start_date, end = end_date)

df_pred_AR3[start_date:end_date].plot(figsize = (20,5), color = "red")
try:
     df_test.fullmonth[start_date:end_date].plot(color = "blue")
except ValueError:  
    pass
plt.title("Predictions vs Actual", size = 24)
plt.show()

"""# **MA MODEL**"""

sgt.plot_acf(df_comp.fullmonth , zero = False)
plt.title("ACF for Fullmonth", size=24)
plt.show()

model_volume_1 = ARIMA(df_train.fullmonth, order=(0,0,1))
results_volume_1 = model_volume_1.fit()
print(results_volume_1.summary())

df_pred_MA1= results_volume_1.predict(start = start_date, end = end_date)

df_pred_MA1[start_date:end_date].plot(figsize = (20,5), color = "red")
try:
     df_test.fullmonth[start_date:end_date].plot(color = "blue")
except ValueError:  
    pass
plt.title("Predictions vs Actual", size = 24)
plt.show()
df_comp["MA1-predictions"] = df_pred_MA1
df_predictions["MA1_Predictions"] =df_comp["MA1-predictions"]

model_volume_2 = ARIMA(df_train.fullmonth, order=(0,0,2))
results_volume_2 = model_volume_2.fit()
print(results_volume_2.summary())

df_pred_MA2= results_volume_2.predict(start = start_date, end = end_date)

df_pred_MA2[start_date:end_date].plot(figsize = (20,5), color = "red")
try:
     df_test.fullmonth[start_date:end_date].plot(color = "blue")
except ValueError:  
    pass
plt.title("Predictions vs Actual", size = 24)
plt.show()
df_comp["MA2-predictions"] = df_pred_MA1
df_predictions["MA2_Predictions"] =df_comp["MA2-predictions"]

model_volume_3 = ARIMA(df_train.fullmonth, order=(0,0,3))
results_volume_3 = model_volume_3.fit()
print(results_volume_3.summary())

df_pred_MA3= results_volume_3.predict(start = start_date, end = end_date)

df_pred_MA3[start_date:end_date].plot(figsize = (20,5), color = "red")
try:
     df_test.fullmonth[start_date:end_date].plot(color = "blue")
except ValueError:  
    pass
plt.title("Predictions vs Actual", size = 24)
plt.show()
df_comp["MA3-predictions"] = df_pred_MA3
df_predictions["MA3_Predictions"] =df_comp["MA3-predictions"]

"""# **ARMA**"""

model_arima_101 = ARIMA(df_comp.fullmonth, order=(1,0,1))
results_arima_101 = model_arima_101.fit()
print(results_arima_101.summary())

df_pred_ARMA= results_arima_101.predict(start = start_date, end = end_date)

df_pred_ARMA[start_date:end_date].plot(figsize = (20,5), color = "red")
try:
    df_test.fullmonth[start_date:end_date].plot(color = "blue")
except ValueError:  
    pass
plt.title("Predictions vs Actual", size = 24)
plt.show()
df_comp["ARMA_predictions"] = df_pred_ARMA
df_predictions["ARMA_Predictions"] =df_comp["ARMA_predictions"]



"""# **ARIMA**"""

model_arima_111 = ARIMA(df_comp.fullmonth, order=(1,1,1))
results_arima_111 = model_arima_111.fit()
print(results_arima_111.summary())

df_pred_ARIMA = results_arima_111.predict(start = start_date, end = end_date)

df_pred_ARIMA[start_date:end_date].plot(figsize = (20,5), color = "red")
try:
    df_test.fullmonth[start_date:end_date].plot(color = "blue")
except ValueError:  
    pass
plt.title("Predictions vs Actual", size = 24)
plt.show()
df_comp["ARIMA_predictions"] = df_pred_ARMA
df_predictions["ARIMA_Predictions"] =df_comp["ARIMA_predictions"]

"""# **Auto ARIMA**"""

from pmdarima.arima import auto_arima

model_auto = auto_arima(df_comp.fullmonth[1:])

df_auto_pred = pd.DataFrame(model_auto.predict(n_periods = len(df_test[start_date:end_date])), index = df_test[start_date:end_date].index)

df_auto_pred.plot(figsize=(20,5), color="red")
df_test.fullmonth[start_date:end_date].plot(color = "blue")
plt.title("auto model predictions vs real data" , size = 24)
plt.show()

model_auto.summary()

df_comp["AutoARIMA_predictions"] = df_auto_pred
df_predictions["AutoARIMA_Predictions"] =df_comp["AutoARIMA_predictions"]

"""# Saving results"""

df_predictions.to_csv('Volume_Predictions.csv')