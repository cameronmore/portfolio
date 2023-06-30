import pandas as pd
import matplotlib.pyplot as plt

##1. Merge the two datasets

#Read the first dataset, which serves as our core
df1 = pd.read_csv('PsychData.csv')
#Read only part of the second which we will merge with the core
df2 = pd.read_csv('AlterPsychData.csv', usecols=['id','level_of_neurosis','number_of_freudian_slips_per_analytic_session','level_of_perceived_death_drive','number_of_physical_symptoms','type_of_physical_symptoms'])
#Merge on the patient 'id'
df_master = pd.merge(df1,df2, how='left',on='id')

#Find any initial visual correlation
df_master.plot(x='number_of_freudian_slips_per_analytic_session',y='level_of_neurosis')
df_master.boxplot('nightmare_frequency')

#Now that we see there are a number of nigh-nigtmare patients, let's investigate further

#Let's separate out our categories of interest into two dataframes
nightmare_patients = df_master[df_master['nightmare_frequency']>2]

#How many nightmare-suffering patients are there?
print(len(nightmare_patients))

#Does this correlate with our high neurosis patients?

#Let's separate out the high-neurosis patients first
high_neurosis_patients = df_master[df_master['level_of_neurosis']>8]
high_neurosis_patients.head(5)
print(len(high_neurosis_patients))

#It looks like we have 30 high-neurosis patients and 30 nightmare-suffering patients

#Let's see if nightmare patients have a higher average level of neurosis than the entire set of patients
