import heapq

def a_star_search(graph, start, goal):

    open_list = [(graph[start]['h'], 0, start, [start])]
    
    closed_set = set()
    
    langkah = 0
    while open_list:
        langkah += 1
        print(f"\n===== LANGKAH {langkah} =====")
        
        _f_cost, g_cost, current_city, path = heapq.heappop(open_list)

        print(f"Kota terpilih dari antrean: {current_city}")
        print(f"   -> Jalur saat ini: {' -> '.join(path)}")
        print(f"   -> Biaya g(n) sejauh ini: {g_cost} km")

        if current_city in closed_set:
            print(f"   -> Kota {current_city} sudah pernah dieksplorasi. Melanjutkan...")
            continue
        
        closed_set.add(current_city)

        if current_city == goal:
            print(f"\n>> TUJUAN '{goal}' TERCAPAI! <<")
            return path, g_cost

        print(f"\n--- Mengeksplorasi Tetangga dari {current_city} ---")

        for neighbor, distance in graph[current_city]['neighbors'].items():
            if neighbor in closed_set:
                continue
            
            print(f"  * Tetangga: {neighbor}")
            
            new_g_cost = g_cost + distance
            h_cost = graph[neighbor]['h']
            new_f_cost = new_g_cost + h_cost
            
            print(f"    -> Jarak dari {current_city} ke {neighbor}: {distance} km")
            print(f"    -> Kalkulasi g(n) baru: {g_cost} (g dari {current_city}) + {distance} km = {new_g_cost} km")
            print(f"    -> Heuristik h(n) dari {neighbor}: {h_cost} km")
            print(f"    -> Total biaya f(n) = g(n) + h(n) = {new_g_cost} + {h_cost} = {new_f_cost}")
            
            new_path = path + [neighbor]
            heapq.heappush(open_list, (new_f_cost, new_g_cost, neighbor, new_path))
            print(f"    -> Jalur '{' -> '.join(new_path)}' ditambahkan ke antrean prioritas.\n")
            
    return None, None

if __name__ == "__main__":
    ROMANIA_MAP = {
        'Arad': {'neighbors': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118}, 'h': 366},
        'Zerind': {'neighbors': {'Arad': 75, 'Oradea': 71}, 'h': 374},
        'Oradea': {'neighbors': {'Zerind': 71, 'Sibiu': 151}, 'h': 380},
        'Sibiu': {'neighbors': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80}, 'h': 253},
        'Timisoara': {'neighbors': {'Arad': 118, 'Lugoj': 111}, 'h': 329},
        'Lugoj': {'neighbors': {'Timisoara': 111, 'Mehadia': 70}, 'h': 244},
        'Mehadia': {'neighbors': {'Lugoj': 70, 'Drobeta': 75}, 'h': 241},
        'Drobeta': {'neighbors': {'Mehadia': 75, 'Craiova': 120}, 'h': 242},
        'Craiova': {'neighbors': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138}, 'h': 160},
        'Rimnicu Vilcea': {'neighbors': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97}, 'h': 193},
        'Fagaras': {'neighbors': {'Sibiu': 99, 'Bucharest': 211}, 'h': 176},
        'Pitesti': {'neighbors': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101}, 'h': 100},
        'Bucharest': {'neighbors': {}, 'h': 0},
    }

    titik_awal = 'Sibiu'
    titik_tujuan = 'Bucharest'
    
    print(f"Mencari rute optimal dari {titik_awal} ke {titik_tujuan} menggunakan A*...")
    
    hasil_jalur, total_jarak = a_star_search(ROMANIA_MAP, titik_awal, titik_tujuan)
    
    print("\n\n===== HASIL AKHIR =====")
    if hasil_jalur:
        print("Jalur optimal ditemukan! ✅")
        print(f"Rute: {' -> '.join(hasil_jalur)}")
        print(f"Total Jarak: {total_jarak} km")
    else:
        print("Jalur tidak ditemukan. ❌")