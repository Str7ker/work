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
        <v-btn flat color="grey">
          <v-icon left>check_circle_outline</v-icon>
          <span>Оставить заявку</span>
        </v-btn>
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
            <v-btn flat class="white--text">
              <v-icon left>check_circle_outline</v-icon>
              <span>Оставить заявку</span>
            </v-btn>
            <v-btn flat class="white--text">
              <v-icon left>input</v-icon>
              <span>Войти</span>
            </v-btn>
          </f-flex>
          <v-flex class="mt-2 mb-2">
            <Cargadd />
          </v-flex>
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

<!--    Карусель-->

    <v-container fluid >
      <v-layout row wrap>
          <v-flex >
            <v-parallax>
            <v-carousel hide-controls>
                <v-carousel-item
                  v-for="item in items"
                  :src="item.image"
                  :key="item.id">
                  <div class="cs">
                  <div class="titlename display-3" >{{item.titlename}} </div>
                  <div class="text display-1">{{item.text}} </div>
                  <v-btn class="btn headline py-1" color="warning">Подробнее</v-btn>
                  </div>
                </v-carousel-item>
              </v-carousel>
            </v-parallax>
          </v-flex>
      </v-layout>
    </v-container>

<!--Услуги-->

    <section>
      <v-layout
        column
        wrap
        class="my-5"
        align-center
      >
        <v-flex xs12 sm4 class="my-3">
          <div class="text-xs-center">
            <h2 class="headline">Наши услуги</h2>
          </div>
        </v-flex>
        <v-flex xs12>
          <v-container grid-list-md text-xs-center>
            <v-layout row wrap>
              <v-flex v-for="usluga in uslugi" :key="`4${usluga}`" xs12 md4>
                <v-card>
                  <v-card-text class="px-0" >
                    <v-card-text class="px-0">
                      <v-avatar size="100" class="logo">
                        <img :src="usluga.avatar">
                      </v-avatar>
                    </v-card-text>
                    <v-card-title primary-title class="layout justify-center px-0">
                      <div class="headline text-xs-center">{{usluga.name}}</div>
                    </v-card-title>
                    <v-card-text>
                      {{usluga.text}} <br>
                      <a href="" class="body-1"> Подробнее: </a>
                    </v-card-text>
                  </v-card-text>
                </v-card>
              </v-flex>
            </v-layout>
          </v-container>
        </v-flex>
      </v-layout>
    </section>

<!--    Карта-->

    <v-container fluid>
      <iframe src="https://yandex.ru/map-widget/v1/?um=constructor%3A385a02d2667b03f0c453ef757171093c0c1ba8bf72c596d0fabebf513eb2cc5f&amp;source=constructor" width="100%" height="576" frameborder="0"></iframe>
    </v-container>

<!--    Партнеры-->

    <v-container fluid >

    </v-container>

<!--    Футер-->

    <v-container fluid>
      <v-footer
        dark
        height="auto"
      >
        <v-card
          class="flex"
          flat
          tile
        >
          <v-card-title class="teal">
            <strong class="subheading">ООО "Ресурс-Логистика"</strong>

            <v-spacer></v-spacer>
            <v-btn flat color="white">
              <v-icon left>check_circle_outline</v-icon>
              <span>Оставить заявку</span>
            </v-btn>
            <v-btn flat color="white">
              <v-icon left>input</v-icon>
              <span>Войти</span>
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn
              v-for="icon in icons"
              :key="icon"
              class="mx-3"
              dark
              icon
            >
              <v-icon size="24px">{{icon}}</v-icon>
            </v-btn>
          </v-card-title>
        </v-card>
      </v-footer>
    </v-container>
  </v-container>
</template>

<script>
import Main from './Main'
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
export default {
  el: '#app',
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
  .cs {
    text-align: center;
    color: white;
    background-color: rgba(0,0,0,0.5) !important;
  }
  .titlename {
    padding-top: 15%;
  }
  .text {
    padding-bottom: 30px;
  }
  .us {
    background-color: red;
  }
  .logo {
    margin: 0 50px;
  }
</style>
