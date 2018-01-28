<template>
  <div class="footer__app">
    <div class="container">
      <div class="row">
        <div class="col-xs-6">
          <div class="f__logo">
            <img src="/static/img/logo.png">
          </div>
          <div class="f__info">
            <p>Telf: +51 1 923 495 617</p>
            <p>Email: miguel@fansstore.co</p>
            <div class="clearfix">
              <ul class="nav nav__social">
                <li><a href=""><img src="/static/img/icon-fb.png"></a></li>
                <li><a href=""><img src="/static/img/icon-inst.png"></a></li>
              </ul>
            </div>
          </div>
        </div>
        <div class="col-xs-6">
          <div class="clearfix">
            <h5>FANS STORE</h5>
          </div>
          <ul class="nav nav__menu">
            <li>
              <router-link :to="{name: 'HomeView'}">
                <span class="name_a">Inicio</span>
              </router-link>
            </li>
            <li>
              <router-link :to="{name: 'AboutPage'}">
                <span class="name_a">Nosotros</span>
              </router-link>
            </li>
            <li>
              <router-link :to="{name: 'FaqView'}">
                <span class="name_a">Puntos de Venta</span>
              </router-link>
            </li>
            <li>
              <router-link :to="{name: 'FaqView'}">
                <span class="name_a">Dudas</span>
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>