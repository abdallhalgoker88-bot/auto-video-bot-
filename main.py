import os
import json
import requests
from gtts import gTTS
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
import google.generativeai as genai

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

def generate_content():
    prompt = """
    أنت خبير في صناعة المحتوى. اختر حقيقة نفسية مذهلة وقصيرة.
    اكتب الرد بملف JSON نقي وبدون أي إضافات بالشكل التالي:
    {
      "script": "نص قصير جداً ومثير للاهتمام بالعربية",
      "search_keyword": "dark aesthetic"
    }
    """
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    
    text_res = response.text.strip()
    if text_res.startswith("```json"):
        text_res = text_res[7:]
    if text_res.endswith("```"):
        text_res = text_res[:-3]
        
    return json.loads(text_res.strip())

def make_audio(text, filename="voice.mp3"):
    tts = gTTS(text=text, lang='ar')
    tts.save(filename)
    return filename

def get_bg_video(keyword, filename="bg.mp4"):
    headers = {"Authorization": PEXELS_API_KEY}
    url = f"https://api.pexels.com/videos/search?query={keyword}&per_page=1&orientation=portrait"
    res = requests.get(url, headers=headers).json()
    video_url = res["videos"][0]["video_files"][0]["link"]
    video_data = requests.get(video_url).content
    with open(filename, "wb") as f:
        f.write(video_data)
    return filename

def render_video(video_path, audio_path, output_path="final.mp4"):
    audio = AudioFileClip(audio_path)
    video = VideoFileClip(video_path).subclip(0, audio.duration)
    video = video.resize(height=1920)
    if video.w > 1080:
        video = video.crop(x1=video.w/2 - 540, width=1080, y1=0, height=1920)
    final = video.set_audio(audio)
    final.write_videofile(output_path, codec="libx264", audio_codec="aac", fps=24)
    return output_path

if __name__ == "__main__":
    print("1. توليد المحتوى...")
    data = generate_content()
    print("2. توليد الصوت...")
    audio = make_audio(data["script"])
    print("3. تحميل الخلفية...")
    bg = get_bg_video(data["search_keyword"])
    print("4. مونتاج الفيديو...")
    render_video(bg, audio)
    print("تم بنجاح!")
