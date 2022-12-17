import time


def read_file_timed(file):
  start_time = time.time()
  try:
      f = open(file, mode='rb')
  except FileNotFoundError as e:
      print(e)
      wasted_time = 0
  else:
      x = f.read()
      end_time = time.time()
      wasted_time = end_time - start_time
      f.close()
      return x
  finally:
      print(f'Time required for {file} = {wasted_time}')




video_data = read_file_timed('video.mp4')  # 155 MB
#Time required for video.mp4 = 0.06553506851196289

# попытка считать отсутствующий файл
video_data = read_file_timed('file_not_exist.mp4')  # 155 MB
#FileNotFoundError: [Errno 2] No such file or directory: 'video2.mp4'
#Time required for video2.mp4 = 0.0
