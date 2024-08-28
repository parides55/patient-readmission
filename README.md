## How to use this repo

1. Use this template to create your GitHub project repo

1. Log into your cloud IDE with your GitHub account.

1. On your Dashboard, click on the New Workspace button

1. Paste in the URL you copied from GitHub earlier

1. Click Create

1. Wait for the workspace to open. This can take a few minutes.

1. Open a new terminal and `pip3 install -r requirements.txt`

1. Open the jupyter_notebooks directory, and click on the notebook you want to open.

1. Click the kernel button and choose Python Environments.

Note that the kernel says Python 3.8.18 as it inherits from the workspace, so it will be Python-3.8.18 as installed by our template. To confirm this, you can use `! python --version` in a notebook code cell.

## Cloud IDE Reminders

To log into the Heroku tool belt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

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

## Business Requirements

This project aims to reduce patient readmission rates to improve healthcare quality and reduce costs. Potential stakeholders/clients can Healthcare providers, hospital administrators, insurance companies.

* Business requirement 1
  - By performing data analysis identify key factors and patterns that could contribute to patient readmission. This should help healthcare providers identify high-risk patients and implement targeted interventions to reduce readmission rates.

* Business requirement 2
  - By using a dashboard, the client, can input patient's information and predict whether this patient is likely to be readmitted or not.

## Hypothesis and how to validate?

* Hypothesis 1:

Patients with a higher number of lab procedures are more likely to be readmitted.
This hypothesis assumes that a higher number of lab procedures indicates a more severe or complex medical condition, which could lead to a higher chance of readmission.

* Hypothesis 2:

Patients who had a change in their diabetes medication during their hospital stay are more likely to be readmitted. This hypothesis suggests that changes in diabetes management might lead to instability in blood sugar control, increasing the likelihood of readmission.

* Hypothesis 3:

Patients of higher age have a higher probability of readmission. This hypothesis is based on the idea that patients of higher age are more likely to have multiple chronicle health issues leading to readmissions.

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

## ML Business Case

* In the previous bullet, you potentially visualized an ML task to answer a business requirement. You should frame the business case using the method we covered in the course 

## Dashboard Design

* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).

## Unfixed Bugs

* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

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

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site

## Acknowledgements (optional)

* Thank the people that provided support through this project.