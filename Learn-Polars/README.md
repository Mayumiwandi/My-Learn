## Polars
[Polars Docs ](https://docs.pola.rs/)  

Polars adalah pustaka DataFrame berkinerja tinggi, yang dirancang untuk memberikan kemampuan pemrosesan data yang cepat dan efisien. Terinspirasi oleh perpustakaan panda yang ada, Polars membawa segalanya ke tingkat yang lebih tinggi, menawarkan pengalaman yang mulus untuk bekerja dengan kumpulan data besar yang mungkin tidak muat dalam memori.

## Polars Philosophy
Tujuan Polars adalah menyediakan pustaka DataFrame secepat kilat yang:

- Memanfaatkan semua inti yang tersedia di mesin Anda.
- Mengoptimalkan kueri untuk mengurangi alokasi kerja/memori yang tidak diperlukan.
- Menangani kumpulan data yang jauh lebih besar daripada RAM yang tersedia.
- API yang konsisten dan dapat diprediksi.
- Mematuhi skema yang ketat (tipe data harus diketahui sebelum menjalankan kueri).
Polars ditulis dalam Rust yang memberikan kinerja C/C++ dan memungkinkannya untuk sepenuhnya mengontrol kinerja bagian-bagian penting dalam mesin kueri.

## Instalasi
Polars adalah perpustakaan dan instalasinya semudah memanggil manajer paket bahasa pemrograman yang sesuai.
```python
pip install polars
```
### Feature Flags
```python
# For example
pip install 'polars[numpy,fsspec]'
```












