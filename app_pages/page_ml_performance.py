import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

from src.data_management import load_pkl_file
from src.machine_learning.evaluate_clf import clf_performance


def page_ML_performance_body():

    version = 'v1'
    # load needed files for the page
    dc_fe_pipeline = load_pkl_file(
        f"outputs/ml_pipeline/predict_readmission/{version}/"
        f"clf_pipeline_data_cleaning_feat_eng.pkl"
    )
    model_pipeline = load_pkl_file(
        f"outputs/ml_pipeline/predict_readmission/{version}/"
        f"clf_pipeline_model.pkl"
    )
    best_features = (pd.read_csv(f"outputs/ml_pipeline/predict_readmission/"
                                 f"{version}/X_train.csv").columns.to_list())
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_readmission/{version}/X_train.csv"
        )
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_readmission/{version}/y_train.csv"
        )
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_readmission/{version}/X_test.csv"
        )
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_readmission/{version}/y_test.csv"
        )
    features_importance = plt.imread(
        f"outputs/ml_pipeline/predict_readmission/{version}/"
        f"features_importance.png"
        )

    st.write(f"### ML Pipeline: Binary Classification Model\n\n")

    st.info(
        f"The model is trained to predict whether a patient will be "
        f"readmitted or not following a hospital visit.\n"
        f"* For this tasks we set the following success metrics:\n"
        f"  - at least 70% recall for readmission on the train and test sets\n"
        f"* The model will be considered a failure if:\n"
        f"  - the model fails to achieve 70% recall for readmission.\n"
        f"  - the model fails to achieve 60% precision for no readmission "
        f"(falsely indicating patients are at risk).\n"
    )

    st.write("---")

    # display the 2 pipelines used in the model
    st.write(
        f"#### The 2 Pipelines used in the model are:\n"
        f"1. Data Cleaning and Feature Engineering Pipeline\n"
    )

    st.write(dc_fe_pipeline)

    st.write(
        f"2. Feature Scaling and Modeling Pipeline\n"
    )

    st.write(model_pipeline)

    st.write("---")

    # display important features that the model was trained on
    st.write("* The features the model was trained and their importance.")
    st.write(X_train.columns.to_list())
    st.image(features_importance)

    st.write("---")

    # display the performance of the model on the train and test sets
    st.write("#### Pipeline Performance")
    clf_performance(X_train=X_train, y_train=y_train,
                    X_test=X_test, y_test=y_test,
                    pipeline=model_pipeline,
                    label_map=["Will readmit", "Will not readmit"])
