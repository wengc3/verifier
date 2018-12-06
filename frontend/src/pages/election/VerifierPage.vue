<template>
  <v-container>
    <h2 class="my-3" v-t="'homePage.welcome.title'"></h2>
    <p v-t="'homePage.welcome.text'"></p>
    <v-btn flat blue @click="verify()" :to="{ name: 'verifierrun'}"><v-icon>mdi-arrow-right-bold-circle</v-icon> Start</v-btn>
  </v-container>
</template>

<script>
export default {
  methods: {
    verify: function () {
      this.$http.post('verifyElection', {
        'election': this.$route.params['electionId']
      }).then(response => {
        response.json().then((data) => {
          // success callback
          // this.$toasted.success('Successfully checked confirmation')
        })
      }).catch(e => {
        this.$toasted.error(e.body.message)
      })
    }
  }
}
</script>
