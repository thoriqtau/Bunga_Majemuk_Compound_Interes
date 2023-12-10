import os 
# import numpy as np
total_list1 = []
total_list2 = []

tahun_list1 = []
tahun_list2 = []

def bunga_majemuk(modal_awal, bunga, periode):
    if periode == 0:
        return 0 
    else:
        return modal_awal * pow((1 + bunga), periode) + bunga_majemuk(modal_awal, bunga, periode - 1)

def Menu1(periode):
    while periode <= 75:
        total = bunga_majemuk(modal_awal, bunga, periode)
        total_list1.append(f'{total:,.0f}')
        periode += 1
    
    for tahun in range(0, 76):
        tahun_list1.append(tahun)

    total_list1[0] = f'{5000000:,.0f}'
    for index, value in zip(tahun_list1,total_list1):
        print(f'{index:^10} | Rp{value}')

def Menu2(periode):
    while periode <= 75:
        total = bunga_majemuk(modal_awal, bunga, periode)
        total_list2.append(f'{total:,.0f}')
        periode += 1
    
    for tahun in range(0, 75):
        tahun_list2.append(tahun)

    total_list2.pop(0)
    for index, value in zip(tahun_list2,total_list2):
        print(f'{index:^10} | Rp{value}')

if __name__ == '__main__':
    sistem_operasi = os.name
    while True:
        modal_awal = 5000000  
        bunga = 0.07    
        periode = 0  
        match sistem_operasi:
            case 'posix': os.system('clear')
            case 'nt': os.system('cls')
        print(f"{'SELAMAT DATANG DI PROGRAM':^40}")
        print(f"{'MENGHITUNG BUNGA MAJEMUK':^40}")
        print('-'*40)
        print('1. Bunga Majemuk fx')
        print('2. Bunga Majemuk fx(1+r)^0')
        print('3. Keluar')
        option = input('Masukkan Nomer Menu: ')
        match option:    
            case '1':
                print(f'{"Tahun ke -":<10} | {"Hasil Investasi"}')
                print(f'{"":<10} | {"":<30}')
                Menu1(periode)
                # print(f'{tahun}{"|":>10}, {display()}') 
                is_done = input("\nSelesai Melihat? ")
                if is_done:
                    continue
            case '2':
                print(f'{"Tahun ke -":<10} | {"Hasil Investasi"}')
                print(f'{"":<10} | {"":<30}')
                Menu2(periode)
                # print(f'{tahun}{"|":>10}, {display()}') 
                is_done = input("\nSelesai Melihat? ")
                if is_done:
                    continue
            case '3':
                break



