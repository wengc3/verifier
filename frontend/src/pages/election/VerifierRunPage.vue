<template>
  <v-container grid-list-md>
    <v-layout row wrap>
      <v-flex mx-2 text-xs-center v-for="category in categories" :key="`category_${category.id}`" xs2>
        <h3>{{category.title}}</h3>
        <verfier-category @get-info="getInfo" :phase_id="category.id" :disabled="!isCompleted"></verfier-category>
      </v-flex>
      <v-flex mx-5 v-if="!hideBarAndStatus" xs10>
        <v-progress-linear height="10" v-model="progress"></v-progress-linear>
        <p>{{getStatus}}</p>
      </v-flex>
      <v-layout row wrap v-if="hideBarAndStatus">
        <v-radio-group @change="filterChanged"xs2 v-model="filter" :mandatory="false">
          <v-radio label="All results" value="all"></v-radio>
          <v-radio label="Succesfull results" value="successful"></v-radio>
          <v-radio label="Failed results" value="failed"></v-radio>
        </v-radio-group>
        <v-flex xs10>
          <v-flex v-for="phase in currentResults" :key="phase.id">
            <h4>{{phase.title}}</h4>
            <verfier-result-tree :results="phase.results"></verfier-result-tree>
          </v-flex>
        </v-flex>
      </v-layout>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    hideBarAndStatus: false,
    isCompleted: false,
    filter: 'all',
    currentCategory: 0,
    items: []
  }),
  methods: {
    getInfo: function (id) {
      this.hideBarAndStatus = true
      this.currentCategory = id
      let isFailed = this.$store.state.Verifier.categories[id - 1].failed
      if (isFailed){
        this.filter = 'failed'
      } else {
        this.filter = 'successful'
      }
      this.filterChanged()
    },
    filterChanged: function () {
      this.$store.state.Verifier.commit('calcResult',{
        id: this.currentCategory,
        filter: this.filter
    )}
  },
  computed: {
    getStatus: function () {
      if (this.isCompleted) {
        return 'All test are complete please klick on a number to get more information'
      } else {
        return 'Current Test: ' + this.$store.state.Verifier.currentTest
      }
    },
    progress: function () {
      let progress = this.$store.state.Verifier.progress
      if (progress === 100) {
        this.isCompleted = true
      }
      return progress
    },
    categories: function() {
      return this.$store.state.Verifier.categories
    },
    currentResults: function() {
      return this.$store.state.Verifier.currentResults
    }
  }
}
</script>


<style media="screen">
.status{
  text-align: left;
}
</style>
