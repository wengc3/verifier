<template>
  <v-btn @click="$emit('get-info', category_id)" fab
  v-bind:color="getColor(getCategory.value)"
  v-bind:style="{opacity: getOpacity}"
  class="verfier-catogory">{{category_id}}</v-btn>
</template>

<script>
import getColorMixin from '../mixins/getColorMixin.js'

export default {
  mixins: [getColorMixin],
  computed: {
    getCategory: function () {
      return this.$store.state.Verifier.categories[this.category_id - 1]
    },
    getOpacity: function () {
      switch (this.getCategory.state) {
        case 'running':
          return 0.4
        case 'completed':
          return 1
        default:
          return 1
      }
    }
  },
  props: {
    category_id: {
      type: Number,
      required: true,
      default: 1
    }
  }
}
</script>

<style media="screen">
  .verfier-catogory{
    font-size: 3em;
    height: 100px;
    width: 100px;
    border: 5px solid;
  }
</style>
