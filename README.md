# MachDatum AI Chatbot

A intelligent web-based chatbot powered by Google's Gemini 2.5 Flash API, designed to provide accurate information about MachDatum's products, services, and company using real-time website content analysis using url context tool.
---

This project demonstrates how to build a production-ready chatbot that:

* Collects and feeds multiple URLs into Gemini using *urlContext*
* Prevents hallucination by restricting the model to website-based knowledge
* Provides a clean UI and API endpoint
* Works as a standalone backend or can be integrated into any frontend

---

## Features

### URL Context Scraping

The bot sends a list of MachDatum website URLs to Gemini’s *urlContext* tool.
This allows Gemini to fetch, parse, and use real website data in its answers.

### Hallucination-Free Responses

All responses are grounded strictly in the provided URL data.
If the model fails to find relevant info, a fallback message is returned.

### Flask API Backend

A simple and clean Flask server handles:

* Rendering the frontend
* Receiving user messages
* Sending requests to Gemini
* Returning AI responses

### Gemini API Integration

The model used:

```
gemini-2.5-flash
```

Configured with:

* Low temperature (0.1) for accuracy
* Large token limit (2048) for detailed answers

### ✔ Frontend Hook

The `index.html` file acts as the chatbot UI, making POST requests to `/chat`.

---

## 🧠 How the Bot Works (Architecture Overview)

### 1. **URL Collector / Extractor**

A predefined list of MachDatum URLs is stored in the backend.

```python
URLS = [
    "https://www.machdatum.com",
    "https://www.machdatum.com/book-a-demo",
    ...
]
```

These URLs are combined into a text block and sent to Gemini as:

```
Use urlContext to fetch ALL the following URLs:
<all URLs>

Use ONLY information from these pages.
```

This forces the AI to reference ONLY this data.

---

### 2. **Flask Chat Endpoint**

The `/chat` endpoint accepts a JSON request:

```json
{
  "message": "your question here"
}
```

It constructs a payload for Gemini:

```python
payload = {
    "contents": [...],
    "tools": [{"urlContext": {}}],
    "generationConfig": { ... }
}
```

Then sends it to:

```
https://generativelanguage.googleapis.com/v1beta/models/<model>:generateContent
```

---

### 3. **Gemini Response Handling**

If Gemini responds with valid text:

```python
answer = data["candidates"][0]["content"]["parts"][0]["text"]
```

It is returned to the frontend.

If not, a fallback message is used to keep UX smooth.

---

### 4. **Error Handling**

Handles:

* Missing messages
* Network errors
* Invalid AI responses
* Unexpected server issues

All errors produce JSON output for easy debugging.

---

## 🛠 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2. Install Dependencies

```bash
pip install flask requests
```

### 3. Add Your Gemini API Key

Inside the code:

```python
API_KEY = "YOUR_API_KEY_HERE"
```

### 4. Run the Server

```bash
python app.py
```

The bot will start at:

```
http://localhost:5000
```

---

## 📁 Project Structure

```
├── app.py                # Main Flask server
├── templates/
│     └── index.html      # Chatbot frontend UI
├── README.md             # Project documentation
```

---

## 📬 API Usage Example

**POST** → `/chat`

Body:

```json
{
  "message": "What is MachDatum's CMMS?"
}
```

Response:

```json
{
  "response": "... accurate content extracted from the website ...",
  "status": "success"
}
```

---

## 🧩 Key Design Decisions

* **Gemini urlContext** is used instead of manually scraping webpages.
* Hardcoded URLs ensure consistent data input for the AI.
* A low-temperature setting reduces hallucination.
* Fallback logic guarantees that the user always gets a meaningful answer.
* Structure matches the standalone CLI version (run_chatbot_ai.py) to maintain consistency.

---

## 📜 License

This project is open-source and free to use for learning or integration.

---

## 🛠️ Technology Stack

**Backend:**
- Flask - Lightweight Python web framework
- Google Gemini API - Advanced AI language model (gemini-2.5-flash)
- Requests - HTTP library for API communication

**Frontend:**
- HTML5/CSS3 - Modern semantic markup and styling
- Vanilla JavaScript - No framework dependencies for better performance
- Custom CSS animations - Smooth, professional UI effects

## 📋 Prerequisites

Before running this project, ensure you have:

- Python 3.7 or higher
- A Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))
- Modern web browser (Chrome, Firefox, Safari, Edge)

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/MachDatum-chatbot.git
cd MachDatum-chatbot
```

### 2. Set Up Virtual Environment

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install flask requests
```

### 4. Configure API Key

Open `app.py` and replace the API key:

```python
API_KEY = "your-google-gemini-api-key-here"
```

