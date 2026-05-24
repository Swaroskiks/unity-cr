<template>
  <div class="demo-view">
    <h2 class="glitch" data-text="DÉMO PROJET">DÉMO PROJET</h2>
    <p class="subtitle">> Lancement de la séquence de démonstration...</p>

    <div class="video-container">
      <div class="video-frame">
        <div class="scanlines"></div>
        <video 
          ref="videoPlayer" 
          controls 
          class="cyber-video"
          @loadedmetadata="checkSource"
          @play="checkSource"
        >
          <source :src="'/video/demo.mp4'" type="video/mp4" />
          <source :src="'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4'" type="video/mp4" />
          Votre navigateur ne supporte pas la lecture de vidéos.
        </video>
      </div>

      <!-- Info/Alert box when fallback is active -->
      <Transition name="fade">
        <div v-if="isFallback" class="info-box">
          <div class="info-tag">SYSTEM NOTICE</div>
          <p>
            Vous visionnez la vidéo d'exemple par défaut. Pour utiliser la vidéo de votre projet, placez votre fichier MP4 sous :
          </p>
          <code>unity-ui/public/video/demo.mp4</code>
        </div>
      </Transition>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const videoPlayer = ref<HTMLVideoElement | null>(null);
const isFallback = ref(false);

const checkSource = () => {
  if (videoPlayer.value) {
    // If the browser loaded the fallback URL, set isFallback to true
    if (videoPlayer.value.currentSrc.includes('BigBuckBunny')) {
      isFallback.value = true;
    }
  }
};
</script>

<style scoped>
.demo-view {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
  padding: 1rem 0;
  max-width: 1000px;
  margin: 0 auto;
}

.demo-view h2 {
  font-size: 3rem;
  color: var(--color-primary);
  margin: 0;
  text-align: center;
}

.subtitle {
  color: #666;
  font-family: monospace;
  font-size: 1rem;
  margin: 0;
}

.video-container {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 2rem;
  margin-top: 1rem;
}

.video-frame {
  position: relative;
  width: 100%;
  aspect-ratio: 16/9;
  background-color: #000;
  border: 2px solid var(--color-primary);
  box-shadow: 0 0 20px rgba(204, 255, 0, 0.2);
  overflow: hidden;
}

.video-frame::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  box-shadow: inset 0 0 40px rgba(0, 255, 255, 0.1);
  pointer-events: none;
  z-index: 2;
}

.scanlines {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    rgba(18, 16, 16, 0) 50%, 
    rgba(0, 0, 0, 0.25) 50%
  );
  background-size: 100% 4px;
  z-index: 3;
  pointer-events: none;
}

.cyber-video {
  width: 100%;
  height: 100%;
  object-fit: contain;
  display: block;
}

/* Info Box */
.info-box {
  background-color: rgba(255, 0, 255, 0.05);
  border: 1px solid var(--color-secondary);
  box-shadow: 0 0 10px rgba(255, 0, 255, 0.1);
  padding: 1.5rem;
  color: #ddd;
  font-family: monospace;
  position: relative;
}

.info-tag {
  position: absolute;
  top: -10px;
  left: 15px;
  background-color: var(--color-secondary);
  color: #000;
  font-size: 0.75rem;
  font-weight: bold;
  padding: 2px 8px;
  text-transform: uppercase;
}

.info-box p {
  margin: 0 0 1rem 0;
  font-size: 0.95rem;
  line-height: 1.5;
}

.info-box code {
  display: block;
  background-color: #000;
  border: 1px solid #333;
  padding: 0.6rem 1rem;
  color: var(--color-accent);
  font-size: 0.9rem;
}

/* Transitions */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
