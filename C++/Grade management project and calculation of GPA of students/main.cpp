#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
using namespace std;

// Constants
const int MAX_STUDENTS = 100;
const int MAX_COURSES = 10;

// Data arrays
string studentIDs[MAX_STUDENTS];
string studentNames[MAX_STUDENTS];
string courseNames[MAX_STUDENTS][MAX_COURSES];
int courseCredits[MAX_STUDENTS][MAX_COURSES];
float courseGrades[MAX_STUDENTS][MAX_COURSES];
int courseCounts[MAX_STUDENTS];
float studentGPAs[MAX_STUDENTS];
int studentCount = 0;

void addStudent();
void displayStudents();
void searchStudent();
void deleteStudent();
void saveToFile();
void loadFromFile();
float calculateGPA(int studentIndex);

int main() {
    loadFromFile();
    int choice;

    do {
        cout << "\nStudent Management System" << endl;
        cout << "1. Add New Student" << endl;
        cout << "2. Display All Students" << endl;
        cout << "3. Search Student" << endl;
        cout << "4. Delete Student" << endl;
        cout << "5. Save and Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                addStudent();
                break;
            case 2:
                displayStudents();
                break;
            case 3:
                searchStudent();
                break;
            case 4:
                deleteStudent();
                break;
            case 5:
                saveToFile();
                cout << "Data saved. Exiting..." << endl;
                break;
            default:
                cout << "Invalid choice. Please try again." << endl;
        }
    } while (choice != 5);

    return 0;
}

void addStudent() {
    if (studentCount >= MAX_STUDENTS) {
        cout << "Maximum student limit reached!" << endl;
        return;
    }

    cout << "Enter Student ID: ";
    cin >> studentIDs[studentCount];
    cout << "Enter Student Name: ";
    cin.ignore();
    getline(cin, studentNames[studentCount]);

    cout << "Enter number of courses: ";
    cin >> courseCounts[studentCount];

    for (int i = 0; i < courseCounts[studentCount]; ++i) {
        cout << "Enter Course Name: ";
        cin.ignore();
        getline(cin, courseNames[studentCount][i]);
        cout << "Enter Credits: ";
        cin >> courseCredits[studentCount][i];
        do {
            cout << "Enter Grade (0-20): ";
            cin >> courseGrades[studentCount][i];
        } while (courseGrades[studentCount][i] < 0 || courseGrades[studentCount][i] > 20);
    }

    studentGPAs[studentCount] = calculateGPA(studentCount);
    studentCount++;
    cout << "Student added successfully!" << endl;
}

void displayStudents() {
    for (int i = 0; i < studentCount; ++i) {
        cout << "\nStudent ID: " << studentIDs[i] << endl;
        cout << "Student Name: " << studentNames[i] << endl;
        for (int j = 0; j < courseCounts[i]; ++j) {
            cout << "Course: " << courseNames[i][j] << ", Credits: " << courseCredits[i][j] << ", Grade: " << courseGrades[i][j] << endl;
        }
        cout << "GPA: " << fixed << setprecision(2) << studentGPAs[i] << endl;
    }
}

void searchStudent() {
    string query;
    cout << "Enter Student ID or Name to search: ";
    cin.ignore();
    getline(cin, query);

    for (int i = 0; i < studentCount; ++i) {
        if (studentIDs[i] == query || studentNames[i] == query) {
            cout << "\nStudent ID: " << studentIDs[i] << endl;
            cout << "Student Name: " << studentNames[i] << endl;
            for (int j = 0; j < courseCounts[i]; ++j) {
                cout << "Course: " << courseNames[i][j] << ", Credits: " << courseCredits[i][j] << ", Grade: " << courseGrades[i][j] << endl;
            }
            cout << "GPA: " << fixed << setprecision(2) << studentGPAs[i] << endl;
            return;
        }
    }
    cout << "Student not found." << endl;
}

void deleteStudent() {
    string query;
    cout << "Enter Student ID or Name to delete: ";
    cin.ignore();
    getline(cin, query);

    for (int i = 0; i < studentCount; ++i) {
        if (studentIDs[i] == query || studentNames[i] == query) {
            for (int j = i; j < studentCount - 1; ++j) {
                studentIDs[j] = studentIDs[j + 1];
                studentNames[j] = studentNames[j + 1];
                courseCounts[j] = courseCounts[j + 1];
                for (int k = 0; k < courseCounts[j]; ++k) {
                    courseNames[j][k] = courseNames[j + 1][k];
                    courseCredits[j][k] = courseCredits[j + 1][k];
                    courseGrades[j][k] = courseGrades[j + 1][k];
                }
                studentGPAs[j] = studentGPAs[j + 1];
            }
            studentCount--;
            cout << "Student deleted successfully!" << endl;
            return;
        }
    }
    cout << "Student not found." << endl;
}

void saveToFile() {
    ofstream file("students.txt");
    if (!file) {
        cout << "Error saving data to file." << endl;
        return;
    }

    for (int i = 0; i < studentCount; ++i) {
        file << studentIDs[i] << endl;
        file << studentNames[i] << endl;
        file << courseCounts[i] << endl;
        for (int j = 0; j < courseCounts[i]; ++j) {
            file << courseNames[i][j] << " " << courseCredits[i][j] << " " << courseGrades[i][j] << endl;
        }
        file << studentGPAs[i] << endl;
    }
    file.close();
}

void loadFromFile() {
    ifstream file("students.txt");
    if (!file) {
        return; // No file exists yet
    }

    while (!file.eof() && studentCount < MAX_STUDENTS) {
        file >> studentIDs[studentCount];
        file.ignore();
        getline(file, studentNames[studentCount]);
        file >> courseCounts[studentCount];

        for (int i = 0; i < courseCounts[studentCount]; ++i) {
            file >> courseNames[studentCount][i] >> courseCredits[studentCount][i] >> courseGrades[studentCount][i];
        }
        file >> studentGPAs[studentCount];
        studentCount++;
    }
    file.close();
}

float calculateGPA(int studentIndex) {
    float totalGradePoints = 0;
    int totalCredits = 0;

    for (int i = 0; i < courseCounts[studentIndex]; ++i) {
        totalGradePoints += courseGrades[studentIndex][i] * courseCredits[studentIndex][i];
        totalCredits += courseCredits[studentIndex][i];
    }

    return totalCredits > 0 ? totalGradePoints / totalCredits : 0;
}
