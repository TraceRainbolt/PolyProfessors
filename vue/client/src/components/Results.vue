<template>
    <div v-if="loading">
        <div class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>
    </div>
    <div class="results" v-else>
        <div v-if="this.$route.name === 'professors'">
            <h4 class="results-heading"> {{ results.length }} professors </h4>
            <div class="filters">
                <dropdown class="sort-select filter" :options="sorts" :selected="sort"
                        v-on:updateOption="changeSort"></dropdown>
                <dropdown class="dep-select filter" :options="courses" :selected="course"
                        v-on:updateOption="changeDepartment"></dropdown>
                <input class="search-text" type="text" v-model="filter"
                    v-on:input="updateSearch(filter)" placeholder="Filter professors..." />
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
                    {{ formatDepartment(result[3]) }}
                </div>
                <div class="eval-num">
                    {{ result[5] }} evaluations
                </div>
            </li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios';
import Dropdown from '@/components/Dropdown';
import departments from '@/departments';

export default {
    name: 'Results',
    data() {
        return {
            results: [],
            loading: true,
            terms: null,
            filter: null,
            normalSearch: true,
            orderby: 'alphabetical',
            course: { name: 'All' },
            courses: [{ name: 'All' }],
            sort: { name: 'Alphabetical', val: 'alphabetical' },
            sorts: [{ name: 'Alphabetical', val: 'alphabetical' },
                { name: 'Rating', val: 'rating' },
                { name: 'Department', val: 'department' },],
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
            let baseUrl = 'http://localhost:5000/search?';

            if (!terms) {
                this.terms = this.filter;
            } else {
                this.terms = terms;
            }

            if (this.terms) {
                baseUrl += `terms=${this.terms}&`;
            }
            if (this.department && !this.normalSearch) {
                baseUrl += `department=${this.department}&`;
            }
            if (this.sort && !this.normalSearch) {
                baseUrl += `sort=${this.orderby}`;
            }
            axios.get(baseUrl)
                .then((res) => {
                    this.results = res.data;
                    this.loading = false;
                    if(this.normalSearch){
                        document.title = `${this.terms} - search`;
                    }
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
        getCourseList() {
            const path = 'http://localhost:5000/courses';
            axios.get(path)
                .then((res) => {
                    res.data.map(c => this.courses.push({ name: c }));
                })
                .catch((error) => {
                    this.courses = error;
                });
        },
        updateSearch(filter) {
            this.filterUpdates += 1;
            setTimeout(() => {
                this.filterUpdates -= 1;
                if (this.filterUpdates === 0) {
                    this.getResults(filter);
                }
            }, 500);
        },
        formatRating(rating) {
            if (rating < 0) {
                return 'N/A';
            }
            if (rating !== null) {
                return rating.toFixed(2);
            }
            return '';
        },
        formatDepartment(department) {
            return departments[department];
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
            this.sort = sort;
            this.getResults(this.filter);
        },
        changeDepartment(department) {
            this.course = department;
            this.department = department.name;
            this.getResults(this.filter);
        },
        resetData() {
            this.terms = null;
            this.loading = true;
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
        if (this.$router.previous.name === 'search'
            && this.$router.history.current.name === 'results') {
            this.normalSearch = true;
            this.resetData();
            this.render();
        } else {
            this.normalSearch = false;
        }
    },
    created() {
        this.render();
        this.getCourseList();
    },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>


input[type="text"], input[type="password"], textarea, select {
    outline: none;
    border: 0;
    font-size: 26px;
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
    margin-top: 2rem;
    position: absolute;
    left: 50%;
    transform: translate(-50%, 0);

    width: 100%;
    max-width: 800px;
    padding-left: calc(100vw - 100%); /* Trick to keep centered even with scrollbar */
    text-align: left;
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
    margin-top: -8px;
    display: inline;
    float: right;
    font-size: 40px;
    color: #555555;
}

.eval-num {
    margin-top: -28px;
    display: inline;
    float: right;
    font-size: 22px;
    color: darkgrey;
}

.filters {
    margin-top: 10px;
    margin-left: 16px;
    width: 750px;
    display: grid;
    grid-column-gap: 16px;
    grid-template-areas:
    'sort dep-filter search-text';
}

.filter {
    margin: 0;
    padding: 4px 8px 14px 8px;
    background: white;
    font-size: 26px;
    border-radius: 4px;
    filter: drop-shadow(0 3px 2px #b9b9b9);
    border: none;
    background-image: none;
}

.sort-select {
    width: 180px;
}

.dep-select {
    width: 110px;
}

.search-text {
    margin: 0;
    width: 400px;
    height: 56px;

    padding-left: 15px;

    background: #ffffff;
    filter: drop-shadow(0 3px 2px #b9b9b9);
    border-radius: 4px;

    color: #111111;
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
