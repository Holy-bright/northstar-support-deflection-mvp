import json
import os
import re
import html

with open(os.path.join(os.path.dirname(__file__), "data", "orders.json")) as f:
    ORDERS = json.load(f)
 
with open(os.path.join(os.path.dirname(__file__), "data", "products.json")) as f:
    PRODUCTS = json.load(f)


GREETINGS = {"hi", "hello", "hey", "help", "start"}

WELCOME = (
    "Hi! I'm the Northstar Support Bot 👋\n\n"
    "I can help you with:\n\n"
    "1. 📦 Order status\n"
    "   Enter your order number, e.g. NS1002\n\n"
        "2. 🔄 Returns & refunds\n"
    "   Ask me about returning an item or getting a refund.\n\n"
    "3. 🏷️ Stock check\n"
    "   Ask if a product is in stock, e.g. 'is the yoga mat in stock?'\n\n"
    "What can I help you with?"
)


RETURN_PROMPT = "Sure! Please provide your order number (e.g. NS1002) and I'll check if it's eligible for a return."

REFUND_INFO = (
    "Refunds are processed after your returned item has been received and inspected.\n"
    "Once approved:\n"
    "• The refund is sent to your original payment method.\n"
    "• You'll receive a confirmation email.\n"
    "• Allow 5–7 business days for it to appear.\n\n"
    "If it's been more than 10 business days, share your order number and we'll investigate."
)


def _order_status_reply(order_id: str) -> str:
    order = ORDERS.get(order_id.upper())
    if not order:
        return (
            f"I couldn't find order {html.escape(order_id)}. "
            "Please double-check the number (format: NS followed by 4 digits) or contact support."
        )
    status = order["status"]
    item = html.escape(order["item"])
    safe_id = html.escape(order_id.upper())
    if status == "processing":
        eta = html.escape(order['eta'])
        return f"Order {safe_id} ({item}) is still being processed. Estimated ship time: {eta}."
    if status == "shipped":
        eta = html.escape(order['eta'])
        tracking = html.escape(order['tracking'])
        return (
            f"Order {safe_id} ({item}) has shipped! "
            f"Tracking number: {tracking}. ETA: {eta}."
        )

    if status == "delivered":
        return f"Order {safe_id} ({item}) was delivered. If you didn't receive it, please contact support."
    return "I found your order but couldn't read its status. Please contact support."


def _return_eligibility_reply(order_id: str) -> str:
    order = ORDERS.get(order_id.upper())
    if not order:
        return (
            f"I couldn't find order {html.escape(order_id)}. "
            "Please double-check the number or contact support."
        )
    safe_id = html.escape(order_id.upper())
    item = html.escape(order["item"])
    if order["status"] == "delivered":
        return (
            f"Order {safe_id} ({item}) is eligible for a return within 30 days of delivery.\n"
            "To start your return, visit northstar.example.com/returns and enter your order number."
        )
    if order["status"] == "shipped":
        return (
            f"Order {safe_id} ({item}) hasn't been delivered yet — it's currently in transit.\n"
            "You can request a return once it's delivered."
        )
    return (
        f"Order {safe_id} ({item}) is still being processed and hasn't shipped yet.\n"
        "Returns can be started after delivery."
    )
 
 
def _stock_reply(query: str) -> str:
    q = re.sub(r"[^a-z0-9]", "", query.lower())
    match = next(
        (
            name for name in PRODUCTS
            if re.sub(r"[^a-z0-9]", "", name.lower()) in q
        ),
        None,
    )
    if not match:
        return (
            "WhichProduct would you like me to check? "
            "Please include the product name, e.g. 'is the yoga mat instock?'"
        )
    stock = PRODUCTS[match]["stock"]
    safe_name = html.escape(match.title())
    if stock > 0:
        return f"Yes, {safe_name} is instock — {stock} units available."
    return f"Sorry, {safe_name} is currently outofstock. We'll restock soon — check back later."
 
 
def get_reply(user_message: str) -> str:

    try:
        msg = user_message.strip().lower()

        if not msg:
            return WELCOME

        if msg in GREETINGS:
            return WELCOME

        # Order ID present — check if context is return or general status
        match = re.search(r"\bns\d+\b", msg)
        if match:
            order_id = match.group().upper()
            if any(w in msg for w in ("return", "send back", "exchange")):
                return _return_eligibility_reply(order_id)
            return _order_status_reply(order_id)

        # Return intent without order number
        if any(w in msg for w in ("return", "send back", "exchange")):
            return RETURN_PROMPT

        # Refund intent
        if any(w in msg for w in ("refund", "money back", "reimburs", "when will i get")):
            return REFUND_INFO

       # Stock check intent
        if any(w in msg for w in ("stock", "available", "in stock")):
            return _stock_reply(msg)
 
        # Order status intent without order number
        if any(w in msg for w in ("where", "order", "shipped", "shipping", "status", "track", "deliver")):

            return (
                "I can look up your order! "
                "Please share your order number (e.g. NS1002) and I'll check right away."
            )

        return (
            "I'm not sure I understood that. I can help with:\n"
            "• Order status — share your order number like NS1002\n"
            "• Returns — type 'return'\n"
            "• Refunds — type 'refund'\n"
            "• Stock — ask 'is <product> in stock?'\n\n"
            "For anything else, please contact our support team."
        )

    except Exception:
        return "Something went wrong on my end. Please try again or contact support."