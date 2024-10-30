"""Script to compress video files using ffmpeg with specified quality settings."""

import subprocess
import os


def get_this_folder_video_files():
    """Get all video files in the current directory."""
    return [f for f in os.listdir() if f.endswith((".mp4", ".mkv", ".mov"))]


def compress_video():
    """
    Compress video files from source directory to destination directory using ffmpeg.

    Args:
        src_dir (str): Source directory path
        dst_dir (str): Destination directory path

    Note:
        * c:v libx264: Specifies the H.264 codec.
        * preset slow: Controls the encoding speed (the slower, the better compression efficiency).
            * Options: `ultrafast`, `superfast`, `faster`, `fast`, `medium`, `slow`, `slower`, `veryslow`.
        * crf 23: Constant Rate Factor; controls quality. Lower is better quality (18-28 range).
            * CRF 18-23 is usually a good range; `23` is a balanced starting point.
        * c:a aac -b:a 128k: Audio codec and bitrate, using 128 kbps AAC for efficient compression.
    """
    files = get_this_folder_video_files()

    for filename in files:
        print("[INFO] Processing:", filename)
        try:
            full_path_input = os.path.join(os.getcwd(), filename)
            full_path_output = os.path.join(
                os.getcwd() + "\\compressed", filename[:-4] + ".mp4"
            )

            os.makedirs("compressed", exist_ok=True)

            subprocess.call(
                [
                    "ffmpeg",
                    "-i",
                    full_path_input,
                    "-c:v",
                    "libx264",  # Video codec
                    "-preset",
                    "slow",  # Encoding preset
                    "-crf",
                    "23",  # Quality setting (23 is default)
                    "-c:a",
                    "aac",  # Audio codec
                    "-b:a",
                    "128k",  # Audio bitrate
                    "-loglevel",
                    "error",  # Hide ffmpeg output
                    "-y",  # Overwrite output file if it exists
                    full_path_output,
                ]
            )

            print("[DONE] Compressing: ", filename)
        except:
            print("[ERROR] Compressing: ", filename)


if __name__ == "__main__":
    compress_video()
    os.system("pause")
