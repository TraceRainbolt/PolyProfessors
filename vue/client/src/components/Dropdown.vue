<template>
    <div class="btn-group">
        <li @click="toggleMenu()" class="dropdown-toggle"
            v-if="selectedOption.name !== undefined">
          {{ selectedOption.name }}
          <span class="caret"></span>
      </li>

      <li @click="toggleMenu()" class="dropdown-toggle"
      v-if="selectedOption.name === undefined">
          {{placeholderText}}
          <span class="caret"></span>
      </li>

      <ul class="dropdown-menu" v-if="showMenu">
        <li v-for="option in options" v-bind:key="option.name">
            <a href="javascript:void(0)" @click="updateOption(option)">
                {{ option.name }}
            </a>
        </li>
    </ul>
</div>
</template>

<script>
export default {
    data() {
        return {
            selectedOption: {
                name: '',
            },
            showMenu: false,
            placeholderText: '',
        };
    },
    props: {
        options: {
            type: [Array, Object],
        },
        selected: {},
        placeholder: [String],
    },
    mounted() {
        this.selectedOption = this.selected;
        if (this.placeholder) {
            this.placeholderText = this.placeholder;
        }
    },
    methods: {
        updateOption(option) {
            this.selectedOption = option;
            this.showMenu = false;
            this.$emit('updateOption', this.selectedOption);
        },
        setOption(option) {
            this.selectedOption = option;
        },
        toggleMenu() {
            this.showMenu = !this.showMenu;
        },
    },
};
</script>

<style>

.btn-group {
  height: 40px;
  position: relative;
  margin: 10px 1px;
  display: inline-block;
  vertical-align: middle;
}

.btn-group a:hover {
  text-decoration: none;
}

.dropdown-toggle {
  padding: 10px;
  text-transform: none;
  font-family: 'Helvetica';

  font-weight: 300;
  margin-bottom: 7px;
  border: 0;

  background: transparent;
  transition: background 0s ease-out;
  float: none;
  box-shadow: none;
  border-radius: 0;
}
.dropdown-toggle:hover {
  border-radius: 4px;
  background: #F0F0F0;
  cursor: pointer;
}

.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  float: left;
  padding: 5px 0;
  margin: 2px 0 0;
  font-family: 'Helvetica';
  background: white;

  list-style: none;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  background-clip: padding-box;
  max-height: 200px;
  overflow-y: scroll;
}

.dropdown-menu > li > a {
  padding: 10px 40px 10px 20px;
  display: block;
  clear: both;
  font-weight: normal;
  line-height: 1.6;
  color: #333333;
  white-space: nowrap;
  text-decoration: none;
}

.dropdown-menu > li > a:hover {
  background: #efefef;
  color: green;
}

.dropdown-menu > li {
  overflow: hidden;
  width: 100%;
  position: relative;
  margin: 0;
}

.caret {
  display: relative;
  width: 0;
  position: relative;
  top: 10px;
  height: 0;
  margin-left: 2px;
  vertical-align: middle;
  border-top: 4px dashed;
  border-top: 4px solid 9;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
  float: right;
}

li {
    list-style: none;
}
</style>
