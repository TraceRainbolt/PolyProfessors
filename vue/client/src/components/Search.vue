<template>
    <div id="app">
        <div class="nav">
            <span v-on:click="viewProfList()">View professor list</span>
            <span>Add a professor</span>
            <span v-on:click="viewAbout">About poly professors</span>
        </div>
        <h4>Find a professor</h4>
        <input class="search-text" type="text" v-model="terms"
        placeholder="Search for a professor..." />
        <div class="search">
            <div class="search-btn" v-on:click="goToResults()">
                <img class="icon" src="@/assets/search-icon.png" />
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'SearchPage',
    data() {
        return {
            terms: '',
        };
    },
    methods: {
        goToResults() {
            if (this.terms) {
                this.$router.push({ name: 'results', params: { terms: this.terms } });
            }
        },
        viewProfList() {
            this.$router.push({ name: 'professors' });
        },
        viewAbout() {
            this.$router.push({ name: 'about' });
        },
    },
};

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

input[type="text"], input[type="password"], textarea, select {
    outline: none;
    border: 0;
    font-size: 30px;
}

::-ms-input-placeholder { /* Microsoft Edge */
    color: darkgrey;
}

::placeholder { /* Everything else */
    color: darkgrey;
}

h4 {
    position: absolute;
    left: 50%;
    top: 290px;
    transform: translateX(-50%);
    font-size: 38px;
}

h3 {
    font-size: 25px;
    color: #666666;
}

.nav {
    position: absolute;
    left: 50%;
    top: 30px;
    transform: translateX(-50%);
    width: 100%;
}

.nav > span {
    margin: 0 70px;
    padding: 10px 15px;
    border-radius: 4px;
    font-size: 23px;
}

.nav > span:hover {
    background: #cecbc0;
    cursor: pointer;
}

.search {
    position: absolute;
    left: 50%;
    top: 460px;
    transform: translateX(-50%);
    width: 600px;
    height: 70px;
    background: #ffffff;
    filter: drop-shadow(0 3px 2px #b9b9b9);
    border-radius: 4px;
}

.search-text {
    margin-top: 6px;
    position: absolute;
    top: 460px;
    width: 490px;
    height: 60px;
    transform: translateX(-50%);

    background: none;
    color: #111111;
    left: calc(50% - 33px);
    z-index: 1;
}

.icon {
    top: 18px;
    right: 24px;
    z-index: 3;
    position: absolute;
    width: 40px;
    height: 40px;
}

.search-btn {
    position: relative;
    left: 100%;
    z-index: 2;
    transform: translateX(-50%);
    width: 90px;
    height: 70px;
    border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
    background: #119235;
    cursor: pointer;
}

.search-btn:hover {
    background: #128232;
}
</style>
