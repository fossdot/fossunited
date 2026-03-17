<template>
  <div v-if="merchItems.length > 0" class="mt-4 border-t pt-4">
    <h3 class="text-sm font-semibold text-ink-gray-7 mb-3">Merchandise (Optional)</h3>

    <!-- Horizontal scrollable row -->
    <div class="relative">
      <div
        v-if="showRightFade"
        class="scroll-fade-right pointer-events-none absolute right-0 top-0 bottom-0 w-10 z-10"
      />
      <div
        ref="scrollContainer"
        class="flex gap-4 overflow-x-auto pb-1"
        style="-webkit-overflow-scrolling: touch; scrollbar-width: none;"
        @scroll="onScroll"
      >
        <div
          v-for="item in merchItems"
          :key="item.merch_name"
          class="flex-shrink-0 w-40 flex flex-col"
        >
          <!-- Image -->
          <div
            class="w-full h-40 rounded-lg bg-surface-gray-1 flex items-center justify-center overflow-hidden p-2"
            :class="(item.images && item.images.length) ? 'cursor-pointer' : ''"
            @click="item.images && item.images.length && openZoom(item)"
          >
            <img
              v-if="item.images && item.images.length"
              :src="item.images[0]"
              :alt="item.merch_name"
              class="w-full h-full object-contain"
            />
            <svg
              v-else
              xmlns="http://www.w3.org/2000/svg"
              class="h-8 w-8 text-outline-gray-3"
              fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1"
            >
              <rect x="3" y="3" width="18" height="18" rx="2" stroke-width="1.2" />
              <circle cx="8.5" cy="8.5" r="1.5" />
              <path stroke-linecap="round" stroke-linejoin="round" d="M21 15l-5-5L5 21" />
            </svg>
          </div>

          <!-- Info -->
          <div class="mt-2 flex-1 flex flex-col gap-1.5">
            <p class="text-sm font-semibold text-ink-gray-9 leading-snug">{{ item.merch_name }}</p>

            <!-- Price + size on same row -->
            <div class="flex items-center justify-between">
              <span class="text-xs font-medium text-ink-gray-5">₹{{ item.price }}</span>
              <select
                v-if="item.size_options.length"
                :value="selectedSize(item)"
                class="min-w-[4rem] rounded border border-outline-gray-3 px-1.5 py-0.5 text-xs text-ink-gray-9 focus:border-ink-gray-5 focus:outline-none bg-surface-white"
                @change="setSize(item, $event.target.value)"
              >
                <option v-for="size in item.size_options" :key="size" :value="size">{{ size }}</option>
              </select>
            </div>

            <!-- Colour swatches -->
            <div v-if="item.color_options.length" class="flex flex-wrap gap-1.5 items-center">
              <button
                v-for="color in item.color_options"
                :key="color"
                type="button"
                :title="color"
                class="h-5 w-5 rounded-full border-2 transition-all focus:outline-none"
                :class="selectedColor(item) === color
                  ? 'border-ink-gray-8 scale-110 shadow-sm'
                  : 'border-outline-gray-2 hover:scale-105'"
                :style="{ backgroundColor: colorToHex(color) }"
                @click="setColor(item, color)"
              />
            </div>

            <!-- Qty stepper -->
            <div v-if="cartEntry(item)" class="flex items-center gap-1 mt-auto">
              <button
                type="button"
                class="flex h-7 w-7 items-center justify-center rounded border border-outline-gray-3 text-ink-gray-7 hover:bg-surface-gray-1 transition-colors"
                @click="decrement(item)"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M5 12h14" />
                </svg>
              </button>
              <span class="flex-1 text-center text-sm font-bold text-ink-gray-9">{{ cartEntry(item).quantity }}</span>
              <button
                type="button"
                class="flex h-7 w-7 items-center justify-center rounded border border-outline-gray-3 text-ink-gray-7 hover:bg-surface-gray-1 transition-colors"
                @click="increment(item)"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M12 5v14M5 12h14" />
                </svg>
              </button>
            </div>

            <!-- Add button -->
            <button
              v-else
              type="button"
              :disabled="!canAdd(item)"
              class="w-full rounded border py-1.5 text-xs font-semibold transition-colors focus:outline-none mt-auto"
              :class="canAdd(item)
                ? 'border-ink-gray-8 text-ink-gray-8 hover:bg-ink-gray-8 hover:text-white'
                : 'cursor-not-allowed border-outline-gray-2 text-ink-gray-3'"
              :title="!canAdd(item) ? addDisabledReason(item) : ''"
              @click="addToCart(item)"
            >+ Add</button>
          </div>
        </div>
      </div>
    </div>

    <p v-if="validationHint" class="mt-2 text-xs text-red-500">{{ validationHint }}</p>

    <!-- Zoom / carousel overlay -->
    <Teleport to="body">
      <div
        v-if="zoomItem"
        class="fixed inset-0 z-50 flex items-center justify-center bg-black/85 p-4"
        @click="closeZoom"
      >
        <div class="relative max-w-sm w-full flex flex-col items-center" @click.stop>
          <!-- Image -->
          <img
            :src="zoomItem.images[zoomIndex]"
            :alt="zoomItem.merch_name"
            class="w-full rounded-xl object-contain max-h-[70vh]"
          />

          <!-- Prev / Next -->
          <template v-if="zoomItem.images.length > 1">
            <button
              type="button"
              class="absolute left-0 top-1/2 -translate-y-1/2 -translate-x-4 flex h-9 w-9 items-center justify-center rounded-full bg-white/90 text-ink-gray-8 shadow"
              @click.stop="zoomIndex = (zoomIndex - 1 + zoomItem.images.length) % zoomItem.images.length"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
              </svg>
            </button>
            <button
              type="button"
              class="absolute right-0 top-1/2 -translate-y-1/2 translate-x-4 flex h-9 w-9 items-center justify-center rounded-full bg-white/90 text-ink-gray-8 shadow"
              @click.stop="zoomIndex = (zoomIndex + 1) % zoomItem.images.length"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
              </svg>
            </button>

            <!-- Dots -->
            <div class="flex gap-1.5 mt-3">
              <button
                v-for="(_, i) in zoomItem.images"
                :key="i"
                type="button"
                class="h-1.5 rounded-full transition-all"
                :class="i === zoomIndex ? 'w-4 bg-white' : 'w-1.5 bg-white/40'"
                @click.stop="zoomIndex = i"
              />
            </div>
          </template>

          <p class="mt-3 text-center text-white text-sm font-medium">{{ zoomItem.merch_name }}</p>

          <!-- Close -->
          <button
            type="button"
            class="absolute -top-3 -right-3 flex h-8 w-8 items-center justify-center rounded-full bg-white text-ink-gray-9 shadow-lg"
            @click="closeZoom"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
      </div>
    </Teleport>
  </div>
