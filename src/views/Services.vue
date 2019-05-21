<template>
  <div class="company">
    <h1 class="subheading grey--text">Контакты</h1>
    <v-container class="my-3" >
      <v-layout row wrap >
        <f-flex xs12 sm6 md4 lg3 v-for="person in contact" :key="person.first_name">
          <v-card flat class="text-xs-center ma-3 blue-grey lighten-5">
            <v-responsive class="pt-4">
              <v-avatar size="100" class="grey lighten-2">
                <img :src="person.avatar">
              </v-avatar>
            </v-responsive>
            <v-card-text>
              <div class="subheading font-weight-bold">{{ person.first_name }} {{ person.last_name }}</div>
              <div class="body-2">{{ person.phone }}</div>
              <div class="body-2">{{ person.email }}</div>
              <div class="body-2">{{ person.position }}</div>
            </v-card-text>
            <v-card-actions>
              <v-btn flat >
                <v-icon small left>message</v-icon>
                <span>Сообщение</span>
              </v-btn>
            </v-card-actions>
          </v-card>
        </f-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
export default {
  name: 'Services'
}
</script>

<style scoped>

</style>
