from PIL import Image
import matplotlib.pyplot as plt

def counting_sort_colors(arr):
    # Renklerin RGB değerlerine göre sıralama yapacağız
    min_val = min(arr)
    max_val = max(arr)
    
    # Sayma dizisini oluştur
    count = [0] * (max_val - min_val + 1)
    
    # Her rengin sayısını tut
    for color in arr:
        count[color - min_val] += 1
    
    # Sıralı listeyi oluştur
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i + min_val] * count[i])
    
    return sorted_arr

def get_image_colors(image_path):
    try:
        # Görseli açalım
        img = Image.open(image_path)
        
        # Görseli RGB modunda aç
        img = img.convert('RGB')
        
        # Görseldeki tüm renkleri al
        colors = list(img.getdata())
        
        return colors
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        return None

def show_sorted_colors(sorted_colors):
    # Sıralanan renkleri görselleştirelim
    plt.figure(figsize=(8, 2))
    plt.imshow([sorted_colors], aspect='auto')
    plt.axis('off')
    plt.show()

# Görsel yolunu gir
image_path = 'CountingSort.png'  # Görsel dosyanızın yolu

# Görseldeki renkleri al
colors = get_image_colors(image_path)

if colors:
    # RGB bileşenlerinin toplamını al
    color_values = [sum(color) for color in colors]

    # Renkleri sıralama
    sorted_color_values = counting_sort_colors(color_values)

    # Sıralı renklerin RGB karşılıklarını al
    sorted_colors = [colors[color_values.index(val)] for val in sorted_color_values]

    # Sıralı renkleri görselleştirelim
    show_sorted_colors(sorted_colors)
else:
    print("Görsel açılamadı veya başka bir hata oluştu.")
