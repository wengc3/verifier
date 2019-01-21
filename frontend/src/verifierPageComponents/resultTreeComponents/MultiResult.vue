<template>
  <div>
    <v-flex v-for="result in iterResult" :key="getId(result.id)">
      <result :result="result">
        <iteration-result :result="result"></iteration-result>
      </result>
    </v-flex>
  </div>
</template>

<script>
import getIdMixin from '../../mixins/getIdMixin.js'
import getTotalChildrenMixin from '../../mixins/getTotalChildrenMixin.js'

export default{
  data: () => ({
    iterResult: []
  }),
  props: {
    result: {
      type: Object,
      required: true,
      default: {}
    }
  },
  mixins: [getIdMixin, getTotalChildrenMixin],
  methods: {
    getChildren: function (id) {
      let children = []
      this.result.children.forEach(function (result) {
        children.push(result.children.find(child => child.id.startsWith(id)))
      })
      return children
    },
    createResult: function (res) {
      let result = JSON.parse(JSON.stringify(res))
      let doublePointIndex = this.result.title.indexOf(':')
      let preTitle = this.result.title.substring(0, doublePointIndex)
      result.title = preTitle + ': ' + res.description
      result.id = res.id.substring(0, res.id.length - 2)
      result.children = this.getChildren(result.id)
      return result
    }
  },
  created: function () {
    this.result.children[0].children.forEach((result) => {
      this.iterResult.push(this.createResult(result))
    })
  }
}
</script>
