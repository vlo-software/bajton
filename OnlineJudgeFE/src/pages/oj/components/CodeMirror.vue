<template>
  <div style="margin: 0px 0px 15px 0px; position: relative">
    <Grid justify="between" align="center" class="header">
      <div>
        <span>{{ $t('m.Language') }}:</span>
        <Select :value="language" @on-change="onLangChange" class="adjust">
          <Option v-for="item in languagesData" :key="item" :value="item"
            >{{ item }}
          </Option>
        </Select>

        <Tooltip
          :content="this.$i18n.t('m.Reset_to_default_code_definition')"
          placement="top"
          style="margin-left: 10px"
        >
          <Button icon="arrow-clockwise" @click="onResetClick"></Button>
        </Tooltip>

        <Tooltip
          :content="this.$i18n.t('m.Upload_file')"
          placement="top"
          style="margin-left: 10px"
        >
          <Button icon="upload" @click="onUploadFile"></Button>
        </Tooltip>

        <Tooltip
          :content="this.$i18n.t('m.Toggle_vim')"
          placement="top"
          style="margin-left: 10px"
        >
          <Button @click="onToggleVim" icon="keyboard">
            <!-- <img style="" height="20px" src="../../../assets/vim.svg"/> -->
          </Button>
        </Tooltip>

        <input
          type="file"
          id="file-uploader"
          style="display: none"
          @change="onUploadFileDone"
        />
      </div>
      <div>
        <div class="fl-right">
          <span>{{ $t('m.Theme') }}:</span>
          <Select :value="theme" @on-change="onThemeChange" class="adjust">
            <Option v-for="item in themes" :key="item.label" :value="item.value"
              >{{ item.label }}
            </Option>
          </Select>
        </div>
      </div>
    </Grid>
    <codemirror
      :value="value"
      :options="options"
      @change="onEditorCodeChange"
      ref="myEditor"
    >
    </codemirror>
  </div>
</template>
<script>
import utils from '@/utils/utils'
import { codemirror } from 'vue-codemirror-lite'
import { Card, Button, Select, Option, Tooltip, Grid } from '@oj/bajton-ui'

// theme
import 'codemirror/theme/monokai.css'
import 'codemirror/theme/solarized.css'
import 'codemirror/theme/material.css'

// mode
import 'codemirror/mode/clike/clike.js'
import 'codemirror/mode/python/python.js'
import 'codemirror/mode/go/go.js'
import 'codemirror/mode/javascript/javascript.js'
import 'codemirror/mode/perl/perl.js'
import 'codemirror/mode/brainfuck/brainfuck.js'

// active-line.js
import 'codemirror/addon/selection/active-line.js'

// foldGutter
import 'codemirror/addon/fold/foldgutter.css'
import 'codemirror/addon/fold/foldgutter.js'
import 'codemirror/addon/fold/brace-fold.js'
import 'codemirror/addon/fold/indent-fold.js'

// keymaps
import 'codemirror/keymap/vim.js'
import 'codemirror/keymap/sublime.js'

