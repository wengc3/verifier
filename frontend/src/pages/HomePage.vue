<template>
  <v-container>
    <h2 class="my-3" v-t="'homePage.welcome.title'"></h2>
    <p v-t="'homePage.welcome.text'"></p>
    <v-flex xs12 text-xs-center >
      <v-btn :to="{ name: 'about'}" flat small>More Details</v-btn>
    </v-flex>
    <v-btn flat blue :to="{ name: 'elections'}"><v-icon>mdi-arrow-right-bold-circle</v-icon> Start</v-btn>
  </v-container>
</template>
