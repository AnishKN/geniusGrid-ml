# import pandas as pd
# import statsmodels.api as sm

# def perform_regression_analysis(data):
#     # Extract necessary data from the input
#     subjects = data.get('subjects', [])
#     exams = data.get('exams', [])
#     study_plans = data.get('study_plans', [])
#     events = data.get('events', [])

#     # For this example, let's assume we want to predict the number of exams based on study plans and events
#     # Convert the data into a DataFrame
#     df_subjects = pd.DataFrame(subjects)
#     df_exams = pd.DataFrame(exams)
#     df_study_plans = pd.DataFrame(study_plans)
#     df_events = pd.DataFrame(events)

#     # Create a simple dataset for regression analysis
#     # This is a simplified example. In a real-world scenario, you would preprocess your data accordingly
#     df = pd.DataFrame({
#         'exams_count': df_exams['subjectName'].value_counts().reindex(df_subjects['subName'], fill_value=0),
#         'study_plans_count': df_study_plans['category'].value_counts().reindex(df_subjects['subName'], fill_value=0),
#         'events_count': df_events['name'].value_counts().reindex(df_subjects['subName'], fill_value=0),
#     }).reset_index()

#     df.columns = ['subject', 'exams_count', 'study_plans_count', 'events_count']

#     # Perform regression analysis
#     X = df[['study_plans_count', 'events_count']]
#     y = df['exams_count']
#     X = sm.add_constant(X)  # Adds a constant term to the predictor

#     model = sm.OLS(y, X).fit()
#     predictions = model.predict(X)

#     # Summarize the regression analysis
#     summary = model.summary().as_text()

#     # Convert the predictions to a dictionary
#     predictions_dict = predictions.to_dict()

#     return {
#         'summary': summary,
#         'predictions': predictions_dict
#     }


# regression_analysis.py
# import pandas as pd
# import statsmodels.api as sm

# def perform_regression_analysis(data):
#     # Extract relevant data
#     subjects = data['subjects']
#     exams = data['exams']
#     study_plans = data['study_plans']
#     events = data['events']

#     # Create DataFrame
#     df = pd.DataFrame({
#         'exams_count': [len(exams)],
#         'study_plans_count': [len(study_plans)],
#         'events_count': [len(events)]
#     })

#     # Define the dependent variable
#     y = df['exams_count']

#     # Define the independent variables
#     X = df[['study_plans_count', 'events_count']]
#     X = sm.add_constant(X)  # Adds a constant term to the predictor

#     # Perform the regression
#     model = sm.OLS(y, X).fit()

#     # Make predictions
#     predictions = model.predict(X)

#     # Return the summary of the regression and the predictions
#     return {
#         "summary": model.summary().as_text(),
#         "predictions": predictions.tolist()
#     }

# regression_analysis.py
import pandas as pd
import statsmodels.api as sm

def perform_regression_analysis(data):
    # Extract relevant data
    subjects = data['subjects']
    exams = data['exams']
    study_plans = data['study_plans']
    events = data['events']

    # Create DataFrame
    df = pd.DataFrame({
        'exams_count': [len(exams)],
        'study_plans_count': [len(study_plans)],
        'events_count': [len(events)]
    })

    # Ensure there are at least 2 data points
    if df.shape[0] < 2:
        return {
            "error": "Not enough data points to perform regression analysis. At least 2 data points are required."
        }

    # Define the dependent variable
    y = df['exams_count']

    # Define the independent variables
    X = df[['study_plans_count', 'events_count']]
    X = sm.add_constant(X)  # Adds a constant term to the predictor

    # Perform the regression
    model = sm.OLS(y, X).fit()

    # Make predictions
    predictions = model.predict(X)

    # Return the summary of the regression and the predictions
    return {
        "summary": model.summary().as_text(),
        "predictions": predictions.tolist()
    }

