from transformers import pipeline


summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn",
    device=-1
)

def chunk_transcript(transcript, chunk_size, overlap):
    chunks = []
    start = 0

    while start < len(transcript):
        end = start + chunk_size
        chunk = transcript[start:end]
        chunks.append(chunk)
        start = end - overlap

    return chunks


def summarize_chunk(chunk):
    summary=summarizer(chunk,max_length=130,min_length=60,do_sample=False)
    return summary[0]['summary_text']

def summarize_transcript(transcript,chunk_size,over_lap):
    chunks=chunk_transcript(transcript,chunk_size,over_lap)
    summaries=[summarize_chunk(chunk) for chunk in chunks]
    final_summary=" ".join(summaries)
    return final_summary

if __name__=="__main__":
    file_name=input("Enter the transcript file name: ")+".txt"
    with open(file_name,'r') as file:
        transcript=file.read()
    chunk_size=int(input("Enter chunk size (800-1400) (number of characters): "))
    over_lap=int(input("Enter overlap size (100-200) (number of characters): "))
    summary=summarize_transcript(transcript,chunk_size,over_lap)

    new_file_name=input("Enter the output summary file name: ")+".txt"
    with open(new_file_name,'w') as file:
        file.write(summary)
    
    optional_print=input("Do you want to summarize the summary again? if yes type 1 else type 0: ")
    if optional_print=='1':
        new_chunk_size=int(input("Enter new chunk size (number of characters): "))
        new_over_lap=int(input("Enter new overlap size (number of characters): "))
        summary_again=summarize_transcript(summary,new_chunk_size,new_over_lap)
        final_file_name=input("Enter the final output summary file name: ")+".txt"
        with open(final_file_name,'w') as file:
            file.write(summary_again)
        
    if optional_print=='0':    
        print("Summary process completed.")
        exit()
