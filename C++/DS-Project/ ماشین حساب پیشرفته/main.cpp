#include <iostream>
#include <stack>
#include <string>
#include <cctype>
#include <sstream>
#include <stdexcept>

using namespace std;

// Function to determine the precedence of operators
int precedence(char op) {
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    return 0;
}

// Function to perform arithmetic operations
int applyOperation(int a, int b, char op) {
    switch (op) {
        case '+': return a + b;
        case '-': return a - b;
        case '*': return a * b;
        case '/':
            if (b == 0) throw invalid_argument("Division by zero.");
            return a / b;
        default: throw invalid_argument("Invalid operator.");
    }
}

// Function to check if a character is an operator
bool isOperator(char c) {
    return c == '+' || c == '-' || c == '*' || c == '/';
}

// Function to convert an Infix expression to Postfix
string infixToPostfix(const string& infix) {
    stack<char> operators;
    string postfix;

    for (size_t i = 0; i < infix.length(); ++i) {
        char c = infix[i];

        // Skip spaces
        if (isspace(c)) continue;

        // If the character is a digit, append it to the postfix expression
        if (isdigit(c)) {
            while (i < infix.length() && (isdigit(infix[i]) || infix[i] == '.')) {
                postfix += infix[i];
                ++i;
            }
            postfix += ' ';
            --i;
        }
            // If the character is '(', push it onto the stack
        else if (c == '(') {
            operators.push(c);
        }
            // If the character is ')', pop and append until '(' is found
        else if (c == ')') {
            while (!operators.empty() && operators.top() != '(') {
                postfix += operators.top();
                postfix += ' ';
                operators.pop();
            }
            if (operators.empty()) throw invalid_argument("Unbalanced parentheses.");
            operators.pop();
        }
            // If the character is an operator
        else if (isOperator(c)) {
            while (!operators.empty() && precedence(operators.top()) >= precedence(c)) {
                postfix += operators.top();
                postfix += ' ';
                operators.pop();
            }
            operators.push(c);
        } else {
            throw invalid_argument("Invalid character in expression.");
        }
    }

    // Pop all the remaining operators
    while (!operators.empty()) {
        if (operators.top() == '(') throw invalid_argument("Unbalanced parentheses.");
        postfix += operators.top();
        postfix += ' ';
        operators.pop();
    }

    return postfix;
}

// Function to evaluate a Postfix expression
int evaluatePostfix(const string& postfix) {
    stack<int> values;
    istringstream iss(postfix);
    string token;

    while (iss >> token) {
        if (isdigit(token[0]) || (token[0] == '-' && token.length() > 1)) {
            values.push(stoi(token));
        } else if (isOperator(token[0])) {
            if (values.size() < 2) throw invalid_argument("Invalid postfix expression.");
            int b = values.top(); values.pop();
            int a = values.top(); values.pop();
            values.push(applyOperation(a, b, token[0]));
        } else {
            throw invalid_argument("Invalid token in postfix expression.");
        }
    }

    if (values.size() != 1) throw invalid_argument("Invalid postfix expression.");
    return values.top();
}

int main() {
    string infix;

    cout << "Advanced Calculator\n";
    cout << "Enter an expression in Infix notation: ";
    getline(cin, infix);

    try {
        string postfix = infixToPostfix(infix);
        cout << "Postfix Expression: " << postfix << endl;
        int result = evaluatePostfix(postfix);
        cout << "Result: " << result << endl;
    } catch (const exception& e) {
        cerr << "Error: " << e.what() << endl;
    }

    return 0;
}

