import os
import click
import yt_dlp


@click.command()
@click.argument("playlist_urls", nargs=-1)
@click.option(
    "--output-dir",
    "-o",
    default="data/audio/original",
    help="Output directory to save the MP3 files",
)
def download_youtube_playlist(playlist_urls, output_dir):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Set YouTube DL options
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        "ignoreerrors": True,
        "ffmpeg_location": "utils/ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download(playlist_urls)
            click.echo(f"Download from {playlist_urls} completed.")
        except Exception as e:
            click.echo(f"Error downloading from {playlist_urls}: {e}", err=True)

    # convert_folder_webm_to_mp3(output_dir, output_dir)


if __name__ == "__main__":
    download_youtube_playlist()
