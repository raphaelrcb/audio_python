import pyaudio
import wave
import speech_recognition as sr
from speech_recognition import Microphone
import subprocess
from commands import Commander

def say(text):
    print(text)
    call_string = "echo " + text + " | cscript \"C:\\Program Files\\Jampal\\ptts.vbs\""
    print(call_string)
    subprocess.call(call_string, shell=True)

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()

def initSpeech(r, mic_index):
    #ajustando sensibilidade do microfone
    cmd = Commander()
    r.energy_threshold = 300

    print("Fala tu que eu te escuto")
    play_audio("./audio/franky_aaaau.wav")
    print("AGORA")
    with sr.Microphone(mic_index) as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, timeout=5, phrase_time_limit=10)

    play_audio("./audio/catcha_one_piece.wav")
    command = ""

    with open("resultado.wav", "wb") as f:
        f.write(audio.get_wav_data())

    try:
        command = r.recognize_google(audio, language="pt-BR")
        print("Você disse:")
        print(command)
    except sr.UnknownValueError:
        print("Google disse: Fala direito mermão")
        print(command)
    except sr.RequestError as e:
        print(f"Erro de reconhecimento; {e}")

    cmd.discover(command)
    if command == "sair":
        return False
    return True

def CheckMic():
    m = None
    index = None
    name = ""

    for i, microphone_name in enumerate(Microphone.list_microphone_names()):
        if microphone_name == 'Padrão (Tecnologia Intel® Smart' or i == 1:
            m = Microphone(device_index=i)
            name = microphone_name
            index = i

    if m is not None:
        print(name)
        print("Mic ready")
        return index
    else:
        print ("Mic not found")


if __name__ == '__main__':
    print("Checking Mic")
    mic_index = CheckMic()
    r = sr.Recognizer()
    running = True
    if mic_index:
        while running:
            running = initSpeech(r, mic_index)