# Go-Live Readiness Note — Northstar Support Deflection MVP

**Date:** End of Sprint Week  
**Prepared by:** Pod Team  
**Audience:** Northstar Retail Co. internal team

---

## What Works ✅

| Capability | Status | Notes |
|---|---|---|
| Order status lookup by order ID | ✅ Working | Supports NS-format IDs; returns status, tracking number, and ETA |
| Returns policy self-serve answer | ✅ Working | Covers 30-day window, return portal link, and process |
| Refund timeline self-serve answer | ✅ Working | Covers 5–7 day processing, confirmation email, and escalation path |
| Keyword routing (order / return / refund) | ✅ Working | Handles common phrasings; falls back gracefully to a help menu |
| Web chat UI | ✅ Working | Runs locally on port 5000; mobile-responsive layout |

---

## What's Known-Broken / Out of Scope ⚠️
- **Live order data** — the prototype uses `data/orders.json` (5 mock orders). Real deployment requires connecting to Northstar's order management API.
- **Authentication** — there is no customer login. Any user can look up any order ID. Do not go live without adding auth or at minimum a verification step (e.g. order ID + email).
- **No persistent chat history** — conversations are not stored. Each page refresh starts a new session.
- **No escalation handoff** — when the bot can't answer, it tells the user to "contact support" but does not open a ticket or route to a live agent automatically.

---

## What Northstar's Team Needs to Pick This Up 🔧

1. **Replace mock data** — swap `data/orders.json` with a real API call in `chatbot.py` → `_order_status_reply()`. The function signature stays the same.
2. **Add customer verification** — before returning order details, verify the customer owns the order (e.g. match order ID + email on file).
3. **Deploy the Flask app** — the app is production-ready with a WSGI server (e.g. `gunicorn app:app`). Recommend deploying behind a reverse proxy (nginx) or on a PaaS (e.g. AWS Elastic Beanstalk, Render).
4. **Integrate with support ticketing system** — add a fallback route that creates a ticket in Zendesk/Freshdesk when the bot replies with the "I'm not sure" message.
5. **Expand to stock availability** — add a third flow in `chatbot.py` following the same pattern as the order and returns flows.

---

## Estimated Effort to Production-Ready

| Item | Effort |
|---|---|
| Connect live order API | 1–2 days |
| Add customer verification | 1 day |
| Deploy + configure HTTPS | 0.5 day |
| Ticketing system integration | 1–2 days |
| Stock availability flow | 1 day |
