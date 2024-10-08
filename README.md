# [Patient Readmission Predictor](https://patient-readmission-c43bc847bc51.herokuapp.com/) - A Predictive Classification Model for predicting patient's readmission

![Responsive image showing the live website](https://github.com/parides55/patient-readmission/blob/2de65ccfcb550cf578b83a414a5bbb5d84002f37/assets/readme_docs/am_i_responsivepng.png)

Generally the hospital readmissions are costly for Hospitals and Health providers and use a lot of resources that can be utilized better to achieve better and more expeditious health care services.

The goal of this project is to develop a predictive analytics application that forecasts the likelihood of patient readmission after discharge from the hospital. This application aims to assist healthcare providers in identifying high-risk patients, thereby enabling targeted interventions to reduce readmission rates and improve patient outcomes.

To achieve the goal I have used a binary classification model and through data analysis and visualization I have made3 hypotheses.

## Table of Contents

- [Dataset Content](#dataset-content)
- [Business Requirements](#business-requirements)
- [Hypothesis and how to validate?](#hypothesis-and-how-to-validate)
- [The rationale to map the business requirements to the Data Visualizations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualizations-and-ml-tasks)
- [ML Business Case](#ml-business-case)
- [Epics and User Stories](#epics-and-user-stories)
- [Dashboard Design](#dashboard-design)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

## Dataset Content

Tha dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/dubradave/hospital-readmissions) and provides access to ten years of patient information. Each row represents a patient and each column contains information regarding the patient's hospital admission and if the patient has been readmitted.

| Value             | Meaning                                   | Unit           |
|-------------------|-------------------------------------------|----------------|
| age               | Age group of the patient                  | Years          |
| time_in_hospital  | Duration of hospital stay                 | Days           |
| n_lab_procedures  | Number of lab procedures performed        | Count          |
| n_procedures      | Number of other procedures performed      | Count          |
| n_medications     | Number of medications prescribed          | Count          |
| n_outpatient      | Number of outpatient visits               | Count          |
| n_inpatient       | Number of inpatient visits                | Count          |
| n_emergency       | Number of emergency visits                | Count          |
| medical_specialty | Medical specialty of the attending doctor | Speciality of physician|
| diag_1            | Primary diagnosis                         | Diagnosis Code |
| diag_2            | Secondary diagnosis                       | Diagnosis Code |
| diag_3            | Tertiary diagnosis                        | Diagnosis Code |
| glucose_test      | Whether a glucose test was performed      | high(>200)/ normal/ not performed|
| A1Ctest           | Whether an A1C test was performed         | high(>7%)/ normal/ not performed|
| change            | Change in diabetes medication             | Yes/No         |
| diabetes_med      | Whether diabetes medication was prescribed| Yes/No         |
| readmitted        | Whether the patient was readmitted        | Yes/No         |

[Back to top](#table-of-contents)

## Business Requirements

This project aims to reduce patient readmission rates to improve healthcare quality and reduce costs. Potential stakeholders/clients can Healthcare providers, hospital administrators, insurance companies.

- Business requirement 1
  - By performing data analysis identify key factors and patterns that could contribute to patient readmission. This should help healthcare providers identify high-risk patients and implement targeted interventions to reduce readmission rates.

- Business requirement 2
  - By using a dashboard, the client, can input patient's information and predict whether this patient is likely to be readmitted or not.

[Back to top](#table-of-contents)

## Hypothesis and how to validate?

- Hypothesis 1:

  - Patients with a higher number of lab procedures are more likely to be readmitted. This hypothesis assumes that a higher number of lab procedures indicates a more severe or complex medical condition, which could lead to a higher chance of readmission.
  - **Validation** : By ploting the two variables, carying out a correlation study between them and perform statistical test.

- Hypothesis 2:

  - Patients who had a change in their diabetes medication during their hospital stay are more likely to be readmitted. This hypothesis suggests that changes in diabetes management might lead to instability in blood sugar control, increasing the likelihood of readmission.
  - **Validation** : By ploting the "change" variable and the target variable "readmitted " in a barplot and using variable "diabetes_med" as hue and perform statistical tests.

- Hypothesis 3:

  - Patients of higher age have a higher probability of readmission. This hypothesis is based on the idea that patients of higher age are more likely to have multiple chronicle health issues leading to readmissions.
  - **Validation** : Groupe the various age categories to see their distribution against the target variable "readmitted" and perform statistical tests.

[Back to top](#table-of-contents)

## The rationale to map the business requirements to the Data Visualizations and ML tasks

- Business requirement 1: Data Visualization and Correlation study
  - We need to perform a correlation study to determine which features correlate most closely to the target.
  - A Pearson's correlation will indicate linear relationships between numerical variables.
  - A Spearman's correlation will measure the monotonic relationships between variables.
  - A Predicitve Power Score can also be used to determine relationships between the variables and if they have any predictive power to against the target variable.
  - This will be performed during the Data Collection and Preparation steps of the CRISP-DM workflow.

- Business requirement 2: Classification Model
  - We need to predict whether a patient will be readmitted or not.
  - For this task we need to build a binary classification model.
  - Extensive hyperparameter optimization will give us the best chance at a highly accurate prediction.
  - This will be performed during the Modeling and Evaluation step of the CRISP -M workflow.

[Back to top](#table-of-contents)

## ML Business Case

Classification Model

- We want a ML model to predict whether a patient be readmitted after being released from hospital based upon previously gathered patient data. The target variable, 'readmitted', is categorical and contains two classes: 0 (not readmitted) and 1 (readmitted).
- We will consider a classification model, a supervised model with a two-class output that matches the target.
- The model success metrics are:
  - at least 70% recall for readmission on the train and test sets
- The model will be considered a failure if:
  - the model fails to achieve 70% recall for readmission
  - the model fails to achieve 60% precision for no readmission (falsely indicating patients are at risk, which still will not put patient's in danger)
- The model output is defined as a text output, indicating the probability of a patient to be readmitted or not.
- The training data to fit the model comes from: [Kaggle](www.kaggle.com )
- The dataset contains: 25000 observations and 16 attributes.
- Target: readmitted; Features: all other attributes.

[Back to top](#table-of-contents)

## Epics and User Stories

For better planning, preparation and execution of this project I have decided to divide the project into 5 Epics. Below I'm listing the user stories for each Epic.

### Epic 1 : Data Collection and Preparation

- As a data analyst, I need to gather and pre-process patient data to ensure it is ready for analysis.

### Epic 2 : Data Analysis, Visualization and Cleaning

- As a data analyst I can visualize each feature and its distribution so I can determine what cleaning tasks I need to carry out.
- As a data analyst I can find and handle appropriately missing data so I can prepare the dataset for ML model.
- As a data analyst I can determine whether the target variable requires balancing so I can ensure the ML model is not fed imbalance data.
- As a data scientist I can carry out feature engineering so I can best transform data for the ML model
- As a data scientist I can visualize and analyze the dataset so i can determine which attributes correlate most with the target variable and validate the project's hypotheses.

### Epic 3: Model Training, Otpimization and Validation

- As data engineer I can determine the best algorith and best hyperparameters so I can ensure the ML model gives the best results.
- As data engineer I can determine the best features from the ML pipeline to determine whether the ML model can be optimized further.
- As data scientist I can evaluate the ML model's performance to determine whether it can successfully predict patient readmission.

### Epic 4 : Dashboard Design and Development

- As a non-technical user, I can view a project summary that describes the project, dataset and business requirements so I can understand what the project is about.
- As a non-technical user, I can view the project hypotheses and validations to determine what the project was trying to achieve and whether it was successful.
- As a technical user, I can view the correlation analysis to see how the outcomes were reached.
- As a non-technical/technical user, I can enter unseen data into the model and receive a prediction.
- As a technical user, I can view all the data to understand the model performance and see statistics related to the model.

### Epic 5: Dashboard Deployment and Release

- As a user, I can view the project dashboard on a live deployed website.

[Back to top](#table-of-contents)

## Dashboard Design

### Page 1: Project Summary

- Section 1- Quick summary
  - Introduction to project
  - Description of dataset, where was it sourced
  - Link to readme
- Section 2 - Business Requirements
  - Description of business requirements

### Page 2: Project Hypotheses

- Outline the three project hypothesis
- Present validation of each hypothesis
- Each hypothesis has a checkbox. When its checked presents the associated plot and results from statisticla tests.

### Page 3: Feature Correlation study

- State business requirement 1
- Overview of dataset - display first 10 rows of data and describe dataset shape
- Display correlation results and PPS heatmap
- Display distributions of correlated features against target using a parallel plot.
- Conclusions

### Page 4: Predict Patient readmission

- State business requirement 2
- Widget inputs for prediction
- "Run prediction" button to run inputted data through the ML model and output a prediction and % chance

### Page 5: Classification Performance Metrics

- Summary of model performance and metrics
- Model pipeline, features used to train the model and how they were selected
- Documentation of model performance on train and test sets

[Back to top](#table-of-contents)

## Technologies Used

The technologies used throughout the development are listed below:

### Languages

- Python

### Python Packages

- [Pandas](https://pandas.pydata.org/docs/index.html) - Open source library for data manipulation and analysis.
- [Numpy](https://numpy.org/doc/stable/index.html) - Adds support for large, multi-dimensional arrays and matrices, and high-level mathematical functions.
- [YData Profiling](https://docs.profiling.ydata.ai/latest/) - For data profiling and exploratory data analysis.
- [Matplotlib](https://matplotlib.org/) - Comprehensive library for creating static, animated and interactive visualizations.
- [Seaborn](https://seaborn.pydata.org/) - Another data visualization library for drawing attractive and informative statistical graphics.
- [Plotly Express](https://plotly.com/python/) - OAnother data visualization library for drawing attractive and informative statistical graphics.
- [Feature-engine](https://feature-engine.trainindata.com/en/latest/) - Library with multiple transformers to engineer and select features for machine learning models.
- [ppscore](https://pypi.org/project/ppscore/) - Library for detecting linear or non-linear relationships between two features.
- [scikit-learn](https://scikit-learn.org/stable/) - Open source machine learning library that features various algorithms for training a ML model.
- [SciPy](https://scipy.org/) - Library used for scientific computing and technical computing.
- [XGBoost](https://xgboost.readthedocs.io/en/stable/) - Optimized distributed gradient boosting library.
- [Imbalanced-learn](https://imbalanced-learn.org/stable/) - Provides tools for dealing with classification problems with imbalanced classes.
- [Joblib](https://joblib.readthedocs.io/en/stable/) - Provides tools for lightweight pipelining, e.g. caching output values.

[Back to top](#table-of-contents)

## Testing

### Manual Testing

The Jupyter Notebooks have covered and fulfilled satisfactory all the data analyst, data scientist and data engineer user stories so no manual testing was necessary.

#### User Story Testing (technical and non-technical users)

- *As a non-technical user, I can view a project summary that describes the project, dataset and business requirements so I can understand what the project is about.*

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Quick Project Summary page | Navigate to page and display information | Clicking on navbar link in sidebar navigates to correct page and all information and functions work and displayed correctly | Functions as intended|

- *As a non-technical user, I can view the project hypotheses and validations to determine what the project was trying to achieve and whether it was successful.*

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Project hypotheses page | Navigate to page and display information | Clicking on navbar link in sidebar navigates to correct page and all information and functions work and displayed correctly | Functions as intended|

- *As a non-technical/technical user, I can enter unseen data into the model and receive a prediction.*

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Correlation study page | Navigate to page and display information | Clicking on navbar link in sidebar navigates to correct page and all information and functions work and displayed correctly | Functions as intended|

- *As a technical user, I can view the correlation analysis to see how the outcomes were reached.*

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| Patient Readmission Prediction page | Navigate to page and display information | Clicking on navbar link in sidebar navigates to correct page and all information and functions work and displayed correctly | Functions as intended|

- *As a technical user, I can view all the data to understand the model performance and see statistics related to the model.*

| Feature | Action | Expected Result | Actual Result |
| --- | --- | --- | --- |
| ML Performance page | Navigate to page and display information | Clicking on navbar link in sidebar navigates to correct page and all information and functions work and displayed correctly | Functions as intended|

### Validation

All code in the app_pages and src directories was validated as conforming to PEP8 standards using CodeInstitute's PEP8 Linter.

<details>

<summary>PEP8 validations screenshots</summary>

![app.py](https://github.com/parides55/patient-readmission/blob/f0f2a81202967980db5caa66764bdffc4623411a/assets/readme_docs/app.png)
![multipage.py](https://github.com/parides55/patient-readmission/blob/f0f2a81202967980db5caa66764bdffc4623411a/assets/readme_docs/multipage.png)
![summary_page](https://github.com/parides55/patient-readmission/blob/f0f2a81202967980db5caa66764bdffc4623411a/assets/readme_docs/summary.png)
![hypotheses_page](https://github.com/parides55/patient-readmission/blob/f0f2a81202967980db5caa66764bdffc4623411a/assets/readme_docs/hypotheses.png)
![correlation_page](https://github.com/parides55/patient-readmission/blob/f0f2a81202967980db5caa66764bdffc4623411a/assets/readme_docs/app.png)
![predict_readmission_page](https://github.com/parides55/patient-readmission/blob/f0f2a81202967980db5caa66764bdffc4623411a/assets/readme_docs/page_predict_readmission.png)
![ml_performance_pae](https://github.com/parides55/patient-readmission/blob/f0f2a81202967980db5caa66764bdffc4623411a/assets/readme_docs/MLperformance.png)
![data_maangement_functions](https://github.com/parides55/patient-readmission/blob/f0f2a81202967980db5caa66764bdffc4623411a/assets/readme_docs/data_management.png)
![predict_readmission_function](https://github.com/parides55/patient-readmission/blob/f0f2a81202967980db5caa66764bdffc4623411a/assets/readme_docs/predict_readmission.png)
![evaluate_function](https://github.com/parides55/patient-readmission/blob/f0f2a81202967980db5caa66764bdffc4623411a/assets/readme_docs/evaluate.png)

</details>

- Some files had warnings due to 'line too long', however these were related to long strings when writing to the dashboard.
- These warnings were ignored as it did not effect the readability of any functions.

### Automated Unit Tests

No automated unit tests have been carried out at this time.

[Back to top](#table-of-contents)

## Unfixed Bugs

- No unfixed bugs found at the moment of deployment.

[Back to top](#table-of-contents)

## Deployment

### Heroku

- The App live link is: [Patient-Readmission](https://patient-readmission-c43bc847bc51.herokuapp.com/) 
- Set the runtime.txt Python version to a [Heroku-22](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

### Forking the GitHub Project

To make a copy of the GitHub repository to use on your own account, one can fork the repository by doing as follows:

- On the page for the repository, go to the 'Fork' button on the top right of the page, and click it to create a copy of the repository which should then be on your own GitHub account.

### Making a Local Clone

- On the page for the repository, click the 'Code' button
- To clone the repository using HTTPS, copy the HTTPS URL provided there.
- Open your CLI application of choice and change the current working directory to the location where you want the cloned directory to be made.
- Type git clone, and then paste the previously copied URL to create the clone

[Back to top](#table-of-contents)

## Credits

- Through the whole project I was following particularly the CI's *Churnometer* walkthrough project and example.

### Content and Code

- The code for the histogram/QQ plots were taken from the Code Institute *Churnometer* walkthrough project.
- The idea to apply LogTransformer, StandardScaler and PCA to the numerical values was taken from the [Code Section](https://www.kaggle.com/code/dubradave/predicting-hospital-readmission) in kaggle, from the user "DD".
- The code for the PPS heatmap function was taken from the Code Institute "Exploratory Data Analysis Tools" module.
- The code to asses missing values and levels was taken form the Code Institute *Churnometer* walkthrough project.
- The custom function for analyzing transformations during feature engineering was taken from the Code Institute "Data Analytics Packages - ML: feature-engine" module.
- The custom function for carrying out hyperparameter optimization was taken from the Code Institute "Data Analytics Packages - ML: Scikit-learn" module.
- The custom function for displaying the confusion matrix and analyzing model performance was taken from the Code Institute "Data Analytics Packages - ML: Scikit-learn" module.
- The multi-page class was taken from the Code Institute "Data Analysis & Machine Learning Toolkit" streamlit lessons.

[Back to top](#table-of-contents)

## Acknowledgements

- I would like to thank very much my mentor Mo Shami, who provided me with a big amount of information and a lot of inspiration to help me deliver this project.
- Also, I could not thank enough my family, who gave me the necessary time and space needed to finish this project.

[Back to top](#table-of-contents)
