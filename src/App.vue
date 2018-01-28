<template>
  <div id="app">
    <navbar-view />
    <router-view />
    <footer-view />
  </div>
</template>

<script>
  import NavbarView from './components/NavbarView.vue'
  import FooterView from './components/FooterView.vue'
  export default {
    name: 'app',
    components: {
      NavbarView,
      FooterView
    }
  }
</script>