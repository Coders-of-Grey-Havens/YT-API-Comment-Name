from Youtube import Youtube

if __name__ == "__main__":
    youtube = Youtube()
    videoId = '9GinJ8oT_sg'
    text = youtube.get_latest_comment(videoId)
    youtube.update_name(text, 22)