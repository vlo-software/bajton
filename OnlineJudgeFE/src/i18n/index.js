import Vue from 'vue'
import VueI18n from 'vue-i18n'
// ivew UI
import ivenUS from 'iview/dist/locale/en-US'
// element UI
import elenUS from 'element-ui/lib/locale/lang/en'
import elplPL from 'element-ui/lib/locale/lang/pl'

Vue.use(VueI18n)

const languages = [
  {value: 'pl-PL', label: 'Polski', iv: ivenUS, el: elplPL},
  {value: 'en-US', label: 'English', iv: ivenUS, el: elenUS}
]
const messages = {}

// combine admin and oj
for (let lang of languages) {
  let locale = lang.value
  let m = require(`./oj/${locale}`).m
  Object.assign(m, require(`./admin/${locale}`).m)
  Object.assign(m, require(`./next/${locale}`).m)
  let ui = Object.assign(lang.iv, lang.el)
  messages[locale] = Object.assign({m: m}, ui)
}
// load language packages
export default new VueI18n({
  locale: 'pl-PL',
  messages: messages
})

export {languages}
