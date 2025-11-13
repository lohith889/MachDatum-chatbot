# MachDatum AI Chatbot

A modern, intelligent web-based chatbot powered by Google's Gemini 2.5 Flash API, designed to provide accurate information about MachDatum's products, services, and company using real-time website content analysis.

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🌟 Features

- **🤖 AI-Powered Intelligence** - Leverages Google Gemini 2.5 Flash for smart, context-aware responses
- **🌐 Real-time URL Context** - Automatically fetches and analyzes content from 20+ MachDatum web pages
- **💬 Modern Chat Interface** - Beautiful, responsive UI with:
  - Animated gradient backgrounds with floating blur effects
  - Smooth message transitions and animations
  - Advanced typing indicator with ripple animation
  - Auto-expanding input field
  - Mobile-friendly responsive design
- **📝 Smart Text Formatting** - Automatically formats AI responses with bold text, lists, and paragraphs
- **⚡ Real-time Updates** - AJAX-based communication for instant responses without page reloads
- **🎯 Accurate Information** - Strict prompt engineering prevents AI hallucination

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

## 🔒 Security Best Practices

⚠️ **Important Security Notes:**

1. **Never commit API keys** to GitHub or version control
2. Use environment variables for sensitive data:
   ```python
   import os
   API_KEY = os.environ.get('GEMINI_API_KEY')
   ```
3. **Add `.gitignore`:**
   ```
   .venv/
   __pycache__/
   *.pyc
   .env
   config.py
   ```
4. **Production Deployment:**
   - Use a production WSGI server (Gunicorn, uWSGI)
   - Implement rate limiting
   - Add HTTPS/SSL encryption
   - Enable CORS properly
   - Add user authentication if needed

## 📦 Dependencies

Create a `requirements.txt` file:

```
Flask==3.0.0
requests==2.31.0
```

Install with:
```bash
pip install -r requirements.txt
```

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

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Lohith**

- GitHub: [@yourusername](https://github.com/yourusername)
- Project Link: [https://github.com/yourusername/MachDatum-chatbot](https://github.com/yourusername/MachDatum-chatbot)

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
