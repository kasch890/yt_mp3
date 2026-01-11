import yt_dlp
import os

def main():
    playlist_url = input("Enter YouTube playlist URL: ")
    folder_name = input("Enter folder name for downloads: ")

    # Base directory where all folders go
    base_dir = "C:/Users/kaife/Music"

    # Make folder name filesystem-safe
    safe_folder_name = "".join(
        c for c in folder_name if c.isalnum() or c in (" ", "_", "-")
    ).strip()

    download_path = os.path.join(base_dir, safe_folder_name)

    # Create folder if it doesn't exist
    os.makedirs(download_path, exist_ok=True)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(download_path, "%(title)s.%(ext)s"),
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "noplaylist": False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

    print(f"\nDownloads saved to: {download_path}")

if __name__ == '__main__':
    main()