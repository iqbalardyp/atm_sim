# ATMProgram
import random
import datetime
from customer import Customer

atm = Customer()
mesin = True
debt = []
n_change = 0


# Define Method
def CekSaldo():
    return print('Saldo Anda: Rp', atm.CekSaldo(), '\n')


def UbahPIN():
    while True:
        verPIN = int(input('Masukkan PIN Anda: '))
        while verPIN != int(atm.CekPIN()):
            verPIN = int(input('PIN Salah! Masukkan PIN Anda: '))

        newPIN = int(input('Masukkan PIN Baru: '))
        ver_newPIN = int(input('Masukkan Ulang PIN Baru: '))
        attempt = 0
        while ver_newPIN != newPIN and attempt < 3:
            ver_newPIN = int(input('PIN Berbeda! Masukkan Ulang PIN Baru: '))
            attempt += 1
            if attempt == 3:
                print('Penggantian PIN gagal! Untuk Mengganti PIN, silakan ke Cabang terdekat\n')
                break

        atm.pin = newPIN
        print('Nomor PIN telah diperbaharui!\n')
        break


def TarikTunai():
    global n_change
    while True:
        val = float(input('Masukkan nominal (kelipatan Rp50.000 atau Rp100.000):'))
        while atm.balance - val < 50000:
            print('Saldo tidak mencukupi!')
            val = float(input('Masukkan nominal (kelipatan Rp50.000 atau Rp100.000):'))
        print('Anda ingin menarik saldo sebesar Rp', val, '?')
        confirm = input('Konfirmasi (Y/N): ')
        if confirm == 'Y':
            atm.balance -= val
            debt.append(val)
            n_change += 1
            print('Transaksi berhasil. Saldo Anda: ', atm.CekSaldo(), '\n')
            cetak_struk()
            break
        else:
            break


def SetorTunai():
    global n_change
    while True:
        val = float(input('Masukkan nominal (kelipatan Rp50.000 atau Rp100.000):'))
        print('Anda ingin menambah saldo sebesar Rp', val, '?')
        confirm = input('Konfirmasi (Y/N): ')
        if confirm == 'Y':
            atm.balance += val
            debt.append(val)
            n_change += 1
            print('Transaksi berhasil. Saldo Anda: ', atm.CekSaldo(), '\n')
            cetak_struk()
            break
        else:
            print('Silakan ambil kembali uang Anda\n')
            break


def Keluar():
    global mesin
    print('Terima kasih telah menggunakan layanan ATM\n')
    mesin = False


# Struk
def tanggal():
    return datetime.datetime.now()


def nostruk():
    return random.randint(50000, 100000)


# format struk
transc = {'2': 'D', '3': 'C'}
msg_plus = '+++++++++++++++++++++++++++++++++++++'
msg_min = '-------------------------------------'
msg_struk = 'No. Struk: '
msg_tgl = 'Tanggal: '
msg_header = '++++++++++++++Transaksi++++++++++++++'
# msg_transc = 'D/C'
# msg_balance = 'Saldo Akhir'
msg_footer = '            Terima Kasih              \n'


def cetak_struk():
    print(msg_plus)
    print(msg_struk, nostruk())
    print(msg_tgl, tanggal())
    print(msg_header)
    print(transc[str(menu)], ': Rp', int(debt[n_change - 1]))
    print(msg_min)
    print('Saldo Akhir: Rp', atm.CekSaldo())
    print(msg_plus)
    print(msg_footer)


# Daftar
daftar_menu = ['Cek Saldo', 'Tarik Tunai', 'Setor Tunai', 'Ubah PIN', 'Keluar']
# daftar_method = ['CekSaldo', 'TarikTunai', 'SetorTunai', 'UbahPIN', 'Keluar']


# Verification
while True:
    ID = int(input('Masukkan Nomor PIN Anda: '))
    attempt = 0
    while ID != atm.pin and attempt < 3:
        ID = int(input('PIN Salah. Masukkan Nomor PIN Anda:'))
        attempt += 1
        if attempt == 3:
            print('Kartu Anda Terblokir. Silakan ke Cabang Terdekat.')
            break
    break
# Interface Menu
while mesin == True:
    print('Selamat Datang!\nSilakan Pilih Menu:')
    for i in range(len(daftar_menu)): print(i + 1, '-', daftar_menu[i])
    menu = int(input('\nPilih Menu: '))
    eval(daftar_menu[menu - 1].replace(' ', '') + '()')