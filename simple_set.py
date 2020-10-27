web_browsers = set()
web_browsers = {["Chrome", "Firefox", "Edge"]}

user_web_browsers = ["Chrome", "Firefox", "Chrome", "Firefox", "Edge", "Firefox"]
unique_web_browsers = { list_of_web_browsers }

web_browsers.add("Opera")
web_browsers.add(("Opera", 2))
web_browsers.remove("Edge")

print (web_browsers)