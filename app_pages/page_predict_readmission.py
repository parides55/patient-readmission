import streamlit as st
import pandas as pd

from src.data_management import load_hospital_dataset, load_pkl_file
#from src.machine_learning.predict_readmission import predict_patient_readmission

def page_prediction_body():
    
    version = "v1"
    # dc_fe_pipeline = load_pkl_file(
    #     f"outputs/ml_pipeline/predict_readmission/{version}/data_cleaning_and_feat_engineering_pipeline.pkl"
    # )
    # model_pipeline = load_pkl_file(
    #     f"outputs/ml_pipeline/predict_readmission/{version}/classification_pipeline.pkl"
    # )
    
    st.info(
        f"##### Business requirement 2: Classification Model\n\n"
        f" - We need to predict whether a patient will be readmitted or not.\n"
        f" - For this task we need to build a binary classification model.\n"
        f" - Extensive hyperparameter optimization will give us the best "
        f"chance at a highly accurate prediction.\n"
    )
    
    st.write("---")
    
    X_live = DrawInputsWidgets()
    
    if st.button("Run Predictive Analysis"):
        st.write("predict_patient_readmission(X_live, dc_fe_pipeline, model_pipeline)"
        )


def DrawInputsWidgets():
    
        # load dataset
        df = load_hospital_dataset('HospitalReadmissions.csv')
    
    # we create input widgets only for 6 features
        col1, col2, col3, col4, col5 = st.columns(5)
        col6, col7, col8, col9, col10 = st.columns(5)
        col11, col12, col13, col14, col15 = st.columns(5)
    
        # create an empty DataFrame, which will be the live data
        X_live = pd.DataFrame([], index=[0])
    
        # from here on we draw the widget based on the variable type (numerical or categorical)
        # and set initial values
        with col1:
            feature = "age"
            st_widget = st.selectbox(
                label=feature,
                options=df[feature].unique()
            )
        X_live[feature] = st_widget
    
        with col2:
            feature = "time_in_hospital"
            st_widget = st.number_input(
            label=feature,
            min_value=0,
            value=int(df[feature].median())
            )
        X_live[feature] = st_widget
    
        with col3:
            feature = "n_lab_procedures"
            st_widget = st.number_input(
            label=feature,
            min_value=0,
            value=int(df[feature].median())
            )
        X_live[feature] = st_widget
    
        with col4:
            feature = "n_procedures"
            st_widget = st.number_input(
            label=feature,
            min_value=0,
            value=int(df[feature].median())
            )
        X_live[feature] = st_widget
    
        with col5:
            feature = "n_medications"
            st_widget = st.number_input(
            label=feature,
            min_value=0,
            value=int(df[feature].median())
            )
        X_live[feature] = st_widget
    
        with col6:
            feature = "n_outpatient"
            st_widget = st.number_input(
            label=feature,
            min_value=0,
            value=int(df[feature].median())
            )
        X_live[feature] = st_widget
        
        with col7:
            feature = "n_inpatient"
            st_widget = st.number_input(
            label=feature,
            min_value=0,
            value=int(df[feature].median())
            )
        X_live[feature] = st_widget
        
        with col8:
            feature = "n_emergency"
            st_widget = st.number_input(
            label=feature,
            min_value=0,
            value=int(df[feature].median())
            )
        X_live[feature] = st_widget
        
        with col9:
            feature = "diag_1"
            st_widget = st.selectbox(
                label=feature,
                options=df[feature].unique()
            )
        X_live[feature] = st_widget
        
        with col10:
            feature = "diag_2"
            st_widget = st.selectbox(
                label=feature,
                options=df[feature].unique()
            )
        X_live[feature] = st_widget
        
        with col11:
            feature = "diag_3"
            st_widget = st.selectbox(
                label=feature,
                options=df[feature].unique()
            )
        X_live[feature] = st_widget
        
        with col12:
            feature = "glucose_test"
            st_widget = st.selectbox(
                label=feature,
                options=df[feature].unique()
            )
        X_live[feature] = st_widget
        
        with col13:
            feature = "A1Ctest"
            st_widget = st.selectbox(
                label=feature,
                options=df[feature].unique()
            )
        X_live[feature] = st_widget
        
        with col14:
            feature = "change"
            st_widget = st.selectbox(
                label=feature,
                options=df[feature].unique()
            )
        X_live[feature] = st_widget
        
        with col15:
            feature = "diabetes_med"
            st_widget = st.selectbox(
                label=feature,
                options=df[feature].unique()
            )
        X_live[feature] = st_widget
    
        return X_live