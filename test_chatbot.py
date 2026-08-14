from chatbot import get_reply

tests = [
    ("hello",                       "northstar"),
    ("where is my order",           "ns1002"),
    ("NS1002",                      "shipped"),
    ("NS9999",                      "couldn"),
    ("I want to return something",  "order number"),
    ("NS1003",                      "delivered"),
    ("NS1003 return",               "eligible for a return"),
    ("NS1002 return",               "in transit"),
    ("NS1004 return",               "hasn"),
    ("when will i get my refund",   "5"),
    ("refund",                      "5"),
    ("",                            "northstar"),
]

all_pass = True
for msg, expected in tests:
    reply = get_reply(msg)
    ok = expected.lower() in reply.lower()
    print(("PASS" if ok else "FAIL") + ": " + repr(msg))
    if not ok:
        print("  GOT: " + reply[:80])
        all_pass = False

print()
print("All tests passed." if all_pass else "Some tests FAILED.")
