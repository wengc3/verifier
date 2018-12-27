export default {
  methods: {
    getColor: function (value) {
      switch (value) {
        case 'failed':
          return '#F00E13'
        case 'successful':
          return '#2AE517'
        case 'skipped':
          return '#ff9900'
        default:
          return '#fafafa'
      }
    }
  }
}
