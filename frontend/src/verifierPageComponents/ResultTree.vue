<template>
  <v-flex>
    <v-flex v-for="result in results" :key="getId(result.id)">
      <result :result="result">
        <result-card v-if="getTotalChildren(result) === 0" :result="result"></result-card>
        <v-flex v-if="getTotalChildren(result) > 0">
          <iteration-result :result="result" v-if="getTotalChildren(result.children[0]) === 0"></iteration-result>
          <multi-result :result="result" v-if="getTotalChildren(result.children[0]) > 0"></multi-result>
        </v-flex>
      </result>
    </v-flex>
  </v-flex>
</template>

<script>
import getIdMixin from '../mixins/getIdMixin.js'
import getTotalChildrenMixin from '../mixins/getTotalChildrenMixin.js'

export default{
  mixins: [getIdMixin, getTotalChildrenMixin],
  props: {
    results: {
      type: Array,
      required: true
    }
  }
}
</script>
