# Patient Readmission Predictor - A Predictive Classification Model for predicting patient's readmission

## Table of Contents

- [Patient Readmission Predictor - A Predictive Classification Model for predicting patient's readmission](#patient-readmission-predictor---a-predictive-classification-model-for-predicting-patients-readmission)
  - [Table of Contents](#table-of-contents)
  - [Dataset Content](#dataset-content)
  - [Business Requirements](#business-requirements)
  - [Hypothesis and how to validate?](#hypothesis-and-how-to-validate)
  - [The rationale to map the business requirements to the Data Visualizations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualizations-and-ml-tasks)
  - [ML Business Case](#ml-business-case)
  - [Epics and User Stories](#epics-and-user-stories)
  - [Dashboard Design](#dashboard-design)
    - [Page 1:](#page-1)
    - [Page 2:](#page-2)
    - [Page 3:](#page-3)
    - [Page 4:](#page-4)
    - [Page 5:](#page-5)
  - [Technologies Used](#technologies-used)
    - [Languages:](#languages)
    - [Python Packages](#python-packages)
  - [Testing](#testing)
    - [Manual Testing](#manual-testing)
      - [User Story Testing](#user-story-testing)
    - [Validation](#validation)
    - [Automated Unit Tests](#automated-unit-tests)
  - [Unfixed Bugs](#unfixed-bugs)
  - [Deployment](#deployment)
    - [Heroku](#heroku)
    - [Forking the GitHub Project](#Forking the GitHub Project)
    - [Making a Local Clone](#Making a Local Clone)
  - [Credits](#credits)
    - [Content](#content)
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

* Business requirement 1
  - By performing data analysis identify key factors and patterns that could contribute to patient readmission. This should help healthcare providers identify high-risk patients and implement targeted interventions to reduce readmission rates.

* Business requirement 2
  - By using a dashboard, the client, can input patient's information and predict whether this patient is likely to be readmitted or not.

[Back to top](#table-of-contents)

## Hypothesis and how to validate?

* Hypothesis 1:

  - Patients with a higher number of lab procedures are more likely to be readmitted. This hypothesis assumes that a higher number of lab procedures indicates a more severe or complex medical condition, which could lead to a higher chance of readmission.
  - **Validation** : By ploting the two variables, carying out a correlation study between them and perform statistical test.

* Hypothesis 2:

  - Patients who had a change in their diabetes medication during their hospital stay are more likely to be readmitted. This hypothesis suggests that changes in diabetes management might lead to instability in blood sugar control, increasing the likelihood of readmission.
  - **Validation** : By ploting the "change" variable and the target variable "readmitted " in a barplot and using variable "diabetes_med" as hue and perform statistical tests.

* Hypothesis 3:

  - Patients of higher age have a higher probability of readmission. This hypothesis is based on the idea that patients of higher age are more likely to have multiple chronicle health issues leading to readmissions.
  - **Validation** : Groupe the various age categories to see their distribution against the target variable "readmitted" and perform statistical tests.

[Back to top](#table-of-contents)

## The rationale to map the business requirements to the Data Visualizations and ML tasks

* Business requirement 1: Data Visualization and Correlation study

 - We need to perform a correlation study to determine which features correlate most closely to the target.
 - A Pearson's correlation will indicate linear relationships between numerical variables.
 - A Spearman's correlation will measure the monotonic relationships between variables.
 - A Predicitve Power Score can also be used to determine relationships between the variables and if they have any predictive power to against the target variable.
 - This will be performed during the Data Collection and Preparation steps of the CRISP-DM workflow. 

* Business requirement 2: Classification Model

 - We need to predict whether a patient will be readmitted or not.
 - For this task we need to build a binary classification model.
 - Extensive hyperparameter optimisation will give us the best chance at a highly accurate prediction.
 - This will be performed during the Modeling and Evaluation step of the CRISP -M workflow.

[Back to top](#table-of-contents)

## ML Business Case

Classification Model

* We want a ML model to predict whether a patient be readmitted after being realeased from hospital based upon previously gathered patient data. The target variable, 'readmitted', is categorical and contains two classes: 0 (not readmitted) and 1 (readmitted).
* We will consider a classification model, a supervised model with a two-class, single-label output that matches the target.
* The model success metrics are:
 - at least 70% recall for readmission on the train and test sets
* The model will be considered a failure if:
 - the model fails to achieve 70% recall for readmission
 - the model fails to achieve 70% precision for no readmission (falsely indicating patients are at risk)
* The model output is defined as a flag, indicating if a patient will have heart disease or not and the associated probability of heart disease.
* The training data to fit the model comes from: [Kaggle](www.kaggle.com )
* The dataset contains: 25000 observations and 16 attributes.
* Target: readmitted; Features: all other attributes.

[Back to top](#table-of-contents)

## Epics and User Stories

[Back to top](#table-of-contents)

## Dashboard Design

### Page 1: Poriject Summary 

* Section 1- Quick summary
 - Introduction to project
 - Description of dataset, where was it sourced
 - Link to readme
* Section 2 - Business Requirements
 - Description of business requirements

### Page 2: Project Hypotheses

* Outline the three project hypothesis
* Present validation of each hypothesis

### Page 3: Feature Correlation study

* State business requirement 1
* Overview of dataset - display first 10 rows of data and describe dataset shape
* Display correlation results and PPS heatmap
* Display distributions of correlated features against target using a prallel plot.
* Conclusions

### Page 4: Predict Patient readmission

* State business requirement 2
* Widget inputs for prediction
* "Run prediction" button to run inputted data through the ML model and output a prediction and % chance

### Page 5: Classification Performance Metrics

* Summary of model performance and metrics
* Model pipeline, features used to train the model and how they were selected
* Documentation of model performance on train and test sets

[Back to top](#table-of-contents)

## Technologies Used

The technologies used throughout the development are listed below:

### Languages:

 - Python

### Python Packages

* [Pandas](https://pandas.pydata.org/docs/index.html) - Open source library for data manipulation and analysis.
* [Numpy](https://numpy.org/doc/stable/index.html) - Adds support for large, multi-dimensional arrays and matrices, and high-level mathematical functions.
* [YData Profiling](https://docs.profiling.ydata.ai/latest/) - For data profiling and exploratory data analysis.
* [Matplotlib](https://matplotlib.org/) - Comprehensive library for creating static, animated and interactive visualisations.
* [Seaborn](https://seaborn.pydata.org/) - Another data visualisation library for drawing attractive and informative statistical graphics.
* [Pingouin](https://pingouin-stats.org/build/html/index.html) - Open source statistical package for simple yet exhaustive stats functions.
* [Feature-engine](https://feature-engine.trainindata.com/en/latest/) - Library with multiple transformers to engineer and select features for machine learning models.
* [ppscore](https://pypi.org/project/ppscore/) - Library for detecting linear or non-linear relationships between two features.
* [scikit-learn](https://scikit-learn.org/stable/) - Open source machine learning library that features various algorithms for training a ML model.
* [SciPy](https://scipy.org/) - Library used for scientific computing and technical computing.
* [XGBoost](https://xgboost.readthedocs.io/en/stable/) - Optimised distributed gradient boosting library.
* [Imbalanced-learn](https://imbalanced-learn.org/stable/) - Provides tools for dealing with classification problems with imbalanced classes.
* [Joblib](https://joblib.readthedocs.io/en/stable/) - Provides tools for lightweight pipelining, e.g. caching output values.

[Back to top](#table-of-contents)

## Testing

### Manual Testing

#### User Story Testing

### Validation

All code in the app_pages and src directories was validated as conforming to PEP8 standards using CodeInstitute's PEP8 Linter.

 - Some files had warnings due to 'line too long', however these were related to long strings when writing to the dashboard.
 - These warnings were ignored as it did not effect the readability of any functions.

### Automated Unit Tests

No automated unit tests have been carried out at this time.

[Back to top](#table-of-contents)

## Unfixed Bugs

* No unfixed bugs found at the moment of deployment.

[Back to top](#table-of-contents)

## Deployment

### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

### Forking the GitHub Project

To make a copy of the GitHub repository to use on your own account, one can fork the repository by doing as follows:

* On the page for the repository, go to the 'Fork' button on the top right of the page, and click it to create a copy of the repository which should then be on your own GitHub account.

### Making a Local Clone

* On the page for the repository, click the 'Code' button
* To clone the repository using HTTPS, copy the HTTPS URL provided there.
* Open your CLI application of choice and change the current working directory to the location where you want the cloned directory to be made.
* Type git clone, and then paste the previously copied URL to create the clone

## Credits

[Back to top](#table-of-contents)

### Content

## Acknowledgements

* Thank the people that provided support through this project.

[Back to top](#table-of-contents)
