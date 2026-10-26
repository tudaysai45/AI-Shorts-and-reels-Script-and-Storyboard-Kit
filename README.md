# ReelCraft AI — Shorts & Reels Script and Storyboard Kit

An AI-powered web app that helps creators plan short-form videos for Instagram Reels, YouTube Shorts and similar platforms. Enter a topic and generate a hook, voice-over script, scene-by-scene storyboard, captions, hashtags and production tips.

## Features
- Professional responsive interface
- AI-generated hook and voice-over script
- Scene storyboard with timing, visuals, on-screen text and camera suggestions
- Caption, hashtags and call to action
- English, Telugu, Tamil, Hindi and Hinglish language choices
- Print or save the generated kit as PDF from the browser
- API key stored in a local environment file, not in source code or the form

## Technology stack
- Python + Flask
- OpenAI API
- HTML, CSS, Jinja templates
- python-dotenv

## Requirements
- Python 3.10 or newer
- An OpenAI API key and API access
- Internet connection for AI generation

## Setup (Windows)
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Copy `.env.example` to a new file named `.env`.
6. Open `.env` and replace `your_api_key_here` with your API key. Never upload `.env` to GitHub.
7. Start the app:
   ```bash
   python app.py
   ```
8. Open `http://127.0.0.1:5000` in your browser.

## Setup (macOS / Linux)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your API key
python app.py
```
Then visit `http://127.0.0.1:5000`.

## Configuration
`OPENAI_API_KEY` is required. `OPENAI_MODEL` is optional; it defaults to `gpt-4.1-mini` in this starter project. Change it to a model available to your API account if necessary. API usage may incur charges according to your provider account.

## Project structure
```text
AI-Shorts-Reels-Storyboard-Kit/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── docs/
    ├── PROJECT_REPORT.md
    └── PRESENTATION_GUIDE.md
```

## How it works
1. User submits a topic and creative preferences.
2. Flask validates the topic and reads the API key from environment variables.
3. The app sends structured instructions to the language model.
4. The response is parsed as JSON.
5. Jinja renders the script, storyboard, caption and hashtags in the results panel.

## Security notes
- Never commit your real `.env` file or API key.
- Do not paste API keys into screenshots, issue reports or public commits.
- Set `debug=False` and use a production WSGI server before deploying publicly.
- Add rate limiting, authentication and usage controls before offering this app to public users.
- Review generated content for accuracy, copyright and platform rules before publishing.

## Limitations
- The app generates a plan, not a finished video file.
- API availability, model names and pricing depend on your API account.
- AI output can be inaccurate or repetitive; human review is recommended.
- No database or user login is included in this starter version.

## Future enhancements
- Export storyboard as PDF or DOCX
- Save projects and user accounts
- Voice generation and subtitle export
- Image-generation integration for storyboard frames
- Multiple script versions and A/B hooks
- Usage limits, moderation and deployment configuration

## License
For academic use, add a license file appropriate to your project and institution before publishing.
