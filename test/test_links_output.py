links = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page1",  # Duplicate
    "https://example.com/page3",
]

# Ensure no duplicates
prof_links = "\n".join(f"- {link}" for link in set(links))

print(prof_links)