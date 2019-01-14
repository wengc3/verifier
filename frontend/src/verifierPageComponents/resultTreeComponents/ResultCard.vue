<template>
  <v-card>
    <v-card-text class="grey lighten-3">
      <v-flex xs8 md8>{{result.description}}:</v-flex>
      <v-flex xs12 v-for="item in result.data" >
        <v-flex v-for="(value,key) in item">
          <v-flex v-if="isBigValue(value)">
            <v-flex md3 xs3>{{key}}:</v-flex>
            <data-parser :value="value"></data-parser>
          </v-flex>
          <v-layout v-else row-wrap>
            <v-flex md3 xs3>{{key}}:</v-flex>
            <p>{{JSON.stringify(value,undefined, 2)}}</p>
          </v-layout>
        </v-flex>
      </v-flex>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props: {
    result: {
      type: Object,
      required: true,
      default: {}
    }
  },
  methods: {
    isBigValue: function (value) {
      return JSON.stringify(value).length > 70
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
