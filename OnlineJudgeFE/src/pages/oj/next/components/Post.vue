<template>
  <div class="main">
    <div class="header">
      <div class="user">
        <img :src="this.avatar" alt="avatar" class="avatar" />
        <div class="name">
          {{ `${this.username}${this.school ? ' | ' + this.school : ''}` }}
        </div>
      </div>
      <div class="date">
        <i class="bi bi-calendar3"></i>
        <div class="text">{{ creationDate }}</div>
      </div>
    </div>
    <div class="content">
      <span v-html="markdownHtml"></span>
    </div>
    <div class="footer">
      <div v-if="onReply">
        <i class="bi bi-reply"></i>
        <button @click="onReply">Odpowiedz</button>
      </div>
    </div>
  </div>
</template>

<script>
import { marked } from 'marked'
import DOMPurify from 'dompurify'
import api from '@oj/api'

export default {
  name: 'forum-post',
  props: {
    content: String,
    createdAt: String,
    author: String,
    onReply: Function
  },
  data () {
    return {
      username: '',
      school: null,
      avatar: ''
    }
  },
  methods: {
    loadProfile () {
      api.getUserInfo(this.author).then((res) => {
        const profile = res.data.data
        this.username = profile.user.real_name || profile.user.username
        this.school = profile.school
        this.avatar = profile.avatar
      })
    }
  },
  mounted () {
    marked.setOptions({
      renderer: new marked.Renderer(),
      highlight: function (code, lang) {
        const hljs = require('highlight.js')
        const language = hljs.getLanguage(lang) ? lang : 'plaintext'
        return hljs.highlight(code, { language }).value
      },
      langPrefix: 'hljs language-', // highlight.js css expects a top-level 'hljs' class.
      pedantic: false,
      gfm: true,
      breaks: false,
      sanitize: false,
      smartLists: true,
      smartypants: false,
      xhtml: false
    })
    this.loadProfile() // Loads the username and the avatar
  },
  computed: {
    markdownHtml () {
      return marked(
        DOMPurify.sanitize(
          this.content,
          { USE_PROFILES: {} } // Doesn't allow mathMl, html nor svg
        )
      )
    },
    creationDate () {
      const date = new Date(this.createdAt)
      return date.toLocaleDateString('pl-PL', {
        // TODO: Make this language dependent
        month: 'long',
        day: 'numeric',
        year: 'numeric'
      })
    }
  }
}
</script>

<style lang="less" scoped>
.main {
  width: 100%;
  background: #f0f0f0;
  border-radius: 12px;
  font-family: 'Poppins', sans-serif;
  --secondary: #5f5f5f;
}

.header {
  height: 70px;
  width: 100%;
  display: flex;
  justify-content: space-between;
}

.user {
  height: 100%;
  display: flex;
  align-items: center;
}

.avatar {
  height: 42px;
  width: 42px;
  border-radius: 50%;
  margin-left: 15px;
}

.name {
  font-size: 18px;
  margin-left: 15px;
}

.date {
  display: flex;
  align-items: center;
  opacity: 0.8;
  i {
    font-size: 25px;
  }
  .text {
    font-size: 18px;
    margin-left: 15px;
    margin-right: 25px;
  }
}

.content {
  padding: 0px 30px;
}

.footer {
  width: 100%;
  min-height: 30px;
  margin-top: 20px;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  color: var(--secondary);
  div {
    display: flex;
    align-items: center;
    margin: 10px 25px;
  }
  i {
    font-size: 24px;
  }
  button {
    font-family: inherit;
    color: inherit;
    font-size: 14px;
    border: none;
    outline: none;
    background: transparent;
    transition: 0.2s ease;
    &:hover {
      text-shadow: 0px 0px 10px rgb(126, 126, 126);
    }
  }
}
</style>
