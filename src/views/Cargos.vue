<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
<v-card>
<v-card-title class="subheading grey--text">
Грузы
<v-spacer></v-spacer>
<v-text-field
v-model="search"
append-icon="search"
label="Поиск"
single-line
hide-details
></v-text-field>
</v-card-title>
<v-data-table
:headers="headers"
:items="names"
:search="search"
>
<template v-slot:items="cargos">
<td>{{ cargos.item.name }}</td>
<td class="text-xs-right">{{ cargos.item.at }}</td>
<td class="text-xs-right">{{ cargos.item.volume }}</td>
<td class="text-xs-right">{{ cargos.item.data }}</td>
<td class="text-xs-right">{{ cargos.item.status }}</td>
</template>
<template v-slot:no-results>
<v-alert :value="true" color="error" icon="warning">
Ваши данные по заданному поиску "{{ search }}" не найдены.
</v-alert>
</template>
</v-data-table>
</v-card>
</template>

<script>
export default {
data () {
return {
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
names: [
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
}
}
}
</script>
