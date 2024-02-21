# Dokumentasi
---
Modul Transaksi
---
## Contoh Penggunaan Modul
### Tambah Barang
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