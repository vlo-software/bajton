<template>
  <div>
    <Header />
    <div v-if="error" class="error">Problem not found!</div>
    <div v-else-if="loading" class="loading">loading ...</div>
    <div v-else class="layout">
      <div v-for="post in posts" v-bind:key="post.id">
        <Post
          :content="post.content"
          :createdAt="post.created_at"
          :edited="post.edited"
          :author="post.author.username"
          :onReply="() => {}"
        />
        <div v-for="comment in post.comments" v-bind:key="comment.id">
          <div class="comment-spacer">
            <div></div>
          </div>
          <Post
            :content="comment.content"
            :createdAt="comment.created_at"
            :edited="comment.edited"
            :author="comment.author.username"
          />
        </div>
        <div class="spacer"></div>
      </div>
    </div>
  </div>
</template>

<script>
import Header from '@oj/next/components/Header.vue'
import Post from '@oj/next/components/Post.vue'
import api from '@oj/api'

export default {
  name: 'landing-problem',
  components: { Header, Post },
  data () {
    return {
      problemName: '',
      problemId: this.$route.params.problemId,
      posts: [],
      loading: true,
      error: false
    }
  },
  methods: {
    loadPosts () {
      api
        .getPosts(this.problemId)
        .then((res) => {
          this.posts = res.data.data
          this.loading = false
        })
        .catch(() => {
          this.error = true // This will happen whenever the problem doesn't exist
        })
    }
  },
  mounted () {
    this.loadPosts() // Checks if problem exists and loads its posts
  }
}
</script>

<style lang="less" scoped>
.layout {
  width: 66.6vw;
  margin-left: calc(33.3vw / 2);
  min-height: calc(100vh - 120px);
  margin-top: 20px;
  @media (max-width: 1024px) {
    width: calc(100vw - 40px);
    margin-left: 20px;
  }
}

.comment-spacer {
  height: 15px;
  width: 100%;
  display: flex;
  justify-content: center;
  div {
    height: 100%;
    width: 5px;
    background: #c4c4c4;
  }
}

.spacer {
  height: 60px;
  width: 100%;
}
</style>
