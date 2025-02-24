#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>

using namespace std;

// Function prototypes
void inputGrades(string names[], float grades[], int size);
void displayGrades(const string names[], const float grades[], int size, float passingGrade);
float calculateAverage(const float grades[], int size);
float findMaxGrade(const float grades[], int size);
float findMinGrade(const float grades[], int size);
void sortGrades(string names[], float grades[], int size);
int countPasses(const float grades[], int size, float passingGrade);

int main() {
    int numStudents;
    float passingGrade;

    // Input number of students and passing grade
    cout << "Enter the number of students: ";
    cin >> numStudents;

    if (numStudents <= 0) {
        cerr << "Invalid number of students. Exiting program." << endl;
        return 1;
    }

    cout << "Enter the passing grade: ";
    cin >> passingGrade;

    string* names = new string[numStudents];
    float* grades = new float[numStudents];

    // Input student names and grades
    inputGrades(names, grades, numStudents);

    // Display grades and statistics
    displayGrades(names, grades, numStudents, passingGrade);

    // Clean up dynamic memory
    delete[] names;
    delete[] grades;

    return 0;
}

void inputGrades(string names[], float grades[], int size) {
    for (int i = 0; i < size; ++i) {
        cout << "Enter student " << i + 1 << " name: ";
        cin >> ws; // Clear input buffer
        getline(cin, names[i]);

        cout << "Enter student " << i + 1 << " grade: ";
        cin >> grades[i];

        while (grades[i] < 0 || grades[i] > 20) { // Assuming grades are between 0 and 20
            cerr << "Invalid grade. Please enter a grade between 0 and 20: ";
            cin >> grades[i];
        }
    }
}

void displayGrades(const string names[], const float grades[], int size, float passingGrade) {
    cout << "\nStudent Grades:\n";
    for (int i = 0; i < size; ++i) {
        cout << i + 1 << ". " << names[i] << ": " << fixed << setprecision(2) << grades[i]
             << (grades[i] >= passingGrade ? " (Pass)" : " (Fail)") << endl;
    }

    float average = calculateAverage(grades, size);
    float maxGrade = findMaxGrade(grades, size);
    float minGrade = findMinGrade(grades, size);
    int passCount = countPasses(grades, size, passingGrade);

    cout << "\nAverage Grade: " << fixed << setprecision(2) << average << endl;
    cout << "Highest Grade: " << maxGrade << endl;
    cout << "Lowest Grade: " << minGrade << endl;
    cout << "Number of Passes: " << passCount << endl;
    cout << "Number of Fails: " << size - passCount << endl;

    cout << "\nSorted Grades (Ascending):\n";
    string* sortedNames = new string[size];
    float* sortedGrades = new float[size];

    copy(names, names + size, sortedNames);
    copy(grades, grades + size, sortedGrades);

    sortGrades(sortedNames, sortedGrades, size);

    for (int i = 0; i < size; ++i) {
        cout << i + 1 << ". " << sortedNames[i] << ": " << sortedGrades[i] << endl;
    }

    delete[] sortedNames;
    delete[] sortedGrades;
}

float calculateAverage(const float grades[], int size) {
    float sum = 0;
    for (int i = 0; i < size; ++i) {
        sum += grades[i];
    }
    return sum / size;
}

float findMaxGrade(const float grades[], int size) {
    float maxGrade = grades[0];
    for (int i = 1; i < size; ++i) {
        if (grades[i] > maxGrade) {
            maxGrade = grades[i];
        }
    }
    return maxGrade;
}

float findMinGrade(const float grades[], int size) {
    float minGrade = grades[0];
    for (int i = 1; i < size; ++i) {
        if (grades[i] < minGrade) {
            minGrade = grades[i];
        }
    }
    return minGrade;
}

void sortGrades(string names[], float grades[], int size) {
    for (int i = 0; i < size - 1; ++i) {
        for (int j = 0; j < size - i - 1; ++j) {
            if (grades[j] > grades[j + 1]) {
                swap(grades[j], grades[j + 1]);
                swap(names[j], names[j + 1]);
            }
        }
    }
}

int countPasses(const float grades[], int size, float passingGrade) {
    int count = 0;
    for (int i = 0; i < size; ++i) {
        if (grades[i] >= passingGrade) {
            ++count;
        }
    }
    return count;
}

