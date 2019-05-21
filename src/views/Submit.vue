<template>
  <v-dialog v-model="dialog" max-width="600px" >
    <v-btn flat slot="activator" class="white--text">
      <v-icon left>check_circle_outline</v-icon>
      Оставить заявку
    </v-btn>
    <v-card >
      <v-card-title>
        <h2>Добавление заявки</h2>
        <v-spacer></v-spacer>
        <v-btn flat color="primary" @click="dialog=false">Закрыть</v-btn>
      </v-card-title>
      <v-card-text>
        <v-form class="px-3" ref="form">
          <v-text-field label="Как Вас зовут (ФИО)?" :counter="30" v-model="name" prepend-icon="people" :rules="inputRules"></v-text-field>
          <v-select :items="items" label="Что хотите перевезти? (Подробнее в описании!)" v-model="cargo" prepend-icon="airport_shuttle"></v-select>
          <v-select :items="cities" label="Адрес отправления (Подробнее в описании!)" v-model="adress1" prepend-icon="not_listed_location"></v-select>
          <v-select :items="cities" label="Адрес доставления (Подробнее в описании!)" v-model="adress2" prepend-icon="place"></v-select>
          <v-text-field label="Оставьте Вашу электронную почту" v-model="phone" :rules="emailRules" prepend-icon="alternate_email"></v-text-field>
          <v-text-field label="Оставьте Ваш номер телефона" :counter="15" :rules="phoneRules" v-model="email" prepend-icon="phone"></v-text-field>
          <v-textarea label="Подробное описание" :rules="textRules" v-model="text" prepend-icon="textsms"></v-textarea>
          <!--            <v-text-field label="Дата" v-model="data" prepend-icon="today"></v-text-field>-->
          <!--            <v-text-field label="Статус" v-model="status" prepend-icon="update"></v-text-field>-->
          <v-menu>
            <v-text-field :value="data" slot="activator" label="Дата" prepend-icon="today"></v-text-field>
            <v-date-picker v-model="data"></v-date-picker>
          </v-menu>

          <v-spacer></v-spacer>
          <v-btn flat class="success mx-0 mt-3" @click="submit">Оставить заявку</v-btn>

        </v-form>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  data () {
    return {
      name: '',
      cargo: '',
      adress1: '',
      adress2: '',
      phone: '',
      email: '',
      text: '',
      data: null,
      dialog: false,
      inputRules: [
        v => v.length >= 15 || 'Пожалуйста, напишите ваше ФИО'
      ],
      emailRules: [
        v => !!v || 'Введите электронную почту',
        v => /.+@.+/.test(v) || 'Электронная почта должна быть действительна'
      ],
      phoneRules: [
        v => v.length >= 6 || 'Телефон должен быть не меньше 6 символов'
      ],
      textRules: [
        v => v.length >= 10 || 'Текст должен содержать не меньше 10 символов'
      ],
      items: ['Техника', 'Мебель', 'Прочее'
      ],
      cities: ['Тольятти', 'Москва', 'Прочее'
      ],
      // status: ''
    }
  },
  methods: {
    submit () {
      if (this.$refs.form.validate()) {
        console.log(this.name, this.cargo, this.adress1)
      }
    }
  },
  name: 'submit'
}
</script>ы

<style scoped>

</style>
