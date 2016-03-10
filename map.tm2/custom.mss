#building[zoom>=14] {
  polygon-fill: #eee;
  line-width: 0.5;
  line-color: #ddd;
}

#building[zoom>=16] {
  building-fill: #eee;
  building-fill-opacity: 0.9;
  building-height: 4;
}

#landuse[class='park'] {
  polygon-fill: #dec;
}

#poi_label[maki='park'][scalerank<=3][zoom>=15] {
  text-name: @name;
  text-face-name: @sans;
  text-size: 10;
  text-wrap-width: 60;
  text-fill: #686;
  text-halo-fill: #fff;
  text-halo-radius: 1;
  text-halo-rasterizer: fast;
}

#road_label[zoom>=13] {
  text-name: @name;
  text-face-name: @sans;
  text-size: 10;
  text-placement: line;
  text-avoid-edges: true;
  text-fill: #68a;
  text-halo-fill: #fff;
  text-halo-radius: 1;
  text-halo-rasterizer: fast;
}