import streamlit as st
import pandas as pd

DATASET = pd.read_csv(
    f"outputs/datasets/collection/HospitalReadmissions.csv").head(10)


def page_summary_body():
    st.write(f'#### **Project Summary**\n\n')

    st.write(
        f'Generally the hospital readmissions are costly for Hospitals and '
        f'Health providers and use a lot of resources that can be utilised '
        f'better to achieve better and more expeditious health care '
        f'services.\n\n'
        f'The goal of this project is to develop a predictive analytics '
        f'application that forecasts the likelihood of patient readmission '
        f'after discharge from the hospital.'
        f'This application aims to assist healthcare providers in identifying '
        f'high-risk patients, thereby enabling targeted interventions to '
        f'reduce readmission rates and improve patient outcomes.'
    )

    st.write(
        f"* Visit the [project's documentation](https://github.com/"
        f"parides55/patient-readmission) for more information.\n"
    )

    st.info(
        f"#### **Project's Dataset**\n\n"
        f"The dataset used in this project, sourced from Kaggle, contains "
        f"25,000 records of hospital admissions, with 17 attributes "
        f"describing various aspects of patient demographics, clinical "
        f"factors, and hospital stay details. Key features include: \n"
        f"* **Patient Demographics:** Age group.\n"
        f"* Hospital Stay Information: Length of stay (time_in_hospital), "
        f"number of procedures, medications, outpatient visits, "
        f"inpatient visits, and emergency visits.\n"
        f"* Clinical Information: Primary, secondary, and tertiary diagnoses "
        f"(diag_1, diag_2, diag_3), glucose levels, and A1C test results."
        f"*(The A1C test is a common blood test used to diagnose type 1 and "
        f"type 2 diabetes. if you're living with diabetes, the test is also "
        f"used to monitor how well you're managing blood sugar levels.)*\n"
        f"* Treatment Information: Whether the patient's treatment plan "
        f"included changes (change) in their medication, and whether diabetes "
        f"medications were administered (diabetes_med).\n"
        f"* Target Variable: A binary indicator (readmitted) showing whether "
        f"the patient was readmitted.\n"
    )

    st.write(f"Below find the first 10 rows of the dataset.\n")

    st.dataframe(DATASET)

    st.info(
        f"#### **Feature Terminology**\n\n"
        f"* **age** - age bracket of the patient\n"
        f"* **time_in_hospital** - days (from 1 to 14)\n"
        f"* **n_procedures** - number of procedures performed during the "
        f"hospital stay\n"
        f"* **n_lab_procedures** - number of laboratory procedures performed "
        f"during the hospital stay\n"
        f"* **n_medications** - number of medications administered during the "
        f"hospital stay\n"
        f"* **n_outpatient** - number of outpatient visits in the year before "
        f"a hospital stay\n"
        f"* **n_inpatient** - number of inpatient visits in the year before "
        f"the hospital stay\n"
        f"* **n_emergency** - number of visits to the emergency room in the "
        f"year before the hospital stay\n"
        f"* **medical_specialty** - the specialty of the admitting physician\n"
        f"* **diag_1** - primary diagnosis (Circulatory, Respiratory, "
        f"Digestive, etc.)\n"
        f"* **diag_2** - secondary diagnosis\n"
        f"* **diag_3** - additional secondary diagnosis\n"
        f"* **glucose_test** - whether the glucose serum came out as high "
        f"(> 200), normal, or not performed\n"
        f"* **A1Ctest** - whether the A1C level of the patient came out as "
        f"high (> 7%), normal, or not performed\n"
        f"* **change** - whether there was a change in the diabetes "
        f"medication (1 = 'yes' or 0 = 'no')\n"
        f"* **diabetes_med** - whether a diabetes medication was prescribed "
        f"(1 = 'yes' or 0 = 'no')\n"
        f"* **readmitted** - if the patient was readmitted at the hospital "
        f"(1 = 'yes' or 0 = 'no')\n"
    )

    st.success(
        f"#### **Business Requirements**\n\n"
        f"**Business Requirements 1** - The client is interested to know the "
        f"key factors that will make a patient to be readmitted.\n\n"
        f"**Business Requirements 2** - The client is interested to know "
        f"whether a patient will be readmitted or not by using patient's "
        f"data.\n\n"
    )
