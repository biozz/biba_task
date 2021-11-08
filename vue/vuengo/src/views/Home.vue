<template>
  <div class="home">
    <h1 class="title">biba</h1>

    <hr>
    <div class="columns">
      <div class="column is-3 is-offset-3">
        <form v-on:submit.prevent="addTask">
        <h2 class="subtitle">add task</h2>

        <div class="field">
          <label class="label">Description</label>
            <div class="control">
              <input class="input" type="text" v-model="description">
            </div>
        </div>
          <div class="field">
          <label class="lebel">Status</label>
            <div class="control">
              <div class="select">
                <select v-model="status">
                <option value="todo">to do</option>
                <option value="done">done</option>
                </select>
              </div>
            </div>
              <button type="submit" class="button is-link my-3">Submit</button>
          </div>
        </form>
      </div>
    </div>
    <div class="columns">
      <div class="column is-6">
        <h2 class="subtitle">to do</h2>
        <div class="todo">
          <div
            class="card"
            v-for="task in getTodoSatus"
            :key="task.id"
          >
            <div class="card-content">{{ task.description }}</div>
            <hr>
            <footer class="card-foter">
              <a
                class="card-footer-item"
                @click="setStatus(task.id, 'done')"
              >Done</a>
            </footer>
          </div>
        </div>
      </div>
      <div class="column is-6">
        <h2 class="subtitle">done</h2>
        <div class="done">
          <div
            class="card"
            v-for="task in getDoneSatus"
            :key="task.id"
          >
            <div class="card-content">{{ task.description }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  name: 'Home',
  data () {
    return {
      tasks: [],
      description: '',
      status: ''
    }
  },
  mounted () {
    this.getTasks()
    // this.getStatus()
  },
  methods: {
    getTasks () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/to-do'
      }).then(response => { this.tasks = response.data })
    },
    addTask () {
      if (this.description) {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/api/to-do',
          data: {
            description: this.description,
            status: this.status
          }
        }).then((response) => {
          const newTask = {
            id: response.data.id,
            description: this.description,
            status: this.status
          }

          this.tasks.push(newTask)

          this.description = ''
          this.status = ''
        }).catch((error) => {
          console.log(error)
        })
      }
    },
    setStatus (taskId, status) {
      const task = this.tasks.filter(task => task.id === taskId)[0]
      const description = task.description
      axios({
        method: 'put',
        url: 'http://127.0.0.1:8000/api/to-do/' + taskId,
        data: {
          status: status,
          description: description
        }
      }).then(() => {
        task.status = status
      }).catch((error) => {
        console.log(error)
      })
    }
  },
  computed: {
    getTodoSatus: function () {
      return this.tasks.filter(function (task) {
        return task.status === 'todo'
      })
    },
    getDoneSatus: function () {
      return this.tasks.filter(function (task) {
        return task.status === 'done'
      })
    }
  }
}
</script>

<style lang="scss">
.select, select {
  width: 100%;
}

.card {
  margin-bottom: 20px;
}

.done {
  opacity: 0.3;
}
</style>
