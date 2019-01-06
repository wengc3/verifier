// filter function
function filterItems (result, filter) {
  return result.children.filter(function (elem) {
    return filter === elem.value
  })
}

const getDefaultState = () => {
  return {
    categories: [
      {id: 1, title: 'Completness', state: 'idle', value: '', results: []},
      {id: 2, title: 'Integrity', state: 'idle', value: '', results: []},
      {id: 3, title: 'Consistency', state: 'idle', value: '', results: []},
      {id: 4, title: 'Evidence', state: 'idle', value: '', results: []},
      {id: 5, title: 'Authenticity', state: 'idle', value: '', results: []}
    ],
    currentTest: '',
    progress: 0,
    completed: false
  }
}

// initial state
const state = getDefaultState()

// mutations
const mutations = {

  SOCKET_NEWSTATE: (state, data) => {
    let runningState = JSON.parse(data)
    let category = state.categories[Number(runningState.id) - 1]
    category.state = runningState.value
    console.log('newState:', runningState)
    if (runningState.value === 'running') {
      category.value = 'successful'
    }
  },

  SOCKET_TESTRUNNING: (state, title) => {
    state.currentTest = title
    console.log('currentTest:', title)
  },

  SOCKET_ALLRESULTS: (state, data) => {
    let results = JSON.parse(data)
    results.forEach(function (result) {
      state.categories[result.id - 1].results = result.children
    })
    console.log('allResults:', results)
    console.log('categories:', state.categories)
    state.completed = true
  },

  SOCKET_NEWPROGRESS: (state, prg) => {
    state.progress = Number(prg)
    console.log('newProgress:', prg)
  },

  SOCKET_RESULTFAILED: (state, data) => {
    let failedResult = JSON.parse(data)
    state.categories[Number(failedResult.id) - 1].value = failedResult.value
    console.log('resultFailed:', failedResult.id, failedResult.value)
  },

  calcResult: function (state, payload) {
    state.currentResults = []
    let results = JSON.parse(JSON.stringify(state.categories[payload.id - 1].results)) // a coppy of results
    // let results = state.categories[payload.id - 1].results
    if (payload.filter === 'all') {
      state.currentResults = results
    } else {
      results.forEach(function (elem) {
        elem.children = filterItems(elem, payload.filter)
        if (elem.children.length > 0) {
          state.currentResults.push(elem)
        }
      })
    }
  },

  resetState: function (state) {
    Object.assign(state, getDefaultState())
  }
}

const getters = {
  currentResults: (state) => (payload) => {
    let currentResults = []
    let results = JSON.parse(JSON.stringify(state.categories[payload.id - 1].results)) // a coppy of results
    if (payload.filter === 'all') {
      return results
    } else {
      results.forEach(function (elem) {
        elem.children = filterItems(elem, payload.filter)
        if (elem.children.length > 0) {
          currentResults.push(elem)
        }
      })
    }
    return currentResults
  }
}

export default {
  state,
  mutations,
  getters
}
