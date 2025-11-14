from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

# Configuration - exact same as run_chatbot_ai.py
API_KEY = "YOUR API KEY"
MODEL_ID = "gemini-2.5-flash"
ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_ID}:generateContent?key={API_KEY}"

# All MachDatum URLs to fetch using urlContext
URLS = [
    "https://www.machdatum.com",
    "https://www.machdatum.com/book-a-demo",
    "https://www.machdatum.com/thingsight",
    "https://www.machdatum.com/cmms",
    "https://www.machdatum.com/asset-management",
    "https://www.machdatum.com/work-order-management",
    "https://www.machdatum.com/spare-part-management",
    "https://www.machdatum.com/blogs",
    "https://www.machdatum.com/use-cases",
    "https://www.machdatum.com/articles",
    "https://www.machdatum.com/our-story",
    "https://www.machdatum.com/people",
    "https://www.machdatum.com/contact-us",
    "https://www.machdatum.com/privacy-policy",
    "https://www.machdatum.com/devices/rs485-to-ethernet-converter",
    "https://www.machdatum.com/devices/rs485-to-wifi-converter",
    "https://www.machdatum.com/blogs/the-7-most-important-cmms-maintenance-kpis-every-manufacturer-must-track-in-2025",
    "https://www.machdatum.com/blogs/what-is-3w1h-practical-framework-manufacturing-problem-solving",
    "https://www.machdatum.com/blogs/a3-thinking-in-toyota-origins-evolution-and-impact-on-lean-manufacturing",
    "https://www.machdatum.com/blogs/mistake-proofing-your-factory-a-practical-guide-to-poka-yoke",
]

@app.route('/')
def index():
    """Render the chatbot interface."""
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages and return AI responses - uses exact same logic as run_chatbot_ai.py"""
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided', 'status': 'error'}), 400
        
        print(f"User said: {user_message}")
        url_text = "\n".join(URLS)
        
        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": (
                                "Use urlContext to fetch ALL the following URLs:\n\n"
                                f"{url_text}\n\n"
                                "Use ONLY information from these pages. Do NOT hallucinate.\n"
                                f"Task: {user_message}"
                            )
                        }
                    ]
                }
            ],
            "tools": [
                {
                    "urlContext": {}
                }
            ],
            "generationConfig": {
                "temperature": 0.1,
                "max_output_tokens": 2048
            }
        }
        print("Sending request to Gemini model...")

        response = requests.post(
            ENDPOINT,
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload)
        )
        print("Received response from Gemini.")

        data = response.json()
        try:
            answer = data["candidates"][0]["content"]["parts"][0]["text"]
            
            return jsonify({
                'response': answer,
                'status': 'success'
            })
        except:
            print("AI did not provide a valid response. Using fallback answer.")
            
            return jsonify({
                'response': (
                    "That's a great question! For detailed information about that, I'd recommend booking a demo with "
                    "our team or filling out our contact form so our experts can provide you with the most accurate "
                    "information. Is there anything else I can help clarify?"),
                'status': 'fallback'
            })

    
    except requests.exceptions.RequestException as e:
        print(f"Network error while contacting Gemini: {str(e)}")
        return jsonify({
            'response': f'Error: {str(e)}',
            'status': 'error'
        }), 500
    
    except Exception as e:
        print(f"Unexpected server error: {str(e)}")
        return jsonify({
            'response': f'Error: {str(e)}',
            'status': 'error'
        }), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
