<<<<<<< HEAD
print("Hello, Coin Management!")
=======
import getpass
import time
import pyfiglet
import json
import os

# Fungsi untuk menampilkan teks dengan warna
def print_color(text, color_code):
    print(f"\033[{color_code}m{text}\033[00m")

# Fungsi untuk menampilkan teks besar dengan pyfiglet
def print_big_text(text):
    big_text = pyfiglet.figlet_format(text)
    print(big_text)

# Fungsi untuk membersihkan layar
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk melakukan autentikasi
def authenticate():
    print_color("Welcome", "38;5;220")
    password = getpass.getpass("Password: ")
    id_pengenal = input("ID Pengenal: ")
    if password == "000111":
        return True, id_pengenal
    else:
        return False, id_pengenal

# Fungsi untuk menampilkan profil
def display_profile(id_pengenal, coins):
    print_color("Profile Account", "90")
    print("ID: ", end="")
    print_color(id_pengenal, "34")
    print("Rank: ", end="")
    if id_pengenal == "nurtipurnama":
        print_color("Admin", "38;5;196")  # Warna merah terang dari rainbow
    elif id_pengenal == "andrew":
        print_color("Tester", "38;5;94")  # Warna coklat
    else:
        print_color("Rookie", "38;5;130")
    print("Coins: ", end="")
    if id_pengenal == "nurtipurnama":
        print_color("Infinite", "38;5;196")  # Warna merah terang dari rainbow
    elif id_pengenal == "andrew":
        print_color(str(coins), "38;5;94")  # Warna coklat
    else:
        print_color(str(coins), "36")

# Fungsi untuk menghitung rata-rata
def calculate_average(scores):
    return sum(scores) / len(scores)

# Fungsi untuk menyimpan data koin ke file
def save_coins_data(data):
    with open('coins_data.json', 'w') as f:
        json.dump(data, f)

