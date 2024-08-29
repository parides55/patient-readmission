import streamlit as st
import pandas as pd

from src.data_management import load_hospital_dataset, load_pkl_file
#from src.machine_learning.classification import predict_patient_readmission

def page_prediction_body():
    
    st.info(
        f"##### Business requirement 2: Classification Model\n\n"
        f" - We need to predict whether a patient will be readmitted or not.\n"
        f" - For this task we need to build a binary classification model.\n"
        f" - This will be performed during the Modeling and Evaluation step of "
        f"the CRISP -M workflow.\n"
    )
    
    X_live = DrawInputWidgets()
    
    # if st.button("Run Predictive Analysis"):
    #     predict_patient_readmission(
    #         X_live, dc_fe_pipeline, model_pipeline
    #     )


def DrawInputWidgets():
    
    df= load_hospital_dataset("HospitalReadmissions.csv")