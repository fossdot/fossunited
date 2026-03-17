<template>
  <Dialog
    v-model="showDialog"
    :options="{
      title: isNew ? 'Add Merch Item' : 'Edit Merch Item',
      width: 'md',
    }"
  >
    <template #body-content>
      <div class="flex flex-col gap-4">
        <FormControl
          v-model="form.merch_name"
          label="Merch Name *"
          placeholder="e.g. Conference T-Shirt"
        />
        <FormControl
          v-model="form.price"
          label="Price (INR) *"
          type="number"
          :min="1"
          placeholder="499"
        />
        <div class="flex items-center justify-between rounded border border-outline-gray-2 px-3 py-2">
          <span class="text-sm font-medium text-ink-gray-8">Enabled</span>
          <input
            v-model="form.enabled"
            type="checkbox"
            class="h-4 w-4 rounded border-outline-gray-3 text-ink-gray-8 focus:ring-ink-gray-7"
          />
        </div>

        <!-- Images -->
        <div>
          <label class="block text-xs text-ink-gray-5 mb-2">Images *</label>
          <div class="flex flex-wrap gap-2">
            <!-- Existing image thumbnails -->
            <div
              v-for="(url, idx) in allImages"
              :key="url"
              class="relative h-20 w-20 flex-shrink-0 rounded border border-outline-gray-3 overflow-hidden group"
            >
              <img :src="url" class="h-full w-full object-cover" alt="Merch image" />
              <!-- Primary badge -->
              <span
                v-if="idx === 0"
                class="absolute bottom-0 left-0 right-0 text-center text-white text-[9px] font-semibold bg-black/50 py-0.5"
              >Primary</span>
              <!-- Remove button -->
              <button
                type="button"
                class="absolute top-1 right-1 flex h-5 w-5 items-center justify-center rounded-full bg-white/90 text-ink-gray-7 shadow opacity-0 group-hover:opacity-100 transition-opacity"
                @click="removeImage(idx)"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>

            <!-- Add image button -->
            <label
              class="h-20 w-20 flex-shrink-0 flex flex-col items-center justify-center gap-1 rounded border border-dashed border-outline-gray-3 cursor-pointer hover:bg-surface-gray-1 transition-colors"
              :class="{ 'opacity-50 pointer-events-none': extraUploading }"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-ink-gray-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4" />
              </svg>
              <span class="text-[10px] text-ink-gray-4">{{ extraUploading ? 'Uploading…' : 'Add' }}</span>
              <input
                type="file"
                accept="image/*"
                class="sr-only"
                :disabled="extraUploading"
                @change="handleAddImage"
              />
            </label>
          </div>
          <p class="mt-1 text-xs text-ink-gray-4">First image is the thumbnail. Add more for a gallery. PNG, JPG, WEBP.</p>
        </div>

        <div>
          <label class="block text-xs text-ink-gray-5 mb-1">Colour Options (hex codes)</label>
          <textarea
            v-model="form.color_options"
            rows="4"
            placeholder="One hex code per line, e.g.:&#10;#000000&#10;#FFFFFF&#10;#1E3A5F"
            class="w-full rounded border border-outline-gray-3 px-3 py-2 text-sm text-ink-gray-9 placeholder-ink-gray-4 focus:border-ink-gray-5 focus:outline-none resize-none bg-surface-white"
          />
          <p class="mt-1 text-xs text-ink-gray-4">Enter one hex colour code per line (e.g. #FF5733). Leave blank for no colour picker.</p>
        </div>
        <div>
          <label class="block text-xs text-ink-gray-5 mb-1">Size Options</label>
          <textarea
            v-model="form.size_options"
            rows="4"
            placeholder="One size per line, e.g.:&#10;XS&#10;S&#10;M&#10;L&#10;XL&#10;XXL"
            class="w-full rounded border border-outline-gray-3 px-3 py-2 text-sm text-ink-gray-9 placeholder-ink-gray-4 focus:border-ink-gray-5 focus:outline-none resize-none bg-surface-white"
          />
          <p class="mt-1 text-xs text-ink-gray-4">Enter one size per line. Leave blank for no size picker.</p>
        </div>
        <ErrorMessage :message="errorMessage" />
      </div>
    </template>
    <template #actions>
      <div class="flex gap-2 w-full">
        <Button
          v-if="!isNew"
          icon="trash"
          theme="red"
          :loading="deleteRes.loading"
          @click="handleDelete"
        />
        <Button class="flex-1" label="Cancel" @click="showDialog = false" />
        <Button
          class="flex-1"
          variant="solid"
          :label="isNew ? 'Add' : 'Save'"
          :loading="saveRes.loading"
          @click="handleSave"
        />
      </div>
    </template>
  </Dialog>
</template>

<script setup>
import { ref, reactive, computed, watch } from 'vue'
import { Dialog, FormControl, ErrorMessage, Button, createResource } from 'frappe-ui'
import { toast } from 'vue-sonner'

const props = defineProps({
  event: { type: Object, required: true },
  isNew: { type: Boolean, default: true },
  row: { type: Object, default: () => ({}) },
})

const emit = defineEmits(['refresh'])

const showDialog = defineModel({ type: Boolean, default: false })

const defaultForm = {
  merch_name: '',
  price: '',
  enabled: true,
  image: '',
  extra_images: '',
  color_options: '',
  size_options: '',
}

const form = reactive({ ...defaultForm })
const errorMessage = ref('')
const extraUploading = ref(false)

// All images as array: [primary, ...extras]
const allImages = computed(() => {
  const extras = form.extra_images
    ? form.extra_images.split('\n').map(u => u.trim()).filter(Boolean)
    : []
  return form.image ? [form.image, ...extras] : extras
})

watch(
  () => props.row,
  (row) => {
    if (!row || !row.name) {
      Object.assign(form, defaultForm)
      return
    }
    form.merch_name    = row.merch_name    || ''
    form.price         = row.price         || ''
    form.enabled       = row.enabled !== undefined ? Boolean(row.enabled) : true
    form.image         = row.image         || ''
    form.extra_images  = row.extra_images  || ''
    form.color_options = row.color_options || ''
    form.size_options  = row.size_options  || ''
  },
  { immediate: true },
)

const validate = () => {
  const errors = []
  if (!form.merch_name.trim()) errors.push('Merch name is required.')
  if (!form.price || Number(form.price) <= 0) errors.push('Price must be greater than 0.')
  if (!form.image && !form.extra_images) errors.push('At least one merch image is required.')
  return errors
}

// ── image upload ─────────────────────────────────────────────────────────────

async function uploadFile(file) {
  const fd = new FormData()
  fd.append('file', file, file.name)
  fd.append('is_private', '0')
  fd.append('folder', 'Home/Attachments')
  const res = await fetch('/api/method/upload_file', {
    method: 'POST',
    headers: { 'X-Frappe-CSRF-Token': window.csrf_token },
    body: fd,
  })
  const data = await res.json()
  if (!data.message?.file_url) throw new Error('Upload failed')
  return data.message.file_url
}

const handleAddImage = async (event) => {
  const file = event.target.files?.[0]
  if (!file) return
  extraUploading.value = true
  errorMessage.value = ''
  try {
    const url = await uploadFile(file)
    if (!form.image) {
      form.image = url
    } else {
      const extras = form.extra_images
        ? form.extra_images.split('\n').map(u => u.trim()).filter(Boolean)
        : []
      extras.push(url)
      form.extra_images = extras.join('\n')
    }
  } catch {
    errorMessage.value = 'Image upload failed. Please try again.'
  } finally {
    extraUploading.value = false
    event.target.value = ''
  }
}

const removeImage = (idx) => {
  const imgs = allImages.value.slice()
  imgs.splice(idx, 1)
  form.image = imgs[0] || ''
  form.extra_images = imgs.slice(1).join('\n')
}

// ── save (insert or update) ──────────────────────────────────────────────────

const saveRes = createResource({
  url: 'fossunited.api.tickets.save_event_merch_item',
  onSuccess() {
    toast.success(props.isNew ? 'Merch item added!' : 'Merch item updated!')
    errorMessage.value = ''
    showDialog.value = false
    emit('refresh')
  },
  onError(err) {
    errorMessage.value = err.message || String(err)
  },
})

const handleSave = () => {
  const errors = validate()
  if (errors.length) { errorMessage.value = errors.join(' '); return }
  errorMessage.value = ''
  saveRes.submit({
    event:         props.event.name,
    row_name:      props.isNew ? null : props.row.name,
    merch_name:    form.merch_name.trim(),
    price:         Number(form.price),
    enabled:       form.enabled ? 1 : 0,
    image:         form.image,
    extra_images:  form.extra_images,
    color_options: form.color_options,
    size_options:  form.size_options,
  })
}

// ── delete ───────────────────────────────────────────────────────────────────

const deleteRes = createResource({
  url: 'fossunited.api.tickets.delete_event_merch_item',
  onSuccess() {
    toast.info('Merch item removed.')
    showDialog.value = false
    emit('refresh')
  },
  onError(err) {
    errorMessage.value = err.message || String(err)
  },
})

const handleDelete = () => {
  deleteRes.submit({ event: props.event.name, row_name: props.row.name })
}
</script>
