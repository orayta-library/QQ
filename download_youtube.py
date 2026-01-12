import sys
from pytube import YouTube

def download_video(url, output_path='.'):
    """
    מוריד סרטון מ-YouTube
    
    Args:
        url: כתובת הסרטון ב-YouTube
        output_path: תיקיית היעד להורדה
    """
    try:
        print(f"מוריד סרטון מ: {url}")
        yt = YouTube(url)
        
        # בחירת הסטרים באיכות הגבוהה ביותר
        stream = yt.streams.get_highest_resolution()
        
        print(f"כותרת: {yt.title}")
        print(f"אורך: {yt.length} שניות")
        print(f"מוריד...")
        
        # הורדת הסרטון
        stream.download(output_path=output_path)
        
        print(f"הסרטון הורד בהצלחה!")
        return 0
        
    except Exception as e:
        print(f"שגיאה בהורדת הסרטון: {str(e)}")
        return 1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("שימוש: python download_youtube.py <URL>")
        sys.exit(1)
    
    video_url = sys.argv[1]
    exit_code = download_video(video_url)
    sys.exit(exit_code)
