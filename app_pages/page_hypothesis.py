import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import ttest_ind, chi2_contingency, pearsonr
from src.data_management import load_hospital_dataset


def hypothesis_1():
    
    df_parallel = load_hospital_dataset("HospitalReadmissionsParallel.csv")
    df = load_hospital_dataset("HospitalReadmissions.csv")

    st.dataframe(
        df_parallel[['n_lab_procedures_bins','readmitted']]
        .value_counts(normalize=True).mul(100).round(2)
        )

    fig, ax = plt.subplots(figsize=(8,4))
    ax = sns.countplot(data=df_parallel, x=df_parallel['n_lab_procedures_bins'], hue=df_parallel['readmitted'])
    st.pyplot(fig)

    # Hypothesis 1: Correlation between number of lab procedures and readmission
    # Pearson correlation test between n_lab_procedures and readmitted
    correlation, p_value_correlation = pearsonr(df['n_lab_procedures'], df['readmitted'])

    # Hypothesis 1: T-test to compare average lab procedures between readmitted and non-readmitted patients
    readmitted_lab_procedures = df[df['readmitted'] == 1]['n_lab_procedures']
    non_readmitted_lab_procedures = df[df['readmitted'] == 0]['n_lab_procedures']

    t_stat_lab_procedures, p_value_lab_procedures = ttest_ind(readmitted_lab_procedures, non_readmitted_lab_procedures)

    # Results

    st.write(f"Hypothesis 1 - Correlation: {correlation}, {p_value_correlation}")
    st.write(f"Hypothesis 1 - T-test: {t_stat_lab_procedures}, {p_value_lab_procedures}")


def hypothesis_2():
    
    df = load_hospital_dataset("HospitalReadmissions.csv")
    
    st.dataframe(
        df[['change','readmitted', 'diabetes_med']]
    .value_counts(normalize=True).mul(100).round(2)
    )
    
    fig,ax = plt.subplots(figsize=(8,4))
    ax = sns.barplot(data=df, x='change', y='readmitted', hue='diabetes_med')
    st.pyplot(fig)
    
    # Hypothesis 2: Chi-Square test between change in diabetes medication and readmission
    contingency_table = pd.crosstab(df['change'], df['readmitted'])
    chi2, p_value_chi2, _, _ = chi2_contingency(contingency_table)

    # Results
    st.write(f"Hypothesis 2 - Chi-Square Test: {chi2}, {p_value_chi2}")
    

def hypothesis_3():
    
    df = load_hospital_dataset("HospitalReadmissions.csv")
    
    st.dataframe(
        df[['age']].value_counts(normalize=True).mul(100).round(2)
        )
    
    fig,ax = plt.subplots(figsize=(8,4))
    ax = sns.countplot(data=df, x=df['age'], hue=df['readmitted'])
    st.pyplot(fig)
        
    def categorize_age(age):
        if age in ['[0-10)', '[10-20)', '[20-30)', '[30-40)', '[40-50)', '[50-60)']:
            return 'Under 60'
        elif age in ['[60-70)', '[70-80)']:
            return '60-80'
        elif age in ['[80-90)', '[90-100)']:
            return 'Over 80'
        else:
            return 'Unknown'  # For any unexpected values

    # Apply the function to create a new column with categorized age groups
    df_age_group = df[['age']].copy()
    df_age_group['age_group'] = df['age'].apply(categorize_age)
    
    df_age_group['age_group'].value_counts(normalize=True).mul(100).round(2).astype(str) + '%'
    
    contingency_table_age = pd.crosstab(df_age_group['age_group'], df['readmitted'])
    chi2_age, p_value_age, _, _ = chi2_contingency(contingency_table_age)
    
    # Results
    st.write(f"Chi-Square Statistic: {chi2_age}")
    st.write(f"P-Value: {p_value_age}")


def page_hypothesis_body():
    st.write(f"#### **Hypothesis**\n\n")
    
    st.info(
        f"###### **Hypothesis 1**\n"
        f"Patients with a higher number of lab procedures are more likely to be readmitted. "
        f"This hypothesis assumes that a higher number of lab procedures indicates a more severe "
        f"or complex medical condition, which could lead to a higher chance of readmission."
    )
    
    st.write(f"##### Findings:\n\n")
    
    st.warning(
        f"* There is a very weak positive correlation between the number of lab procedures and readmission, but it is statistically significant due to the low p-value.\n\n"
        f"**Conclusion**: Hypothesis 1 is supported by the data, as there is a statistically significant but weak relationship between the number of lab procedures and the likelihood of readmission."
    )
    
    if st.checkbox("Check the data for hypothesis 1"):
        hypothesis_1()
    
    st.info(
        f"###### **Hypothesis 2**\n"
        f"Patients who had a change in their diabetes medication during their hospital stay "
        f"are more likely to be readmitted. This hypothesis suggests that changes in diabetes "
        f"management might lead to instability in blood sugar control, increasing the "
        f"likelihood of readmission."
    )
    
    st.write(f"##### Findings:\n\n")
    
    st.success(
            f"There is a significant association between a change in diabetes medication and readmission.\n\n"
            f"**Conclusion**: Hypothesis 2 is strongly supported by the data, indicating that patients who had a change in their diabetes medication are indeed more likely to be readmitted."
        )
        
    if st.checkbox("Check the data for hypothesis 2"):
        hypothesis_2()
    
    st.info(
        f"###### **Hypothesis 3**\n"
        f"Patients of higher age have a higher probability of readmission. This hypothesis "
        f"is based on the idea that patients of higher age are more likely to have multiple "
        f"chronicle health issues leading to readmissions."
    )
    
    st.write(f"##### Findings:\n\n")
    
    st.success(
                f"The very low p-value indicates a statistically significant association between age group and readmission. This suggests that patients of higher age groups are more likely to be readmitted, supporting Hypothesis 3.\n\n"
                f"**Conclusion**: Hypothesis 3 is valid based on the data, indicating that higher age groups have a higher probability of readmission."
            )
            
    if st.checkbox("Check the data for hypothesis 3"):
        hypothesis_3()