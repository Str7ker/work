<template>
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
                <span>Выйти</span>
                <v-icon right>exit_to_app</v-icon>
            </v-btn>
        </v-toolbar>

        <v-navigation-drawer app v-model="drawer"  class="indigo darken-1">
            <!--            <p class="deep-orange  white&#45;&#45;text title"  >Добро пожаловать, имя!</p>-->
          <v-layout column align-center>
            <f-flex class="mt-5" >
              <v-avatar size="100" class="logo">
                <img src="/1.png" alt="">
              </v-avatar>
              <p class="white--text title mt-1">
              Добро пожаловать, {{name}} !
              </p>
            </f-flex>
            <v-flex class="mt-2 mb-2">
              <Cargadd />
            </v-flex>
          </v-layout>
                <v-list>
<!--                    <v-list-tile-title class="title logo">-->
<!--                        Добро пожаловать, {{name}}!-->
<!--                    </v-list-tile-title>-->
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
</template>

<script>
  import Cargadd from './Cargaad'
export default {
    components: {Cargadd},
  data () {
    return {
      drawer: false,
      links: [
        { icon: 'departure_board', text: 'Грузы', route: '/cargos' },
        // { icon: 'home', text: 'О компании', route: '/company' },
        { icon: 'call', text: 'Контакты', route: '/about' }
      ],
      name: 'Ваня'
    }
  }
}
</script>

<style scoped>
    .logo {
      margin: 0 50px;
    }
</style>
