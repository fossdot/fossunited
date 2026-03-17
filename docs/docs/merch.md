# Event Merchandise

Organizers can add merchandise (t-shirts, caps, hoodies, stickers, etc.) to any paid event. Attendees select and pay for merch during ticket checkout.

## Setting Up Merch

1. Open the **FOSS Chapter Event** in Frappe Desk
2. Enable **Is paid event?**
3. Scroll to the **Merchandise** section
4. Add rows to the merch table — each item has:

| Field | Description |
|-------|-------------|
| `merch_name` | Display name (e.g. "Tshirt", "Cap") |
| `price` | Price in INR |
| `image` | Main product image |
| `extra_images` | Additional images, one URL per line |
| `color_options` | Newline-separated color variants — named colors (`Red`, `Black`) or hex codes (`#FF5733`) |
| `size_options` | Newline-separated size variants (`XS`, `S`, `M`, `L`, `XL`, `2XL`, `3XL`) |
| `enabled` | Uncheck to hide an item without deleting it |

## Attendee Flow

On the **Buy Tickets** page, each attendee sees a horizontal scrollable merch carousel below their details form:

- Tap an image to open a zoom gallery
- Select a color swatch (if variants defined)
- Select a size from the dropdown (if variants defined)
- Click **+ Add** → quantity stepper appears to increase/decrease
- Merch cost is added to the **Ticket Summary** in real time

Merch is optional — attendees can proceed without adding any.

## Pricing & Security

Prices are validated **server-side** before payment is created. The client-submitted total is checked against the authoritative prices stored on the event. This prevents price manipulation.

## APIs

All in `fossunited/api/tickets.py`:

| Method | Description |
|--------|-------------|
| `save_event_merch_item` | Add or update a merch item on an event |
| `delete_event_merch_item` | Remove a merch item from an event |
| `get_merch_insights(event_id)` | Sales totals and revenue per item/variant |
| `get_merch_delivery(event_id, search_query)` | Search tickets by name/email, returns merch + delivery status |
| `mark_merch_delivered(ticket_name, merch_row_name, delivered)` | Toggle delivered flag for a merch row |

## Fulfillment Tracking

Each merch row on a ticket has a `delivered` flag. Use `get_merch_delivery` + `mark_merch_delivered` to track what's been handed out at the event.

## Data Model

```
FOSS Chapter Event
└── merch_items (child table: FOSS Event Merch)
    └── name, price, image, color_options, size_options, enabled

FOSS Event Ticket
└── merch_items (child table: FOSS Ticket Merch)
    └── merch_name, price, quantity, color, size, delivered
```

## Relevant Files

| File | Purpose |
|------|---------|
| `fossunited/ticketing/doctype/foss_event_merch/` | Merch config doctype (child of event) |
| `fossunited/ticketing/doctype/foss_ticket_merch/` | Merch purchase record (child of ticket) |
| `dashboard/src/components/tickets/AttendeeMerchPicker.vue` | Frontend carousel component |
| `dashboard/src/pages/BuyTickets.vue` | Ticket purchase page |
| `fossunited/api/tickets.py` | All merch-related API methods |
