<template>
    <div class="evaluate">
        <div  v-if="this.$route.name === 'add'">
            <h4>Add a Professor</h4>
            <div class="add-professor" >
                <input class="first name" type="text" v-model="terms"
                    placeholder="First Name" />
                <input class="last name" type="text" v-model="terms"
                    placeholder="Last Name" />
                <dropdown class="dropdown prof-dep" ref="courses" :options="courses" :selected="course"
                    v-on:updateOption="updateCourse"></dropdown>
            </div>
        </div>
        <div v-else>
            <h4> Evaluate {{ `${professor[1]} ${professor[2]}` }}</h4>
        </div>
        <div class="form">
            <div class="info">
                <div class="prof-grade-select">
                    <h5>How would you rate this professor?</h5>
                    <dropdown :options="ratings" :selected="rating"
                        v-on:updateOption="updateRating"></dropdown>
                </div>
                <div class="course-select">
                    <h5>Select the course:</h5>
                    <dropdown class="dropdown" ref="courses" :options="courses" :selected="course"
                        v-on:updateOption="updateCourse"></dropdown>
                    <input class="course-num" v-model="courseNum" placeholder="101" />
                </div>
                <div class="grade-select">
                    <h5>Select your grade:</h5>
                    <dropdown :options="grades" :selected="grade"
                        v-on:updateOption="updateGrade"></dropdown>
                </div>
                <div class="year-select">
                    <h5>Select your year:</h5>
                    <dropdown :options="years" :selected="year"
                        v-on:updateOption="updateYear"></dropdown>
                </div>
                <div class="req-select">
                    <h5>Select class fufillment:</h5>
                    <dropdown :options="fufillments" :selected="fufillment"
                        v-on:updateOption="updateFufillment"></dropdown>
                </div>
            </div>
            <div class="review">
                <h5>Please enter your review below:</h5>
                <textarea v-model="review"></textarea>
                <div class="help">Before submitting your application,
                    remember that what you submit cannot be edited or deleted.
                    Make sure you like what you're submitting.
                </div>
                <button v-on:click="submitReview">Submit Evaluation</button>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import Dropdown from '@/components/Dropdown';

export default {
    name: 'Evaluate',
    data() {
        return {
            professor: '',
            review: '',
            courses: [],
            courseNum: 101,
            course: { name: 'AERO' },

            grade: { name: 'A' },
            grades: [{ name: 'N/A' },
                { name: 'A' },
                { name: 'B' },
                { name: 'C' },
                { name: 'D' },
                { name: 'F' },
                { name: 'Credit' },
                { name: 'No Credit' }],

            year: { name: 'Freshman' },
            years: [{ name: 'Freshman' },
                { name: 'Sophomore' },
                { name: 'Junior' },
                { name: 'Senior' },
                { name: '5th/6th Year' },
                { name: 'Grad Student' }],

            fufillment: { name: 'Major' },
            fufillments: [{ name: 'Elective' },
                { name: 'General Ed' },
                { name: 'Major' },
                { name: 'Support' }],

            rating: { name: 'A' },
            ratings: [{ name: 'A' },
                { name: 'B' },
                { name: 'C' },
                { name: 'D' },
                { name: 'F' }],

            id: -1,
        };
    },
    components: {
        dropdown: Dropdown,
    },
    methods: {
        render() {
            this.id = this.$route.params.id;
            this.getProfessor();
            this.getReleventCourses();
        },
        setCourse(payload) {
            this.course = payload;
        },
        getProfessor() {
            const path = `http://localhost:5000/professor?id=${this.id}`;
            axios.get(path)
                .then((res) => {
                    this.professor = res.data;
                    document.title = `${this.professor[1]} ${this.professor[2]} - evaluate`;
                })
                .catch((error) => {
                    this.professor = error;
                });
        },
        getReleventCourses() {
            const path = `http://localhost:5000/courses?id=${this.id}`;
            axios.get(path)
                .then((res) => {
                    this.courses = res.data;
                    this.$refs.courses.setOption({ name: res.data[0] || 'AERO' });
                    this.getCourseList();
                })
                .catch((error) => {
                    this.courses = error;
                });
        },
        getCourseList() {
            const path = 'http://localhost:5000/courses';
            axios.get(path)
                .then((res) => {
                    const newCourses = res.data;
                    newCourses.filter((course) => {
                        if (!this.courses.includes(course)) {
                            this.courses.push(course);
                        }
                        return null;
                    });
                    this.courses = this.courses.map(c => ({ name: c }));
                })
                .catch((error) => {
                    this.courses = error;
                });
        },
        updateRating(rating) {
            this.rating = rating;
        },
        updateCourse(course) {
            this.course = course;
        },
        updateGrade(grade) {
            this.grade = grade;
        },
        updateYear(year) {
            this.year = year;
        },
        updateFufillment(fufillment) {
            this.fufillment = fufillment;
        },
        submitReview() {
            const path = 'http://localhost:5000/reviews';
            const bodyFormData = new FormData();

            bodyFormData.set('grade', this.grade.name);
            bodyFormData.set('year', this.year.name);
            bodyFormData.set('requirement', this.fufillment.name);
            bodyFormData.set('rating', this.rating.name);
            bodyFormData.set('review', this.review);
            bodyFormData.set('profId', this.id);
            bodyFormData.set('num', this.courseNum);
            bodyFormData.set('department', this.course.name);

            axios.post(path, bodyFormData)
                .then((res) => {
                    this.result = res;
                    this.$router.go(-1);
                })
                .catch((error) => {
                    this.error = error;
                });
        },
    },
    activated() {
        this.render();
    },
    created() {
        // this.render();
    },
};
</script>

