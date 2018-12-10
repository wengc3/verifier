<template>
  <div>
    <v-card-text  @mouseenter="isBigData" ref="card" class="grey lighten-3">
      <v-flex xs8 md8>{{result.description}}:</v-flex>
      <div xs12 v-for="value,key in result.data" >
        <v-layout row wrap fill-hight>
          <v-flex xs3 md3>{{key}}:</v-flex>
          <v-flex v-if="!isBigData(value)" xs9 md9>{{value}}</v-flex>
            <v-flex :grow="true" d-flex v-if="isBigData(value)" :max-width="600">
            <v-data-iterator
            :items="value[0]"
            :rows-per-page-items="rowsPerPageItems"
            :pagination.sync="pagination"
            content-tag="v-flex"
            >
            <v-card  :max-width="900" slot="item" slot-scope="props">
              <v-card-text>
                <p class="subheading">
                {{ key}}:
                </p>
                <div class="wrap">{{ props.item.toString()}}</div>
              </v-card-text>
            </v-card>
          </v-data-iterator>
        </v-flex>
      </v-layout>
    </div>
  </v-card-text>
</div>
</template>

<script>
export default {
  data: () => ({
    rowsPerPageItems: [1, 4, 8, 12],
    pagination: {
      rowsPerPage: 1
    }
  }),
  props: {
    result: {
      type: Object,
      required: true,
      default: {}
    }
  },
  methods: {
    isBigData: function (value) {
      return value.toString().length > 74
    }
  }
}
</script>

<style scoped>
.wrap {
  overflow-wrap: break-word;
  word-wrap: break-word;
  white-space: pre-wrap;
}
</style>
