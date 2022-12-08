import pandas as pd


df = customers

df1 = orders

df_copy = df.merge(df1 , how = 'inner' , left_on = 'id' ,right_on = 'cust_id').drop(['id_x','id_y'],axis=1)

#df_copy['count_customers'] = df_copy['cust_id'].nunique()


df_copy = df_copy.groupby(['city','cust_id']).sum().reset_index()
df_copy['customer_count'] = 1

#df_copy['city'].value_counts(sort = False).reset_index()
df_copy.groupby(['city']).sum().reset_index().drop('cust_id',axis=1)