from flask import Blueprint, request, jsonify, send_file
import os
from .plots import generate_learning_styles_graph, generate_study_times_heatmap, generate_preferred_subjects_graph, generate_goals_wordcloud, generate_study_env_preferences_graph
from .time_series_analysis import perform_time_series_analysis  # Import the time series analysis function
from .anamoly_detection import perform_anamoly_detection
from .regression_analysis import perform_regression_analysis
from .generate_study_plan import perform_generate_study_plan

main_bp = Blueprint('main', __name__)

@main_bp.route('/recommendations', methods=['POST'])
def recommendations():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400

    try:
        graphs = {
            'learning_styles': generate_learning_styles_graph(data),
            'study_times_heatmap': generate_study_times_heatmap(data),
            'preferred_subjects': generate_preferred_subjects_graph(data),
            'goals_wordcloud': generate_goals_wordcloud(data),
            'study_env_preferences': generate_study_env_preferences_graph(data)
        }

        response = {key: f'/graph/{os.path.basename(value)}' for key, value in graphs.items()}

        return jsonify(response)
    except Exception as e:
        return jsonify({"error": f"Error generating graphs: {e}"}), 500

@main_bp.route('/graph/<filename>', methods=['GET'])
def get_graph(filename):
    directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'images')
    file_path = os.path.join(directory, filename)
    if os.path.exists(file_path):
        return send_file(file_path, mimetype='image/png')
    else:
        return 'Graph not found', 404

@main_bp.route('/time_series_analysis', methods=['GET'])
def get_time_series_analysis():
    time_series_data = perform_time_series_analysis()
    return jsonify(time_series_data)

@main_bp.route('/anamoly_detection', methods=['POST'])
def get_anamoly_detection():
    data = request.json
    anamoly_detection_data = perform_anamoly_detection(data)
    return jsonify(anamoly_detection_data)

@main_bp.route('/regression_analysis', methods=['POST'])
def regression_analysis():
    data = request.json
    regression_analysis_data = perform_regression_analysis(data)
    return jsonify(regression_analysis_data)

@main_bp.route('/generate_study_plan', methods=['POST'])
def generate_study_plan():
    data = request.json
    generate_study_plan_data = perform_generate_study_plan(data)
    return jsonify(generate_study_plan_data)