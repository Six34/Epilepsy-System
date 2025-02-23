// Libraries
#include <chrono>
#include <thread>
#include <iostream>

// Constants
const double TICKRATE = 60.0;
const double TICK_INTERVAL = 1.0 / TICKRATE;
double LOOP_DUR = 0.0;

int main() {

    auto lastTime = std::chrono::high_resolution_clock::now();

    while (true) {

        // Calculate delta time
        auto currentTime = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double> deltaTime = currentTime - lastTime;
        lastTime = currentTime;


        //TODO MAIN LOOP FOR COMPUTATION


        // example
        std::cout << "Hello World" << std::endl;


        // Sleep to keep the tickrate
        LOOP_DUR = deltaTime.count();
        if (LOOP_DUR < TICK_INTERVAL) {
            std::this_thread::sleep_for(std::chrono::duration<double>(TICK_INTERVAL - LOOP_DUR));
        }
    }

    return 0;
}