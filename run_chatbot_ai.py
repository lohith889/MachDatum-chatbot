import requests
import json

def main():
    API_KEY = "YOUR API KEY"
    MODEL_ID = "gemini-2.5-flash"
    ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_ID}:generateContent?key={API_KEY}"

    urls = [
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

    url_text = "\n".join(urls)

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
                            "Task: Provide a brief summary of what this use case says \"Assembly Digitalization and Digital Valve Test Certificate\"."
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

    response = requests.post(
        ENDPOINT,
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload)
    )

    # Extract ONLY the model's output text
    data = response.json()
    try:
        answer = data["candidates"][0]["content"]["parts"][0]["text"]
        print("\nFINAL OUTPUT:\n")
        print(answer)
    except:
        print("\n❌ ERROR (Full JSON for debugging):\n")
        print(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()
