<template>
  <v-container
    fill-height
    fluid
    grid-list-xl>
    <v-layout
      justify-center
      wrap
    >
      <v-flex
        xs12
        md8
      >
        <material-card
          color="green"
          title="Редактирование профиля"
          text="Заполните свой профиль"
        >
          <v-form>
            <v-container py-0>
              <v-layout wrap>
<!--                <v-flex-->
<!--                  xs12-->
<!--                  md4-->
<!--                >-->
<!--                  <v-text-field-->
<!--                    label="Company (disabled)"-->
<!--                    disabled/>-->
<!--                </v-flex>-->
                <v-flex
                  xs12
                  md6
                >
                  <v-text-field
                    class="purple-input"
                    label="Ваш никнейм"
                    :rules="inputRules"
                    :counter="15"
                  />
                </v-flex>
                <v-flex
                  xs12
                  md6
                >
                  <v-text-field class="purple-input" label="Оставьте Вашу электронную почту" v-model="phone" :rules="emailRules"></v-text-field>
                </v-flex>
                <v-flex
                  xs12
                  md6
                >
                  <v-text-field
                    label="Имя"
                    :rules="nameRules"
                    :counter="10"
                    class="purple-input"/>
                </v-flex>
                <v-flex
                  xs12
                  md6
                >
                  <v-text-field
                    label="Фамилия"
                    :rules="lastnameRules"
                    :counter="15"
                    class="purple-input"/>
                </v-flex>
                <v-flex
                  xs12
                  md12
                >
                  <v-text-field
                    label="Адрес"
                    class="purple-input"/>
                </v-flex>
                <v-flex
                  xs12
                  md6>
                  <v-select
                    label="Город"
                    class="purple-input"
                    :items="cities"
                  />
                </v-flex>
                <v-flex
                  xs12
                  md6>
                  <v-text-field
                    label="Россия"
                    class="purple-input"
                    disabled/>
                </v-flex>
<!--                <v-flex-->
<!--                  xs12-->
<!--                  md4>-->
<!--                  <v-text-field-->
<!--                    class="purple-input"-->
<!--                    label="Postal Code"-->
<!--                    type="number"/>-->
<!--                </v-flex>-->
                <v-flex xs12>
                  <v-textarea
                    class="purple-input"
                    label="Обо мне"
                    value="Ответственный работник!"
                  />
                </v-flex>
                <v-flex
                  xs12
                  text-xs-right
                >
                  <v-btn
                    class="mx-0 font-weight-light"
                    color="success"
                  >
                    Сохранить
                  </v-btn>
                </v-flex>
              </v-layout>
            </v-container>
          </v-form>
        </material-card>
      </v-flex>
      <v-flex
        xs12
        md4
      >
        <material-card class="v-card-profile">
          <v-avatar
            slot="offset"
            class="mx-auto d-block"
            size="130"
          >
            <img
              src="http://pngimg.com/uploads/steve_jobs/steve_jobs_PNG33437.png"
            >
          </v-avatar>
          <v-card-text class="text-xs-center">
            <h6 class="category text-gray font-weight-thin mb-3">Основатель Apple</h6>
            <h4 class="card-title font-weight-light">Стив Джобс</h4>
            <p class="card-description font-weight-light">Будь честен с самим собой, и с людьми, всегда делай все вовремя, никогда не сдавайся, иди к своим целям, даже если все плохо.</p>
<!--            <v-btn-->
<!--              color="success"-->
<!--              round-->
<!--              class="font-weight-light"-->
<!--            >Follow</v-btn>-->
          </v-card-text>
        </material-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  export default {
    data() {
      return {
        nameRules: [
          v => !!v || 'Введите имя',
          v => v.length >= 4 || 'Имя должно содержать не меньше 4 символов'
        ],
        lastnameRules: [
          v => !!v || 'Введите фамилию',
          v => v.length <= 15 || 'Фамилия должна содержать не больше 15 символов'
        ],
        inputRules: [
          v => v.length >= 4 || 'Пожалуйста, напишите ваш никнейм, не меньше 4 символов'
        ],
        emailRules: [
          v => !!v || 'Введите электронную почту',
          v => /.+@.+/.test(v) || 'Электронная почта должна быть действительна'
        ],
        cities: [ 'Волгоград', 'Воронеж', 'Екатеринбург', 'Казань', 'Краснодар', 'Красноярск', 'Москва', 'Нижний Новгород', 'Новосибирск', 'Омск', 'Пермь', 'Ростов-на-Дону', 'Самара', 'Санкт-Петербург', 'Саратов','Тольятти', 'Тюмень', 'Уфа', 'Челябинск'],
      }
    }
  }
</script>
