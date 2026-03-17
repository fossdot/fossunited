<template>
  <div v-if="event.data" class="flex flex-col gap-6">
    <MerchSection :event="event" />
    <MerchDeliverySection :event="event" />
  </div>
</template>
<script setup>
import MerchSection from '@/components/event/MerchSection.vue'
import MerchDeliverySection from '@/components/event/MerchDeliverySection.vue'

const props = defineProps({
  event: { type: Object, required: true },
})
</script>
