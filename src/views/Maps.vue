<template>
  <div>
    <div class="mapouter">
      <div class="gmap_canvas">
        <iframe src="https://yandex.ru/map-widget/v1/?um=constructor%3A06ff42df4b9d7a561d5d434cc1b55f5519573aeaa2fd4217b81c5b6f595f87f8&amp;source=constructor" width="100%" height="720" frameborder="0"></iframe>
      </div>
    </div>
  </div>
</template>

<style>
.mapouter {
  text-align:right;
  height:100%;
  width:100%;
  position: absolute;
}
.gmap_canvas {
  overflow:hidden;
  background:none!important;
  height:100%;
  width:100%;
}
</style>
