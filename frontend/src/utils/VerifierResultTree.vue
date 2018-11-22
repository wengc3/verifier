<template>
  <div>
    <v-flex xs12 md12 v-for="result in results" :key="result.id" >
      <verifier-result-node :result="result">
        <v-flex ml-3 xs10 md10 v-for="child in result.children " :key="child.id">
          <verifier-result-node :result="child"></verifier-result-node>
        </v-flex>
      </verifier-result-node>
    </v-flex>
  </div>
</template>

<script>
export default{
  props: {
    results: {
      type: Array,
      required: true,
      default: []
    }
  }
}
</script>
