import streamlit as st
import pandas as pd

DATASET = pd.read_csv(f"outputs/datasets/collection/HospitalReadmission.csv").head(10)

def page_summary_body():
    st.write(f'#### **Project Summary**\n\n')
    
    st.write(
        f'Generally the hospital readmissions are costly for Hospitals and Health providers '
        f'and use a lot of resources that can be utilised better to achieve better and more '
        f'expeditious health care services.\n\n'
        f'The goal of this project is to develop a predictive analytics application that'
        f'forecasts the likelihood of patient readmission after discharge from the hospital. '
        f'This application aims to assist healthcare providers in identifying high-risk patients, '
        f'thereby enabling targeted interventions to reduce readmission rates and '
        f'improve patient outcomes.'
    )
    
    st.write(
        f"* Visit the [project's documentation](https://github.com/parides55/patient-readmission) "
        f"for more information.\n"
    )
    
    st.info(
        f"#### **Project's Dataset**\n\n"
        f"The dataset used in this project, sourced from Kaggle, contains 25,000 records of hospital "
        f"admissions, with 17 attributes describing various aspects of patient demographics, "
        f"clinical factors, and hospital stay details. Key features include: \n"
        f"* **Patient Demographics:** Age group.\n"
        f"* Hospital Stay Information: Length of stay (time_in_hospital), number of procedures, "
        f"medications, outpatient visits, inpatient visits, and emergency visits.\n"
        f"* Clinical Information: Primary, secondary, and tertiary diagnoses (diag_1, diag_2, diag_3), "
        f"glucose levels, and A1C test results.\n"
        f"* Treatment Information: Whether the patient's treatment plan included changes (change) "
        f"in their medication, and whether diabetes medications were administered (diabetes_med).\n"
        f"* Target Variable: A binary indicator (readmitted) showing whether the patient was readmitted.\n"
    )
    
    st.write(f"Below find the first 10 rows of the dataset.\n")
    
    st.dataframe(DATASET)
    
    st.info(
        f"#### **Feature Terminology**\n\n"
        f"* **age** - age bracket of the patient\n"
        f"* **time_in_hospital** - days (from 1 to 14)\n"
        f"* **n_procedures** - number of procedures performed during the hospital stay\n"
        f"* **n_lab_procedures** - number of laboratory procedures performed during the hospital stay\n"
        f"* **n_medications** - number of medications administered during the hospital stay\n"
        f"* **n_outpatient** - number of outpatient visits in the year before a hospital stay\n"
        f"* **n_inpatient** - number of inpatient visits in the year before the hospital stay\n"
        f"* **n_emergency** - number of visits to the emergency room in the year before the hospital stay\n"
        f"* **medical_specialty** - the specialty of the admitting physician\n"
        f"* **diag_1** - primary diagnosis (Circulatory, Respiratory, Digestive, etc.)\n"
        f"* **diag_2** - secondary diagnosis\n"
        f"* **diag_3** - additional secondary diagnosis\n"
        f"* **glucose_test** - whether the glucose serum came out as high (> 200), normal, or not performed\n"
        f"* **A1Ctest** - whether the A1C level of the patient came out as high (> 7%), normal, or not performed\n"
        f"* **change** - whether there was a change in the diabetes medication ('yes' or 'no')\n"
        f"* **diabetes_med** - whether a diabetes medication was prescribed ('yes' or 'no')\n"
        f"* **readmitted** - if the patient was readmitted at the hospital ('yes' or 'no')\n"
    )
    
    st.success(
        f"#### **Business Requirements**\n\n"
        f"**Business Requirements 1** - The client is interested to know the key factors "
        f"that will make a patient to be readmitted.\n\n"
        f"**Business Requirements 2** - The client is interested to know whether a patient "
        f"be readmitted or not by using patient's data.\n\n"
    )