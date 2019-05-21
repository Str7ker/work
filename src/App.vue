<template>
    <v-app>
        <!--    <v-toolbar app light>-->
        <!--      <v-toolbar-title class="headline text-uppercase">-->
        <!--        <span>Vuetify</span>-->
        <!--        <span class="font-weight-light">MATERIAL DESIGN</span>-->
        <!--      </v-toolbar-title>-->
        <!--      <v-spacer></v-spacer>-->
        <!--      <v-btn-->
        <!--        flat-->
        <!--        href="https://github.com/vuetifyjs/vuetify/releases/latest"-->
        <!--        target="_blank"-->
        <!--      >-->
        <!--        <span class="mr-2">Latest Release</span>-->
        <!--      </v-btn>-->
        <!--    </v-toolbar>-->

<!--      Форма входа-->

        <v-content v-if="a" fluid>
          <v-flex >
            <v-card class="elevation-12">
              <v-toolbar dark color="primary">
                <v-toolbar-title>Форма входа</v-toolbar-title>
                <v-spacer></v-spacer>
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field prepend-icon="person" name="login" label="Логин" type="text"></v-text-field>
                  <v-text-field prepend-icon="lock" name="password" label="Пароль" id="password" type="password"></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary">Вход</v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-content>
      <!--    Вид пользователя-->
        <v-content v-else class="mx-4 mt-3" grid-list-md text-xs-center fluid>
            <!--      <Home/>-->
            <router-view></router-view>
<!--            <Main/>-->
                <Page/>
        </v-content>
    </v-app>
</template>

<script>
// import HelloWorld from './components/HelloWorld'
import Main from './views/Main'
import 'bootstrap-css-only/css/bootstrap.min.css'
import 'mdbvue/build/css/mdb.css'
import Page from './views/Page'
export default {
  name: 'App',
  components: {
    Page,
    Main
  },
  data () {
    return {
      a: false,
      //
    }
  }
}
</script>
