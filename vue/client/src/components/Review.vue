<template>
  <div id="reviews">
    <div v-if="loading">
      <div class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>
    </div>
    <div v-else>
        <div class="header">
            <h4 class="name"> {{ `${professor[1]} ${professor[2]}` }}</h4>
            <h4 class="rating"> {{ formatRating(professor[4]) }} / 4.00</h4>
            <h4 class="department"> {{ formatDepartment(professor[3]) }} </h4>
            <h4 class="eval-num"> {{ reviews.length }} evaulations </h4>
            <h4 class="add-eval" v-on:click="gotoEvaluate()"> Leave an evaluation </h4>
            <h4 class="avg-grade"> {{ averageGrade(reviews) }} average </h4>
        </div>
        <div class="filters">
            <h4>Filter by class: </h4>
            <input class="course-num" v-model="courseNum" placeholder="101" />
            <h4>Sort reviews: </h4>
            <dropdown class="filter" :options="sorts" :selected="sort"></dropdown>
        </div>
        <ul>
            <li class="review" v-for="review in reviews" v-bind:key="review[0]">
                <div class="review-data">
                    <span class="course">{{ `${review[1]} ${review[2]}` }}</span>
                    <span>{{ toYear(review[4]) }}</span>
                    <span>{{ toReq(review[5]) }}</span>
                    <span>{{ review[6] }}</span>
                    <span>{{ toDate(review[7]) }}</span>
                </div>
                <div class="review-text">
                    {{ review[9] }}
                </div>
            </li>
        </ul>
    </div>
</div>
</template>

<script>
import axios from 'axios';
import departments from '@/departments';
import Dropdown from '@/components/Dropdown';

export default {
    name: 'Results',
    data() {
        return {
            id: -1,
            professor: ['', '', '', '', ''],
            reviews: [],
            course: { name: 'Any' },
            courses: [{ name: 'Any' }],
            sort: { name: 'Alphabetical' },
            sorts: [{ name: 'Alphabetical' }],
            loading: true,
        };
    },
    components: {
        dropdown: Dropdown,
    },
    methods: {
        getProfessor(id) {
            const path = `http://localhost:5000/professor?id=${id}`;
            axios.get(path)
                .then((res) => {
                    this.professor = res.data;
                    document.title = `${this.professor[1]} ${this.professor[2]} - reviews`;
                })
                .catch((error) => {
                    this.professor = error;
                });
        },
        getReviews(profId) {
            const path = `http://localhost:5000/reviews?id=${profId}`;
            this.profId = profId;

            axios.get(path)
                .then((res) => {
                    this.reviews = res.data;
                    this.loading = false;
                })
                .catch((error) => {
                    this.reviews = error;
                    this.loading = false;
                });
        },
        gotoEvaluate() {
            this.$router.push({ name: 'evaluate', params: { id: this.profId } });
        },
        formatRating(rating) {
            if (rating !== null) {
                return rating.toFixed(2);
            }
            return '';
        },
        averageGrade(reviews) {
            const gradeVals = { F: 0, D: 1, C: 2, B: 3, A: 4, 'N/A': -1 };
            let totalGrade = 0;
            let numGrades = 0;

            reviews.forEach((review) => {
                const grade = gradeVals[review[6]];
                if (grade > 0) {
                    totalGrade += grade;
                    numGrades += 1;
                }
            });
            return Object.keys(gradeVals)[Math.round(totalGrade / numGrades)];
        },
        formatDepartment(department) {
            return departments[department];
        },
        toYear(year) {
            const years = ['Freshman', 'Sophomore', 'Junior', 'Senior', '5th Year', 'Grad Student'];
            return years[year];
        },
        toReq(req) {
            const reqs = ['General Ed', 'Major', 'Support', 'Elective', 'N/A'];
            return reqs[req];
        },
        toDate(date) {
            const dates = date.split(' ');
            return `${dates[2]} ${dates[3]}`;
        },
    },
    activated() {
        this.loading = true;
        const id = this.$route.params.id;
        this.getProfessor(id);
        this.getReviews(id);
    },
    created() {
        const id = this.$route.params.id;
        this.getProfessor(id);
        this.getReviews(id);
    },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

ul {
    padding: 0;
    position: absolute;
    z-index: -1;
    top: 8rem;
    left: 50%;
    width: 100vw;
    transform: translate(-50%, 0);
    max-width: 1100px;
}



.review {
    margin-bottom: 1rem;
    display: grid;

    grid-template-areas:
    'review-data review-text';
    grid-template-columns: 70px auto;

    font-family: 'Arial', sans-serif;
}

span {
    display: block;
    margin-bottom: 4px;
}

.course {
    color: #2c3e50;
}

.review-data {
    margin-top: 4px;
    margin-right: 0.4rem;

    text-align: right;

    font-weight: bold;
    font-size: 8pt;
}

.review-text {
    display: inline;

    margin: 0;
    margin-right: 0.5rem;
    padding: 0.5rem;

    font-size: 8pt;
    text-align: left;
    filter: drop-shadow(0 1px 2px #b9b9b9);

    background: white;
    border-left: 3px #2c3e50 solid;
}

.header {
    display: grid;
    position: absolute;
    left: 50%;

    width: 95%;
    max-width: 1100px;

    grid-template-areas:
    'name rating'
    'department eval-num'
    '. avg-grade';

    transform: translate(-50%, 0);
    text-align: left;
}

.name {
    margin: 0;
    left: 0;
    font-size: 16pt;
}

.rating {
    margin: 0;
    text-align: right;

    font-family: Montserrat Regular;
    font-size: 16pt;
    color: #666666;
}

.department {
    margin: 0;
    margin-top: 0.1rem;
    font-family: Montserrat Regular;
    font-size: 12pt;
    color: #666666;
}

.eval-num {
    margin: 0;

    margin-top: 0.1rem;
    text-align: right;
    font-family: Montserrat Regular;
    font-size: 12pt;
}

.avg-grade {
    margin: 0;

    margin-top: 0.2rem;
    text-align: right;
    font-family: Montserrat Regular;
    font-size: 12pt;
}

.add-eval {
    margin: 0;

    margin-top: 0.2rem;
    font-family: Montserrat Regular;
    font-size: 12pt;
    border-radius: 4px;
    color: grey;
}

.add-eval:hover {
    color: #2c3e50;
    cursor: pointer;
}

.filters {
    display: none;
    position: absolute;
    top: 220px;
    left: 50%;

    transform: translate(-50%, 0);
    text-align: left;
    width: 1100px;
}

.filters h4 {
    display: inline;
    font-size: 18px;
}

.filter {
    margin: 0;
    margin-left: 10px;
    margin-right: 30px;
    margin-bottom: 5px;
    padding: 2px;
    background: transparent;
    font-size: 18px;

    border: none;
    background-image: none;
}

@media (min-width:800px) {

    ul {
        margin-top: 9rem;
    }

    .review {
        margin-bottom: 1.7rem;
        width: 100%;
        grid-template-columns: 160px auto;
    }

    .review-data {
        margin-right: 1rem;
        font-size: 16pt;
    }

    .review-text {
        padding: 16px;
        font-size: 16pt;
    }

    .header {
        margin-top: 2rem;
    }

    .name {
        font-size: 38pt;
    }

    .rating {
        font-size: 42pt;
    }

    .department {
        margin-top: -0.6rem;
        font-size: 26pt;
    }

    .eval-num {
        margin-top: -0.1rem;
        font-size: 22pt;
    }

    .avg-grade {
        margin-top: -0.1rem;
        font-size: 22pt;
    }

    .add-eval {
        font-size: 22pt;
    }

}

</style>
