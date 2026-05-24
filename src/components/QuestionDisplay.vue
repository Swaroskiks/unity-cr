<script setup>
const props = defineProps({
  currentQuestion: Object,
  selectedAnswerIndex: {
    type: Number,
    default: null
  }
});

const emit = defineEmits(['answer-selected']);

function selectAnswer(answerIndex) {
  emit('answer-selected', answerIndex);
}
</script>

<template>
  <div class="question-display" v-if="currentQuestion">
    <h2 class="question-title">{{ currentQuestion.title }}</h2>
    
    <div class="question-text" v-if="currentQuestion.description || currentQuestion.text">
      {{ currentQuestion.description || currentQuestion.text }}
    </div>
    
    <img 
      v-if="currentQuestion.image" 
      :src="currentQuestion.image" 
      alt="Question image"
      class="question-image"
    />
    
    <div class="answers-list" v-if="currentQuestion.possibleAnswers || currentQuestion.answers">
      <button
        v-for="(answer, index) in (currentQuestion.possibleAnswers || currentQuestion.answers)"
        :key="index"
        @click="selectAnswer(index + 1)"
        class="answer-button"
        :class="{ 
          'answer-selected': selectedAnswerIndex === index + 1,
          'answer-pulse': selectedAnswerIndex === index + 1
        }"
        :disabled="selectedAnswerIndex !== null"
      >
        {{ answer.text || answer.answer_text }}
      </button>
    </div>
  </div>
</template>

<style scoped>
.question-display {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem 1rem;
  background: rgba(255, 255, 255, 0.8);
  border-radius: 20px;
  box-shadow: 0 8px 32px rgba(102, 126, 234, 0.1);
  backdrop-filter: blur(10px);
}

.question-title {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-size: 1.75rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  line-height: 1.4;
}

.question-text {
  color: #374151;
  font-size: 1.1rem;
  margin-bottom: 1.5rem;
  line-height: 1.6;
}

.question-image {
  max-width: 550px;
  max-height: 300px;
  width: auto;
  height: auto;
  object-fit: contain;
  border-radius: 12px;
  margin-bottom: 2rem;
  box-shadow: 0 4px 16px rgba(102, 126, 234, 0.15);
  display: block;
  margin-left: auto;
  margin-right: auto;
}

.answers-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.answer-button {
  width: 100%;
  padding: 1rem 1.5rem;
  font-size: 1rem;
  text-align: left;
  background: rgba(255, 255, 255, 0.9);
  border: 2px solid rgba(102, 126, 234, 0.2);
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  color: #1a1a1a;
  box-shadow: 0 2px 8px rgba(102, 126, 234, 0.1);
}

.answer-button:hover {
  border-color: #667eea;
  background: rgba(248, 249, 255, 0.95);
  transform: translateX(4px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.2);
}

.answer-button:active {
  transform: translateX(2px);
  box-shadow: 0 2px 6px rgba(102, 126, 234, 0.15);
}

.answer-button:disabled {
  cursor: not-allowed;
  opacity: 0.7;
}

.answer-selected {
  border-color: #667eea !important;
  background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%) !important;
  transform: translateX(4px) scale(1.02);
  box-shadow: 0 6px 20px rgba(102, 126, 234, 0.3) !important;
}

.answer-pulse {
  animation: pulse 0.5s ease-out;
}

@keyframes pulse {
  0% {
    transform: translateX(4px) scale(1.02);
  }
  50% {
    transform: translateX(4px) scale(1.05);
  }
  100% {
    transform: translateX(4px) scale(1.02);
  }
}
</style>

