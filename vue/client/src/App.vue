<template>
  <div id="app">
    <keep-alive>
      <router-view/>
  </keep-alive>
</div>
</template>

<script>

export default {
    name: 'App',
};

</script>

<style>

html {
    background: #dad7cb;
}

#app {
    font-family: Montserrat;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}

.lds-ellipsis {
    display: inline-block;
    position: relative;
    width: 64px;
    height: 64px;
}

.lds-ellipsis div {
    position: absolute;
    top: 200px;
    width: 26px;
    height: 26px;
    border-radius: 50%;
    background: #2c3e50;
    animation-timing-function: cubic-bezier(0, 1, 1, 0);
}

.lds-ellipsis div:nth-child(1) {
    left: 12px;
    animation: lds-ellipsis1 0.6s infinite;
}
.lds-ellipsis div:nth-child(2) {
    left: 12px;
    animation: lds-ellipsis2 0.6s infinite;
}
.lds-ellipsis div:nth-child(3) {
    left: 50px;
    animation: lds-ellipsis2 0.6s infinite;
}
.lds-ellipsis div:nth-child(4) {
    left: 90px;
    animation: lds-ellipsis3 0.6s infinite;
}

@keyframes lds-ellipsis1 {
    0% {
        transform: scale(0);
    }
    100% {
        transform: scale(1);
    }
}

@keyframes lds-ellipsis3 {
    0% {
        transform: scale(1);
    }
    100% {
        transform: scale(0);
    }
}

@keyframes lds-ellipsis2 {
    0% {
        transform: translate(0, 0);
    }
    100% {
        transform: translate(39px, 0);
    }
}

</style>