### 5. Run the Application

```bash
python app.py
```

### 6. Access the Chatbot

Open your browser and navigate to:
- **Local:** http://127.0.0.1:5000
- **Network:** http://your-ip-address:5000

## 📁 Project Structure

```
MachDatum-chatbot/
│
├── app.py                      # Flask backend server with API integration
├── templates/
│   └── index.html             # Main chat interface with embedded CSS and JS
├── static/
│   └── images/                # Image assets
│       ├── logo.png           # MachDatum company logo
│       ├── bot.png            # AI assistant avatar
│       └── user.png           # User avatar
├── run_chatbot_ai.py          # Standalone test script for API
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies (optional)
```

## ⚙️ Configuration

### Customize Information Sources

Edit the `URLS` list in `app.py` to modify which web pages the chatbot analyzes:

```python
URLS = [
    "https://www.machdatum.com",
    "https://www.machdatum.com/products",
    "https://www.machdatum.com/services",
    # Add or remove URLs as needed
]
```

### Adjust AI Behavior

Modify the `generationConfig` in `app.py`:

```python
"generationConfig": {
    "temperature": 0.1,         # 0.0-1.0: Lower = focused, Higher = creative
    "max_output_tokens": 2048   # Maximum response length
}
```

### Change Port or Host

Update the last line in `app.py`:

```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Change port as needed
```

## 🎨 UI Components

### Header Section
- **Logo:** MachDatum branding
- **Status Indicator:** Animated online status with pulsing dot

### Chat Area
- **Gradient Background:** Smooth blue-to-purple gradient
- **Animated Blobs:** Floating blur effects for visual interest
- **Message Bubbles:** Distinct styling for user (blue) and bot (white) messages
- **Avatar Images:** Custom icons for user and bot

### Typing Indicator
- **4-Circle Animation:** Sophisticated loading animation
- **Ripple Effects:** Expanding outlines for modern feel
- **Synchronized Timing:** Sequential delays for wave effect

### Input Section
- **Auto-Expanding Textarea:** Grows with content up to 120px
- **Animated Send Button:** Jello effect on hover with curved arrow icon
- **Keyboard Shortcuts:** 
  - `Enter` - Send message
  - `Shift + Enter` - New line

## 🔧 API Integration Details

The chatbot uses Google Gemini API's URL Context feature:

1. **URL Fetching:** Gemini automatically fetches content from specified URLs
2. **Content Analysis:** AI analyzes and synthesizes information from all sources
3. **Response Generation:** Creates accurate answers based only on fetched content
4. **Hallucination Prevention:** Strict prompting ensures AI doesn't make up information

**API Endpoint:**
```
https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent
```

## 🎯 Use Cases

- ✅ **Customer Support** - Automated responses to common inquiries
- ✅ **Product Information** - Detailed product specifications and features
- ✅ **Company Info** - About us, team, contact details
- ✅ **Blog Content** - Summaries and information from blog articles
- ✅ **Technical Docs** - Device specifications and setup guides

## 🐛 Troubleshooting

### Common Issues

**1. API Key Error**
```
Error: Invalid API key
```
→ Check that your Gemini API key is correct and active

**2. Module Not Found**
```
ModuleNotFoundError: No module named 'flask'
```
→ Ensure virtual environment is activated and dependencies are installed

**3. Port Already in Use**
```
OSError: [Errno 48] Address already in use
```
→ Change the port in `app.py` or kill the process using port 5000

**4. Images Not Loading**
```
404 Error on /static/images/logo.png
```
→ Ensure all images are in the `static/images/` directory

## 🚀 Deployment Options

### Heroku
```bash
heroku create machdatum-chatbot
git push heroku main
```

### Railway
1. Connect GitHub repository
2. Add environment variables
3. Deploy automatically

### Docker
Create a `Dockerfile`:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

## 👨‍💻 Author

**Lohith**

- GitHub: [@lohith889](https://github.com/lohith889)
- Project Link: [https://github.com/lohith889/MachDatum-chatbot](https://github.com/lohith889/MachDatum-chatbot)

## 🙏 Acknowledgments

- [MachDatum](https://www.machdatum.com) - For the amazing CMMS and IoT solutions
- [Google Gemini](https://ai.google.dev/) - For the powerful AI API
- [Flask](https://flask.palletsprojects.com/) - For the lightweight web framework
- [Uiverse.io](https://uiverse.io/) - For the beautiful UI components inspiration

## 📧 Support

For questions or support, visit [www.machdatum.com/contact-us](https://www.machdatum.com/contact-us)

---

**⭐ If you find this project helpful, please give it a star!**

**Built with ❤️ using Flask and Google Gemini AI**
