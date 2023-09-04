import random

def spin_gacha():
    items = ["Item A", "Item B", "Item C"] # Daftar item
    probabilities = [0.3, 0.5, 0.2] # Probabilitas munculnya masing-masing item
    total_prob = sum(probabilities) # Total probabilitas
    
    random_num = random.random() # Menghasilkan angka acak antara 0 dan 1
    
    cumulative_prob = 0
    for i in range(len(items)):
        cumulative_prob += probabilities[i]
        if random_num <= cumulative_prob/total_prob:
            return items[i] # Mengembalikan hadiah yang dipilih
        
    return "No item" # Jika tidak ada item yang dipilih

# Contoh penggunaan
result = spin_gacha()
print("Anda mendapatkan:", result)
