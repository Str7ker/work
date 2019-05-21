<template>
<!--  <div id="app">-->
<!--    <v-app id="inspire">-->
<!--      <v-container>-->
<!--      <v-carousel hide-delimiters>-->
<!--        <v-carousel-item-->
<!--          v-for="(item,i) in items"-->
<!--          :key="i"-->
<!--          :src="item.src"-->
<!--        ></v-carousel-item>-->
<!--      </v-carousel>-->
<!--      </v-container>-->
<!--    </v-app>-->

  <v-container fluid>

<!--    Шапка-->

    <nav>
      <v-toolbar flat app >
        <v-toolbar-side-icon class="grey--text" @click="drawer = !drawer"></v-toolbar-side-icon>
        <v-toolbar-title class="text-uppercase grey--text">
          <span class="font-weight-light">Ресурс</span>
          <span>Логистика</span>
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-menu offset-y>
          <v-btn flat slot="activator" color="grey">
            <v-icon left>expand_more</v-icon>
            <span>Меню</span>
          </v-btn>
          <v-list>
            <v-list-tile v-for="link in links" :key="link.text" router :to="link.route">
              <v-list-tile-title>{{link.text}}</v-list-tile-title>
            </v-list-tile>
          </v-list>
        </v-menu>
        <span color="grey"><Submit /></span>
        <v-btn flat color="grey">
        <v-icon left>input</v-icon>
        <span>Войти</span>
        </v-btn>
      </v-toolbar>

<!--      Боковая навигация-->
      <v-navigation-drawer app v-model="drawer"  class="indigo darken-1">
        <v-layout column align-center>
          <f-flex class="mt-5 ml-3 justify-center">
            <v-avatar size="100" class="">
              <img src="/g.png" alt="">
            </v-avatar>
            <p class="white--text title mt-1">
              Добро пожаловать, {{name}} !
            </p>
<!--            <v-btn flat class="white&#45;&#45;text">-->
<!--              <v-icon left>check_circle_outline</v-icon>-->
<!--              <span>Оставить заявку</span>-->
<!--            </v-btn>-->
            <v-btn flat class="white--text">
              <v-icon left>input</v-icon>
              <span>Войти</span>
            </v-btn>
            <v-spacer></v-spacer>
            <Submit />
          </f-flex>
        </v-layout>
        <v-list>
          <v-list-tile active-class="orange lighten-1" v-for="link in links" :key="link.text" router :to="link.route">
            <v-list-tile-action>
              <v-icon  class="white--text"> {{link.icon}} </v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title class="white--text" > {{link.text}} </v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
      </v-navigation-drawer>

    </nav>
  </v-container>
</template>


<script>
import Main from './Main'
// import Cargadd from './Cargaad'
// export default {
//   name: 'App',
//   components: {
//     Main
//   },
//   data () {
//     return {
//       //
//     }
//   }
// }
  import Submit from './Submit'
export default {
  components: { Submit },
  data () {
    return {
      drawer: false,
      name: 'Гость',
      items: [
        { image: '/dostavka.png', id: '1', titlename: 'Быстрая доставка', text: 'Наши грузочные машины доставят ваши вещи куда угодно!' },
        { image: '/high.jpg', id: '2', titlename: 'Доставляем крупный груз', text: 'Доставим любой груз до 20000 кг!' },
        { image: '/hr.jpg', id: '3', titlename: 'Доставляем хрупкий груз', text: 'Можете не беспокоиться за свои хрупкие вещи!' },
        { image: '/sklad.jpg', id: '4', titlename: 'Ответственное хранение', text: 'В наших складах найдется место для ваших вещей!' }
      ],
      uslugi: [
        { name: 'Услуги экспедитора', text: 'Мы осуществляем перевозки собственным парком и транспортом наших партнёров.', avatar: '/1.jpg' },
        { name: 'Транспортные услуги', text: 'Мы осуществляем перевозки по всей территории РФ.', avatar: '/2.jpg' },
        { name: 'Хранение груза', text: 'Мы готовы разместить вашу продукцию на хранение.', avatar: '/3.jpg' }
      ],
      icons: [
        'fab fa-vk',
        'fab fa-instagram'
      ]
    }
  }

}
</script>

<style scoped>
  /*.cs {*/
  /*  text-align: center;*/
  /*  color: white;*/
  /*  background-color: rgba(0,0,0,0.5) !important;*/
  /*}*/
  /*.titlename {*/
  /*  padding-top: 15%;*/
  /*}*/
  /*.text {*/
  /*  padding-bottom: 30px;*/
  /*}*/
  /*.us {*/
  /*  background-color: red;*/
  /*}*/
  .logo {
    margin: 0 50px;
  }
</style>
