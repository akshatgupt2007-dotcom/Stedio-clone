// Quiz App - tracks and displays the final score (C++)
#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct Question {
    string text;
    string options[4];
    int answer;  // 1-4
};

int main() {
    vector<Question> quiz = {
        {"Which language is used for the Linux kernel?", {"Python", "C", "Java", "Ruby"}, 2},
        {"Which is NOT a C++ feature?", {"Classes", "Templates", "Garbage collector by default", "Operator overloading"}, 3},
        {"Which data structure works on LIFO?", {"Queue", "Array", "Stack", "Tree"}, 3},
        {"What does HTML stand for?", {"HyperText Markup Language", "High Text Machine Language", "Hyper Tool Multi Language", "None"}, 1},
        {"Time complexity of binary search?", {"O(n)", "O(log n)", "O(n^2)", "O(1)"}, 2},
    };

    int score = 0;
    cout << "=== QUIZ APP ===\n\n";

    for (size_t i = 0; i < quiz.size(); i++) {
        cout << "Q" << i + 1 << ". " << quiz[i].text << "\n";
        for (int j = 0; j < 4; j++)
            cout << "  " << j + 1 << ") " << quiz[i].options[j] << "\n";

        int choice = 0;
        while (true) {
            cout << "Your answer (1-4): ";
            if (cin >> choice && choice >= 1 && choice <= 4) break;
            cin.clear();
            cin.ignore(1000, '\n');
            cout << "Invalid input, try again.\n";
        }

        if (choice == quiz[i].answer) {
            score++;
            cout << "Correct!\n\n";
        } else {
            cout << "Wrong. Correct answer: " << quiz[i].answer << ") "
                 << quiz[i].options[quiz[i].answer - 1] << "\n\n";
        }
    }

    cout << "=== FINAL SCORE: " << score << " / " << quiz.size() << " ===\n";
    double pct = 100.0 * score / quiz.size();
    cout << "Percentage: " << pct << "%\n";
    return 0;
}
