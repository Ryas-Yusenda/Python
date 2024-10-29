"""Generates subtitles from a video file in SRT format using the Whisper model."""

import os
import time
import tempfile
import ffmpeg
from faster_whisper import WhisperModel


def extract_audio(input_video: str) -> str:
    """Extracts audio from a video file and saves it as a WAV file.

    Args:
        input_video (str): The input video file path.

    Returns:
        str: The path to the extracted audio file.
    """
    print(f"Extracting audio from video: {input_video}")

    # Create a temporary file path for the audio output
    extracted_audio = os.path.join(tempfile.gettempdir(), "extracted_audio.wav")

    # Use ffmpeg to extract audio, downsampling to 16kHz mono for Whisper compatibility
    ffmpeg.input(input_video).output(
        extracted_audio, acodec="pcm_s16le", ac=1, ar="16k"
    ).run(quiet=True, overwrite_output=True)

    print("✅ Audio extraction complete.")
    return extracted_audio


def format_time(seconds: str) -> str:
    """Formats seconds into the SRT format: HH:MM:SS,SSS."""
    time_format = time.strftime("%H:%M:%S", time.gmtime(float(seconds)))
    millis = seconds.split(".")[1]
    return f"{time_format},{millis}"


def transcribe(audio_path: str, translate: str) -> tuple[str, list]:
    """Transcribes audio using the Whisper model with optimized settings.

    Args:
        audio_path (str): The path to the audio file.
        translate (str): The language code to translate to (e.g., "id" for Indonesian).

    Returns:
        tuple[str, list]: The detected language and a list of transcribed
    """
    print("Starting transcription")

    # Whisper model configuration
    model_size = (
        "openai/whisper-large-v3-turbo"  # models--openai--whisper-large-v3-turbo
    )
    device = "cuda"  # check nvidia-smi
    compute_type = "float16"  # "int8"

    model = WhisperModel(model_size, device=device, compute_type=compute_type)

    # Perform transcription with minimal VAD filtering to improve processing time
    segments, info = model.transcribe(
        audio_path,
        vad_filter=False,
        vad_parameters={"min_silence_duration_ms": 100},
        language=translate,
        # task="translate",
    )

    data = (info.language, list(segments))
    print("✅ Transcription complete.")

    return data


def save_segments_to_srt(segments: list, output_file: str) -> str:
    """Generates an SRT file from transcription segments.

    Args:
        segments (list): A list of transcribed segments.
        output_file (str): The output SRT file path.
    """
    print("Generating SRT file...")

    # Create subtitle folder if it doesn't exist
    os.makedirs("subtitle", exist_ok=True)

    # Convert video file path to SRT path in subtitle folder
    output_file = os.path.join("subtitle", os.path.splitext(output_file)[0] + ".srt")

    # Write each segment to the SRT file
    with open(output_file, "w", encoding="utf-8") as f:
        for idx, segment in enumerate(segments, start=1):
            start_time = format_time(format(segment.start, ".3f"))
            end_time = format_time(format(segment.end, ".3f"))
            text = segment.text.strip()
            f.write(f"{idx}\n{start_time} --> {end_time}\n{text}\n\n")

    print("✅ SRT file generation complete.")

    return output_file


def insert_subtitle(video_file: str, srt_file: str) -> None:
    """Inserts subtitles into a video file.

    Args:
        video_file (str): The input video file path.
        srt_file (str): The SRT file path.
    """
    print(f"Inserting subtitles into video: {video_file}")

    # Create video-with-subtitle folder if it doesn't exist
    os.makedirs("video-with-subtitle", exist_ok=True)

    width_video = ffmpeg.probe(video_file)["streams"][0]["width"]
    font_size = round((1.3625 + (width_video * 0.0135)))

    part_save_video = os.path.join("video-with-subtitle", video_file)
    # get absolute path and escape for ffmpeg
    part_save_video = os.path.abspath(part_save_video)
    srt_file = os.path.abspath(srt_file).replace("\\", "\\\\").replace(":", "\\:")
    # Escape the path for ffmpeg

    print(f"Output path: {part_save_video}")
    print(f"Subtitle path: {srt_file}")

    ffmpeg.input(video_file).output(
        part_save_video,
        filter_complex=f"subtitles='{srt_file}':force_style='FontName=Arial,FontSize={font_size}rem,PrimaryColour=&HFFFFFF,&H000000'",
    ).run(quiet=True, overwrite_output=True)

    print("✅ Subtitle insertion complete.")


def main():
    """Main workflow: extract audio, transcribe, and save as SRT."""

    allow_format = (".mp4", ".mkv")

    # scan all file in current directory
    video_files = [f for f in os.listdir() if f.endswith(allow_format)]

    for video_file in video_files:
        audio_path = extract_audio(video_file)
        _, segments = transcribe(audio_path, translate="id")
        srt_file = save_segments_to_srt(segments, video_file)

        insert_subtitle(video_file, srt_file)

        # Clean up the temporary audio file
        os.remove(audio_path)


if __name__ == "__main__":
    main()
