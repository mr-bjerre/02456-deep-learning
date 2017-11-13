import os
import pandas as pd

__name__ = r'C:\GitRepository\02456-deep-learning\project\model.py'
os.chdir(os.path.dirname(__name__))
os.getcwd()

desc = pd.DataFrame(pd.read_excel('data\\mc_data_v0.xlsx', sheetname='DataDescription', parse_cols='A:D'))
data = pd.DataFrame(pd.read_excel('data\\mc_data_v0.xlsx', sheetname='Data1', header=None))
data.columns = desc['Alias']
