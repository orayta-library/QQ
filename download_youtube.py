import sys
import os
import yt_dlp

def download_video(url, output_path='.'):
    """
    מוריד סרטון מ-YouTube
    
    Args:
        url: כתובת הסרטון ב-YouTube
        output_path: תיקיית היעד להורדה
    """
    ydl_opts = {
        'format': 'best[height<=720]/best',  # פורמט פשוט יותר
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'extractor_retries': 3,
        'fragment_retries': 3,
        'sleep_interval': 1,
        'max_sleep_interval': 5,
        'no_check_certificate': True,
    }
    
    # אם קיים קובץ cookies, השתמש בו
    if os.path.exists('cookies.txt'):
        ydl_opts['cookiefile'] = 'cookies.txt'
        print("משתמש ב-cookies לאימות")
    
    try:
        print(f"מוריד סרטון מ: {url}")
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            print(f"כותרת: {info.get('title', 'לא ידוע')}")
            print(f"אורך: {info.get('duration', 0)} שניות")
            print(f"מוריד...")
            
            try:
                ydl.download([url])
            except Exception as download_error:
                print(f"נכשל בפורמט הראשון, מנסה פורמט חלופי...")
                # נסה פורמט פשוט יותר
                ydl_opts['format'] = 'worst[height>=360]/worst'
                with yt_dlp.YoutubeDL(ydl_opts) as ydl_alt:
                    ydl_alt.download([url])
        
        print(f"הסרטון הורד בהצלחה!")
        return 0
        
    except Exception as e:
        print(f"שגיאה בהורדת הסרטון: {str(e)}")
        print("\nטיפים לפתרון בעיות:")
        print("1. וודא שיש חיבור אינטרנט יציב")
        print("2. נסה שוב מאוחר יותר")
        print("3. עדכן yt-dlp: pip install --upgrade yt-dlp")
        return 1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("שימוש: python download_youtube.py <URL>")
        sys.exit(1)
    
    video_url = sys.argv[1]
    exit_code = download_video(video_url)
    sys.exit(exit_code)
