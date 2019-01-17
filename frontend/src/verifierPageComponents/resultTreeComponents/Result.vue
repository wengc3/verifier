<template>
  <v-expansion-panel>
    <v-expansion-panel-content v-bind:style="{ 'background-color': getColor(result.value), border: '1.5px solid' }">
      <div slot="header">
        <v-layout row wrap>
          <v-flex mr-2 xs1 md1>{{result.id}}</v-flex>
          <v-flex v-if="getTotalChildren(result) != 0">({{getTotalChildren(result)}} Tests)</v-flex>
          <v-flex xs8 md8>{{result.title}}</v-flex>
          <v-flex mx-3 text-xs-right>{{result.value}}</v-flex>
        </v-layout>
      </div>
      <slot></slot>
    </v-expansion-panel-content>
  </v-expansion-panel>
</template>

<script>
import getColorMixin from '../../mixins/getColorMixin.js'
import getTotalChildrenMixin from '../../mixins/getTotalChildrenMixin.js'
export default {
  mixins: [getColorMixin, getTotalChildrenMixin],
  props: {
    result: {
      type: Object,
      required: true,
      default: {}
    }
  }
}
  </script>
