<template>
  <v-btn @click="$emit('get-info', phase_id)" fab v-bind:color="getColor" class="verfier-phase">{{phase_id}}</v-btn>
</template>

<script>
export default {
  computed: {
    getColor: function () {
      let state = this.$store.state.Verifier[this.phase_id]
      let rgb = '42,229,23,'
      let opacity = '0'
      if (state.failed) {
        rgb = '240,14,19,'
      }

      if (state.state === 'running') {
        opacity = '0.4'
      } else if (state.state === 'completed') {
        opacity = '1'
      }
      return 'rgba(' + rgb + opacity + ')'
    }
  },
  props: {
    phase_id: {
      type: Number,
      required: true,
      default: 1
    }
  }
}
</script>

<style media="screen">
  .verfier-phase{
    font-size: 3em;
    height: 100px;
    width: 100px;
    border: 5px solid;
  }
</style>
