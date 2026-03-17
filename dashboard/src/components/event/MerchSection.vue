<template>
  <ManageMerchDialog
    v-model="showDialog"
    :event="event.data"
    :is-new="isNew"
    :row="selectedRow"
    @refresh="event.fetch()"
  />

  <div>
    <div class="prose w-full mb-4">
      <h2 class="mb-1">Merchandise</h2>
      <p class="text-sm">
        Add merch items (T-shirts, hoodies, stickers, etc.) that attendees can add to their ticket
        order. When at least one item is enabled here, the old "Add a T-shirt?" checkbox is
        replaced by the new multi-merch picker on the buy-tickets page.
      </p>
      <Button variant="solid" label="Add Merch Item" icon-left="plus" @click="handleCreate" />
    </div>

    <!-- Empty state -->
    <div
      v-if="!merch.length"
      class="mt-4 rounded border border-dashed border-outline-gray-3 px-6 py-10 text-center"
    >
      <p class="text-sm text-ink-gray-5">No merch items yet. Add your first item above.</p>
    </div>

    <!-- Merch cards -->
    <div v-else class="mt-4 flex flex-col gap-3">
      <div
        v-for="item in merch"
        :key="item.name"
        class="flex items-start gap-4 rounded border border-outline-gray-2 bg-surface-gray-1 px-4 py-3"
        :class="{ 'opacity-50': !item.enabled }"
      >
        <!-- Status dot -->
        <div class="mt-1 flex-shrink-0">
          <span
            class="inline-block h-2.5 w-2.5 rounded-full"
            :class="item.enabled ? 'bg-green-500' : 'bg-outline-gray-4'"
            :title="item.enabled ? 'Enabled' : 'Disabled'"
          />
        </div>

        <!-- Info -->
        <div class="flex-1 min-w-0">
          <div class="flex items-baseline gap-2 flex-wrap">
            <span class="font-semibold text-ink-gray-9">{{ item.merch_name }}</span>
            <span class="text-sm text-ink-gray-5">₹{{ item.price }}</span>
          </div>
          <div class="mt-1 flex flex-wrap gap-x-4 gap-y-0.5 text-xs text-ink-gray-5">
            <span v-if="colorList(item).length">
              Colours: {{ colorList(item).join(', ') }}
            </span>
            <span v-if="sizeList(item).length">
              Sizes: {{ sizeList(item).join(', ') }}
            </span>
            <span v-if="!colorList(item).length && !sizeList(item).length">
              No variants
            </span>
          </div>
        </div>

        <!-- Actions -->
        <div class="flex-shrink-0 flex gap-2 items-center">
          <Button
            size="sm"
            :label="item.enabled ? 'Disable' : 'Enable'"
            :theme="item.enabled ? 'red' : 'gray'"
            @click="toggleEnabled(item)"
          />
          <Button size="sm" icon="edit-2" @click="handleEdit(item)" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { Button, createResource } from 'frappe-ui'
import { useRoute } from 'vue-router'
import { toast } from 'vue-sonner'
import ManageMerchDialog from '@/components/event/ManageMerchDialog.vue'

const props = defineProps({
  event: { type: Object, required: true },
})

const route = useRoute()
const showDialog = ref(false)
const isNew = ref(true)
const selectedRow = ref({})

const merch = computed(() => props.event.data?.merch_items || [])

const colorList = (item) =>
  (item.color_options || '').split('\n').map((s) => s.trim()).filter(Boolean)

const sizeList = (item) =>
  (item.size_options || '').split('\n').map((s) => s.trim()).filter(Boolean)

const handleCreate = () => {
  isNew.value = true
  selectedRow.value = {}
  showDialog.value = true
}

const handleEdit = (item) => {
  isNew.value = false
  selectedRow.value = { ...item }
  showDialog.value = true
}

const toggleEnabledRes = createResource({
  url: 'fossunited.api.tickets.save_event_merch_item',
  onSuccess() {
    props.event.fetch()
  },
  onError(err) {
    toast.error(err.message || String(err))
  },
})

const toggleEnabled = (item) => {
  toggleEnabledRes.submit({
    event: props.event.data.name,
    row_name: item.name,
    merch_name: item.merch_name,
    price: item.price,
    enabled: item.enabled ? 0 : 1,
    image: item.image || '',
    extra_images: item.extra_images || '',
    color_options: item.color_options || '',
    size_options: item.size_options || '',
  })
}
</script>
