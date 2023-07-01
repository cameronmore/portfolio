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

'''

I don't want to find the rate of each item in a given dictionary separately,
I want to iterate through the dictionary and return a new dictionary with the values as percentages

I know thatthis code works:
def get_symptom_percentage(dictionary, item):
         return (dictionary[item] * 1.0 / sum(dictionary.values()))*100

Can I use that function to iterate through a dictionary?

def get_symptom_rates(dictionary):
   for item in dictionary.items():
      def get_symptom_percentage(dictionary, item):
         return (dictionary[symptom] * 1.0 / sum(dictionary.values()))*100
      get_symptom_percentage(dictionary, item)


get_symptom_rates(freq_of_symp_in_nightmare)

Or should I totally scratch that and just create a new function that iterates through the dictionary and returns the rate of the values

Could I do this:
def rates_of_values(dictionary):
   for k, v in dictionary:
      d={}
      d[k] = dictionary[v] * 1.0 / sum(dictionary.values())

'''

