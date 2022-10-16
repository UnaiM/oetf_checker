const audio = document.getElementById('audio')
const props = new Set()
const test = document.getElementById('test')
const viewport = document.getElementById('viewport')
let enabled = true
let slide = 0

document.getElementById('play').addEventListener('click', () => {
  test.pause()
  test.play()
})

document.getElementById('begin').addEventListener('click', () => {
  change('viewport.style.visibility', 'visible')
  viewport.requestPointerLock()
  viewport.requestFullscreen()
  enabled = false
  // This ensures that the 'press Esc to exit fullscreen' popup is gone.
  window.setTimeout(() => {
    enabled = true
  }, 5000)
  incr()
})

viewport.addEventListener('fullscreenchange', () => {
  if (! document.fullscreenElement) {
    audio.pause()
    props.forEach(p => {
      eval(`${p} = null`)
    })
    slide = 0
  }
})

viewport.addEventListener('click', next)

function change(prop, value) {
  eval(`${prop} = ${JSON.stringify(value)}`)
  props.add(prop)
}

function incr() {
  slide ++
  audio.pause()
  audio.src = `audio/slide${slide}.mp3`
  audio.load()
  audio.addEventListener('loadeddata', () => {
    audio.play()
  })
}

function next() {
  if (enabled) {
    switch (slide) {
      case 1:
        change('viewport.style.backgroundImage', 'url(images/clip_check.gif)')
        incr()
        break;
      case 2:
        change('viewport.style.backgroundImage', 'url(images/focus_check.gif)')
        incr()
        break;
      case 3:
        change('viewport.style.backgroundImage', 'url(images/clip_check.gif)')
        incr()
        break;
      case 4:
        change('viewport.style.backgroundImage', 'url(images/dither_sequence.gif)')
        incr()
        break;
      case 5:
        document.exitFullscreen()
    }
  }
}
