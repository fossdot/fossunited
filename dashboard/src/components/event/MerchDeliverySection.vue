<template>
  <div>
    <div class="prose w-full mb-4">
      <h2 class="mb-1">Merch Delivery</h2>
      <p class="text-sm">
        Search attendees by ticket ID, name, or email to track merch distribution at the event.
      </p>
    </div>

    <!-- Search input -->
    <div class="relative mb-4">
      <input
        v-model="searchQuery"
        type="text"
        placeholder="Search by ticket ID, name or email..."
        class="w-full rounded border border-outline-gray-3 px-4 py-2 pr-10 text-sm text-ink-gray-9 placeholder-ink-gray-4 focus:border-ink-gray-5 focus:outline-none"
        @input="onInput"
      />
      <svg
        v-if="!deliveryRes.loading"
        xmlns="http://www.w3.org/2000/svg"
        class="absolute right-3 top-1/2 -translate-y-1/2 h-4 w-4 text-ink-gray-4"
        fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"
      >
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-4.35-4.35M17 11A6 6 0 1 1 5 11a6 6 0 0 1 12 0z" />
      </svg>
      <LoadingIndicator v-else class="absolute right-3 top-1/2 -translate-y-1/2 h-4 w-4" />
    </div>

    <!-- Empty / hint state -->
    <div
      v-if="!searchQuery.trim()"
      class="rounded border border-dashed border-outline-gray-3 px-6 py-10 text-center"
    >
      <p class="text-sm text-ink-gray-5">Enter a name, email, or ticket ID above to search.</p>
    </div>

    <!-- No results -->
    <div
      v-else-if="!deliveryRes.loading && deliveryRes.data && !deliveryRes.data.length"
      class="rounded border border-dashed border-outline-gray-3 px-6 py-10 text-center"
    >
      <p class="text-sm text-ink-gray-5">No matching attendees with merch found.</p>
    </div>

    <!-- Results -->
    <div v-else-if="deliveryRes.data && deliveryRes.data.length" class="flex flex-col gap-3">
      <div
        v-for="ticket in deliveryRes.data"
        :key="ticket.ticket_name"
        class="rounded border border-outline-gray-2 bg-surface-gray-1 px-4 py-3"
      >
        <!-- Attendee header -->
        <div class="mb-3">
          <div class="flex items-center gap-2 flex-wrap">
            <span class="font-semibold text-ink-gray-9">{{ ticket.full_name || 'No name' }}</span>
            <span class="text-xs text-ink-gray-5 font-mono">{{ ticket.ticket_name }}</span>
          </div>
          <div class="text-xs text-ink-gray-5 mt-0.5">{{ ticket.email }}</div>
        </div>

        <!-- Merch items -->
        <div class="flex flex-col gap-2">
          <div
            v-for="item in ticket.merch_items"
            :key="item.name"
            class="flex items-center gap-3 rounded border border-outline-gray-2 bg-surface-white px-3 py-2"
            :class="{ 'opacity-60': item.delivered }"
          >
            <!-- Check icon when delivered -->
            <span
              class="flex-shrink-0 h-5 w-5 rounded-full flex items-center justify-center"
              :class="item.delivered ? 'bg-green-500' : 'bg-outline-gray-3'"
            >
              <svg
                v-if="item.delivered"
                xmlns="http://www.w3.org/2000/svg"
                class="h-3 w-3 text-white"
                fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="3"
              >
                <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
              </svg>
            </span>

            <!-- Item details -->
            <div class="flex-1 min-w-0">
              <span
                class="text-sm font-medium text-ink-gray-9"
                :class="{ 'line-through text-ink-gray-5': item.delivered }"
              >
                {{ item.merch_name }}
              </span>
              <span v-if="item.color || item.size" class="ml-2 text-xs text-ink-gray-5">
                <span v-if="item.color">{{ item.color }}</span>
                <span v-if="item.color && item.size"> · </span>
                <span v-if="item.size">{{ item.size }}</span>
              </span>
              <span v-if="item.quantity > 1" class="ml-2 text-xs text-ink-gray-5">× {{ item.quantity }}</span>
            </div>

            <!-- Deliver toggle -->
            <Button
              size="sm"
              :label="item.delivered ? 'Undeliver' : 'Mark Delivered'"
              :theme="item.delivered ? 'gray' : 'green'"
              :loading="pendingRow === item.name"
              @click="toggleDelivered(ticket, item)"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { createResource, LoadingIndicator, Button } from 'frappe-ui'
import { toast } from 'vue-sonner'

const props = defineProps({
  event: { type: Object, required: true },
})

const searchQuery = ref('')
const pendingRow = ref(null)
let debounceTimer = null

const deliveryRes = createResource({
  url: 'fossunited.api.tickets.get_merch_delivery',
  makeParams() {
    return {
      event_id: props.event.data.name,
      search_query: searchQuery.value.trim(),
    }
  },
})

const onInput = () => {
  clearTimeout(debounceTimer)
  if (!searchQuery.value.trim()) return
  debounceTimer = setTimeout(() => {
    deliveryRes.fetch()
  }, 300)
}

const markRes = createResource({
  url: 'fossunited.api.tickets.mark_merch_delivered',
  onSuccess() {
    pendingRow.value = null
  },
  onError(err) {
    pendingRow.value = null
    toast.error(err.message || String(err))
  },
})

const toggleDelivered = (ticket, item) => {
  pendingRow.value = item.name
  const newVal = item.delivered ? 0 : 1
  markRes.submit(
    {
      ticket_name: ticket.ticket_name,
      merch_row_name: item.name,
      delivered: newVal,
    },
    {
      onSuccess() {
        item.delivered = newVal
        pendingRow.value = null
      },
    },
  )
}
</script>
