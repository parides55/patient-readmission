import streamlit as st
from app_pages.multipage import Multipage

from app_pages.page_hypothesis import page_hypothesis_body
from app_pages.page_project_summary import page_summary_body

app = Multipage(app_name="Patient readmission prediction")

app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Hypothesis", page_hypothesis_body)

app.run()