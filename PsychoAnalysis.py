import pandas as pd

##1. Merge the two datasets

#Read the first set, which serves as our core
df1 = pd.read_csv('PsychData.csv')
#Read only part of the second which we will merge with the core
df2 = pd.read_csv('AlterPsychData.csv', usecols=['id','level_of_neurosis','number_of_freudian_slips_per_analytic_session','level_of_perceived_death_drive','number_of_physical_symptoms','type_of_physical_symptoms','level_of_addictive_tendency'])
#Merge on the patient 'id'
df_master = pd.merge(df1,df2, how='left',on='id')

print(df_master)
