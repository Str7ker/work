<template>
  <v-container
    fill-height
    fluid
    grid-list-xl
  >
    <v-layout
      justify-center
      wrap
    >
      <v-flex
        md12
      >
        <material-card
          color="green"
          title="Грузы"
          text="Здесь находятся все Ваши грузы:"
        >
          <v-text-field
                  v-model="search"
                  append-icon="mdi-search"
                  label="Поиск"
                  single-line
                  hide-details
          ></v-text-field>
          <v-data-table
            :headers="headers"
            :items="items"
            :search="search"
          >
            <template
              slot="headerCell"
              slot-scope="{ header }"
            >
              <span
                class="subheading font-weight-light text-success text--darken-3"
                v-text="header.text"
              />
            </template>
            <template
              slot="items"
              slot-scope="{ item }"
            >
              <td>{{ item.name }}</td>
              <td>{{ item.at }}</td>
              <td>{{ item.volume }}</td>
              <td>{{ item.data }}</td>
              <td>{{ item.status }}</td>
              <td class="text-xs-right">{{ item.salary }}</td>
            </template>
          </v-data-table>
        </material-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    search: '',
    headers: [
      {
        text: 'Название груза',
        align: 'left',
        sortable: false,
        value: 'name'
      },
      { text: 'Вес (кг)', value: 'at' },
      { text: 'Объём (м)', value: 'volume' },
      { text: 'Дата заказа', value: 'data' },
      { text: 'Статус', value: 'status' },
    ],
    items: [
      {
        name: 'Диван',
        at: 20,
        volume: 6,
        data: '01.05.2019',
        status: 'Доставлено',
      },
      {
        name: 'Шкаф',
        at: 30,
        volume: 9,
        data: '02.05.2019',
        status: 'Доставлено',
      },
      {
        name: 'Стол',
        at: 5,
        volume: 5,
        data: '04.05.2019',
        status: 'Ожидает отправление',
      },
      {
        name: 'Холодильник',
        at: 20,
        volume: 2.5,
        data: '06.05.2019',
        status: 'В пути',
      },
      {
        name: 'Плита',
        at: 20,
        volume: 1,
        data: '10.09.2019',
        status: 'В пути',
      },
    ]
  })
}
</script>

<style>

</style>
