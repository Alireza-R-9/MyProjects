#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>

using namespace std;

// Node structure for Huffman Tree
struct Node {
    char ch;
    int freq;
    Node *left, *right;
    Node(char c, int f) : ch(c), freq(f), left(nullptr), right(nullptr) {}
};

// Comparison function for priority queue
struct Compare {
    bool operator()(Node* a, Node* b) {
        return a->freq > b->freq;
    }
};

// Function to generate Huffman codes
void generateCodes(Node* root, string code, unordered_map<char, string>& huffmanCode) {
    if (!root) return;
    if (!root->left && !root->right) {
        huffmanCode[root->ch] = code;
    }
    generateCodes(root->left, code + "0", huffmanCode);
    generateCodes(root->right, code + "1", huffmanCode);
}

// Function to build Huffman Tree and return encoded data
string huffmanEncode(const string& text, unordered_map<char, string>& huffmanCode) {
    unordered_map<char, int> freq;
    for (char ch : text) freq[ch]++;

    priority_queue<Node*, vector<Node*>, Compare> pq;
    for (auto pair : freq) {
        pq.push(new Node(pair.first, pair.second));
    }

    while (pq.size() > 1) {
        Node* left = pq.top(); pq.pop();
        Node* right = pq.top(); pq.pop();
        Node* newNode = new Node('\0', left->freq + right->freq);
        newNode->left = left;
        newNode->right = right;
        pq.push(newNode);
    }

    Node* root = pq.top();
    generateCodes(root, "", huffmanCode);

    string encodedString = "";
    for (char ch : text) {
        encodedString += huffmanCode[ch];
    }

    return encodedString;
}

// Function to decode Huffman encoded string
string huffmanDecode(Node* root, const string& encodedText) {
    string decodedText = "";
    Node* current = root;
    for (char bit : encodedText) {
        current = (bit == '0') ? current->left : current->right;
        if (!current->left && !current->right) {
            decodedText += current->ch;
            current = root;
        }
    }
    return decodedText;
}

int main() {
    string text;
    cout << "Enter text to compress: ";
    getline(cin, text);

    unordered_map<char, string> huffmanCode;
    string encodedText = huffmanEncode(text, huffmanCode);

    cout << "Huffman Codes:\n";
    for (auto pair : huffmanCode) {
        cout << pair.first << " : " << pair.second << endl;
    }

    cout << "Encoded Text: " << encodedText << endl;

    return 0;
}
