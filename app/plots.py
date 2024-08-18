import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from wordcloud import WordCloud

def save_plot(fig, filename):
    directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'images')
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, filename)
    fig.savefig(file_path, bbox_inches='tight')
    plt.close(fig)
    return file_path

def generate_learning_styles_graph(students_data):
    learning_styles = [student['learningStyle'] for student in students_data if student['learningStyle']]
    fig, ax = plt.subplots()
    sns.countplot(learning_styles, ax=ax, palette='Set2')
    ax.set_title('Distribution of Learning Styles', fontsize=15)
    ax.set_xlabel('Learning Style', fontsize=12)
    ax.set_ylabel('Number of Students', fontsize=12)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right", fontsize=10)
    return save_plot(fig, 'learning_styles.png')

def generate_study_times_heatmap(students_data):
    study_times = []
    for student in students_data:
        for time in student['preferredStudyTimes']:
            study_times.append((time['dayOfWeek'], time['timeOfDay']))
    
    study_times_df = pd.DataFrame(study_times, columns=['DayOfWeek', 'TimeOfDay'])
    heatmap_data = study_times_df.pivot_table(index='DayOfWeek', columns='TimeOfDay', aggfunc=len, fill_value=0)

    fig, ax = plt.subplots()
    sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='YlGnBu', ax=ax)
    ax.set_title('Preferred Study Times Heatmap', fontsize=15)
    ax.set_xlabel('Time of Day', fontsize=12)
    ax.set_ylabel('Day of Week', fontsize=12)
    return save_plot(fig, 'study_times_heatmap.png')

def generate_preferred_subjects_graph(students_data):
    subjects = [subject['subjectName'] for student in students_data for subject in student['preferredSubjects']]
    fig, ax = plt.subplots()
    sns.countplot(subjects, ax=ax, palette='Set3')
    ax.set_title('Distribution of Preferred Subjects', fontsize=15)
    ax.set_xlabel('Subject', fontsize=12)
    ax.set_ylabel('Number of Students', fontsize=12)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right", fontsize=10)
    return save_plot(fig, 'preferred_subjects.png')

def generate_goals_wordcloud(students_data):
    short_term_goals = ' '.join([student['shortTermGoals'] for student in students_data if student['shortTermGoals']])
    long_term_goals = ' '.join([student['longTermGoals'] for student in students_data if student['longTermGoals']])

    wordcloud_short = WordCloud(width=800, height=400, background_color='white').generate(short_term_goals)
    wordcloud_long = WordCloud(width=800, height=400, background_color='white').generate(long_term_goals)

    fig, ax = plt.subplots(1, 2, figsize=(20, 10))

    ax[0].imshow(wordcloud_short, interpolation='bilinear')
    ax[0].axis('off')
    ax[0].set_title('Short Term Goals Word Cloud', fontsize=15)

    ax[1].imshow(wordcloud_long, interpolation='bilinear')
    ax[1].axis('off')
    ax[1].set_title('Long Term Goals Word Cloud', fontsize=15)

    return save_plot(fig, 'goals_wordcloud.png')

def generate_study_env_preferences_graph(students_data):
    study_envs = [student['studyEnvironment'] for student in students_data if student['studyEnvironment']]
    fig, ax = plt.subplots()
    sns.countplot(study_envs, ax=ax, palette='Pastel1')
    ax.set_title('Study Environment Preferences', fontsize=15)
    ax.set_xlabel('Study Environment', fontsize=12)
    ax.set_ylabel('Number of Students', fontsize=12)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right", fontsize=10)
    return save_plot(fig, 'study_env_preferences.png')
