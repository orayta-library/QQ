# YouTube Video Downloader

הורדת סרטוני YouTube דרך GitHub Actions.

## הגדרה

### ייצוא Cookies מהדפדפן

YouTube חוסם הורדות מ-GitHub Actions, לכן צריך cookies מהדפדפן שלך.

**Chrome / Edge:**
https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc

**Firefox:**
https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/

### שלבים:

1. התקן את התוסף המתאים לדפדפן שלך
2. היכנס ל-YouTube בדפדפן
3. לך ל-youtube.com ולחץ על אייקון התוסף
4. שמור את הקובץ בשם `cookies.txt` בתיקיית הפרויקט
5. העלה את הקובץ ל-repository (הקוד יקרא אותו אוטומטית)

**חשוב:** אל תשתף את קובץ ה-cookies בפומבי! אם ה-repository פומבי, הוסף `cookies.txt` ל-`.gitignore`

## שימוש

1. לך ל-Actions → Download YouTube Video
2. לחץ על "Run workflow"
3. הזן את כתובת הסרטון
4. לחץ "Run workflow"
5. הסרטון יהיה זמין ב-Artifacts

## הרצה מקומית

```bash
pip install -r requirements.txt
python download_youtube.py "https://www.youtube.com/watch?v=VIDEO_ID"
```
