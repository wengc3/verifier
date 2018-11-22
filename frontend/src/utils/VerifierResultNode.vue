<template>
  <v-expansion-panel>
    <v-expansion-panel-content v-bind:class="[hasFailed ? red-background : green-background]">
      <div slot="header">
        <v-flex xs2 md2>{{result.id}}</v-flex>
        <v-flex xs10 md10>{{result.id}}</v-flex>
      </div>
      <v-card>
          <v-card-text class="grey lighten-3">
            <v-flex xs8 md8>{{result.description}}</v-flex>
            <v-flex xs2 md2>{{result.value}}</v-flex>
            <div xs12 v-for="key,value in result.data" >
              <v-flex xs2 md2>{{key}}</v-flex>
              <v-flex xs10 md10>{{value}}</v-flex>
            </div>
          </v-card-text>
      </v-card>
    </v-expansion-panel-content>
  </v-expansion-panel>
</template>

<script>
  export default{
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
