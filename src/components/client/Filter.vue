<template>
  <v-menu
          :close-on-content-click="false"
          bottom
          left
          min-width="300"
          max-width="300"
          nudge-left="12"
          offset-x
          transition="slide-y-transition"
  >
    <v-btn
            slot="activator"
            class="elevation-0"
            color="grey"
            dark
            fab
            fixed
            style="top: 96px;"
            top
    >
      <v-icon>mdi-settings</v-icon>
    </v-btn>
    <v-card>
      <v-container grid-list-xl>
        <v-layout wrap>
          <v-flex xs12>
            <div class="text-xs-center body-2 text-uppercase sidebar-filter">Фильтры боковой панели</div>

            <v-layout justify-center>
              <v-avatar
                      v-for="c in colors"
                      :key="c"
                      :class="[c === color ? 'color-active color-' + c: 'color-' + c]"
                      size="23"

                      @click="setColor(c)"
              />
            </v-layout>
            <v-divider class="mt-3"/>
          </v-flex>
          <v-flex
                  xs12
          >
            <div class="text-xs-center body-2 text-uppercase sidebar-filter">Выберите картинку</div>
          </v-flex>
          <v-flex
                  v-for="img in images"
                  :key="img"
                  xs3
          >
            <v-img
                    :class="[image === img ? 'image-active' : '']"
                    :src="img"
                    height="120"
                    @click.native="setImage(img)"
            />
          </v-flex>
        </v-layout>
      </v-container>
    </v-card>
  </v-menu>
</template>

<script>
  // Utilities
  import {
    mapMutations,
    mapState
  } from 'vuex'

  export default {
    data: () => ({
      colors: [
        'primary',
        'info',
        'success',
        'warning',
        'danger'
      ],
      images: [
        'https://images.wallpaperscraft.ru/image/pole_trava_rassvet_nebo_tuchi_86840_800x1420.jpg',
        'https://www.hdwallpapers.in/download/beautiful_sunset_5k-1080x1920.jpg',
        'https://img2.wbstatic.net/big/new/6890000/6890442-1.jpg',
        'https://actecon.files.wordpress.com/2014/02/bos026388.jpg'
      ]
    }),

    computed: {
      ...mapState('app', ['image', 'color']),
      color () {
        return this.$store.state.app.color
      }
    },

    methods: {
      ...mapMutations('app', ['setImage']),
      setColor (color) {
        this.$store.state.app.color = color
      }
    }
  }
</script>

<style lang="scss">
  .v-avatar,
  .v-responsive {
    cursor: pointer;
  }
</style>
