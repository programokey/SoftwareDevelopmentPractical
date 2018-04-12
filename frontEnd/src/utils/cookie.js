export const cookie = {
  /**
   * 设置cookie
   *
   * @param {any} key 标识
   * @param {any} val 值
   * @param {any} duration 有效时长（持续时长），单位ms
   */
  set: function (key, val, duration) {
    var date = new Date()
    date.setTime(date.getTime() + duration)
    var expires = 'expires=' + date.toGMTString()
    document.cookie = key + '=' + val + '; ' + expires
  },
  /**
   * 获取cookie
   *
   * @param {any} key
   * @returns {String} 如果key存在返回对应的值，否则返回''
   */
  get: function (key) {
    var mKey = key + '='
    var arrCookie = document.cookie.split(';') // 将cookie根据';'截取到数组中
    for (var i = 0; i < arrCookie.length; i++) {
      var itemCookie = arrCookie[i].trim()
      if (itemCookie.indexOf(mKey) === 0) return itemCookie.substring(mKey.length, itemCookie.length)
    }
    return ''
  }
}

/* export */
export default cookie