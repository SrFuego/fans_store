<template>
  <div id="app">
    <navbar-view />
    <router-view/>
  </div>
</template>

<script>
  import NavbarView from './components/NavbarView.vue'
  export default {
    name: 'app',
    components: {
      NavbarView
    }
  }
</script>