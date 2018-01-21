<template>
  <div class="header-app">
    <div class="container">
      <div class="section-logo">
        <img src="/static/img/logo.png">
      </div>
      <div class="section-menu">
        <div class="content-menu">
          <div class="menu-top">
            <ul class="nav nav_menu">
              <li>Telf: +993305902</li>
              <li>/</li>
              <li>Dirección: Jr. Fake 1234</li>
              <li>/</li>
              <li>Correo: consulta@fanstore.com</li>
            </ul>
          </div>
          <div class="divider-menu"></div>
          <div class="menu-bottom">
            <ul class="nav nav_menu">
              <li>
                <router-link :to="{name: 'HomeView'}">
                  <span class="name_a">Inicio</span>
                </router-link>
              </li>
              <li>
                <router-link :to="{name: 'AboutView'}">
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
  </div>
</template>