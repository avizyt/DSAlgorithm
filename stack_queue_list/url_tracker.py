"""Question 3.40 (Algorithm Design Manual)
What is the best data structure for maintaining URLs that have been visited
by a web crawler? Give an algorithm to test whether a given URL has already
been visited, optimizing both space and time.
"""


class URLTracker:
    def __init__(self) -> None:
        self.visited_urls = set()

    def has_been_visited(self, url):
        if url in self.visited_urls:
            return True
        else:
            self.visited_urls.add(url)
            return False


if __name__ == "__main__":
    tracker = URLTracker()

    # Simulate checking URLs
    urls = ["https://example.com", "https://openai.com", "https://example.com"]
    for url in urls:
        if tracker.has_been_visited(url):
            print(f"{url} has already been visited.")
        else:
            print(f"{url} is new and now marked as visited.")
