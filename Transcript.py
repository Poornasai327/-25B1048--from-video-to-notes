from youtube_transcript_api import YouTubeTranscriptApi

video_id = input("Enter the YouTube video ID: ")
raw_script=YouTubeTranscriptApi().fetch(video_id)

script='\n'

for line in raw_script:
   script+=script.join([line.text])
   script+=" "

File_Name=input("Enter the File Name: ") + '.txt'

f= open(File_Name,'w')
f.write(script)
f.close

print('Given Video is Transcripted Succesfully')