<style scoped>

input:focus{
    outline: none;
}

.add-professor {
    text-align: left;
    margin-top: 20px;
}

.name {
    width: calc(100% - 50px);
    font-family: 'Helvetica';
    font-size: 22px;
    margin: 0.8rem;
    padding: 0 10px;
    height: 2.35em;
    border: none;
    background: #ffffff;
    filter: drop-shadow(0 3px 2px #b9b9b9);
    border-radius: 4px;
}

.prof-dep {
    width: calc(100% - 30px);
    z-index: 10;
    margin-left: 0.6em;
    margin-bottom: 1rem;
    background: white;
    font-size: 22px;
    border-radius: 4px;
    filter: drop-shadow(0 3px 2px #b9b9b9);
    border: none;
    background-image: none;
}

textarea {
    width: calc(100% - 0.4rem);
    height: 20rem;
    margin-top: 14px;
    font-family: 'Helvetica';
    font-size: 26px;
    border: 1px #AAAAAA solid;
    border-radius: 4px;
    resize: none;
}

button {
    margin-top: 1rem;
    text-align: left;
    display: inline;
    padding: 20px 10px;
    font-family: Montserrat ExtraBold;
    font-size: 22px;
    color: #2c3e50;
    background: #EEEEEE;
    border: none;
    border-radius: 2px;
}

button:hover {
    background: #DDDDDD;
    cursor: pointer;
}

button:focus {
    outline: none;
}

textarea:focus {
    outline: none;
    border: 1px green solid;
}

h4 {
    max-width: 100vw;
    margin: 0.3rem;
    margin-top: 0.5rem;
    text-align: left;
    font-size: 1.9rem;
}

h5 {
    margin: 0;
    padding: 0;
    font-size: 18pt;
    text-align: left;
}

.info > div {
    height: 100px;
    margin-bottom: 1.2rem
}

.evaluate {
    max-width: 600px;
    margin: 0 auto;
}

.form {
    margin-bottom: 80px;
    display: grid;
    grid-template-areas:
    'info'
    'review';
}

.info {
    display: grid;
    margin: 0.3rem;

    grid-template-areas:
    'course-select'
    'grade-select'
    'year-select'
    'req-select';

    padding: 10px 10px;
    border-top: 4px #2c3e50 solid;

    text-align: left;
    background: white;
    border-radius: 2px;
    filter: drop-shadow(0 3px 2px #b9b9b9);
    font-size: 22px;
}

.review {
    margin: 0.3rem;
    border-top: 4px #2c3e50 solid;
    text-align: left;
    padding: 10px 10px;
    background: white;
    border-radius: 2px;
    filter: drop-shadow(0 3px 2px #b9b9b9);
    font-size: 22px;
}

.dropdown {
    padding-top: 5px;
    padding-bottom: 6px;
    border-bottom: 1px lightgrey solid;
}

.course-num {
    position: relative;
    width: 80px;
    color: #2c3e50;
    font-family: Montserrat;
    padding-bottom: 9px;
    top: 4px;
    left: 30px;
    font-size: 24px;
    border-style: none;
    border-bottom: 1px lightgrey solid;
}

.help {
    font-size: 14px;
    text-align: left;
}

.grade-select {
    position: relative;
    margin-left: 0;
    padding-left: 0;
}

@media (min-width:800px) {

    h4 {
        margin-top: 2rem;
    }

    textarea {
        height: 28rem;
    }

    .add-professor {
        max-width: 1200px;
    }

    .name {
        width: 30%;
    }

    .prof-dep {
        width: 20%;
    }

    .evaluate {
        max-width: 1200px;
    }

    .form {
        margin-top: 1rem;
        grid-template-areas:
        'info review';
    }

    .info {
    }

    .review {
    }
}

</style>
