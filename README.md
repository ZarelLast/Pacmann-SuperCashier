# Dokumentasi
---
## Requirements & Objectives
**Latar Belakang**
Andi ingin menambahkan sistem self-service di supermarket miliknya agar customer bisa membeli barang sesuai kebutuhan mereka di tempat yang jauh dari supermarket, misalnya saat di kota lain
<br/><br/>
**Requirement:**
- **add_item([ <nama_item>, <jumlah_item>, <harga_per_item> ])** <br/>
Method yang digunakan untuk menambahkan item berdasarkan parameter berikut:
  - **<nama_item>:** attribute nama barang yang akan dibeli oleh customer
  - **<jumlah_item>:** attribute jumlah barang yang akan dibeli oleh customer
  - **<harga_per_item>:** attribute harga barang per satuan
- **update_item_name(<id_item>, <update_nama_item>)** <br/>
Method yang digunakan untuk mengupdate item berdasarkan parameter berikut:
	- **<id_item>:** attribute id barang yang akan diubah oleh customer
	- **<update_nama_item>:** attribute nama barang yang baru
- **update_item_qty(<id_item>, <update_jumlah_item>)**
	- **<id_item>**: attribute id barang yang akan diubah oleh customer
	- **<update_jumlah_item>**: attribute jumlah barang yang baru
- **update_item_price(<id_item>, <update_harga_item>)**
	- **<id_item>**: attribute id barang yang akan diubah oleh customer
	-	**<update_harga_item>**: attribute harga barang yang baru
- **delete_item(<id_item>)** <br/>
Method yang digunakan untuk menghapus salah satu atau beberapa item barang dari list keranjang barang yang akan dibeli berdasarkan id barang
  - **<id_item>:** attribute id barang yang akan dihapus oleh customer
- **reset_transaction()** <br/>
Method yang digunakan untuk menghapus semua barang belanjaan di dalam list keranjang yang tidak akan dibeli
- **check_order()** <br/>
Method yang digunakan untuk mengecek barang yang telah diinputkan kedalam keranjang, apakah sudah sesuai dengan keinginan atau tidak. Ditampilkan dalam bentuk tabel.
- **total_price()** <br/>
Method yang digunakan untuk menampilkan harga total keseluruhan item barang yang dibeli beserta diskonnya. Nilai yang ditampilkan adalah total harga yang telah dikenakan diskon.
<br/><br/>
**Objektif:**
Membuat aplikasi python kasir self-service sehingga customer/pelanggan bisa menginput barang sendiri sesuai dengan yang mereka inginkan

## Flowchart
![Flowchart](https://github.com/ZarelLast/Pacmann-SuperCashier/blob/main/flowchart.png?raw=true)

## Conclusion
- Dengan Class yang sudah dibuat 
- Untuk future work, seandainya saya memiliki waktu lebih dan SDM lebih mungkin saya akan mengembangkan modul ini menjadi aplikasi yang memiliki tampilan GUI dan terkoneksi dengan Database

---
## Demonstrasi

---
### Tambah Barang
- Code
```python
# inisialsisasi instance transaksi
transaksi_1 = Transaction()

# menambah item
transaksi_1.add_items(['bakso', 5, 13_000])
transaksi_1.add_items(['soto', 3, 8_000])

# show keranjang
transaksi_1.check_order()

# membuat output sesuai test case
# {'nama_item': [jumlah, harga]}
transaksi_1.test_case_output(transaksi_1.keranjang)
```
- Output
![Add Item](https://github.com/ZarelLast/Pacmann-SuperCashier/blob/main/output/add_item.png?raw=true)
### Update Barang
```python
# inisialsisasi instance transaksi
transaksi_2 = Transaction()

# menambah item
transaksi_2.add_items(['bakso', 5, 13_000])
transaksi_2.add_items(['soto', 3, 8_000])
transaksi_2.add_items(['', '3', '8_000'])

# update nama item
transaksi_2.update_item_name(id_item=3, update_nama='ayam')

# update harga item
transaksi_2.update_item_price(id_item=3, update_harga=3_000)

# update jumlah item
transaksi_2.update_item_qty(id_item=3, update_jumlah=10)

# membuat output sesuai test case
# {'nama_item': [jumlah, harga]}
transaksi_2.test_case_output(transaksi_2.keranjang)
```
### Delete Barang
```python
# inisialsisasi instance transaksi
transaksi_3 = Transaction()

# menambah item
transaksi_3.add_items(['bakso', 5, 13_000])
transaksi_3.add_items(['soto', 3, 8_000])
transaksi_3.add_items(['', '3', '8_000'])

# menghapus item
transaksi_3.delete_item(3)

# membuat output sesuai test case
# {'nama_item': [jumlah, harga]}
transaksi_3.test_case_output(transaksi_3.keranjang)
```
### Check Order
#### Check tanpa error
```python
# inisialsisasi instance transaksi
transaksi_4 = Transaction()

# menambah item
transaksi_4.add_items(['bakso', 5, 13_000])
transaksi_4.add_items(['soto', 3, 8_000])

# menghapus item
print("Dibawah ini output check_order")
transaksi_4.check_order()

# membuat output sesuai test case
# {'nama_item': [jumlah, harga]}
transaksi_4.test_case_output(transaksi_4.keranjang)
```
#### Check jika error
```python
# inisialsisasi instance transaksi
transaksi_5 = Transaction()

# menambah item
transaksi_5.add_items(['bakso', 5, 13_000])
transaksi_5.add_items(['soto', '3', 8_000])

# menghapus item
print("Dibawah ini output check_order")
transaksi_5.check_order()

# membuat output sesuai test case
# {'nama_item': [jumlah, harga]}
transaksi_5.test_case_output(transaksi_5.keranjang)
```
### Reset Transaksi
```python
# inisialsisasi instance transaksi
transaksi_6 = Transaction()

# menambah item
transaksi_6.add_items(['bakso', 5, 13_000])
transaksi_6.add_items(['soto', 3, 8_000])

# membuat output sesuai test case
# {'nama_item': [jumlah, harga]}
transaksi_6.test_case_output(transaksi_6.keranjang)

# reset transaksi
transaksi_6.reset_transaction()

# check order
transaksi_6.check_order()
```
### Total Harga
```python
# inisialsisasi instance transaksi
transaksi_7 = Transaction()

# menambah item
transaksi_7.add_items(['bakso', 5, 13_000])
transaksi_7.add_items(['soto', 3, 8_000])

# membuat output sesuai test case
# {'nama_item': [jumlah, harga]}
transaksi_7.test_case_output(transaksi_7.keranjang)

# hitung total belanja
transaksi_7.total_price()
```
### Menu Transaksi
```python
transaksi = Transaction()
transaksi.menu()
```