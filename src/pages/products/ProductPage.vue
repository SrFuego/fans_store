<template>
  <div class="section_products">
    <div class="banner_section">
      <div class="bg_black"></div>
      <div class="container">
        <h5 class="title"><span>PRODUCTOS</span></h5>
        <p class="subtitle">Los mejores diseños los encontraras aquí</p>
      </div>
    </div>
    <div class="container">
      <div class="content__search">
        <div class="content__filter">
          <h5 class="title">FILTRAR POR TEMA</h5>
          <div class="list_deports">
            <div v-for="item in themes" class="list_deports-item">
              <span>{{item}}</span>
            </div>
          </div>
          <h5 class="title">FILTRAR POR CARACTERISTICAS</h5>
          <div class="list_location">
            <ui-select label="Talla:" placeholder="Escoge tu talla" :options="sizes" v-model="selectSize" @select="onSelectSize"></ui-select>
            <ui-select label="Color:" placeholder="Escoge tu color" :options="colors" v-model="selectColors" @select="onSelectColors"></ui-select>
            <div class="text-center">
              <ui-button @click="onSubmitFilter()" color="sport-primario">Buscar</ui-button>
            </div>
          </div>
        </div>
        
        <div class="content__products">
          <div class="list-products">
            <div class="product-item">
              <div class="item-inner">
                <div class="item-image">
                  <img :src="'/static/img/product1.png'">
                </div>
                <div class="item-info">
                  <h5 class="item-title">Invoker Negro</h5>
                  <div class="item-price">
                    <span class="special-price">s/ 35.00</span>
                    <span class="old-price">s/ 50.00</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="list-products">
            <div class="product-item">
              <div class="item-inner">
                <div class="item-image">
                  <img :src="'/static/img/product2.png'">
                </div>
                <div class="item-info">
                  <h5 class="item-title">Invoker Negro</h5>
                  <div class="item-price">
                    <span class="special-price">s/ 35.00</span>
                    <span class="old-price">s/ 50.00</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="list-products">
            <div class="product-item">
              <div class="item-inner">
                <div class="item-image">
                  <img :src="'/static/img/product3.png'">
                </div>
                <div class="item-info">
                  <h5 class="item-title">Invoker Negro</h5>
                  <div class="item-price">
                    <span class="special-price">s/ 35.00</span>
                    <span class="old-price">s/ 50.00</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="list-products">
            <div class="product-item">
              <div class="item-inner">
                <div class="item-image">
                  <img :src="'/static/img/product4.png'">
                </div>
                <div class="item-info">
                  <h5 class="item-title">Invoker Negro</h5>
                  <div class="item-price">
                    <span class="special-price">s/ 35.00</span>
                    <span class="old-price">s/ 50.00</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  let themes = ['Comics', 'Cine', 'Televisión', 'Videjuegos', 'Anime']
  let sizes = ['Small', 'Medium', 'Large', 'XLarge']
  let colors = ['Rojo', 'Verde', 'Negro', 'Gris', 'Blanco']
  export default {
    name: 'ProductPage',
    data () {
      return {
        themes,
        sizes,
        colors,
        flagJoin: true,
        selectSize: {},
        selectColors: {}
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
      },
      onSelectSize (item) {
        console.log('size', item)
      },
      onSelectColors (item) {
        console.log('color', item)
      },
      onSubmitFilter () {
        console.log('nada')
      }
    }
  }
</script>