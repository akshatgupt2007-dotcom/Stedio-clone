# Quiz App (C++)

A console quiz that asks 5 multiple-choice questions, tracks your score, and displays the final score and percentage at the end.

## Compile & Run
```bash
g++ quiz.cpp -o quiz
./quiz          # Windows: quiz.exe
```

## How it works
- Questions are stored in a `vector<Question>`
- Input is validated (only 1-4 accepted)
- Score increases on every correct answer
- Final score is shown at the end

## Add your own questions
Add more entries to the `quiz` vector in `quiz.cpp`.
