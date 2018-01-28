<template>
  <div class="header__app">
    <div class="container">
      <div class="header__logo">
        <img src="/static/img/logo.png">
      </div>
      <div class="header__menu">
        <div class="content-menu">
          <div class="menu-top clearfix">
            <ul class="nav nav_menu">
              <li>Telf: +993305902</li>
              <li>/</li>
              <li>Dirección: Jr. Fake 1234</li>
              <li>/</li>
              <li>Correo: consulta@fanstore.com</li>
            </ul>
          </div>
          <div class="divider-menu"></div>
          <div class="menu-bottom clearfix">
            <ul class="nav nav_menu">
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
                <router-link :to="{name: 'ProductPage'}">
                  <span class="name_a">Productos</span>
                </router-link>
              </li>
              <li>
                <router-link :to="{name: 'FaqPage'}">
                  <span class="name_a">Dudas</span>
                </router-link>
              </li>
              <!-- li>
                <router-link :to="{name: 'FaqView'}">
                  <span class="name_a">Dudas</span>
                </router-link>
              </li -->
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>