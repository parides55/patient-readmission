import streamlit as st

def page_hypothesis_body():
    st.write(f"#### **Hypothesis**\n\n")
    
    st.info(
        f"###### **Hypothesis 1**\n"
        f"Patients with a higher number of lab procedures are more likely to be readmitted. "
        f"This hypothesis assumes that a higher number of lab procedures indicates a more severe "
        f"or complex medical condition, which could lead to a higher chance of readmission."
    )
    
    st.info(
        f"###### **Hypothesis 2**\n"
        f"Patients who had a change in their diabetes medication during their hospital stay "
        f"are more likely to be readmitted. This hypothesis suggests that changes in diabetes "
        f"management might lead to instability in blood sugar control, increasing the "
        f"likelihood of readmission."
    )
    
    st.info(
        f"###### **Hypothesis 3**\n"
        f"Patients with multiple comorbidities (diagnosed with multiple conditions) have a "
        f"higher probability of readmission. This hypothesis is based on the idea that "
        f"patients with multiple health issues are more challenging to manage and therefore "
        f"more likely to experience complications leading to readmission."
    )