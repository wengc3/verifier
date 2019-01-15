export default {
  methods: {
    getTotalChildren: function (result) {
      if (result.children.length > 0) {
        if (result.children[0].children.length > 0) {
          return result.children[0].children.length
        } else {
          return result.children.length
        }
      }
      return 0
    }
  }
}
