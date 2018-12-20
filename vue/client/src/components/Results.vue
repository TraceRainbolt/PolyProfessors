<template>
    <div v-if="loading">
        <div class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>
    </div>
    <div class="results" v-else>
        <h4 class="results-heading" v-if="terms === null"> {{ results.length }} professors </h4>
        <h4 class="results-heading" v-else-if="results.length == 1"> 1 result for '{{ terms }}'</h4>
        <h4 class="results-heading" v-else> {{ results.length }} results for '{{ terms }}' </h4>
        <ul>
            <li v-for="result in results" v-bind:key="result[0]" v-on:click="getReview(result)">
                <div class="name">
                    {{ result[2] }},
                    {{ result[1] }}
                </div>
                <div class="rating">
                    {{ formatRating(result[4]) }}
                </div>
                <div class="department">
                    {{ result[3] }}
                </div>
            </li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Results',
    data() {
        return {
            results: [],
            loading: true,
            terms: null,
        };
    },
    methods: {
        getReview(result) {
            this.$router.push({ name: 'review', params: { id: result[0] } });
        },
        getResults(terms) {
            const path = `http://localhost:5000/search?terms=${terms}`;
            this.terms = terms;
            axios.get(path)
                .then((res) => {
                    this.results = res.data;
                    this.loading = false;
                    document.title = `${terms} - search`;
                    if (this.results.length === 1) {
                        this.$router.replace({ name: 'review',
                            params: { id: this.results[0][0] } });
                    }
                })
                .catch((error) => {
                    this.results = error;
                    this.loading = false;
                });
        },
        getAllProfs() {
            const path = 'http://localhost:5000/search';
            axios.get(path)
                .then((res) => {
                    this.results = res.data;
                    this.loading = false;
                    document.title = 'Professors';
                })
                .catch((error) => {
                    this.results = error;
                    this.loading = false;
                });
        },
        formatRating(rating) {
            if (rating !== null) {
                return rating.toFixed(2);
            }
            return '';
        },
        render() {
            const terms = this.$route.params.terms;
            if (terms) {
                this.getResults(terms);
            } else {
                this.getAllProfs();
            }
        },
    },
    activated() {
        this.loading = true;
        this.terms = null;
        this.render();
    },
    created() {
        this.render();
    },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.results {
    position: absolute;
    left: 50%;
    transform: translate(-50%, 0);
    text-align: left;
}

ul {
    list-style-type: none;
    margin-bottom: 100px;
}

li {
    margin: 15px;
    padding: 12px 15px 15px 16px;
    width: 800px;
    height: 60px;
    background: white;
    border-radius: 4px;
    filter: drop-shadow(0 3px 2px #b9b9b9);
    cursor: pointer;
    border-left: 4px #2c3e50 solid;
}

li:hover {
    border-left: 4px green solid;
    background: #DFDFDF;
}

.loading {
    position: absolute;
    left: 50%;
    transform: translate(-50%, 0);
    top: 100px;
    width: 300px;
}

.results-heading {
    margin: 0;
    padding: 0 0 0 55px;
    font-size: 30px;
}

.name {
    display: inline;
    font-size: 30px;
}

.department {
    display: block;
    font-size: 22px;
    color: darkgrey;
}

.rating {
    display: inline;
    float: right;
    font-size: 46px;
    color: #555555;
}

</style>
