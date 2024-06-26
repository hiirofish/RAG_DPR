from flask import Flask, request, jsonify
from rag import get_response, initialize_system
from body import gpt4_response

app = Flask(__name__)

initialize_system()

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_prompt = data.get('question')
    if not user_prompt:
        return jsonify({"error": "Question is required"}), 400

    search_results = get_response(user_prompt)
    combined_search_results = "\n".join(search_results)
    response = gpt4_response(user_prompt, combined_search_results)
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
