### Regresi Linier Sederhana
Regresi Linear adalah sebuah teknik pemodelan yang menghubungkan suatu variabel dependen dengan suatu variabel independen. Model ini mengasumsikan bahwa variabel - variabel ini memiliki hubungan yang linier. Selain mencari hubungan antara variabel, Regresi linierdapat juga di manfaatkan untuk memprediksi nilai yang tidak diketahu, dengan memasukan nilai pada variabel lain. Bentuk paling dasar dari Regresi Linier adalah Regresi Linier Sederhana l, yang hanya menggunakan satu variabel independen. Regresi linier sederhana dapat dinyatakan dengan persamaan: 


$$Y = \beta_0 + \beta_1X + \varepsilon$$


Keterangan:
- \( Y \) adalah variabel terikat (dependen).
- \( X \) adalah variabel bebas (independen).
- \( \beta_0 \) adalah intersep, yaitu nilai \( Y \) ketika \( X = 0 \).
- \( \beta_1 \) adalah koefisien regresi, yang menunjukkan seberapa besar pengaruh perubahan satu unit \( X \) terhadap \( Y \).
- \( \varepsilon \) adalah error random yang mengikuti distribusi normal dengan rata-rata 0.


Mari kita gunakan contoh yang sederhana untuk memahami konsep Regresi Linier Sederhana. Kita akan menggunakan contoh penjualan es krim berdasarkan suhu hari itu.

Misalkan kita memiliki data penjualan es krim selama 10 hari dengan suhu yang berbeda-beda:


| Suhu (X) | Penjualan Es Krim (Y) |
|----------|-----------------------|
| 20°C     | 50                    |
| 22°C     | 60                    |
| 24°C     | 70                    |
| 26°C     | 80                    |
| 28°C     | 90                    |
| 30°C     | 100                   |
| 32°C     | 110                   |
| 34°C     | 120                   |
| 36°C     | 130                   |
| 38°C     | 140                   |


Dari data ini, kita dapat melihat bahwa semakin tinggi suhu, semakin banyak es krim yang terjual. Sekarang, kita ingin memprediksi berapa banyak es krim yang akan terjual jika suhu adalah 25°C.

Kita akan menggunakan persamaan regresi linier sederhana:

$$ Y = \beta_0 + \beta_1X $$

Dengan mengasumsikan kita telah melakukan perhitungan dan mendapatkan nilai intersep \( \beta_0 \) adalah 10 dan koefisien regresi \( \beta_1 \) adalah 5, persamaan regresi kita menjadi:

$$ Y = 10 + 5X $$

Sekarang, jika kita ingin memprediksi penjualan es krim pada suhu 25°C, kita masukkan nilai X ke dalam persamaan:

$$ Y = 10 + 5(25) $$
$$ Y = 10 + 125 $$
$$ Y = 135 $$

Jadi, berdasarkan model regresi linier sederhana ini, kita memprediksi bahwa akan ada 135 es krim yang terjual pada hari dengan suhu 25°C.

Perlu diingat bahwa ini adalah contoh sederhana untuk tujuan ilustrasi. Dalam praktik nyata, kita akan menggunakan metode statistik untuk menemukan nilai \( \beta_0 \) dan \( \beta_1 \) yang paling akurat berdasarkan data yang kita miliki.