</template>

<script setup>
import { reactive, ref, onMounted, nextTick } from 'vue'

const props = defineProps({
  merchItems: { type: Array, default: () => [] },
})

const modelValue = defineModel({ default: () => [] })

const pendingColor = reactive({})
const pendingSize  = reactive({})
const validationHint = ref('')
const zoomItem  = ref(null)
const zoomIndex = ref(0)
const scrollContainer = ref(null)
const showRightFade = ref(false)

const openZoom = (item) => { zoomItem.value = item; zoomIndex.value = 0 }
const closeZoom = () => { zoomItem.value = null }

const onScroll = () => {
  const el = scrollContainer.value
  if (!el) return
  showRightFade.value = el.scrollLeft + el.clientWidth < el.scrollWidth - 4
}

onMounted(() => nextTick(onScroll))

function cartEntry(item) {
  return modelValue.value.find((e) => e.merch_name === item.merch_name) ?? null
}

function selectedColor(item) {
  const entry = cartEntry(item)
  if (entry) return entry.color
  return pendingColor[item.merch_name] ?? (item.color_options[0] || '')
}

function selectedSize(item) {
  const entry = cartEntry(item)
  if (entry) return entry.size
  return pendingSize[item.merch_name] ?? (item.size_options[0] || '')
}

function setColor(item, color) {
  if (cartEntry(item)) {
    modelValue.value = modelValue.value.map((e) =>
      e.merch_name === item.merch_name ? { ...e, color } : e
    )
  } else {
    pendingColor[item.merch_name] = color
  }
}

function setSize(item, size) {
  if (cartEntry(item)) {
    modelValue.value = modelValue.value.map((e) =>
      e.merch_name === item.merch_name ? { ...e, size } : e
    )
  } else {
    pendingSize[item.merch_name] = size
  }
}

function canAdd(item) {
  if (item.color_options.length && !selectedColor(item)) return false
  if (item.size_options.length  && !selectedSize(item))  return false
  return true
}

function addDisabledReason(item) {
  if (item.color_options.length && !selectedColor(item)) return 'Please select a colour'
  if (item.size_options.length  && !selectedSize(item))  return 'Please select a size'
  return ''
}

function addToCart(item) {
  if (!canAdd(item)) { validationHint.value = addDisabledReason(item); return }
  validationHint.value = ''
  modelValue.value = [
    ...modelValue.value,
    {
      merch_name: item.merch_name,
      price:      item.price,
      color:      selectedColor(item),
      size:       selectedSize(item),
      quantity:   1,
    },
  ]
}

function increment(item) {
  modelValue.value = modelValue.value.map((e) =>
    e.merch_name === item.merch_name ? { ...e, quantity: e.quantity + 1 } : e
  )
}

function decrement(item) {
  const entry = cartEntry(item)
  if (!entry) return
  if (entry.quantity <= 1) {
    modelValue.value = modelValue.value.filter((e) => e.merch_name !== item.merch_name)
  } else {
    modelValue.value = modelValue.value.map((e) =>
      e.merch_name === item.merch_name ? { ...e, quantity: e.quantity - 1 } : e
    )
  }
}

// Supports both hex codes (#FF5733) and named colours for backward compat
const COLOR_MAP = {
  black: '#111827', white: '#f9fafb', red: '#ef4444', blue: '#3b82f6',
  green: '#22c55e', yellow: '#eab308', orange: '#f97316', purple: '#a855f7',
  pink: '#ec4899', grey: '#9ca3af', gray: '#9ca3af', navy: '#1e3a5f',
  'navy blue': '#1e3a5f', teal: '#14b8a6', cyan: '#06b6d4', indigo: '#6366f1',
  violet: '#8b5cf6', maroon: '#7f1d1d', brown: '#92400e', gold: '#d97706',
  silver: '#d1d5db', beige: '#f5f0e8', cream: '#fef3c7',
}

function colorToHex(color) {
  if (!color) return '#e5e7eb'
  const trimmed = color.trim()
  if (/^#[0-9a-f]{3,8}$/i.test(trimmed)) return trimmed
  return COLOR_MAP[trimmed.toLowerCase()] ?? '#e5e7eb'
}
</script>

<style scoped>
div::-webkit-scrollbar { display: none; }
.scroll-fade-right {
  background: linear-gradient(to right, transparent, var(--surface-white));
}
</style>
