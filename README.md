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
  - [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
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
  - **Validation** :

* Hypothesis 2:

  - Patients who had a change in their diabetes medication during their hospital stay are more likely to be readmitted. This hypothesis suggests that changes in diabetes management might lead to instability in blood sugar control, increasing the likelihood of readmission.
  - **Validation** :

* Hypothesis 3:

  - Patients of higher age have a higher probability of readmission. This hypothesis is based on the idea that patients of higher age are more likely to have multiple chronicle health issues leading to readmissions.
  - **Validation** :

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
 - This will be performed during the Modeling and Evaluation step of the CRISP -M workflow.

[Back to top](#table-of-contents)

## ML Business Case

* In the previous bullet, you potentially visualized an ML task to answer a business requirement. You should frame the business case using the method we covered in the course 

[Back to top](#table-of-contents)

## Epics and User Stories

[Back to top](#table-of-contents)

## Dashboard Design

### Page 1:

### Page 2:

### Page 3:

### Page 4:

### Page 5:

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

 - Dashboard was manually tested using user stories as a basis for determining success.
 - Jupyter notebooks were reliant on consecutive functions being successful so manual testing against user stories was deemed irrelevant.

### Validation

All code in the app_pages and src directories was validated as conforming to PEP8 standards using CodeInstitute's PEP8 Linter.

 - Some files had warnings due to 'line too long', however these were related to long strings when writing to the dashboard.
 - These warnings were ignored as it did not effect the readability of any functions.

### Automated Unit Tests

No automated unit tests have been carried out at this time.

[Back to top](#table-of-contents)

## Unfixed Bugs

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

## Main Data Analysis and Machine Learning Libraries

* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.

## Credits

[Back to top](#table-of-contents)

### Content

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site

## Acknowledgements

* Thank the people that provided support through this project.

[Back to top](#table-of-contents)
