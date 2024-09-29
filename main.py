import pyktok


def download_video(url):
    pyktok.specify_browser('chrome')

    pyktok.save_tiktok(url,
                       True,
                       'video_data.csv',
                       'chrome')


download_url = 'https://www.tiktok.com/@djombash/video/7355931604662914309'
download_video(download_url)
