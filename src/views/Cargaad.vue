<template>
    <v-dialog v-model="dialog" max-width="600px" >
      <v-btn flat slot="activator" class="success">Добавить новый груз</v-btn>
      <v-card >
        <v-card-title>
          <h2>Добавить новый груз</h2>
          <v-spacer></v-spacer>
          <v-btn flat color="primary" @click="dialog=false">Закрыть</v-btn>
        </v-card-title>
        <v-card-text>
          <v-form class="px-3" ref="form">
            <v-text-field label="Название груза" v-model="title" prepend-icon="weekend" :rules="inputRules"></v-text-field>
            <v-text-field label="Вес" v-model="at" prepend-icon="airport_shuttle"></v-text-field>
            <v-text-field label="Объем" v-model="volume" prepend-icon="work_outline"></v-text-field>
<!--            <v-text-field label="Дата" v-model="data" prepend-icon="today"></v-text-field>-->
<!--            <v-text-field label="Статус" v-model="status" prepend-icon="update"></v-text-field>-->
            <v-menu>
              <v-text-field :value="data" slot="activator" label="Дата" prepend-icon="today"></v-text-field>
              <v-date-picker v-model="data"></v-date-picker>
            </v-menu>

            <v-spacer></v-spacer>
            <v-btn flat class="success mx-0 mt-3" @click="submit">Добавить груз</v-btn>

          </v-form>
        </v-card-text>
      </v-card>
    </v-dialog>
</template>

<script>
  export default {
    data(){
      return {
        title: '',
        at: '',
        volume: '',
        data: null,
        dialog: false,
        inputRules: [
          v => v.length >=3 || 'Минимум 3 символа!'

        ],
        // status: ''
      }
    },
    methods: {
      submit() {
        if(this.$refs.form.validate()) {
          console.log(this.title, this.at, this.volume)
        }
      }
    },
    name: 'cargaad'
  }
</script>

<style scoped>

</style>
