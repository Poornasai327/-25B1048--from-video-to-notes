# **From video to notes: Building an AI that watches lectures for u...**

This AI extracts transcript from youtube lectures and converts it into clean readable summary.

# Milestone-1 - Youtube transcript extraction

 - Takes Youtube video id as input and extacts it's transcript using **youtube-transcript-api** in the required available transcript language.
 - Extracted Transcript is cleaned and converted into clean readable text
 - Outputs are saved into .txt file which contains cleaned transcript and .json file which contains timestamps and text of transcript.

# Milestone-2 - Text Summarization

 - Building an AI tool that summarizes the given text file using Hugging face transformers
 - Model used is `facebook/bart-large-cnn`
 - Summarization is done chunk by chunk due to token limits.




