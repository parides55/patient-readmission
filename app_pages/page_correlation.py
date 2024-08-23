import streamlit as st
import numpy as np
import plotly.express as px
import ppscore as pps
from feature_engine.discretisation import ArbitraryDiscretiser
from feature_engine.encoding import OrdinalEncoder
from src.data_management import load_hospital_dataset, plot_categorical, plot_numerical, plot_parallel_plot

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")


def correlation(df, method):
    
    ordinal = OrdinalEncoder(encoding_method='arbitrary',
                            variables=df.columns[df.dtypes == 'object'].tolist())
    df_encoded = ordinal.fit_transform(df)
    
    corr = df_encoded.corr(method=method)["readmitted"].sort_values(
        ascending=False, key=abs)[1:].head(10)
    
    return corr


def heatmap_pps(df, threshold, figsize=(20, 12), font_annot=8):
    
    pps_matrix_raw = pps.matrix(df)
    pps_matrix = pps_matrix_raw.filter(['x', 'y', 'ppscore']).pivot(
        columns='x', index='y', values='ppscore')
    
    if len(pps_matrix.columns) > 1:
        mask = np.zeros_like(pps_matrix, dtype=bool)
        mask[abs(pps_matrix) < threshold] = True
        fig, ax = plt.subplots(figsize=figsize)
        ax = sns.heatmap(pps_matrix, annot=True, xticklabels=True, yticklabels=True,
                        mask=mask, cmap='rocket_r', annot_kws={"size": font_annot},
                        linewidth=0.05, linecolor='grey')
        plt.ylim(len(pps_matrix.columns), 0)
        st.pyplot(fig)


def plot_correlated_features(df, features):
    for feature in features:
        if df[feature].dtype == "object":
            plot_categorical(df, feature)
        else:
            plot_numerical(df, feature)


def page_correlation_body():
    
    #load data
    df=load_hospital_dataset()
    
    #copied from the EDAandCorrelation notebook
    correlated_features = ['diabetes_med',
                    'n_emergency',
                    'n_inpatient',
                    'n_medications',
                    'n_outpatient',
                    'n_procedures'
                    ]
    
    st.write(f"### **Feature Analysis**\n\n")
    
    # Business requirement 1
    st.info(
        f"**Business requirement 1:**  Data Visualization and Correlation study\n"
        f" - We need to perform a correlation study to determine which features correlate "
        f"most closely to the target.\n"
        f" - A Pearson's correlation will indicate linear relationships between "
        f"numerical variables.\n"
        f" - A Spearman's correlation will measure the monotonic relationships "
        f"between variables.\n"
        f" - A Predicitve Power Score can also be used to determine relationships "
        f"between the variables and if they have any predictive power against "
        f"the target variable.\n"
    )
    
    # inspect data
    if st.checkbox("Inspect Patient Information Dataset"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 10 rows."
            )

        st.write(df.head(10))
        
    st.write("---")
    
    # Correlation and PPS Study Summary
    st.write(
        f"#### **Correlation and PPS Study Summary**\n\n"
        f"* A correlation study was conducted in the notebook to better understand how "
        f"the feature variables are correlated and try to identify a pattern which will possibly "
        f"help in the prediction of the target variable.\n"
        f"After performing Spearman and Pearson correlation, the following variables "
        f"are the most correlated: **{correlated_features}**\n"
        f"* The correlation study revealed 'very weak' to 'weak' correlation between the "
        f"feature variables and the target variable. \n"
        f"* Also, the PPS score was calculated to determine the predictive power of the "
        f"variables, but it didn't show any predictive power for the target variable.\n"
    )
    
    #checkboxes
    if st.checkbox("View **Pearson** correlation results"):
        st.write(correlation(df, method="pearson"))
    if st.checkbox("View **Spearman** correlation results"):
        st.write(correlation(df, method="spearman"))
    if st.checkbox("View PPS heatmap"):
        st.write(heatmap_pps(df, 0.02))
    
    st.write("---")
    
    st.write(
        f"### **Most Correlated Features**\n\n"
        f"Below we are plotting the most correlated features with the target variable "
        f"in a coountplot and also we are using a parallel plot to better visualize the "
        f"pattern.\n"
    )
    
    if st.checkbox("View Countplot"):
        plot_correlated_features(df, correlated_features)
    if st.checkbox("View Parallel Plot"):
        plot_parallel_plot()
    
    st.success(
        f"From the above correlation study and and by plotting the most correlated features "
        f"we notice a pattern for the readmitted patients.\n"
        f"* A readmitted patient receives medicines for diabetes\n"
        f"* A readmitted patient has 0 or very low number of emergency/inpatient/outpatient visits.\n"
        f"* A readmitted patient receives between 11 and 20 medicines.\n"
        f"* A readmitted patient has 0 or very low number of procedures."
    )
