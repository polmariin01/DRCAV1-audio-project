import os
import mirex_puntuation as punt

db = "giantsteps-key-dataset"

db_path = "db/"+db+"/annotations_key/"
results_path = "results/"+db+"/"

print(os.getcwd())

files_in_db = os.listdir(db_path)
files_in_results = os.listdir(results_path)
print(files_in_db,"\n",files_in_results)


print("Al dataset: " + str(len(files_in_db)) + " elements")
print("Al results: " + str(len(files_in_results)) + " elements")

contador_punts = 0.0
contador_total = 0.0

for files in files_in_db:
    #Obrim ground truth
    file_true = open(db_path + files)
    true_tonality = file_true.readline()
    file_true.close()
    #Obrim resultat
    txt_name = files.replace("key","txt")
    file_result = open(results_path + txt_name)
    result_key = file_result.readline()
    file_result.close()
    #Comparem
    punto, nom_punt = punt.puntuation_mirex(true_tonality, result_key)
    punto = float(punto)
    contador_punts = contador_punts + punto
    contador_total = contador_total + 1.0
    print("\n******************** File - " + files)
    print("True: " + true_tonality + "\tResult: " + result_key)
    print("Retocades:\t" + punt._adjust(true_tonality) + "\t" + punt._adjust(result_key))
    print("Puntuació: " + str(punto) + "\t" + str(nom_punt))

print("\nPunts totals: " + str(contador_punts))
print("Punts possibles: " + str(contador_total))

print("FSCORE = " + str(contador_punts / contador_total))