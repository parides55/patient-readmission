import streamlit as st
import pandas as pd


def predict_readmission(
    X_live, readmission_pipeline_dc_fe,
    readmission_pipeline_model
):

    # from live data, subset features related to this pipeline
    X_live_readmission = X_live
    # apply data cleaning / feat engine pipeline to live data
    X_live_readmission_dc_fe = readmission_pipeline_dc_fe.transform(
        X_live_readmission)

    # predict
    readmission_prediction = readmission_pipeline_model.predict(
        X_live_readmission_dc_fe)
    readmission_prediction_proba = readmission_pipeline_model.predict_proba(
        X_live_readmission_dc_fe)

    # Create a logic to display the results
    readmission_prob = readmission_prediction_proba[
        0, readmission_prediction][0]*100
    if readmission_prediction == 1:
        readmission_result = 'will'
    else:
        readmission_result = 'will not'

    statement = (
        f'### There is {readmission_prob.round(1)}% probability '
        f'that this patient **{readmission_result} be readmitted**.')

    st.write(statement)

    return readmission_prediction
