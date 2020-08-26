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
  async mounted () {
    const response = await axios.get('http://localhost:5000')
    this.info = response.data
  }
}
</script>
