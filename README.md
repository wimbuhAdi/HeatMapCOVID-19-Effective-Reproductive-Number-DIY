# HeatMapCOVID-19-Effective-Reproductive-Number-DIY
Terimakasih kepada Bu Unan atas rekomendasi [paper ini](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3551767). Projek ini adalah respond saya atas minimnya informasi fundamental yang tersedia dan guna untuk memperkaya instrumen yang dapat digunakan sebagai pertimbangan atas transmisi wabahvirus nCOVID19. Goal dari proyek ini adalah penyajian visualisasi nilai Effective Reproductive Number (R) di pulau Jawa menggunakan metode perhitungan nilai R yang dipublikasikan dalam papers [High Temperature and High Humidity Reduce the Transmission of COVID-19](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3551767) yang diterbitkan oleh Social Science Research Network dengan parameter suhu dan kelembaban yang datanya diambil dari API Pengamatan Cuaca. Harap priksa kembali validasi dari data yang didapatkan, karena proyek ini masih pada tahap pengembangan.

## Visualisasi Data
### V2 Visualiassi Pulau jawa
Menggunakan 768 data point yang didapatkan dengan memanggil [API openWeaterMap](https://openweathermap.org/current) dan menampilkan nilai R yang telah dikalkulasi ke dalam heatmap
<img src= https://github.com/wimbuhAdi/HeatMapCOVID-19-Effective-Reproductive-Number-DIY/blob/master/Node-red%20HeatMap%20Visualizer/heatMapJawa.jpg>

### V1 visualisasi Ringroas
<img src= https://github.com/wimbuhAdi/HeatMapCOVID-19-Effective-Reproductive-Number-DIY/blob/master/Node-red%20HeatMap%20Visualizer/ringRoadheatMap.jpg width="320">   <img src= https://github.com/wimbuhAdi/HeatMapCOVID-19-Effective-Reproductive-Number-DIY/blob/master/Node-red%20HeatMap%20Visualizer/With%20Background%20Ring%20Road%20heatMap.jpg width="320">

### Flow realtime Node-red
<img src=https://github.com/wimbuhAdi/HeatMapCOVID-19-Effective-Reproductive-Number-DIY/blob/master/Node-red%20HeatMap%20Visualizer/flow_heatmap.jpg width="720">

### Data Ingest
```
pip install requests
```
<img src=https://github.com/wimbuhAdi/HeatMapCOVID-19-Effective-Reproductive-Number-DIY/blob/master/Node-red%20HeatMap%20Visualizer/dataPULL.jpg width="320">
