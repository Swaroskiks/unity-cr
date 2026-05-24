<script setup>
import { ref, onMounted, watch } from 'vue';
const emit = defineEmits(['file-change']);
const props = defineProps(['fileDataUrl']);
const isSaving = ref(false);
const fileReader = new FileReader();
const fileInput = ref(null);
const file = ref(null);
const fileDataUrl = ref('');

watch(
  () => props.fileDataUrl,
  (newValue, oldValue) => {
    // console.log('image data from props', newValue.substr(0, 30));
    if (newValue !== oldValue) {
      fileDataUrl.value = newValue;
    }
  }
);

onMounted(() => {
  fileReader.addEventListener(
    'load',
    () => {
      // fileReader holds a b64 string of the image
      fileDataUrl.value = fileReader.result;
      isSaving.value = false;
      emit('file-change', fileDataUrl.value);
    },
    false
  );
});
function fileChange(event) {
  isSaving.value = true;
  const input = event.target;
  // pick the first file uploaded
  file.value = input.files[0];
  // set the file into the file reader
  // (next step is in the load eventListener defined in onMounted)
  fileReader.readAsDataURL(file.value);
}
function clickRemoveImageHandler() {
  file.value = null;
  emit('file-change', '');
  if (fileInput.value) {
    fileInput.value.value = '';
  }
}
</script>

<template>
  <input
    tabindex="-1"
    type="file"
    name="uploadInput"
    :disabled="isSaving"
    @change="fileChange"
    accept="image/jpeg, image/png, image/gif"
    class="input-file"
    ref="fileInput"
  />
  <a class="remove-link" href="#" v-if="fileDataUrl" @click="clickRemoveImageHandler"
    >Supprimer l'image</a
  >
</template>

<style scoped>
.input-file {
  display: block;
  width: 100%;
  padding: 0.75rem;
  border: 2px solid rgba(102, 126, 234, 0.2);
  border-radius: 8px;
  font-size: 0.95rem;
  transition: all 0.3s ease;
  background: white;
  cursor: pointer;
}

.input-file:hover:not(:disabled) {
  border-color: #667eea;
}

.input-file:disabled {
  background: #f3f4f6;
  cursor: not-allowed;
  opacity: 0.6;
}

.remove-link {
  display: block;
  margin-top: 0.5rem;
  color: #ef4444;
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 500;
  transition: color 0.3s ease;
}

.remove-link:hover {
  color: #dc2626;
  text-decoration: underline;
}
</style>
