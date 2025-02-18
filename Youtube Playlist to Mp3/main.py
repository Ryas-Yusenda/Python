import os
import yt_dlp


def download_playlist_as_mp3(playlist_url, output_folder="download", ffmpeg_path="ffmpeg"):
    # Buat folder output jika belum ada
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Konfigurasi yt-dlp
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "outtmpl": os.path.join(output_folder, "%(title)s.%(ext)s"),
        "ffmpeg_location": ffmpeg_path,  # Tentukan lokasi FFmpeg
    }

    # Unduh playlist dengan penanganan error
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
        print(f"Download selesai untuk {playlist_url}!")
    except yt_dlp.utils.DownloadError as e:
        print(f"Gagal mengunduh {playlist_url}. Error: {e}")
        with open("error.txt", "a") as error_file:
            error_file.write(f"{playlist_url}\n")


if __name__ == "__main__":
    try:
        import yt_dlp
    except ImportError:
        print("yt-dlp tidak terinstal. Instal dengan: pip install yt-dlp")
        exit(1)

    # Cek apakah ffmpeg tersedia atau tentukan path manual jika diperlukan
    ffmpeg_path = os.path.join(os.getcwd(), "ffmpeg.exe")
    if os.system(f"{ffmpeg_path} -version") != 0:
        alt_ffmpeg_path = input("FFmpeg tidak ditemukan. Masukkan path lengkap ke ffmpeg.exe: ").strip()
        if not os.path.exists(alt_ffmpeg_path):
            print("Path FFmpeg tidak valid. Pastikan FFmpeg telah diinstal.")
            exit(1)
        ffmpeg_path = alt_ffmpeg_path

    with open("playlist.txt", "r") as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        if url:
            download_playlist_as_mp3(url, ffmpeg_path=ffmpeg_path)
