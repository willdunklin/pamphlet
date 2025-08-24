<script setup>
import { ref, onMounted } from 'vue'
import JSZip from 'jszip'

const unzipped = ref()
const fileName = ref()

function downloadFile() {
  if(!unzipped.value) return console.log('file not yet unzipped')

  const blob = new Blob([unzipped.value], { type: 'application/pdf' })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = fileName.value
  document.body.appendChild(a)
  a.click()
  document.body.removeChild(a)
  URL.revokeObjectURL(url)
}


// http://localhost:5173/?title=twote.zip&key=unlocked
async function init() {
  const url = new URL(window.location.href)
  const params = new URLSearchParams(url.search)
  console.log('url', params)

  const title = params.get('title')
  const key = params.get('key')
  if (!/^.nl..k..$/.test(key)) return

  const file = await fetch(`/zips/${title}`)
  console.log('file', file)
  const data = await file.blob()
  console.log('data', data)

  const unzip = await JSZip.loadAsync(await data.bytes())
  console.log('unzip', unzip)

  for (const title of Object.keys(unzip.files)) {
    if (/__MACOSX/.test(title)) continue

    const file = unzip.file(title)
    console.log('unzipfile', file, title)
    const data = await file.async('uint8array')
    console.log('unzipdata', data)
    fileName.value = title
    unzipped.value = data
  }
  // downloadFile()
}

onMounted(init)
</script>

<template>
  <div>
    <button @click="downloadFile">Download</button>
  </div>
</template>

<style scoped>
</style>
