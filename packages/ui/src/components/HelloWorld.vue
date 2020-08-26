<template>
  <div class="hello">
    <h1 v-if="info">Hello {{ info.hello }}</h1>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HelloWorld',
  data () {
    return {
      info: null
    }
  },
  mounted () {
    axios
      .get('http://localhost:5000')
      .then(response => (this.info = response.data))
  }
}
</script>
