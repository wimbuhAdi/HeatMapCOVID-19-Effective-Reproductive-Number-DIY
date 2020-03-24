# HeatMapCOVID-19-Effective-Reproductive-Number-DIY
Terimakasih kepada Bu Unan atas rekomendasi [paper ini](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3551767). Projek ini adalah respond saya atas minimnya informasi fundamental dan instrumen yang dapat digunakan sebagai monitor atas wabah nCOVID19 yang tersedia. Inti dari proyek ini adalah menyajikan visualisasi data Effective Reproductive Number di beberapa area di pulau jawa metode perhitungan yang dipublikasikan dalam papers [High Temperature and High Humidity Reduce the Transmission of COVID-19](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3551767) yang diterbitkan oleh Social Science Research Network dengan parameter suhu dan kelembaban yang datanya  diambil dari API Pengamatan Cuaca

## Visualisasi Data
### V2 Visualiassi Pulau jawa
768 data point dipanggil dan ditampilkan dalam heatmap
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
