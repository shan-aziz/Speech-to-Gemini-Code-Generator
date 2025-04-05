import speech_recognition as sr
import google.generativeai as genai

# Gemini API Setup (replace with your actual API key)
GEN_API_KEY = "GEN_API_KEY"
genai.configure(api_key=GEN_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash-lite")

# Function to convert speech to text
def speech_to_text(recognizer, microphone):
    with microphone as source:
        print("🎙️ Listening... (Say 'stop' or 'exit' to quit)")
        audio = recognizer.listen(source, phrase_time_limit=5)
    try:
        text = recognizer.recognize_google(audio)
        print(f"🗣️ You: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand audio, please try again.")
        return ""
    except sr.RequestError as e:
        print(f"❌ Recognition error: {e}")
        return ""

# Function to get Gemini's response
def generate_gemini_code(prompt):
    print("✨ Generating response from Gemini...")
    response = model.generate_content(
        contents=[{"role": "user", "parts": [{"text": prompt}]}]
    )
    return response.text

# Main conversation loop
def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("🤖 Gemini Voice Assistant Started.")

    while True:
        user_input = speech_to_text(recognizer, microphone)

        if user_input.lower() in ["stop", "exit"]:
            print("👋 Exiting Gemini Voice Assistant. Goodbye!")
            break
        elif user_input:
            gemini_response = generate_gemini_code(user_input + "\nProvide the response in code format.")
            print(f"💡 Gemini's Response:\n\n{gemini_response}\n")

if __name__ == "__main__":
    main()