import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("================================================")
    print("\t\tProgram volume ruang")
    print("Created by Muhammad Daffa Putra Mahardika")
    print("================================================")
    print("[1] Kubus")
    print("[2] Prisma Segitiga")
    print("[3] Tabung")
    print("[4] Kerucut")
    print("[5] Bola")
    print("[0] Keluar")
    selected_menu = str(input("Pilih menu> "))

    if(selected_menu == "1"):
        show_menu_kubus()
    elif(selected_menu == "2"):
        prisma_segitiga()
    elif(selected_menu == "3"):
        show_menu_tabung()
    elif(selected_menu == "4"):
        show_menu_kerucut()
    elif(selected_menu == "5"):
        show_menu_bola()
    elif (selected_menu == "0"):
        close_app()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()


def show_menu_kubus():
    clear_screen()
    print("============================")
    print("\t\tKUBUS")
    print("============================")
    s = int(input('masukan sisi kubus: '))
    V = s ** 3
    print('Volume kubus dengan sisi {} adalah {} \n'. format(s, V))


def prisma_segitiga():
    clear_screen()
    print('============================')
    print('\t\tPRISMA SEGITIGA')
    print('============================')
    a = float(input('masukan alas segitiga: '))
    t = int(input('masukan tinggi segitiga: '))
    La = 1/2 * a * t 
    print('Luas segitiga dengan alas {} tinggi {} adalah {}'.format(a, t, La))

    print('Sudah didapatkan luas alas')
    print('Tinggal menghitung volumenya')
    T = int(input('masukan tinggi prisma segitiga: '))
    V = La * T 
    print('Volume prisma segitiga dengan tinggi {} luas alas {} adalah {} \n'. format(T, La, V ))


def show_menu_tabung():
    clear_screen()
    print('============================')
    print('\t\tTABUNG')
    print('============================')
    r = int(input('masukan jari-jari tabung: '))
    t = int(input('masukan tinggi tabung: '))
    π = 3.14
    V = π ** r * t 
    print('Volume tabung dengan jari-jari {} tinggi {} π {} adalah {} \n'.format(r, t, π, V))


def show_menu_kerucut():
    clear_screen()
    print('============================')
    print('\t\tKERUCUT')
    print('============================')
    r = int(input('masukan jari-jari: '))
    t = int(input('masukan tinggi: '))
    π = 3.14
    V = 1/3 * π ** r * t 
    print('Volume kerucut dengan jari-jari {} tinggi {} π {} adalah {} \n'.format(r, t, π, V))


def show_menu_bola():
    clear_screen()
    print('============================')
    print('\t\tBOLA')
    print('============================')
    r = int(input('masukan jari-jari: '))
    t = int(input('masukan tinggi: '))
    π = 3.14
    V = 4/3 * π ** r * t 
    print('Volume bola dengan jari-jari {} tinggi {} π {} adalah {} \n'.format(r, t, π, V))


def close_app():
    clear_screen()
    print("==========================================================")
    print("Terima kasih telah menggunakan Program Volume Ruang")
    print("==========================================================")
    time.sleep(3)
    exit()

def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()
    
def back_to_kubus():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu_kubus()

def back_to_prisma_segitiga():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu_prisma_segitiga()

def back_to_menu_tabung():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu_tabung()

def back_to_menu_kerucut():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu_kerucut()

def back_to_menu_bola():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu_bola()


if __name__ == "__main__":
    while True:
        show_menu()
