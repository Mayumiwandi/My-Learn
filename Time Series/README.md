# Laporan Proyek Machine Learning - Ahmad Wandi
## Domain Proyek
Domain yang dipilih untuk proyek *machine learning* ini adalah **Pertanian**, dengan judul **Predictive Analytics: Kualitas Apel**  

### Latar Belakang

![foto apel](https://drive.google.com/uc?export=view&id=19yWl1wFNk4kiOmmS3tVMtzZtRAEi71nc)

Buah merupakan asupan penting bagi tubuh manusia, yang mengandung vitamin dan beberapa unsur lain yang dibutuhkan tubuh manusia. Salah satunya buah apel juga diperlukan tubuh manusia selain mengandung vitamin dan unsur-unsur yang diperlukan tubuh manusia juga memiliki rasa segar. Buah apel juga cukup banyak diminati masyarakat Indonesia. Dengan demikian diperlukan penyediaan buah apel dengan kualitas baik, agar bermanfaat bagi tubuh manusia. Untuk mengetahui mutu apel yang baik dan memenuhi standar diterima konsumen secara luas, dibutuhkan pengecekan mutu apel sendiri. Mutu apel salah satunya dapat diketahui dari permukaan kulit dari apel itu sendiri, dan mutu apel juga menentukan harga jual dari apel tentunya mutu baik memiliki harga tinggi disbanding dengan apel yang mutunya sedang memiliki harga sedang.[[1](https://univ45sby.ac.id/ejournal/index.php/industri/article/view/301)]  

Untuk melakukan sortir buah apel dapat dilakukan secara tradisional atau dengan bantuan Artificial Intelligence (AI) atau kecerdasan buatan salah satu adalah machine learning. Dalam model Machine Learning banyak terdapat algoridma yang bisa di pilih. Salah satu algoritma yang paling umum digunakan adalah klasifikasi. Dengan menggunakan klasifikasi dan memasukkan faktor-faktor dari apel yang  diharapkan dapat mengklasifikasikan kualitas apel.[[2](https://hostjournals.com/bulletincsr/article/view/251)]

## Business Understanding
Pengembangan model klasifikasi kualitas apel memiliki potensi untuk memberikan manfaat bagi berbagai pihak, termasuk petani, distributor, dan konsumen. Model ini dapat membantu meningkatkan kualitas panen apel, meningkatkan nilai jual apel, dan meningkatkan kepercayaan konsumen.
### Problem Statements

Berdasarkan latar belakang di atas, berikut ini merupakan rincian masalah yang dapat diselesaikan pada proyek ini:
-  Bagaimana membuat model machine learning yang dapat memprediksi kualitas apel berdasarkan data visual dan sensorik?
-  Model yang seperti apa yang memiliki akurasi paling baik?
-  Bagaimana model ini dapat membantu petani dan distributor dalam meningkatkan kualitas dan nilai jual apel?

### Goals
Tujuan dari proyek ini adalah:
- Membuat model machine learning yang dapat memprediksi kualitas apel berdasarkan data visual dan sensorik.
- Membandingkan beberapa algoritma model untuk menemukan akurasi terbaik dalam memprediksi kualitas apel.
-  Mengembangkan aplikasi yang mudah digunakan untuk membantu petani dan distributor dalam menggunakan model machine learning untuk memprediksi kualitas apel.

### Solution Statements
-  Menganalisis data dengan melakukan univariate analysis dan multivariate analysis. Memahami data juga dapat dilakukan dengan visualisasi. Memahami data dapat membantu untuk mengetahui kolerasi matrix antar fitur dan mendeteksi outlier.
- Melakukan proses data cleaning dan normalisai data agar mendapat prediksi yang baik.
- Membuat beberapa variasi model untuk mendapatkan model yang paling baik dari beberapa model yang telah dibuat untuk prediksi kualitas apel. Diantaranya adalah menggunakan:
    * K-Nearest Neighbor (KNN) adalah algoritma sederhana yang mengklasifikasikan data atau kasus baru berdasarkan ukuran kesamaan. Hal ini sebagian besar digunakan untuk mengklasifikasikan titik data berdasarkan tetangga terdekatnya sebagai acuan.[[3](https://towardsdatascience.com/a-simple-introduction-to-k-nearest-neighbors-algorithm-b3519ed98e)]
    * Random Forest adalah algoritma machine learning yang kuat yang dapat digunakan untuk berbagai tugas termasuk regresi dan klasifikasi. Ini adalah metode ensemble, yang berarti bahwa model random forest terdiri dari banyak decision tree kecil, yang disebut estimator, yang masing-masing menghasilkan prediksi mereka sendiri. Random forest menggabungkan prediksi estimator untuk menghasilkan prediksi yang lebih akurat .[[4](https://deepai.org/machine-learning-glossary-and-terms/random-forest)]
    * Support Vector Machine (SVM) adalah algoritma yang digunakan untuk menemukan hyperplane dalam ruang N-dimensi (N - jumlah fitur) yang secara jelas mengklasifikasikan titik data. SVM dapat digunakan untuk menyelesaikan permasalahan klasifikasi, regresi, dan pendeteksian outlier.[[5](https://towardsdatascience.com/support-vector-machine-introduction-to-machine-learning-algorithms-934a444fca47)]
    * Naive Bayes adalah model machine learning probabilistik yang digunakan untuk tugas klasifikasi. Inti dari classifier ini didasarkan pada teorema Bayes.[[6](https://towardsdatascience.com/naive-bayes-classifier-81d512f50a7c)]
    * Extra trees classifier adalah sejumlah besar pohon keputusan yang belum dipangkas dari kumpulan data pelatihan. Prediksi dibuat dengan merata-ratakan prediksi pohon keputusan dalam kasus regresi atau menggunakan suara terbanyak dalam kasus klasifikasi.[[7](https://machinelearningmastery.com/extra-trees-ensemble-with-python/)]

## Data Understanding

**Informasi Datasets**


| Jenis | Keterangan |
| ------ | ------ |
| Title | Apple Quality |
| Source | [Kaggle](https://www.kaggle.com/datasets/nelgiriyewithana/apple-quality/data) |
| Maintainer | [Nidula Elgiriyewithana ⚡](https://www.kaggle.com/nelgiriyewithana) |
| License | Other (specified in description) |
| Visibility | Publik |
| Tags | Computer Science, Education, Food, Data Visualization, Classification, Exploratory Data Analysis |
| Usability | 10.00 |

Berikut informasi pada dataset: 
- Dataset berupa CSV (Comma-Seperated Values).
- Dataset memiliki 4001 sample dengan 9 fitur.
- Dataset memiliki 7 fitur bertipe float64 dan 2 fitur bertipe object.
- Terdapat 1 missing value dalam dataset.
### Variable - variable pada dataset
- `A_id` : Identifikasi unik untuk setiap buah.
- `Size` : Ukuran buah.
- `Weight` : Berat buah.
- `Sweetness` : Tingkat kemanisan buah.
- `Crunchiness` : Tekstur yang menunjukkan kerenyahan buah.
- `Juiciness` : Tingkat kesegaran buah.
- `Ripeness` : Tahap kematangan buah.
- `Acidity` : Tingkat keasaman buah.
- `Quality` : Kualitas buah secara keseluruhan, baik atau buruk.

Dari ke 9 fitur dapat dilihat bahwa fitur `A_id` tidak mempengaruhi kualitas buah hingga akan di hapus.

### EDA - Univariate Analysis
![Univariate Analysis](https://drive.google.com/uc?export=view&id=19sUPSmeVRmNfiwUuDAFK_Ixp9-f6-SjV)
Dari hasil visualisasi di atas dapat disimpulkan bahwa:
 - Sebagian besar ukuran buah dalam rentan -1.73 sampai 0.37.
 - mean dari berat buah memiliki nilai -0.99.

### EDA - Multivariate Analysis
![Multivariate Analysis](https://drive.google.com/uc?export=view&id=1-CdOamS033K_xIIN2zQoJUtox5hHCKd5)
Dari hasil visualisasi di atas dapat disimpulkan bahwa:
- Dilihat pada semua fitur cenderung bervariasi.

**Matriks Korelasi untuk Fitur Numerik**
![Matriks Korelasi](https://drive.google.com/uc?export=view&id=1dDoFlgAViz56cIw7Yx7kmMKDZSpNBV2a)
Correlation Matrix menunjukkan hubungan antar fitur dalam nilai korelasi. Ukuran buah dan tingkat keasaman buat memiliki nilai korelasi positif yang tinggi yaitu `0.18`.

## Data Preparation
Teknik yang digunakan dalam penyiapan data (Data Preparation) yaitu: 
- Penanganan Missing Values. Pada kasus dataset ini ada 1 kolom dengan missing values yang di hapus.
- Mendeteksi outliers. Outliers adalah titik data yang berbeda secara signifikan dari pengamatan lainnya sehingga dapat berakibat buruk pada model prediksi. Pada proyek ini menggunakan IQR (InterQuartile Range) untuk mendeteksi outliers. IQR dapat menentukan data outliers yang kondisinya di luar batas bawah atau batas atas dari dataset . IQR dapat divisualkan menggunakan boxplot.
- Train test split. Train test split adalah proses membagi data menjadi data latih dan data uji. Data latih akan digunakan untuk membangun model, sedangkan data uji akan digunakan untuk menguji performa model. Pada proyek ini dataset dibagi menjadi dua yaitu: 
    * Total data Latih: 3032
    * Total data Uji: 758
- Normalisasi. Pada proyek ini menggunakan MinMaxScaler, yaitu teknik normalisasi yang mentransformasikan nilai fitur atau variabel ke dalam rentang [0,1] yang berarti bahwa nilai minimum dan maksimum dari fitur/variabel masing-masing adalah 0 dan 1.

## Modeling
Algoritma Penelitian ini melakukan pemodelan dengan 5 algoritma, yaitu:
- K-Nearest Neighbour. K-Nearest Neighbour bekerja dengan membandingkan jarak satu sampel ke sampel pelatihan lain dengan memilih sejumlah k tetangga terdekat. Proyek ini menggunakan sklearn.neighbors.KNeighborsRegressor dengan memasukkan X_train dan y_train dalam membangun model. Parameter yang digunakan pada proyek ini adalah :
```
     n_neighbors = Jumlah k tetangga tedekat
```
- Random Forest Algoritma. Random forest adalah teknik dalam machine learning dengan metode ensemble. Teknik ini beroperasi dengan membangun banyak decision tree pada waktu pelatihan. Proyek ini menggunakan sklearn.ensemble.RandomForestRegressor dengan memasukkan X_train dan y_train dalam membangun model.
- Support Vector Machine (SVM) adalah algoritma yang digunakan untuk menemukan hyperplane dalam ruang N-dimensi (N - jumlah fitur) yang secara jelas mengklasifikasikan titik data.
- Naïve Bayes Classifier merupakan sebuah metoda klasifikasi yang berakar pada teorema Bayes. Metode pengklasifikasian dengan menggunakan metode probabilitas dan statistik yang memprediksi peluang di masa depan berdasarkan pengalaman di masa sebelumnya sehingga dikenal sebagai Teorema Bayes .
- Extra trees classifier adalah sejumlah besar pohon keputusan yang belum dipangkas dari kumpulan data pelatihan. Prediksi dibuat dengan merata-ratakan prediksi pohon keputusan dalam kasus regresi atau menggunakan suara terbanyak dalam kasus klasifikasi. Parameter yang digunakan pada proyek ini adalah :
```
     random_state=100
```
## Evaluation
Dalam tahap evaluasi, metrik yang digunakan adalah `accuracy`
Accuracy didapatkan dengan menghitung persentase dari jumlah prediksi yang benar dibagi dengan jumlah seluruh prediksi. Formula:
```math

    \text{Accuracy} = \frac{\text{TP + TN}}{\text{TN + TP + FN + FP}} \times 100\%
    
```
Memiliki kelebihan yaitu mudah dimengerti dan cocok untuk klasifikasi biner, tetapi tidak efektif untuk klasifikasi kengan kelas yang timpang atau imbalance.

**Tabel berikut merupakan perbandingan 5 buah model yang coba dibandingkan:**

| Model | Accuracy |
| ------ | ------ |
| KNN | 0.90 |
| RandomForest  | 0.89 |
| SVM | 0.89 |
| Naive Bayes | 0.49 |
| Extra Trees Classifier | 0.90 |



**Plot Accuracy**
![Plot Accuracy](https://drive.google.com/uc?export=view&id=1nmlb5VLsMwQH3z68wSUKnKmR0hDZqJUB)
Dari hasil tersebut dapat diketahui bahwa model dengan algoritma KNN memiliki kinerja yang lebih baik. Untuk itu model tersebut yang akan dipilih untuk digunakan.

## Referensi
1. Ahmad Ridho’i, Kukuh Setyadjit, Balok Hariadi.(2022).MENENTUKAN KUALITAS BUAH APEL MALANG BERDASARKAN KULITNYA MEMANFAATKAN PENGOLAHAN CITRA DIGITAL. Vol 25 No 2 (2022): September : Jurnal Teknik Industri.https://univ45sby.ac.id/ejournal/index.php/industri/article/view/301
2. M Afriansyah, Joni Saputra,dkk.(2023).Optimasi Algoritma Naive Bayes Untuk Klasifikasi Buah Apel Berdasarkan Fitur Warna RGB.VOL. 3 NO. 3 (2023): APRIL : BULLETIN OF COMPUTER SCIENCE RESEARCH.https://hostjournals.com/bulletincsr/article/view/251
3. Subramanian, D. (2019). A Simple Introduction to K-Nearest Neighbors Algorithm. Towards Data Science. https://towardsdatascience.com/a-simple-introduction-to-k-nearest-neighbors-algorithm-b3519ed98e
4. Wood, T. -.What is a Random Forest?. DeepAI. https://deepai.org/machine-learning-glossary-and-terms/random-forest
5. Gandhi, R. (2018). Support Vector Machine — Introduction to Machine Learning Algorithms: SVM model from scratch. Towards Data Science. https://towardsdatascience.com/support-vector-machine-introduction-to-machine-learning-algorithms-934a444fca47
6. Gandhi, R. (2018). Naive Bayes Classifier. Towards Data Science. https://towardsdatascience.com/naive-bayes-classifier-81d512f50a7c
7. Jason Brownlee. (2021). How to Develop an Extra Trees Ensemble with Python. https://machinelearningmastery.com/extra-trees-ensemble-with-python/

_