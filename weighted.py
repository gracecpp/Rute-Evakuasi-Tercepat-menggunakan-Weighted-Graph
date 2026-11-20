#WEIGHTED

graph = {
    'A': {'B': 4, 'C': 5, 'D': 6},
    'B': {'A': 4, 'D': 5, 'E': 6},
    'C': {'A': 5, 'D': 4, 'E': 7, 'N': 8},
    'D': {'A': 6, 'B': 5, 'C': 4, 'E': 5, 'F': 5, 'N': 7},
    'E': {'B': 6, 'C': 7, 'D': 5, 'F': 6},
    'F': {'D': 5, 'E': 6, 'G': 3, 'J': 4, 'H': 5},
    'G': {'F': 3, 'H': 4, 'K': 6},
    'H': {'F': 5, 'G': 4, 'I': 5, 'O': 6},
    'I': {'H': 5, 'M': 4},
    'J': {'F': 4, 'K': 5},
    'K': {'G': 6, 'J': 5, 'L': 4},
    'L': {'K': 4, 'M': 6},
    'M': {'I': 4, 'L': 6},
    'N': {'C': 8, 'D': 7, 'O': 4},
    'O': {'N': 4, 'H': 6}
}

posko_target = {'A', 'F', 'H', 'I'}
bencana = {'B', 'C', 'N', 'D', 'E', 'G', 'J', 'K', 'L', 'M', 'O'}
peta_jalan = {}


#DYNAMIC PROGRAMMING
def evakuasi(u, visited=None):
    if u in posko_target:
        return 0, u

    if u in peta_jalan:
        return peta_jalan[u]

    if visited is None:
        visited = []

    visited_baru = visited + [u]
    waktu_tercepat = None
    posko_terdekat = None

    for v in graph[u]:
        if v not in visited_baru:
            bobot = graph[u][v]
            waktu_v, posko_v = evakuasi(v, visited_baru)

            if waktu_v is not None:
                total_waktu = bobot + waktu_v

                if waktu_tercepat is None or total_waktu < waktu_tercepat:
                    waktu_tercepat = total_waktu
                    posko_terdekat = posko_v

    peta_jalan[u] = (waktu_tercepat, posko_terdekat)
    return waktu_tercepat, posko_terdekat

print("Hasil Evakuasi Dynamic Programming")
for node in bencana:
    waktu, posko = evakuasi(node)
    print(f"Lokasi {node} -> Waktu: {waktu} menit, Posko Tujuan: {posko}")





#NAIVE RECURSIVE

graph = {
    'A': {'B': 4, 'C': 5, 'D': 6},
    'B': {'A': 4, 'D': 5, 'E': 6},
    'C': {'A': 5, 'D': 4, 'E': 7, 'N': 8},
    'D': {'A': 6, 'B': 5, 'C': 4, 'E': 5, 'F': 5, 'N': 7},
    'E': {'B': 6, 'C': 7, 'D': 5, 'F': 6},
    'F': {'D': 5, 'E': 6, 'G': 3, 'J': 4, 'H': 5},
    'G': {'F': 3, 'H': 4, 'K': 6},
    'H': {'F': 5, 'G': 4, 'I': 5, 'O': 6},
    'I': {'H': 5, 'M': 4},
    'J': {'F': 4, 'K': 5},
    'K': {'G': 6, 'J': 5, 'L': 4},
    'L': {'K': 4, 'M': 6},
    'M': {'I': 4, 'L': 6},
    'N': {'C': 8, 'D': 7, 'O': 4},
    'O': {'N': 4, 'H': 6}
}

posko_target = {'A', 'F', 'H', 'I'}
bencana = {'B', 'C', 'N', 'D', 'E', 'G', 'J', 'K', 'L', 'M', 'O'}

def eksekusi_naive(u, visited=None):
  if u in posko_target:
    return u, 0

  if visited is None:
    visited = []


    visited_baru = visited + [u]

    waktu_tercepat = None
    posko_terdekat = None

    for v in graph[u]:
        if v not in visited_baru:
            bobot = graph[u][v]
            waktu_v, posko_v = evakuasi(v, visited_baru)

            if waktu_v is not None:
                total_waktu = bobot + waktu_v

                if waktu_tercepat is None or total_waktu < waktu_tercepat:
                    waktu_tercepat = total_waktu
                    posko_terdekat = posko_v

    peta_jalan[u] = (waktu_tercepat, posko_terdekat)
    return waktu_tercepat, posko_terdekat

print("Hasil Evakuasi Naive")
for node in sorted(bencana):
    waktu, posko = evakuasi(node)
    print(f"Lokasi {node} -> Waktu: {waktu} menit, Posko Tujuan: {posko}")