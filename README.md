# Gemini AI Assistant PWA (Django)

An interactive Progressive Web App (PWA) powered by Google Gemini API (`gemini-1.5-flash`), built with Python/Django and Bootstrap 5.

## Features
- **Google Gemini API Integration**: Safe backend communication keeping your API key hidden from the client.
- **PWA Capabilities**: Web App Manifest and Service Worker for installation support on mobile & desktop, along with offline resource caching.
- **Interactive UI**: Dark mode UI built with Bootstrap 5, live typing indicators, auto-expanding text input, and markdown rendering (`marked.js`).
- **Offline Detection**: Real-time network banner informing users when connection drops.

## Prerequisites
- Python 3.9+
- A Google Gemini API Key (Obtain from [Google AI Studio](https://aistudio.google.com/))

## Setup & Local Installation

1. **Unzip the Project**
   Extract `gemini_pwa_project.zip` and navigate into the folder:
   ```bash
   cd gemini_pwa_project
   ```

2. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   Create a `.env` file in the project root directory (same directory as `manage.py`):
   ```bash
   cp .env.example .env
   ```
   Open `.env` and add your Gemini API Key:
   ```env
   GEMINI_API_KEY=AIzaSy...your_actual_api_key
   ```

5. **Run Database Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**
   Open your browser and go to `http://127.0.0.1:8000/`.

---

## Technical Architecture Overview
- **`assistant/views.py`**: Intercepts requests, calls `google.generativeai` SDK securely server-side, and returns structured JSON responses.
- **`assistant/static/sw.js`**: Caches frontend dependencies for offline app rendering.
- **`assistant/static/manifest.json`**: Configures app installability and theme settings.
"# AI-Assistant-Web-Application" 
