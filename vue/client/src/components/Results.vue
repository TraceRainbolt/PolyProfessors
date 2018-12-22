<template>
    <div v-if="loading">
        <div class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>
    </div>
    <div class="results" v-else>
        <div v-if="this.$route.name === 'professors'">
            <h4 class="results-heading"> {{ results.length }} professors </h4>
            <input class="search-text" type="text" v-model="filter"
                v-on:input="updateSearch(filter)" placeholder="Filter professors..." />
            <div class="filters">
                <dropdown class="sort" :options="sorts" :selected="sort"
                        v-on:updateOption="changeSort"></dropdown>
                <div class="search">
                </div>
            </div>
        </div>
        <h4 class="results-heading" v-else> {{ results.length }} results for '{{ terms }}' </h4>
        <ul>
            <li v-for="result in results" v-bind:key="result[0]" v-on:click="getReview(result) ">
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
import Dropdown from '@/components/Dropdown';

export default {
    name: 'Results',
    data() {
        return {
            results: [],
            loading: true,
            terms: null,
            filter: null,
            orderby: 'alphabetical',
            sort: { name: 'Alphabetical' },
            sorts: [{ name: 'Alphabetical', val: 'alphabetical' },
                { name: 'Rating', val: 'rating' },
                { name: 'Department', val: 'department' },
                { name: 'Last Review', val: 'review' }],
            isAll: this.$route.name === 'professors',
            filterUpdates: 0,
        };
    },
    components: {
        dropdown: Dropdown,
    },
    methods: {
        getReview(result) {
            this.$router.push({ name: 'review', params: { id: result[0] } });
        },
        getResults(terms) {
            if (!terms) {
                this.terms = this.filter;
            }
            this.terms = terms;
            const path = `http://localhost:5000/search?terms=${this.terms}&sort=${this.orderby}`;
            axios.get(path)
                .then((res) => {
                    this.results = res.data;
                    this.loading = false;
                    document.title = `${terms} - search`;
                    if (this.results.length === 1 && !this.isAll) {
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
        updateSearch(filter) {
            this.filterUpdates++;
            setTimeout(() => {
                this.filterUpdates--;
                if (this.filterUpdates === 0) {
                    this.getResults(filter);
                }
            }, 500);
        },
        formatRating(rating) {
            if (rating < 0){
                return 'N/A';
            }
            if (rating !== null) {
                return rating.toFixed(2);
            }
            return '';
        },
        filterResults() {
            if (this.filter) {
                this.getResults(this.filter);
            } else {
                this.getAllProfs();
            }
        },
        changeSort(sort) {
            this.orderby = sort.val;
            this.getResults(this.filter);
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


input[type="text"], input[type="password"], textarea, select {
    outline: none;
    border: 0;
    font-size: 30px;
}

ul {
    position: relative;
    z-index: -1;
    width: 800px;
    padding: 0;
    list-style-type: none;
    margin-bottom: 100px;
}

li {
    margin: 15px;
    padding: 12px 15px 15px 16px;
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


.results {
    position: absolute;
    left: 50%;
    transform: translate(-50%, 0);
    text-align: left;
    padding-left: calc(100vw - 100%); /* Trick to keep centered even with scrollbar */
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
    padding: 0 0 0 16px;
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

.filters {
    z-index: 999;
    display: grid;
    grid-template-areas:
    'sort search';
}

.sort {
    padding: 15px 10px;
    background: white;
    margin-left: 16px;
    width: 140px;
    font-size: 18px;
    border-radius: 4px;
    filter: drop-shadow(0 3px 2px #b9b9b9);
    border: none;
    background-image: none;
}

.search {
    width: 600px;
    margin: 10px 0 0 -8px;
    height: 70px;
    background: #ffffff;
    filter: drop-shadow(0 3px 2px #b9b9b9);
    border-radius: 4px;
}

.search-text {
    margin-top: 6px;
    margin-left: 90px;
    position: absolute;
    top: 50px;
    width: 500px;
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
