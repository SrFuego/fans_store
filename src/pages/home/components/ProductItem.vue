<template>
  <div class="list-products">
    <div class="product-item">
      <div class="item-inner">
        <div class="item-image">
          <img :src="'/static/img/product'+num+'.png'">
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
</template>
<script>
  export default {
    name: 'ProductItem',
    props: {
      num: Number
    }
  }
</script>