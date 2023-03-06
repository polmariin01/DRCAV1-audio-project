
key_flat_wheel = ["A","B","C","D","E","F","G"]
n_keys = len(key_flat_wheel)

all_keys = ["A","Bb","B","C","Db","D","Eb","E","F","Gb","G","Ab"]
keys_N = len(all_keys) #12 notes
FIFTH = 7
RELATIU = 3


def _adjust(key : str):
    note = key[0]
    #print(note)
    new_key = ""
    if key[1] == '#':
        index_actual = key_flat_wheel.index(note) 
        nou_index = int(( index_actual + 1 ) % n_keys)
        #print("Vell: " + str(index_actual) + "\tNou: " + str(nou_index))
#        nou_index = ( key_flat_wheel.index(note) + 1 ) % n_keys
        new_key = key_flat_wheel[ nou_index ] #agafa el següent, in a circular way
        new_key = new_key + 'b'
        relatiu = " major"
        if key.__contains__("minor"):
            relatiu = " minor"
        new_key = new_key + relatiu
    else :
        new_key = key        
#    print(key)
    return new_key

def _is_major(key :str):
    # Minor - false
    # Major - 1
    if key.__contains__("minor"):
        return False
    return True

def _get_note(key : str):
    separat = key.split(" ")
    return all_keys.index(separat[0]) , _is_major(separat[1])


def puntuation(key_truth : str, key_result : str) -> float:
    key1 = _adjust(key_truth)
    key2 = _adjust(key_result)

    if(key1 == key2):
        return 1.0
    return 0.0


## Same	1
## Perfect fifth	0.5
## Relative major/minor	0.3
## Parallel major/minor	0.2
def puntuation_mirex(key_truth : str, key_result : str):
#    key1 = _adjust(key_truth)
#    key2 = _adjust(key_result)
    note1, rel1 = _get_note( _adjust(key_truth) )
    note2, rel2 = _get_note( _adjust(key_result) )

    rels = rel1 == rel2
    dist = (keys_N + note2 - note1) % keys_N
    print("Relatiu igual: " + str(rels) + "\tDistancia semitons: " + str(dist))

    if dist == 0:      # Same note
        if rels:    # Same key
            #print("Same")
            return 1 , "Same"
        else :              # Parallel major/minor
            #print("Parallel")
            return 0.2 , "Parallel"
        
    if dist == FIFTH: # Fifth
        #print("Fifth")
        return 0.5 , "Fifth"

    if not rels:
        if rel2 and dist == RELATIU:
            return 0.3 , "Relatiu"
        if rel1 and dist == (keys_N - RELATIU):
            return 0.3 , "Relatiu"
    print("Res")
    return 0 , "No relation"
