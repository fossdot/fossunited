<template>
  <div>
    <div class="prose w-full mb-4">
      <h2 class="mb-1">Merch Sales</h2>
      <p class="text-sm">Sales breakdown for each merchandise item.</p>
    </div>

    <!-- Loading -->
    <div v-if="insights.loading" class="flex items-center justify-center h-24">
      <LoadingIndicator class="w-5 h-5" />
    </div>

    <!-- Empty state -->
    <div
      v-else-if="!insights.data || !insights.data.items.length"
      class="rounded border border-dashed border-outline-gray-3 px-6 py-10 text-center"
    >
      <p class="text-sm text-ink-gray-5">No merch sales yet.</p>
    </div>

    <!-- Data -->
    <div v-else class="flex flex-col gap-4">
      <!-- Summary bar -->
      <div class="flex items-center justify-between">
        <span class="text-sm text-ink-gray-6">
          Grand Total Revenue:
          <span class="font-semibold text-ink-gray-9">₹{{ insights.data.grand_total_revenue.toLocaleString('en-IN') }}</span>
        </span>
        <Button
          size="sm"
          label="Download CSV"
          icon-left="download"
          @click="downloadCsv"
        />
      </div>

      <!-- Per-item cards -->
      <div
        v-for="item in insights.data.items"
        :key="item.merch_name"
        class="rounded border border-outline-gray-2 bg-surface-gray-1"
      >
        <!-- Item header -->
        <div
          class="flex items-center justify-between px-4 py-3 cursor-pointer select-none"
          @click="toggleExpanded(item.merch_name)"
        >
          <div class="flex items-baseline gap-3">
            <span class="font-semibold text-ink-gray-9">{{ item.merch_name }}</span>
            <span class="text-sm text-ink-gray-5">{{ item.total_qty }} sold</span>
            <span class="text-sm text-ink-gray-5">₹{{ item.total_revenue.toLocaleString('en-IN') }}</span>
          </div>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-4 w-4 text-ink-gray-5 transition-transform"
            :class="{ 'rotate-180': expanded.has(item.merch_name) }"
            fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"
          >
            <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
          </svg>
        </div>

        <!-- Breakdown table -->
        <div v-if="expanded.has(item.merch_name)" class="border-t border-outline-gray-2">
          <table class="w-full text-sm">
            <thead>
              <tr class="bg-surface-gray-2 text-ink-gray-5 text-xs">
                <th class="px-4 py-2 text-left font-medium">Colour</th>
                <th class="px-4 py-2 text-left font-medium">Size</th>
                <th class="px-4 py-2 text-right font-medium">Qty</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="(row, i) in item.breakdown"
                :key="i"
                class="border-t border-outline-gray-2"
              >
                <td class="px-4 py-2 text-ink-gray-7">{{ row.color || '—' }}</td>
                <td class="px-4 py-2 text-ink-gray-7">{{ row.size || '—' }}</td>
                <td class="px-4 py-2 text-right text-ink-gray-9 font-medium">{{ row.qty }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { createResource, LoadingIndicator, Button } from 'frappe-ui'

const props = defineProps({
  event: { type: Object, required: true },
})

const expanded = ref(new Set())

const toggleExpanded = (name) => {
  if (expanded.value.has(name)) {
    expanded.value.delete(name)
  } else {
    expanded.value.add(name)
  }
  // Trigger reactivity on Set
  expanded.value = new Set(expanded.value)
}

const insights = createResource({
  url: 'fossunited.api.tickets.get_merch_insights',
  makeParams() {
    return { event_id: props.event.data.name }
  },
  auto: true,
})

const downloadCsv = () => {
  if (!insights.data?.items?.length) return

  const rows = [['Merch Name', 'Colour', 'Size', 'Qty', 'Revenue (INR)']]
  for (const item of insights.data.items) {
    for (const row of item.breakdown) {
      const lineRevenue = (row.qty * (item.total_revenue / item.total_qty)).toFixed(2)
      rows.push([item.merch_name, row.color || '', row.size || '', row.qty, lineRevenue])
    }
  }

  const csv = rows.map((r) => r.map((v) => `"${String(v).replace(/"/g, '""')}"`).join(',')).join('\n')
  const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = `merch-sales-${props.event.data.name}.csv`
  a.click()
  URL.revokeObjectURL(url)
}
</script>
