
import requests
from pytube import YouTube
from tqdm import tqdm
import os

def get_thumbnail(url: str):
   yt = YouTube(url=url)
   
   res = requests.get(yt.thumbnail_url)
   
   if not os.path.exists('thumbnails'): 
        os.mkdir('thumbnails')
       
   if res.status_code == 200:
        with open(f'thumbnails/{yt.video_id}.png', 'wb') as file:
            file.write(res.content)
            print('done')
   else:
        print(f'failed to fetch thumbnail  code:<{res.status_code}>')


def get_best_format(url: str):
    def on_progress(stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        progress_bar.update(bytes_downloaded - progress_bar.n)

    yt = YouTube(
        url=url,
        on_progress_callback=on_progress
    )

    stream = yt.streams.get_highest_resolution()

    with tqdm(total=stream.filesize, unit='bytes', unit_scale=True, unit_divisor=1024) as progress_bar:
        
        stream.download(output_path='highRes')


def get_lowest_format(url: str):

    def on_progress(stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        progress_bar.update(bytes_downloaded - progress_bar.n)

    yt = YouTube(
        url=url,
        on_progress_callback=on_progress
    )

    stream = yt.streams.get_lowest_resolution()

    with tqdm(total=stream.filesize, unit='bytes', unit_scale=True, unit_divisor=1024) as progress_bar:
        
        stream.download(output_path='lowRes')      
