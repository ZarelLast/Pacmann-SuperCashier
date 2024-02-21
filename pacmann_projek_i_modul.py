# -*- coding: utf-8 -*-
"""Pacmann_Projek I - Modul.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sHgbiNllFiJARyosWdD8WPM2CYcsZ6Y_
"""

from tabulate import tabulate
import os

class Transaction():
  '''
    Class Transaction merupakan objek yang mewakili transaksi.

    Class ini menyediakan metode untuk mengelola transaksi, termasuk menambahkan
    item ke keranjang, mengupdate item, dan menghapus item serta menampilkan
    list belanjaan.

  '''

  def __init__(self):
    '''
      inisiasi kelas
    '''
    self.keranjang = []

  def add_items(self, data):
    '''
      Menambahkan item ke keranjang

      Parameter :
      -----------
      data : list/dict
        Data item berisikan nama, jumlah dan harga barang

    '''
    if len(self.keranjang) == 0:
      id_barang = len(self.keranjang) + 1
    else:
      for barang in self.keranjang:
        id_barang = barang['id'] + 1

    try:
      self.keranjang.append({
        "id": id_barang,
        "nama" : data[0],
        "jumlah" : data[1],
        "harga" : data[2],
        "total" : data[1]*data[2]
      })

    except:
      self.keranjang.append({
        "id": id_barang,
        "nama" : data[0],
        "jumlah" : data[1],
        "harga" : data[2],
        "total" : 0
      })

    self.check_order()
    self.test_case_output(self.keranjang)

  def update_item_name(self, id_item, update_nama):
    '''
      Memperbaiki dan mengupdate nama item

      Parameter :
      ----------
      id_item : int
        ID item berdasarkan urutan pemesanan
      update_nama : str
        Nama item baru yang akan diberikan

    '''
    for barang in self.keranjang:
      if barang['id'] == id_item:
        barang.update({
            'id': barang['id'],
            'nama': update_nama,
            'jumlah': barang['jumlah'],
            'harga': barang['harga'],
            'total': barang['total']
          })

    self.check_order()
    self.test_case_output(self.keranjang)

  def update_item_qty(self, id_item, update_jumlah):
    '''
      Memperbaiki dan mengupdate jumlah item

      Parameter :
      ----------
      id_item : int
        ID item berdasarkan urutan pemesanan
      update_jumlah : str
        Jumlah item baru yang akan diberikan

    '''
    for barang in self.keranjang:
      if barang['id'] == id_item:
        barang.update({
            'id': barang['id'],
            'nama': barang['nama'],
            'jumlah': update_jumlah,
            'harga': barang['harga'],
            'total': update_jumlah*barang['harga']
          })

    self.check_order()
    self.test_case_output(self.keranjang)

  def update_item_price(self, id_item, update_harga):
    '''
      Memperbaiki dan mengupdate harga item

      Parameter :
      ----------
      id_item : int
        ID item berdasarkan urutan pemesanan
      update_harga : str
        Harga item baru yang akan diberikan

    '''
    for barang in self.keranjang:
      if barang['id'] == id_item:
        barang.update({
            'id': barang['id'],
            'nama': barang['nama'],
            'jumlah': barang['jumlah'],
            'harga': update_harga,
            'total': barang['jumlah']*update_harga
          })

    self.check_order()
    self.test_case_output(self.keranjang)

  def delete_item(self, id_item):
    '''
      Menghapus salah satu item dari keranjang

      Parameter :
      ----------
      id_item : int
        ID item yang akan dihapus

    '''
    for index, barang in enumerate(self.keranjang):
      if barang['id'] == id_item:
        self.keranjang.pop(index)

    self.check_order()
    self.test_case_output(self.keranjang)

  def reset_transaction(self):
    '''
      Menghapus seluruh item dari keranjang

    '''
    self.keranjang = []
    print("keranjang telah dikosongkan")

  def check_order(self):
    '''
      Mengecek item dan kesalahan yang terdapat dalam keranjang

    '''
    header = ["No.", "Nama Barang", "Jumlah Barang", "Harga Satuan", "Jumlah Harga"]
    table = []
    for barang in self.keranjang:
      table.append([
          barang["id"],
          barang["nama"],
          barang["jumlah"],
          barang["harga"],
          barang["total"]
        ])
    print(tabulate(table, headers = header, tablefmt = "github"))

    try:
      for barang in self.keranjang:
        if len(barang["nama"]) == 0:
          raise ValueError(f"Barang ID - {barang['id']}: Nama tidak sesuai")
        if type(barang["jumlah"]) != int:
          raise ValueError(f"Barang ID - {barang['id']}: Jumlah Barang bukan angka")
        if type(barang["harga"]) != int:
          raise ValueError(f"Barang ID - {barang['id']}: Harga bukan angka")

    except ValueError as e:
      print(e)

    self.total_price()

  def total_price(self):
    '''
      Menampilkan harga keseluruhan item dalam keranjang
      beserta diskon dan harga setelah diskon

    '''
    try:
      total_harga = 0
      for barang in self.keranjang:
        total_harga += barang["total"]
      if total_harga > 500_000:
        total_harga = total_harga - (total_harga * 0.1)
        print("Selamat! Anda mendapatkan diskon sebesar 10%")
      elif total_harga > 300_000:
        total_harga = total_harga - (total_harga * 0.08)
        print("Selamat! Anda mendapatkan diskon sebesar 8%")
      elif total_harga > 200_000:
        total_harga = total_harga - (total_harga * 0.05)
        print("Selamat! Anda mendapatkan diskon sebesar 5%")
      print(f"\nTotal harga yang harus dibayar adalah Rp.{total_harga:,.0f}")

    except TypeError:
      print(TypeError('PESANAN TIDAK SESUAI, Silahkan di cek kembali'))

  def input_validasi(self, teks, type_data):
    """
    Validasi Input dari inputan pelanggan

      Parameter :
      -----------
      teks : str
        teks berisikan teks yang akan di keluarkan pada saat input
      type_data : type
        type_data berisikan type data yang akan digunakan untuk input

      Return :
      -----------
      value : str/int
        value berisikan inputan user yang sudah di validasi
        jika inputan error maka akan return 0 atau string kosong

    """
    if type_data == str:
      try:
        value = str(input(f"{teks}: "))
      except ValueError:
        value = ''
        print(ValueError(f"Input Error - {teks} tidak sesuai, harap update {teks}"))

    if type_data == int:
      try:
        value = int(input(f"{teks}: "))
      except ValueError:
        value = 0
        print(ValueError(f"Input Error - {teks} bukan angka, harap update {teks}"))

    return value

  def test_case_output(self, data):
    """
    Untuk membuat output sesuai dengan keinginan test case

      Parameter :
      -----------
      data : list
        data berisikan list yang didalamnya terdapat dictionary
        [{'nama':'soto', 'jumlah':10, 'harga':8000}]

    """
    res = {}
    for barang in data:
      res[barang['nama']] = [barang['jumlah'], barang['harga']]
    print(f"Barang yang dibeli: \n{res}\n\n\n")

  def menu(self):
    stats = True
    while stats:
      os.system('cls')
      self.check_order()
      print("\n\nMenu Utama")
      header = ["No.", "Opsi"]
      table = [
          [0, "Check Keranjang"],
          [1, "Tambah Item"],
          [2, "Update Nama Item"],
          [3, "Update Jumlah Item"],
          [4, "Update Harga Item"],
          [5, "Hapus Item"],
          [6, "Bayar dan Checkout"],
          [7, "Batal Belanja"]
        ]
      print(tabulate(table, headers = header, tablefmt = "github"))

      try:
        opsi = int(input("\nPilih opsi: "))
      except ValueError:
        opsi = 10

      if opsi == 0:
        self.check_order()
        self.test_case_output(self.keranjang)
      elif opsi == 1:
        nama_item = self.input_validasi(teks="Nama Barang", type_data=str)
        jumlah_item = self.input_validasi(teks="Jumlah Barang", type_data=int)
        harga_item = self.input_validasi(teks="Harga Barang", type_data=int)
        self.add_items([nama_item, jumlah_item, harga_item])
      elif opsi == 2:
        if len(self.keranjang) != 0:
          try:
            id_item = int(input("Id barang: "))
          except:
            print('id tidak tersedia')
            continue
          nama_baru_item = self.input_validasi(teks="Nama Barang", type_data=str)
          self.update_item_name(id_item, nama_baru_item)
        else:
          print('Keranjang anda masih kosong!')
      elif opsi == 3:
        if len(self.keranjang) != 0:
          try:
            id_item = int(input("Id barang: "))
          except:
            print('id tidak tersedia')
            continue
          jumlah_baru_item = self.input_validasi(teks="Jumlah Barang", type_data=int)
          self.update_item_qty(id_item, jumlah_baru_item)
        else:
          print('Keranjang anda masih kosong!')
      elif opsi == 4:
        if len(self.keranjang) != 0:
          try:
            id_item = int(input("Id barang: "))
          except:
            print('id tidak tersedia')
            continue
          harga_baru_item = self.input_validasi(teks="Harga Barang", type_data=int)
          self.update_item_price(id_item, harga_baru_item)
        else:
          print('Keranjang anda masih kosong!')
      elif opsi == 5:
        if len(self.keranjang) != 0:
          try:
            id_item = int(input("Id barang: "))
          except:
            print('id tidak tersedia')
            continue
          pilih = input("Anda yakin ingin menghapus item? (y=ya, t=tidak): ")
          if pilih.lower() == 'y' or pilih.lower() == 'ya':
            self.delete_item(id_item)
          elif pilih.lower() == 't' or pilih.lower() == 'tidak':
            pass
          else:
            print('Opsi tidak tersedia!')
        else:
          print('Keranjang anda masih kosong!')
      elif opsi == 6:
        if len(self.keranjang) != 0:
          self.check_order()
          self.test_case_output(self.keranjang)

          pilih = input("anda yakin ingin checkout? (y=ya, t=tidak): ")
          if pilih.lower() == 'y' or pilih.lower() == 'ya':
            self.test_case_output(self.keranjang)
            self.total_price()
            self.reset_transaction()
            stats = False
          elif pilih.lower() == 't' or pilih.lower() == 'tidak':
            pass
          else:
            print('Opsi tidak tersedia!')
        else:
          print('Keranjang anda masih kosong!')
      elif opsi == 7:
        pilih = input("anda yakin ingin Batal Beli? (y=ya, t=tidak): ")
        if pilih.lower() == 'y' or pilih.lower() == 'ya':
          self.reset_transaction()
          stats = False
        elif pilih.lower() == 't' or pilih.lower() == 'tidak':
          pass
        else:
          print('Opsi tidak tersedia!')
      else:
        print("Opsi tidak tersedia!")