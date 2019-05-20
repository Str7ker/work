<template>
  <div class="about">
    <h1 class="subheading grey--text">Грузы</h1>
    <v-container class="my-5">
    <v-card flat v-for="cargo in cargoes" :key="cargo.name">
      <v-layout row wrap class="orange darken-1" >
        <v-flex xs12 md6 class="mx-1">
          <div class="caption white--text">Название товара</div>
          <div>{{cargo.name}}</div>
        </v-flex>
        <v-flex xs4 sm4 md2>
          <div class="caption white--text mx-1">Вес</div>
          <div class="mx-1">{{cargo.at}}</div>
        </v-flex>
        <v-flex xs4 sm4 md2>
        <div class="caption white--text">Объем</div>
        <div>{{cargo.volume}}</div>
        </v-flex>
        <v-flex xs4 sm4 md2>
        <div class="caption white--text mx-1">Статус</div>
        <div class="mx-1">{{cargo.status}}</div>
        </v-flex>
      </v-layout>
    </v-card>
    </v-container>
  </div>
</template>

<script>
  export default {
    data() {
    return {
    cargoes: [
    { name: "Диван", at: "20 кг", volume: "2 метра", status:"В пути"},
    { name: "Шкаф", at: "30 кг", volume: "2 метра", status:"В пути"},
    { name: "Стол", at: "5 кг", volume: "2 метра", status:"Ожидает отправки"},
    { name: "Холодильник", at: "20 кг", volume: "2,5 метра", status: "Доставлено" },
    { name: "Плита", at: "20 кг", volume: "1 метр", status: "Доставлено" },
    ]
    }
    }
  }
</script>

<style scoped>
</style>
