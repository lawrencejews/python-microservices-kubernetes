import pika, json, tempfile, os 
from bson.objectid import ObjectId 
import moviepy.editor 

def start(message, fs, fs_mp3s, fs_videos, channel):
  message = json.loads(message)
  
  # Empty file for temporaryFile
  tf = tempfile.NamedTemporaryFile()
  
  # Video Contents
  out = fs_videos.get(ObjectId(message["video_fid"]))
  
  # Add video contents to  empty file
  tf.write(out.read())
  
  # Create audio from temp video file
  audio = moviepy.editor.VideoFileClip(tf.name).audio
  tf.close()
  
  # Write audio to own file
  tf_path = tempfile.gettempdir() + f"/{message['video_fid']}.mp3"
  audio.write_audiofile(tf_path)
  
  # Save the file to mongo
  f = open(tf_path, "rb")
  data = f.read()
  fid = fs_mp3s.put(data)
  f.close()
  os.remove(tf_path)
  
  message["mp3_fid"] = str(fid)
  
  try:
    channel.basic_publish(
      exchange="",
      routing_key=os.environ.get("MP3_QUEUE"),
      body=json.dumps(message),
      properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE)
    ),
  except Exception as err:
    fs_mp3s.delete(fid)
    return "Failed to publish message"