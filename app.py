import streamlit as st
from app_pages.multipage import Multipage

from app_pages.page_hypothesis import page_hypothesis_body
from app_pages.page_project_summary import page_summary_body
from app_pages.page_correlation import page_correlation_body
from app_pages.page_predict_readmission import page_prediction_body
from app_pages.page_ml_performance import page_ML_performance_body

app = Multipage(app_name="Patient readmission prediction")

app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Hypothesis", page_hypothesis_body)
app.add_page("Correlation study", page_correlation_body)
app.add_page("Patient Readmission Prediction", page_prediction_body)
app.add_page("ML Performance", page_ML_performance_body)

app.run()