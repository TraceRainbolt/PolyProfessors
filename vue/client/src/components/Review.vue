<template>
  <div id="app">
    <div v-if="loading">
      <div class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>
  </div>
  <div v-else>
      <div class="header">
        <h4 class="name"> {{ `${professor[1]} ${professor[2]}` }}</h4>
        <h4 class="rating"> {{ formatRating(professor[4]) }} / 4.00</h4>
        <h4 class="department"> {{ professor[3] }} </h4>
        <h4 class="eval-num"> {{ reviews.length }} evaulations </h4>
        <h4 class="add-eval" v-on:click="gotoEvaluate()"> Leave an evaluation </h4>
        <h4 class="avg-grade"> {{ averageGrade(reviews) }} average </h4>
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

export default {
    name: 'Results',
    data() {
        return {
            id: -1,
            professor: ['', '', '', '', ''],
            reviews: [],
            loading: true,
        };
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
        toYear(year) {
            const years = ['Freshman', 'Sophomore', 'Junior', 'Senior', '5th Year Senior', 'Graduate Student'];
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
    position: absolute;
    padding: 6px;
    top: 220px;
    left: 50%;
    transform: translate(-50%, 0);
}

.review {
    margin-bottom: 25px;
    display: grid;

    grid-template-areas:
    'review-data review-text';

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
    margin: 4px 18px 0 -110px;
    width: 190px;

    text-align: right;

    font-weight: bold;
    font-size: 20px;
}

.review-text {
    display: inline;

    margin: 0;
    padding: 20px;

    width: 960px;

    font-size: 20px;
    text-align: left;
    filter: drop-shadow(0 1px 2px #b9b9b9);

    background: white;
    border-left: 3px #2c3e50 solid;
}

.header {
    display: grid;

    position: absolute;
    left: 50%;

    width: 1100px;

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
    font-size: 53px;
}

.rating {
    margin: 0;
    text-align: right;

    font-family: Montserrat Regular;
    font-size: 48px;
    color: #666666;
}

.department {
    margin: 0;
    margin-top: -5px;
    margin-left: 1px;

    font-family: Montserrat Regular;
    font-size: 34px;
    color: #666666;
}

.eval-num {
    margin: 0;

    text-align: right;
    font-family: Montserrat Regular;
    font-size: 23px;
}

.avg-grade {
    margin: 0;
    margin-top: -5px;

    text-align: right;
    font-family: Montserrat Regular;
    font-size: 23px;
}

.add-eval {
    margin: 0;
    margin-top: 4px;
    margin-left: 3px;

    width: 218px;

    font-family: Montserrat Regular;
    font-size: 20px;
    border-radius: 4px;
    color: grey;
}

.add-eval:hover {
    color: #2c3e50;
    cursor: pointer;
}

</style>
