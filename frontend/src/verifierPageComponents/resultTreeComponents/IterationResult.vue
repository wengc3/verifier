<template>
  <v-data-iterator
  :items="result.children"
  :pagination.sync="pagination"
  content-tag="v-flex"
  hide-actions
  >
  <v-layout slot="item" slot-scope="props">
    <v-flex text-xs-center xs1>
      <v-btn flat icon>
        <v-icon @click="previous" :disabled="pagination.page === 1" >mdi-chevron-left</v-icon>
      </v-btn>
    </v-flex>
    <v-flex xs10>
      <result :result="props.item">
        <result-card :result="props.item"></result-card>
      </result>
    </v-flex>
    <v-flex text-xs-center xs1>
      <v-btn flat icon>
        <v-icon @click="next" :disabled="pagination.page === getTotalChildren(result)" >mdi-chevron-right </v-icon>
      </v-btn>
    </v-flex>
  </v-layout>
</v-data-iterator>
</template>

<script>
import getTotalChildrenMixin from '../../mixins/getTotalChildrenMixin.js'

export default{
  data: () => ({
    pagination: {
      rowsPerPage: 1,
      page: 1
    }
  }),
  mixins: [getTotalChildrenMixin],
  props: {
    result: {
      type: Object,
      required: true,
      default: {}
    }
  },
  methods: {
    next: function () {
      this.pagination.page++
    },
    previous: function () {
      this.pagination.page--
    }
  }
}
</script>
