##### Penggunaan ulang harus dengan izin dan refrensi ke Pemilik Code

# HeatMap Effective Reproductive Number COVID-19
Terimakasih kepada Bu Unan atas rekomendasi [paper ini](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3551767). Projek ini adalah respond saya atas minimnya informasi fundamental yang tersedia dan guna untuk memperkaya instrumen yang dapat digunakan sebagai pertimbangan atas transmisi wabah virus COVID19. Goal dari proyek ini adalah penyajian visualisasi nilai Effective Reproductive Number (R) di pulau Jawa menggunakan metode perhitungan nilai R yang dipublikasikan dalam papers [High Temperature and High Humidity Reduce the Transmission of COVID-19](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3551767) yang diterbitkan oleh Social Science Research Network dengan parameter suhu dan kelembaban yang datanya diambil dari API Pengamatan Cuaca. Harap priksa kembali validasi dari data yang didapatkan, karena proyek ini masih pada tahap pengembangan.



## Visualisasi Data
### Versi 2 Visualisasi R number Pulau jawa
Menggunakan 768 data point yang didapatkan dengan memanggil [API openWeaterMap](https://openweathermap.org/current) dan menampilkan nilai R yang telah dikalkulasi ke dalam heatmap

<p align="center">
  <img src="https://github.com/wimbuhAdi/HeatMapCOVID-19-Effective-Reproductive-Number-DIY/blob/master/Node-red%20HeatMap%20Visualizer/heatMapJawa.jpg" alt="Size Limit CLI" width="750">
</p>

### Live tweet Kalkulasi R number
Menggunakan python script untuk request weather data dan kalkulasi R-number, kemudian menggunakan library [tweepy](https://www.tweepy.org/) untuk handling [tweeter API](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update)
<p align="center">
  <img src="https://github.com/wimbuhAdi/HeatMapCOVID-19-Effective-Reproductive-Number-DIY/blob/master/TweetBot_R-Covid/Tweet.PNG" alt="Size Limit CLI" width="550">
</p>

### Versi 1 visualisasi R number Ringroad
<p align="center">
  <img src="https://github.com/wimbuhAdi/HeatMapCOVID-19-Effective-Reproductive-Number-DIY/blob/master/Node-red%20HeatMap%20Visualizer/ringRoadheatMap.jpg" alt="Size Limit CLI" width="400">
  <img src="https://github.com/wimbuhAdi/HeatMapCOVID-19-Effective-Reproductive-Number-DIY/blob/master/Node-red%20HeatMap%20Visualizer/With%20Background%20Ring%20Road%20heatMap.jpg" alt="Size Limit CLI" width="390">
</p>

### Flow realtime Node-red
<p align="center">
  <img src="https://github.com/wimbuhAdi/HeatMapCOVID-19-Effective-Reproductive-Number-DIY/blob/master/Node-red%20HeatMap%20Visualizer/flow_heatmap.jpg" alt="Size Limit CLI" width="750">
</p>


## Setup dan Dependensi
### Setup
* Install Node-red : ikuti langkah-langkah di [laman resmi Node-Red](https://nodered.org/docs/getting-started/windows)
  * install [node UI HeatMap](https://flows.nodered.org/node/node-red-contrib-ui-heatmap)
  * import flow dari salah satu [file json](https://github.com/wimbuhAdi/HeatMapCOVID-19-Effective-Reproductive-Number-DIY/tree/master/Node-red%20HeatMap%20Visualizer) dengan copas
* Data Ingest dan Interkoneksi Program : insatll linrary request di python (diuji di python 3) untuk get http API
```
pip install requests
```
  * lalu daftar [akun OpenWeaterAPI](https://openweathermap.org/) untuk mendapat token guna mengakses data cuaca
* install Paho MQTT library :
Ikuti langkah instalasi [ini](https://mosquitto.org/blog/2013/12/paho-mqtt-python-client/)
* Dapat digunakan cloud broker atau [local broker](http://www.steves-internet-guide.com/install-mosquitto-broker/)
### Dependnsi
* Local directori berisi file PNG untuk penyimpanan gambar peta background di node-red, di spesify di node **file in**. 
<img src=https://github.com/wimbuhAdi/HeatMapCOVID-19-Effective-Reproductive-Number-DIY/blob/master/Node-red%20HeatMap%20Visualizer/dataPULL.jpg width="320">
* Library [Tweepy](https://zoomadmin.com/HowToInstall/UbuntuPackage/python-tweepy)
