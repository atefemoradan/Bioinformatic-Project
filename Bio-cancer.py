import pandas as pd
import GEOparse
from pyHSICLasso import HSICLasso
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler

#######
##Preprocessing phase
gse = GEOparse.get_GEO(geo="GSE2034", destdir="/home/atefeh/Desktop/Bio")
dfg=gse.pivot_samples("VALUE")
dfg=dfg.T
dfg1=pd.read_csv('/home/atefeh/Desktop/GEO Accession viewer.csv')
dfg.reset_index(level=0, inplace=True)
dfg.rename(columns={'name':'GEO'}, inplace=True)
dfg1.rename(columns={'GEO ':'GEO'}, inplace=True)
result = pd.merge(dfg1,dfg, how='inner',on='GEO')
result.drop("GEO",axis=1)
result.to_csv("/home/atefeh/Desktop/Bio/cancer.csv")
###############
### Data Normalization
df=pd.read_csv("/home/atefeh/Desktop/Bio/cancer.csv")
ln=df.columns
ln=list(ln)
df1=df[ln]
output_list=['relapse ']
scaler = preprocessing.StandardScaler()
scaled_df = scaler.fit_transform(df1)
df2= pd.DataFrame(scaled_df, columns=ln)
df2.to_csv("/home/atefeh/Desktop/Bio/cancerNormalize.csv",index=False)
df.to_csv("/home/atefeh/Desktop/Bio/cancer1.csv",index=False)
###lasso Implementation for Normalized data
hsic_lasso = HSICLasso()
hlasso=hsic_lasso.input("/home/atefeh/Desktop/Bio/cancerNormalize.csv",output_list=['relapse'])
hsic_lasso.classification(30)
hsic_lasso.get_features()
hsic_lasso.dump()
### Lasso implementation without normalization

hsic_lasso = HSICLasso()
hlasso=hsic_lasso.input("/home/atefeh/Desktop/Bio/cancer1.csv",output_list=['relapse '])
hsic_lasso.classification(30)
hsic_lasso.get_features()
hsic_lasso.dump()