# Fungsi untuk memuat data koin dari file
def load_coins_data():
    try:
        with open('coins_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Fungsi Analyzer Tools
def analyzer_tools(coins):
    if coins < 10:
        print("Koin tidak mencukupi untuk menggunakan Analyzer Tools.")
        return coins
    matches = int(input("Berapa match terakhir yang ingin dianalisis (1-20)? "))
    if matches < 1 or matches > 20:
        print("Jumlah match tidak valid.")
        return coins
    tim1_scores = [float(input(f"Skor tim 1 match {i+1}: ")) for i in range(matches)]
    tim2_scores = [float(input(f"Skor tim 2 match {i+1}: ")) for i in range(matches)]
    tim1_avg_last = calculate_average(tim1_scores)
    tim2_avg_last = calculate_average(tim2_scores)
    print(f"Tim 1 last match average: {tim1_avg_last}")
    print(f"Tim 2 last match average: {tim2_avg_last}")
    h2h = input("Mau menganalisa H2H (y/n)? ")
    if h2h.lower() == 'y':
        tim1_h2h_scores = [float(input(f"Skor H2H tim 1 match {i+1}: ")) for i in range(matches)]
        tim2_h2h_scores = [float(input(f"Skor H2H tim 2 match {i+1}: ")) for i in range(matches)]
        tim1_avg_h2h = calculate_average(tim1_h2h_scores)
        tim2_avg_h2h = calculate_average(tim2_h2h_scores)
        print(f"Tim 1 H2H average: {tim1_avg_h2h}")
        print(f"Tim 2 H2H average: {tim2_avg_h2h}")
        tim1_final_avg = tim1_avg_last + tim1_avg_h2h
        tim2_final_avg = tim2_avg_last + tim2_avg_h2h
        print(f"Tim 1 average last match + average H2H: {tim1_final_avg}")
        print(f"Tim 2 average last match + average H2H: {tim2_final_avg}")
    coins -= 10
    return coins

# Fungsi untuk membandingkan rating pemain
def compare_players(coins):
    if coins < 10:
        print("Koin tidak mencukupi untuk menggunakan Compare Players Tools.")
        return coins
    print("Masukkan nama dan rating pemain untuk tim 1:")
    players_team1 = []
    for i in range(5):
        name = input(f"Nama pemain tim 1 ke-{i+1}: ")
        ratings = [float(input(f"Rating game ke-{j+1} (5-10): ")) for j in range(5)]
        avg_rating = calculate_average(ratings)
        players_team1.append((name, avg_rating))
    
    print("Masukkan nama dan rating pemain untuk tim 2:")
    players_team2 = []
    for i in range(5):
        name = input(f"Nama pemain tim 2 ke-{i+1}: ")
        ratings = [float(input(f"Rating game ke-{j+1} (5-10): ")) for j in range(5)]
        avg_rating = calculate_average(ratings)
        players_team2.append((name, avg_rating))

    print("\nHasil Perbandingan:")
    print("Tim 1:")
    for name, avg_rating in players_team1:
        print_color(f"Nama pemain: {name}", "31")
        print(f"Rating: {avg_rating}")
    print("Tim 2:")
    for name, avg_rating in players_team2:
        print_color(f"Nama pemain: {name}", "34")
        print(f"Rating: {avg_rating}")

    # Menghitung rata-rata rating tim
    avg_team1 = calculate_average([player[1] for player in players_team1])
    avg_team2 = calculate_average([player[1] for player in players_team2])
    
    # Menghitung persentase perbandingan
    total_avg = avg_team1 + avg_team2
    team1_percentage = (avg_team1 / total_avg) * 100
    team2_percentage = (avg_team2 / total_avg) * 100

    print("\nRata-rata Rating:")
    print(f"Rata-rata rating Tim 1: {avg_team1:.2f}")
    print(f"Rata-rata rating Tim 2: {avg_team2:.2f}")
    print(f"Persentase perbandingan: Tim 1 = {team1_percentage:.2f}%, Tim 2 = {team2_percentage:.2f}%")
    
    coins -= 10
    return coins

# Fungsi Corner Specialist Tools
def corner_specialist_tools(coins):
    if coins < 5:
        print("Koin tidak mencukupi untuk menggunakan Corner Specialist Tools.")
        return coins
    matches = int(input("Berapa match terakhir yang ingin dianalisis (1-20)? "))
    if matches < 1 or matches > 20:
        print("Jumlah match tidak valid.")
        return coins
    tim1_corners = [float(input(f"Jumlah corner tim 1 match {i+1}: ")) for i in range(matches)]
    tim2_corners = [float(input(f"Jumlah corner tim 2 match {i+1}: ")) for i in range(matches)]
    avg_corner_tim1 = calculate_average(tim1_corners)
    avg_corner_tim2 = calculate_average(tim2_corners)
    print(f"Average corner tim 1: {avg_corner_tim1}")
    print(f"Average corner tim 2: {avg_corner_tim2}")
    over_under = "over" if (avg_corner_tim1 + avg_corner_tim2) > 9.5 else "under"
    print(f"Match ini akan over/under 9.5: {over_under}")
    coins -= 5
    return coins

# Fungsi Props Tools
def props_tools(coins):
    if coins < 3:
        print("Koin tidak mencukupi untuk menggunakan Props Tools.")
        return coins
    player_name = input("Nama Pemain: ")
    points = [float(input(f"Points match {i+1}: ")) for i in range(5)]
    rebounds = [float(input(f"Rebounds match {i+1}: ")) for i in range(5)]
    assists = [float(input(f"Assists match {i+1}: ")) for i in range(5)]
    points_avg = calculate_average(points)
    rebounds_avg = calculate_average(rebounds)
    assists_avg = calculate_average(assists)
    print(f"Nama: {player_name}")
    print(f"Points average: {points_avg}")
    print(f"Rebounds average: {rebounds_avg}")
    print(f"Assists average: {assists_avg}")
    coins -= 3
    return coins

# Fungsi Win Rate Calculator
def win_rate_calculator(coins):
    if coins < 7:
        print("Koin tidak mencukupi untuk menggunakan Win Rate Calculator.")
        return coins
    matches = int(input("Berapa match terakhir yang ingin dianalisis (1-20)? "))
    if matches < 1 or matches > 20:
        print("Jumlah match tidak valid.")
        return coins
    tim1_results = [input(f"Hasil tim 1 match {i+1} (win/lose): ").lower() for i in range(matches)]
    tim2_results = [input(f"Hasil tim 2 match {i+1} (win/lose): ").lower() for i in range(matches)]
    tim1_wins = tim1_results.count("win")
    tim2_wins = tim2_results.count("win")
    tim1_win_rate = (tim1_wins / matches) * 100
    tim2_win_rate = (tim2_wins / matches) * 100
    print(f"Win rate tim 1: {tim1_win_rate:.2f}%")
    print(f"Win rate tim 2: {tim2_win_rate:.2f}%")
    coins -= 7
    return coins

# Menu utama
def main_menu():
    authenticated, id_pengenal = authenticate()
    
    # Memuat data koin dari file
    coins_data = load_coins_data()
    if id_pengenal == "nurtipurnama":
        coins = float('inf')
    elif id_pengenal == "nickandrew":
        coins = 500
    else:
        coins = coins_data.get(id_pengenal, 100)
    
    if authenticated:
        print_big_text("Tools")
        while True:
            clear_screen()
            display_profile(id_pengenal, coins)
            print("\nMenu:")
            print("1. Analyzer Tools (10 coins)")
            print("2. Corner Specialist Tools (5 coins)")
            print("3. Props Tools (3 coins)")
            print("4. Win Rate Calculator (7 coins)")
            print("5. Compare Players (10 coins)")
            print("6. Exit")
            print("\nScript created by: nurtipurnama")
            print("Source: GitHub")
            print("Since: 2025-02-28")
            choice = input("Pilih opsi (1-6): ")
            clear_screen()
            if choice == '1':
                coins = analyzer_tools(coins)
            elif choice == '2':
                coins = corner_specialist_tools(coins)
            elif choice == '3':
                coins = props_tools(coins)
            elif choice == '4':
                coins = win_rate_calculator(coins)
            elif choice == '5':
                coins = compare_players(coins)
            elif choice == '6':
                print("Terima kasih telah menggunakan script ini. Sampai jumpa!")
                break
            else:
                print("Opsi tidak valid. Silakan coba lagi.")
        
        # Menyimpan data koin ke file sebelum keluar
        if id_pengenal != "nurtipurnama":
            coins_data[id_pengenal] = coins
            save_coins_data(coins_data)
    else:
        print("Autentikasi gagal. Silakan coba lagi.")

if __name__ == "__main__":
    main_menu()
>>>>>>> 63d86016e92cd1267dceba4c189f67c590b3f70b
