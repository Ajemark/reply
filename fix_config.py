with open("/data/.zeroclaw/config.toml", "a") as f:
    f.write("\n[browser]\nenabled = true\nallowed_domains = [\"*\"]\nbackend = \"rust_native\"\nnative_webdriver_url = \"http://zeroclaw-browser:4444\"\n")
    f.write("\n[http_request]\nenabled = true\nallowed_domains = [\"*\"]\n")
    f.write("\n[web_search]\nenabled = true\nprovider = \"duckduckgo\"\n")
