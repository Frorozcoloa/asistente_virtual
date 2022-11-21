import whisper
import record
import time

model = whisper.load_model("base")
audio = record.Recorder()
start = time.time()
print("Start recorded...")
audio.record()
counter = 1

while True:
    timestamp = time.time()
    if (timestamp-start) % 10 == 0:
        print("New timestap")
        audio.save(str(counter))
        audio.record()
        result = model.transcribe(f"{counter}.wav", verbose=None)
        print("Prosecing the audio", str(counter))
        with open("sample.txt", "a") as file_object:
            file_object.write(f'{result["text"]}\n')
        counter += 1