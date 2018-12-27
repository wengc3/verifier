<template>
  <v-flex>
    <v-flex v-if='isPrimitiv(value)'>
      <BigIntLabel v-if='isBigInt(value)' :mpzValue="value.toString()"></BigIntLabel>
      <ByteArrayLabel v-if='!isBigInt(value)' :value="value.toString()"></ByteArrayLabel>
    </v-flex>
    <v-flex v-else>
      <v-flex v-if='isArray(value)' v-for='(val) in value'>
        <v-layout row-wrap >
          <data-parser :value="val"></data-parser>
        </v-layout>
      </v-flex>
      <v-flex v-else v-for='(val,key) in value'>
        <v-layout row-wrap>
          {{key}}:<data-parser :value="val"></data-parser>
        </v-layout>
      </v-flex>
    </v-flex>
  </v-flex>
</template>

<script>
export default {
  props: {
    value: {
      required: true
    }
  },
  methods: {
    isPrimitiv: function (value) {
      return typeof value !== 'object'
    },

    isBigInt: function (value) {
      return /^\d+$/.test(value) && value.length > 47
    },

    isArray: function (value) {
      return Array.isArray(value)
    }
  }
}
</script>

<style lang="css">
</style>
