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

#Let's separate out our categories of interest into two dataframes, which are nightmare patients and high-neurosis patients
nightmare_patients = df_master[df_master['nightmare_frequency']>2]

#How many nightmare-suffering patients are there?
print(len(nightmare_patients))

#Does this correlate with our high neurosis patients?

#Let's separate out the high-neurosis patients
high_neurosis_patients = df_master[df_master['level_of_neurosis']>8]
high_neurosis_patients.head(5)
print(len(high_neurosis_patients))

#It looks like we have 30 high-neurosis patients and 30 nightmare-suffering patients

#Let's see if nightmare patients have a higher average level of neurosis than the entire set of patients

#First, let's find the average level of neurosis for all patients
print(df_master['level_of_neurosis'].mean()) # == 7.04

#Second, let's find the average level of neurosis for nightmare patients
print(nightmare_patients['level_of_neurosis'].mean()) # == 6.76

#Nightmare patients have a slightly below average level of neurosis compared to all patients.

#I predict that when we compare the two sets of patients, we won't find many patients in common.

#First, let's simplify the dataframes down to the patient id in order to compare them easier
nightmare_list = nightmare_patients['id'].tolist()
high_neurosis_list = high_neurosis_patients['id'].tolist()

#Let's see how many nightmare patients are also in the high neurosis list
print(len([x for x in nightmare_list if x in high_neurosis_list])) # == 3
#Only 3!

#My prediction was correct. Let's keep investigating other groups of patients to see if nightmares correlate with any other factors.

#Let's look at the type of other symptoms that our nightmare patients suffer from
nightmare_symptom_list = nightmare_patients['type_of_physical_symptoms'].tolist()

freq_of_symp_in_nightmare = {}
for symptom in nightmare_symptom_list:
   # checking the element in dictionary
   if symptom in freq_of_symp_in_nightmare:
      # incrementing the count
      freq_of_symp_in_nightmare[symptom] += 1
   else:
      # initializing the count
      freq_of_symp_in_nightmare[symptom] = 1

# printing the frequency
print(freq_of_symp_in_nightmare)

#Plotting the frequency
# Create a pie chart
plt.pie(freq_of_symp_in_nightmare.values(), labels=freq_of_symp_in_nightmare.keys())
plt.show()

#It looks like our nightmare patients suffer from headaches and stomachaches the most.
#Is this higher than average?

total_symptom_list = df_master['type_of_physical_symptoms'].tolist()

freq_of_symp_master = {}
for symptom in total_symptom_list:
   if symptom in freq_of_symp_master:
      freq_of_symp_master[symptom] += 1
   else:
      freq_of_symp_master[symptom] = 1

# printing the frequency
print(freq_of_symp_master)

#Let's compare the rates of these symptoms in nightmare patients and our entire set
def calculate_percentages(dictionary):
    total_occurrences = sum(dictionary.values())
    percentages = {}
    for item, occurrences in dictionary.items():
        percentage = (occurrences / total_occurrences) * 100
        percentages[item] = percentage
    return percentages

nightmare_percentages = calculate_percentages(freq_of_symp_in_nightmare)
master_percentages = calculate_percentages(freq_of_symp_master)

#Find the diffeerence of rates between the two sets of patients
def dict_diff(dict1, dict2):
    result = {}
    for key in dict1.keys():
        if key in dict2:
            result[key] = dict1[key] - dict2[key]
    return result

print(dict_diff(nightmare_percentages,master_percentages))

#Is there any sort of relation between nightmares and the types of defense mechanisms people use?
#We can repeat the code above on our columns about defense mechanisms

unique_defenses = list(df_master['defense_mechanism'].unique())
#We have 6 defense mechanisms that patients were surveyed for.
print(df_master['defense_mechanism'].value_counts())
#And compare this to our nightmare patients
print(nightmare_patients['defense_mechanism'].value_counts())

nightmare_defense_list = nightmare_patients['defense_mechanism'].tolist()
master_defense_list = df_master['defense_mechanism']

#Let's count the occurances of each symptom in the two sets of patients
from collections import Counter
def count_occurrences(items):
    occurrences = Counter(items)
    return dict(occurrences)

print(count_occurrences(nightmare_defense_list))
print(count_occurrences(master_defense_list))

#Of the total 30 patients whose primary defense mechanism is denial, 29 of them are also sufferers of frequent nightmares

#Let's plot the kind of defenses against number of nightmares each patient experiences in our total dataframe.

grouped_data = df_master.groupby('defense_mechanism')['nightmare_frequency'].sum()

plt.bar(grouped_data.index, grouped_data.values)
plt.xlabel('defense_mechanism')
plt.ylabel('nightmare_frequency')
plt.title('Comparison of Defense Mechanisms and Nightmares')
plt.show()

#And let's do the same for our nightmare patient data
grouped_data1 = nightmare_patients.groupby('defense_mechanism')['nightmare_frequency'].sum()

plt.bar(grouped_data1.index, grouped_data1.values)
plt.xlabel('defense_mechanism')
plt.ylabel('nightmare_frequency')
plt.title('Comparison of Defense Mechanisms and Nightmares')
plt.show()

'''
Although our data shows a near-even split between all types of defenses (except repression),
Our nightmare patients exhibit denial as their primary symptom.
In psychoanalytic theory, denial would be the cause of a symptom type like high-nightmares,
so we should switch our focus from nightmare patients to denial patients and look for causal factors for their denial.
'''

#Let's create an entirely new dataframe to investigate our denial patients.

denial_patients = df_master[df_master['defense_mechanism']=='denial']
print(denial_patients.head())

#Let's collect some initial demographics
for col in denial_patients:
    print(denial_patients[col].value_counts())

'''
This is the demographic profile of our denial patients:

Most are male, most are widowed, most have 4-5 siblings, most's parents are still together,
Most were 10 or 11 when they experiences their first oedipal trauma, they dream 4 times per week,
They have nightmares, their most common attachment style is avoidant,
Their most common level of neurosis is 6 or 7, they have 10-11 slips per analytic session,
They have a high or low level of percieved death drive (at 4 or 8)
They experience headaches and stomachaches mostly, besides the nightmares
And they have 1 or 3 symptoms at a time (usually)

'''

#Are the rates of these measures higher than the rest of the data?
print('*************************')

for col in df_master:
    print(df_master[col].value_counts())

'''

It seems as though the only major difference is being widowed.
In our denial patients:
27 are widowed, 2 are divorced, and 1 is still married.
In our total patients:
single 61 are single, 31 are married, 30 are divorced, and 28 are widowed.

We have a trifecta of measurement: denial patients are almost always wodowed and experience a high frequency of nightmares.

Having found a demograph of interest, I will cease my exploratory data analysis here.

'''

