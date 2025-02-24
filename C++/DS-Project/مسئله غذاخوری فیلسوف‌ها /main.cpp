#include <iostream>
#include <thread>
#include <mutex>
#include <vector>
#include <chrono>

using namespace std;

const int NUM_PHILOSOPHERS = 5; // Number of philosophers
mutex forks[NUM_PHILOSOPHERS]; // Mutexes representing forks

void philosopher(int id) {
    int leftFork = id;
    int rightFork = (id + 1) % NUM_PHILOSOPHERS;

    for (int i = 0; i < 3; ++i) { // Each philosopher eats 3 times
        cout << "Philosopher " << id << " is thinking...\n";
        this_thread::sleep_for(chrono::seconds(1)); // Simulate thinking

        // Pick up forks (prevent deadlock by picking the lower index first)
        if (id % 2 == 0) {
            forks[leftFork].lock();
            forks[rightFork].lock();
        } else {
            forks[rightFork].lock();
            forks[leftFork].lock();
        }

        // Eating
        cout << "Philosopher " << id << " is eating...\n";
        this_thread::sleep_for(chrono::seconds(2)); // Simulate eating

        // Put down forks
        forks[leftFork].unlock();
        forks[rightFork].unlock();

        cout << "Philosopher " << id << " has finished eating and is back to thinking...\n";
    }
}

int main() {
    vector<thread> philosophers;

    // Create philosopher threads
    for (int i = 0; i < NUM_PHILOSOPHERS; ++i) {
        philosophers.push_back(thread(philosopher, i));
    }

    // Join all threads
    for (auto& p : philosophers) {
        p.join();
    }

    cout << "All philosophers have finished their meals.\n";
    return 0;
}
