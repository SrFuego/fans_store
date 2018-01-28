<template>
<div class="section_home">
  <banner-view />
  <div class="section_products">
    <div class="container">
      <div class="title">
        <h5>DESTACADOS<span></span></h5>
      </div>
      <div class="slider_products">
        <div class="slider-inner clearfix">
          <div id="slider-destacado-tiny" class="slider-controls-tiny">
            <button type="button" class="controls-slider controls-left"><i class="material-icons">&#xE314;</i></button>
            <button type="button" class="controls-slider controls-right"><i class="material-icons">&#xE315;</i></button>
          </div>
          <tiny-slider :loop="false" items="4" :fixed-width="0.320" controls-container="#slider-destacado-tiny">
            <product-item v-for="i in 8" :key="i" :num="i" />
          </tiny-slider>
        </div>
      </div>
    </div>
  </div>
  <div class="section_love">
    <div class="container">
      <div class="content_love">
        <div class="bg_black"></div>
        <div class="description">
          <h5>TE GUSTA NUESTROS PRODUCTOS?</h5>
          <router-link :to="{name: 'HomeView'}">VER MÁS</router-link>
        </div>
      </div>
    </div>
  </div>
  <div class="section_products">
    <div class="container">
      <div class="title">
        <h5>NUEVOS<span></span></h5>
      </div>
      <div class="slider_products">
        <div class="slider-inner clearfix">
          <div id="slider-nuevos-tiny" class="slider-controls-tiny">
            <button type="button" class="controls-slider controls-left"><i class="material-icons">&#xE314;</i></button>
            <button type="button" class="controls-slider controls-right"><i class="material-icons">&#xE315;</i></button>
          </div>
          <tiny-slider :loop="false" items="4" :fixed-width="0.320" controls-container="#slider-nuevos-tiny">
            <product-item v-for="i in 8" :key="i" :num="i" />
          </tiny-slider>
        </div>
      </div>
    </div>
  </div>
  <div class="section_newsletter">
    <div class="bg_black"></div>
    <div class="container">
      <div class="content-block">
        <h5>SUSCRIBETE PARA RECIBIR NOTICIAS</h5>
        <div class="content_signup">
          <ui-textbox placeholder="Ingresa tu dirección de email" type="email" v-model="newsletter"></ui-textbox>
          <ui-button @click="onSubmitJoin()" color="sport-primario">Unirme ya!</ui-button>
        </div>
      </div>
    </div>
  </div>
  <ui-modal class="modal-join" ref="join" remove-close-button remove-header>
    <h5>Fans Store</h5>
    <p>{{ flagJoin ? 'Ahora eres parte de la familia Fans Store, te mantendremos informado sobre las actividades y/o novedades de tu interes.' : 'Tu correo ya esta registrado' }}</p>
    <div slot="footer">
      <ui-button @click="closeModal('join')" color="shades-white-text">Cerrar</ui-button>
    </div>
  </ui-modal>
</div>
</template>
<script>
  import TinySlider from 'vue-tiny-slider'
  import BannerView from './components/BannerView.vue'
  import ProductItem from './components/ProductItem.vue'
  export default {
    name: 'HomeView',
    components: {
      // NavbarView,
      BannerView,
      TinySlider,
      ProductItem
    },
    data () {
      return {
        newsletter: '',
        flagJoin: true
      }
    },
    methods: {
      openModal (name) {
        this.$refs[name].open()
      },
      closeModal (name) {
        this.$refs[name].close()
      },
      onSubmitJoin () {
        this.openModal('join')
      }
    }
  }
</script>