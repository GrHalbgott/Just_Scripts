#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

double mins(double Pm, double Nm, double Tm)
{
    int mm;
    mm = 60 * (fmod((Nm * Tm / Pm) / 60, 1));
    return mm;
}

int main()
{
    double P, N, T;
    int hours;
    std::cout << "How many people will work?" << std::endl;
    std::cin >> P;
    std::cout << "How many tasks to complete?" << std::endl;
    std::cin >> N;
    std::cout << "How long does one person need for one task (minutes)?" << std::endl;
    std::cin >> T;

    hours = (N * T / P) / 60;

    std::cout << "Total time to finish the task (hours/minutes): " << std::setw(2) << std::setfill('0') << hours << ":" << mins(P, N, T) << std::endl;
    return EXIT_SUCCESS;
}
