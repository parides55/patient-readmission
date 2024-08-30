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
    
#     X_live = DrawInputsWidgets()
    
#     # if st.button("Run Predictive Analysis"):
#     #     predict_patient_readmission(
#     #         X_live, dc_fe_pipeline, model_pipeline
#     #     )


# def DrawInputsWidgets():
    
#         # load dataset
#         df = load_hospital_dataset('HospitalReadmissions.csv')
#         percentageMin, percentageMax = 0.4, 2.0
    
#     # we create input widgets only for 6 features
#         col1, col2, col3, col4 = st.beta_columns(4)
#         col5, col6, col7, col8 = st.beta_columns(4)
    
#         # We are using these features to feed the ML pipeline - values copied from check_variables_for_UI() result
    
#         # create an empty DataFrame, which will be the live data
#         X_live = pd.DataFrame([], index=[0])
    
#         # from here on we draw the widget based on the variable type (numerical or categorical)
#         # and set initial values
#         with col1:
#             feature = "Contract"
#             st_widget = st.selectbox(
#                 label=feature,
#                 options=df[feature].unique()
#             )
#         X_live[feature] = st_widget
    
#         with col2:
#             feature = "InternetService"
#             st_widget = st.selectbox(
#                 label=feature,
#                 options=df[feature].unique()
#             )
#         X_live[feature] = st_widget
    
#         with col3:
#             feature = "MonthlyCharges"
#             st_widget = st.number_input(
#                 label=feature,
#                 min_value=df[feature].min()*percentageMin,
#                 max_value=df[feature].max()*percentageMax,
#                 value=df[feature].median()
#             )
#         X_live[feature] = st_widget
    
#         with col4:
#             feature = "PaymentMethod"
#             st_widget = st.selectbox(
#                 label=feature,
#                 options=df[feature].unique()
#             )
#         X_live[feature] = st_widget
    
#         with col5:
#             feature = "OnlineBackup"
#             st_widget = st.selectbox(
#                 label=feature,
#                 options=df[feature].unique()
#             )
#         X_live[feature] = st_widget
    
#         with col6:
#             feature = "PhoneService"
#             st_widget = st.selectbox(
#                 label=feature,
#                 options=df[feature].unique()
#             )
#         X_live[feature] = st_widget
    
#         # st.write(X_live)
    
#         return X_live