<script setup>
import { computed } from 'vue';

const props = defineProps({
  playerName: {
    type: String,
    required: true
  },
  score: {
    type: Number,
    required: true
  },
  rank: {
    type: Number,
    default: null
  },
  highlight: {
    type: Boolean,
    default: false
  }
});

const rankClass = computed(() => {
  if (props.rank === 1) return 'rank-first';
  if (props.rank === 2) return 'rank-second';
  if (props.rank === 3) return 'rank-third';
  return '';
});
</script>

<template>
  <div 
    class="score-card" 
    :class="{ 
      'score-card-highlight': highlight,
      'score-card-first': rank === 1,
      'score-card-second': rank === 2,
      'score-card-third': rank === 3
    }"
  >
    <div class="rank" :class="rankClass" v-if="rank !== null">{{ rank }}</div>
    <div class="player-info">
      <div class="player-name">{{ playerName }}</div>
      <div class="score">{{ score }} points</div>
    </div>
  </div>
</template>

<style scoped>
.score-card {
  display: flex;
  align-items: center;
  padding: 1.25rem 1.5rem;
  background: #ffffff;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  transition: all 0.2s ease;
}

.score-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transform: translateY(-2px);
}

.score-card-highlight {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
}

.score-card-first {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
}

.score-card-second {
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  color: white;
  border: none;
}

.score-card-third {
  background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
  color: white;
  border: none;
}

.score-card-highlight .rank,
.score-card-first .rank,
.score-card-second .rank,
.score-card-third .rank {
  background: rgba(255, 255, 255, 0.2);
  color: white;
}

.rank {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  background: #f3f4f6;
  border-radius: 10px;
  font-weight: 700;
  font-size: 1.1rem;
  color: #6b7280;
  margin-right: 1rem;
  flex-shrink: 0;
}

.player-info {
  flex: 1;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.player-name {
  font-weight: 600;
  font-size: 1.1rem;
  color: inherit;
}

.score {
  font-weight: 500;
  font-size: 0.95rem;
  color: inherit;
  opacity: 0.9;
}
</style>

