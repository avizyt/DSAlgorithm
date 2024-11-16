#include <iostream>
#include <unordered_set>
#include <string>

using namespace std;

class URLTracker {
    private:
    unordered_set<string> visitedUrls;

    public:

    bool hasBeenVisited(const string& url) {
        if (visitedUrls.find(url)   != visitedUrls.end()) {
            return true;
    } else {
        visitedUrls.insert(url);
        return false;
    }
}
};

int main() {
    URLTracker tracker;

    string urls[] = {"https://example.com", "https://openai.com", "https://example.com"};

    for (const auto& url: urls) {
        if (tracker.hasBeenVisited(url)) {
            cout << url << " has already been visited." << endl;
        } else {
            cout << url << " is new and now marked as visited." << endl;
    }
}

return 0;
}