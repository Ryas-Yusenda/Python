"""Script to add 5 seconds of silence at the beginning of all MP3 files in the current directory."""

import os
from pydub import AudioSegment

# Check all mp3 files in the current directory
for file in os.listdir("."):
    if file.endswith(".mp3"):
        # Get the file name full path
        file_name = os.path.realpath(file)

        audio = AudioSegment.from_mp3(file_name)

        # Create a 5-second silent audio segment
        silence_segment = AudioSegment.silent(
            duration=5000
        )  # Duration is in milliseconds (5 seconds)

        # Concatenate the silent segment to the original audio
        output_audio = silence_segment + audio

        # Export the result to a new MP3 file
        output_name_file = file_name + "_silence.mp3"
        output_audio.export(output_name_file, format="mp3")

        print(f"Added 5 seconds of silence to {file_name}")

print("Done!")
os.system("pause")
