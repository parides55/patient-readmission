import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import joblib

# @st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_hospital_dataset():
    df = pd.read_csv("outputs/datasets/collection/HospitalReadmissions.csv")
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
    df_parallel_to_plot = pd.read_csv("outputs/datasets/collection/HospitalReadmissionsParallel.csv")
    fig = px.parallel_categories(df_parallel_to_plot, color='readmitted')
    st.plotly_chart(fig)