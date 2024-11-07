import pyaudio

# Use esse código para descobrir qual microfone você deseja utilizar
# caso queira ou precise especificar um

p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    print(p.get_device_info_by_index(i))
p.terminate()
