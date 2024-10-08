from vosk import Model, KaldiRecognizer
import pyaudio, json




model_listen = Model('D:/My Projects/programming/expo v-2/Models/model_small_en') # model_small | model
rec = KaldiRecognizer(model_listen, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()


def listen_en():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(rec.Result())
            if answer['text']:
                return answer['text']


# Для теста
# while True:
#     s = ''
#     for text in listen_en():
#         s += text
#     print(s)