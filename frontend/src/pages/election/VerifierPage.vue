<template>
  <v-container grid-list-md fluid>
    <v-flex xs12>
      <ContentTitle icon="mdi-checkbox-marked-outline" :title="$t('Verifier.title')"></ContentTitle>
    </v-flex>
    <v-layout align-center justify-center row wrap>
      <v-flex mx-2 text-xs-center v-for="category in categories" :key="`category_${category.id}`" sm2 xs3>
        <h3>{{category.title}}</h3>
        <verifier-category @get-info="getInfo" :category_id="category.id" :disabled="status != 'completed' "></verifier-category>
      </v-flex>
      <v-flex mx-5 v-if="!hideBarAndStatus && status !== 'idle'" xs10>
        <v-progress-linear height="10" v-model="progress"></v-progress-linear>
        <p>{{getStatus}}</p>
      </v-flex>
      <v-flex xs12 text-xs-center >
        <v-btn flat blue v-if="status != 'completed'" @click="verify()">Start Verifier</v-btn>
      </v-flex>
      <v-layout row wrap v-if="hideBarAndStatus">
        <v-radio-group xs2 v-model="filter" :mandatory="false">
          <v-radio label="All results" value="all"></v-radio>
          <v-radio label="Succesfull results" value="successful"></v-radio>
          <v-radio label="Failed results" value="failed"></v-radio>
          <v-radio label="Skipped results" value="skipped"></v-radio>
        </v-radio-group>
        <v-flex xs10>
          <v-tabs v-model="tab">
            <v-tab v-for="(phase,n) in currentResults" :key="n" ripple>
              {{phase.title}}
            </v-tab>
          </v-tabs>
          <v-tabs-items v-model="tab">
            <v-tab-item  v-for="(phase,n) in currentResults" :key="n">
              <result-tree :results="phase.children"></result-tree>
            </v-tab-item>
          </v-tabs-items>
        </v-flex>
      </v-layout>
    </v-layout>
  </v-container>
</template>

<script>
import getIdMixin from '../../mixins/getIdMixin.js'

export default {
  data: () => ({
    hideBarAndStatus: false,
    filter: 'all',
    currentCategory: 0,
    status: 'idle',
    tab: null
  }),
  mixins: [getIdMixin],
  methods: {
    getInfo: function (id) {
      this.hideBarAndStatus = true
      this.currentCategory = id
      this.tab = 0
    },
    verify: function () {
      this.status = 'running'
      this.$http.post('verifyElection', {
        'election': this.$route.params['electionId']
      })
    }
  },
  computed: {
    getStatus: function () {
      if (this.$store.state.Verifier.completed) {
        this.status = 'completed'
        return 'All test are complete please klick on a number to get more information'
      } else {
        return 'Current Test: ' + this.$store.state.Verifier.currentTest
      }
    },
    progress: function () {
      let progress = this.$store.state.Verifier.progress
      return progress
    },
    categories: function () {
      return this.$store.state.Verifier.categories
    },
    currentResults: function () {
      if (this.status === 'completed') {
        return this.$store.getters.currentResults({
          id: this.currentCategory,
          filter: this.filter
        })
      }
    }
  },
  created: function () {
    this.$store.commit({
      type: 'resetState'
    })
  }
}
</script>
