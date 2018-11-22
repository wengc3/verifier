// filter function
function filterItems(filter, result) {
  return result.results.filter(function(elem) {
      return filter.includes(elem.value);
  })
}

// initial state
const state = {
  categories: [
    {id: 1, title: 'Completness', state: 'idle', failed: false, results: []},
    {id: 2, title: 'Integrity', state: 'idle', failed: false, results: [],
    {id: 3, title: 'Consistency', state: 'idle', failed: false, results: []},
    {id: 4, title: 'Evidence', state: 'idle', failed: false, results: []},
    {id: 5, title: 'Authenticity', state: 'idle', failed: false, results: []}
  ],
  currentResults: [],
  currentTest: '',
  progress: 100
}

// mutations
const mutations = {

  SOCKET_CURRENTTEST: (state, title) => {
    state.currentTest = title
  },

  SOCKET_ALLRESULTS: (state, data) => {
    let json = JSON.parse(data)
    state.results = json
  },

  SOCKET_RESULTFAILED: (state, id) => {
    state.categories[id - 1].failed = true
  },

  calcResult: function (state, payload) {
    let filter = []
    filter.push(payload.filter)
    if (filter.includes('failed')) {
      filter.push('skipped')
    }
    let results = state.categories[payload.id - 1].results
    if (filter.includes('all')) {
      state.currentResults = results
    } else {
      results.forEach(function (elem, index) {
        currentResults[index] = filterItems(filter,elem)
      })
    }
  }
}

export default {
  state,
  mutations
}
