<template>
    <div id="app">
        <div class="nav">
            <span v-on:click="viewProfList()">View professor list</span>
            <span v-on:click="addProfessor">Add a professor</span>
            <span v-on:click="viewAbout">About poly professors</span>
        </div>
        <h4>Find a professor</h4>
        <div class="search">
            <input class="search-text" type="text" v-model="terms"
                    placeholder="Search..." />
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
        addProfessor() {
            this.$router.push({ name: 'add' });
        },
    },
};

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

::-ms-input-placeholder { /* Microsoft Edge */
    color: darkgrey;
}

::placeholder { /* Everything else */
    color: darkgrey;
}

h4 {
    position: absolute;
    left: 50%;
    top: calc(56% - 3em);
    transform: translateX(-50%);
    font-size: 28pt;
    width: 100%;
}

h3 {
    color: #666666;
    font-size: 25px;
}

.nav {
    position: absolute;
    left: 50%;
    top: 0.5rem;
    transform: translateX(-50%);
    width: 100%;
}

.nav > span {
    display: block;
    margin: 0 1.0%;
    padding: 6px;
    border-radius: 4px;
    font-size: 16pt;
}

.nav > span:hover {
    background: #cecbc0;
    cursor: pointer;
}

.search {
    display: grid;
    position: absolute;
    top: 56%;
    left: 50%;
    transform: translateX(-50%);

    width: 80%;
    height: 3.6rem;
    max-width: 38rem;

    background: #ffffff;
    filter: drop-shadow(0 3px 2px #b9b9b9);
    border-radius: 4px;
}

.search-text {
    margin-left: 1rem;
    margin-top: 0.9rem;
    height: 2rem;
    width: calc(100% - 2rem);

    background: none;
    color: #111111;
    left: calc(50% - 2rem);
    z-index: 1;

    outline: none;
    border: 0;
    font-size: 18pt;
}

.icon {
    top: 1rem;
    right: .8rem;
    z-index: 3;
    position: absolute;
    width: 2rem;
    height: 2rem;
}

.search-btn {
    position: absolute;
    left: calc(100% - 1.7rem);
    z-index: 2;
    transform: translateX(-50%);
    width: 3.6rem;
    height: 3.6rem;
    border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
    background: #119235;
    cursor: pointer;
}

.search-btn:hover {
    background: #128232;
}

@media (min-width:800px) {

    h4 {
        width: 100%;
        top: calc(48% - 4em);
        font-size: 26pt;
    }

    .nav {
        top: 2rem;
    }

    .nav > span {
        padding: 0 1em;
        display: inline;
        font-size: 18pt;
    }

    .search {
        top: 48%;
        height: 4rem;
    }

    .search-text {
        margin-top: 1.2rem;
        font-size: 20pt;
    }

    .icon {
        width: 2.3rem;
        height: 2.4rem;
    }

    .search-btn {
        height: 4rem;
        width: 4.2rem;
    }
}

@media (max-height: 400px) {
    h4 {
        display: none;
    }
}

</style>
