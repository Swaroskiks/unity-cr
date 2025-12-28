<script setup>
defineProps({
  message: {
    type: String,
    default: 'Une erreur est survenue'
  },
  retry: {
    type: Function,
    default: null
  }
});
</script>

<template>
  <div class="error-container">
    <div class="error-icon">⚠️</div>
    <h3 class="error-title">Oups !</h3>
    <p class="error-message">{{ message }}</p>
    <button v-if="retry" @click="retry" class="retry-button">
      Réessayer
    </button>
  </div>
</template>

<style scoped>
.error-container {
  text-align: center;
  padding: 3rem 2rem;
  background: rgba(255, 255, 255, 0.8);
  border-radius: 20px;
  box-shadow: 0 8px 32px rgba(102, 126, 234, 0.1);
  backdrop-filter: blur(10px);
  border: 2px solid rgba(239, 68, 68, 0.2);
}

.error-icon {
  font-size: 4rem;
  margin-bottom: 1rem;
  animation: shake 0.5s ease-in-out;
}

@keyframes shake {
  0%, 100% { transform: translateX(0); }
  25% { transform: translateX(-10px); }
  75% { transform: translateX(10px); }
}

.error-title {
  background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
}

.error-message {
  color: #6b7280;
  font-size: 1rem;
  margin-bottom: 1.5rem;
  line-height: 1.6;
}

.retry-button {
  padding: 0.75rem 2rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 12px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 14px rgba(102, 126, 234, 0.4);
}

.retry-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(102, 126, 234, 0.5);
}

.retry-button:active {
  transform: translateY(0);
}
</style>

