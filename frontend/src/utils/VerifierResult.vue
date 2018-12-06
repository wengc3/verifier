<template>
  <v-expansion-panel>
    <v-expansion-panel-content v-bind:class="[hasFailed ? 'red-background' : 'green-background']">
      <div slot="header">
        <v-layout row wrap>
          <v-flex xs1 md1>{{result.id}}</v-flex>
          <v-flex xs9 md9>{{result.title}}</v-flex>
          <v-flex xs2 md2>{{result.value}}</v-flex>
        </v-layout>
      </div>
      <v-data-iterator
      v-if="hasChildren"
      :items="result.children"
      :rows-per-page-items="rowsPerPageItems"
      :pagination.sync="pagination"
      content-tag="v-flex"
      >
      <v-card slot="item" slot-scope="props">
        <v-card-title>
          <v-layout row wrap>
          <v-flex xs2 md2>{{props.item.id}}:</v-flex>
          <v-flex xs10 md10>{{props.item.title}}</v-flex>
          </v-layout>
        </v-card-title>
        <verifier-result-card-text :result="props.item"></verifier-result-card-text>
      </v-card>
    </v-data-iterator>
    <v-card v-if="!hasChildren">
      <verifier-result-card-text :result="result"></verifier-result-card-text>
    </v-card>
  </v-expansion-panel-content>
</v-expansion-panel>
</template>

<script>
export default{
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
  computed: {
    hasFailed: function () {
      return this.result.value === 'failed'
    },
    hasChildren: function () {
      return this.result.children.length > 0
    }
  }
}
</script>

<style>
.red-background{
  background-color: #F00E13!important;
  border: 1px solid !important
}
.green-background{
  background-color: #2AE517!important;
  border: 1px solid !important
}
</style>
