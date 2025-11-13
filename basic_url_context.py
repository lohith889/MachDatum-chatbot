"""
Simple, robust runner for the provided GenAI sample.

This file corrects syntax issues present in the original snippet and
prints a helpful message when the `google.genai` SDK isn't available.
"""

try:
	from google import genai
	from google.genai.types import (
		Tool,
		GenerateContentConfig,
		HttpOptions,
		UrlContext,
	)
except Exception:
	genai = None


def main() -> None:
	if genai is None:
		print("google.genai SDK not available. Install it with pip if you want to call the API: pip install google-genai")
		return

	client = genai.Client(http_options=HttpOptions(api_version="v1"))
	model_id = "gemini-2.5-flash"

	url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
	url2 = "https://www.allrecipes.com/recipe/70679/simple-whole-roasted-chicken/"

	url_context = UrlContext(urls=[url1, url2])
	url_context_tool = Tool(url_context=url_context)

	try:
		response = client.models.generate_content(
			model=model_id,
			contents=(
				f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}"
			),
			config=GenerateContentConfig(
				tools=[url_context_tool],
				response_modalities=["TEXT"],
			),
		)

		candidates = getattr(response, "candidates", None)
		if candidates and len(candidates) > 0:
			parts = getattr(candidates[0].content, "parts", [])
			for part in parts:
				print(getattr(part, "text", str(part)))
			print(getattr(candidates[0], "url_context_metadata", {}))
		else:
			print("No candidates returned by the model.")

	except Exception as e:
		print("Error while calling models.generate_content:", e)


if __name__ == "__main__":
	main()
model_id = "gemini-2.5-flash"
url_context_tool = Tool(
url_context = UrlContext
)
url1 =
"https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-19
40592"
url2 = "https://www.allrecipes.com/recipe/70679/simple-whole-roasted-chicken/"
response = client.models.generate_content(
model=model_id,
contents=("Compare the ingredients and cooking times from "
f"the recipes at {url1} and {url2}"),
config=GenerateContentConfig(
tools=[url_context_tool],
response_modalities=["TEXT"],
)
)
for each in response.candidates[0].content.parts:
print(each.text)
# For verification, you can inspect the metadata to see which URLs the
model retrieved
print(response.candidates[0].url_context_metadata)