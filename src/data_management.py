import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import joblib

# @st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_hospital_dataset(file_name):
    df = pd.read_csv(f"outputs/datasets/collection/{file_name}")
    return df


def load_pkl_file(file_path):
    return joblib.load(filename=file_path)


def plot_categorical(df, col):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax = sns.countplot(df, x=col, hue='readmitted')
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)


def plot_numerical(df, col):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax = sns.histplot(df, x=col, kde=True, hue='readmitted')
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)
    

def plot_parallel_plot():
    df_parallel = load_hospital_dataset("HospitalReadmissionsParallel.csv")
    fig = px.parallel_categories(df_parallel, color='readmitted', color_continuous_scale="bluered")
    st.plotly_chart(fig)