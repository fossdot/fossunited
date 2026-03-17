<template>
  <div v-if="event.data">
    <MerchInsightsSection :event="event" />
  </div>
</template>
<script setup>
import MerchInsightsSection from '@/components/event/MerchInsightsSection.vue'

const props = defineProps({
  event: { type: Object, required: true },
})
</script>
