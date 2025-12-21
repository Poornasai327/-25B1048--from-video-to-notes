from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound ,TranscriptsDisabled
import json


video_id = input("Enter the YouTube video ID: ")

try:
   transcript_list=YouTubeTranscriptApi().list(video_id)
   print(transcript_list)
except TranscriptsDisabled or NoTranscriptFound:
   print('No Transcript found for the given video ID.')
   exit()

Required_Script=input('Enter 1 for Manual or 2 for Auto Generated or 3 for Translated: ')
Required_Language=input('Enter the Required Language code: ')

if Required_Script=='1':
   try:
      raw_script=transcript_list.find_manually_created_transcript([Required_Language]).fetch()
   except NoTranscriptFound:
      print('No Manual Transcript found for the given language code.')
      exit()

elif Required_Script=='2':
   try:
      raw_script=transcript_list.find_generated_transcript([Required_Language]).fetch()
   except NoTranscriptFound:
      print('No Auto Generated Transcript found for the given language code.')
      exit()

script='\n'

raw_data=[
   {'time':line.start,
   'text':line.text,
   'duration':line.duration
   }
   for line in raw_script
   ]

for line in raw_script:
   script+=script.join([line.text])
   script+=" "

File_Name=input("Enter the File Name: ")
json.dump(raw_data,open(File_Name + '.json','w',encoding='utf-8'),ensure_ascii=False,indent=4)

File_Name+='.txt'
f= open(File_Name,'w',encoding='utf-8')
f.write(script)
f.close

print('Given Video is Transcripted Succesfully to the ' + File_Name + ' in the required language')
