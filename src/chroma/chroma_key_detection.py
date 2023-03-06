import librosa
print("Librosa imporat")
import numpy as np
print("Numpy imporat")
import keyfinder as kf
print("KeyFinder imporat")
import os
print("OS imporat")

print("import fet")

def key_detect(path2song : str):
    print("*"*50)
    print("Nova cançó per processar: ", path2song)
    y, sr = librosa.load(path2song)
    print("\tCançó llegida")
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    print("\tCanço filtrada")
    tonal = kf.Tonal_Fragment(y_harmonic, sr, tend=22)
    print("\tObjecte tonal creat")
    print("TONALITAT: ", tonal.key)
    return tonal.key


db = "giantsteps-key-dataset"

path = "db/"+db+"/audio/"
path_results = "results/"+db+"/"
#os.chdir("../../")
print(os.getcwd())

a = os.listdir(path)
print(a)

contador=0
contador = score_mirex()
total_songs = len(a)

for song in a:
    key = key_detect(path+song)
    print(key)
    txt_name = song.replace("mp3","txt")
    print(txt_name)
    path_file = path_results+txt_name
    file = open(path_file,"w")
    file.write(str(key))
    file.close()
    contador=contador+1
    print("Acabado elemento ", contador, "de un total de ", total_songs)

    



'''
if verbose:
    tonal.print_chroma()
tonal.print_key()
print(tonal.key)

'''