export default {
  name: 'CodeMirror',
  components: {
    codemirror,
    Card,
    Button,
    Select,
    Option,
    Tooltip,
    Grid
  },
  props: {
    value: {
      type: String,
      default: ''
    },
    languages: {
      type: Array,
      default: () => {
        return ['C', 'C++', 'Java']
      }
    },
    language: {
      type: String,
      default: 'Python3'
    },
    theme: {
      type: String,
      default: 'material'
    }
  },
  data () {
    return {
      options: {
        // codemirror options
        tabSize: 4,
        mode: 'text/x-csrc',
        theme: 'material',
        keyMap: 'sublime',
        lineNumbers: true,
        line: true,
        // 代码折叠
        foldGutter: true,
        gutters: ['CodeMirror-linenumbers', 'CodeMirror-foldgutter'],
        // 选中文本自动高亮，及高亮方式
        styleSelectedText: true,
        lineWrapping: true,
        highlightSelectionMatches: { showToken: /\w/, annotateScrollbar: true }
      },
      mode: {
        Python3: 'text/x-csrc'
      },
      languagesData: [],
      themes: [
        { label: this.$i18n.t('m.Monokai'), value: 'monokai' },
        { label: this.$i18n.t('m.Solarized_Light'), value: 'solarized' },
        { label: this.$i18n.t('m.Material'), value: 'material' }
      ]
    }
  },
  mounted () {
    utils.getLanguages().then((languages) => {
      let mode = {}
      languages.forEach((lang) => {
        mode[lang.name] = lang.content_type
      })
      this.mode = mode
      this.editor.setOption('mode', this.mode[this.language])
    })
    this.editor.focus()
  },
  methods: {
    onEditorCodeChange (newCode) {
      this.$emit('update:value', newCode)
    },
    onLangChange (newVal) {
      if (newVal.toLowerCase() === 'brainf**k') newVal = 'BrainFuck'
      this.editor.setOption('mode', this.mode[newVal])
      this.$emit('changeLang', newVal)
    },
    onThemeChange (newTheme) {
      this.editor.setOption('theme', newTheme)
      this.$emit('changeTheme', newTheme)
    },
    onResetClick () {
      this.$emit('resetCode')
    },
    onUploadFile () {
      document.getElementById('file-uploader').click()
    },
    onToggleVim () {
      const prevKeyMap = this.editor.options.keyMap
      const newKeyMap = prevKeyMap === 'vim' ? 'sublime' : 'vim'
      if (newKeyMap === 'vim') {
        this.$Modal.confirm({
          content: this.$i18n.t('m.Are_you_sure_you_want_to_enable_vim'),
          onOk: () => {
            this.editor.setOption('keyMap', newKeyMap)
            this.$success(this.$i18n.t('m.Vim_enabled'))
          }
        })
      } else {
        this.editor.setOption('keyMap', newKeyMap)
        this.$success(this.$i18n.t('m.Sublime_enabled'))
      }
    },
    onUploadFileDone () {
      let f = document.getElementById('file-uploader').files[0]
      let fileReader = new window.FileReader()
      let self = this
      fileReader.onload = function (e) {
        var text = e.target.result
        self.editor.setValue(text)
        document.getElementById('file-uploader').value = ''
      }
      fileReader.readAsText(f, 'UTF-8')
    }
  },
  computed: {
    editor () {
      // get current editor object
      return this.$refs.myEditor.editor
    }
  },
  watch: {
    theme (newVal, oldVal) {
      this.editor.setOption('theme', newVal)
    },
    languages (newVal, oldVal) {
      this.languagesData = newVal
        .map((lang) =>
          lang.toLowerCase() === 'brainfuck' ? 'BrainF**k' : lang
        )
        .sort((a, b) =>
          a === 'C++' || a === 'C' || a === 'Python3' ? -1 : a.localeCompare(b)
        )
      this.onLangChange(this.languagesData[0])
    }
  }
}
</script>

<style lang="less" scoped>
.header {
  margin: 5px 5px 15px 5px;
  .adjust {
    width: 150px;
    margin-left: 10px;
  }
  .fl-right {
    float: right;
  }
}
</style>

<style>
.CodeMirror {
  height: auto !important;
  border-radius: 8px !important;
}
.cm-s-monokai.CodeMirror {
  background-color: rgb(25, 22, 34) !important;
}
.cm-s-monokai.CodeMirror .CodeMirror-gutters {
  background-color: rgb(25, 22, 34) !important;
}
.cm-s-material.CodeMirror {
  background-color: #272a31 !important;
}
.cm-s-material.CodeMirror .CodeMirror-gutters {
  background-color: #272a31 !important;
}
.cm-s-solarized.CodeMirror {
  box-shadow: none !important;
}
.cm-s-solarized.CodeMirror .CodeMirror-gutters {
  background-color: white !important;
}
.CodeMirror-scroll {
  min-height: 300px;
  max-height: 1000px;
}
pre.CodeMirror-line {
  word-break: break-all !important;
}
</style>
