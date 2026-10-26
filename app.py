import os
import json
from flask import Flask, render_template, request
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
app = Flask(__name__)

def generate_kit(topic, platform, duration, tone, language, audience):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is missing. Add it to your .env file and restart the app.")

    client = OpenAI(api_key=api_key)
    prompt = f"""
Create a practical short-form video planning kit.
Topic: {topic}
Platform: {platform}
Target duration: {duration} seconds
Tone: {tone}
Language: {language}
Target audience: {audience}

Return ONLY valid JSON with this schema:
{{
  "title": "short engaging title",
  "hook": "opening line for the first 1-3 seconds",
  "script": "complete voice-over/dialogue, timed for the requested duration",
  "scenes": [
    {{
      "time": "0-5 sec",
      "visual": "what viewers see",
      "voiceover": "spoken line",
      "on_screen_text": "short overlay text",
      "camera": "suggested camera framing or movement"
    }}
  ],
  "caption": "social post caption",
  "hashtags": ["#tag1", "#tag2"],
  "call_to_action": "clear ending action",
  "production_tips": ["practical tip 1", "practical tip 2"]
}}
Use 4-7 scenes, keep on-screen text brief, make the storyboard specific to the topic,
avoid unsupported factual claims, and do not claim the video has been created.
"""
    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        input=prompt
    )
    output = response.output_text.strip()
    # Accommodate accidental markdown fences from a model response.
    if output.startswith("```"):
        output = output.split("\n", 1)[1]
        output = output.rsplit("```", 1)[0]
    data = json.loads(output)
    data["hashtags"] = data.get("hashtags", [])
    data["scenes"] = data.get("scenes", [])
    data["production_tips"] = data.get("production_tips", [])
    return data

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    form = {
        "topic": "",
        "platform": "Instagram Reels",
        "duration": "30",
        "tone": "Educational",
        "language": "English",
        "audience": "General audience",
    }
    if request.method == "POST":
        for key in form:
            form[key] = request.form.get(key, form[key]).strip()
        if not form["topic"]:
            error = "Please enter a topic before generating your kit."
        else:
            try:
                result = generate_kit(
                    form["topic"], form["platform"], form["duration"],
                    form["tone"], form["language"], form["audience"]
                )
            except json.JSONDecodeError:
                error = "The AI returned an unexpected format. Please try again."
            except Exception as exc:
                app.logger.exception("Kit generation failed")
                error = str(exc) if isinstance(exc, RuntimeError) else (
                    "Generation failed. Check your API key, model setting, internet connection, "
                    "and API account access, then try again."
                )
    return render_template("index.html", result=result, error=error, form=form)

if __name__ == "__main__":
    app.run(debug=True)
