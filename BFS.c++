#include <iostream>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <chrono>

void bfs(const std::map<std::string, std::vector<std::string>>& graph, const std::string& start) {
    std::set<std::string> visited;
    std::queue<std::string> q;

    visited.insert(start);
    q.push(start);

    while (!q.empty()) {
        std::string node = q.front();
        q.pop();
        std::cout << node << " ";

        for (const auto& neighbor : graph.at(node)) {
            if (visited.find(neighbor) == visited.end()) {
                visited.insert(neighbor);
                q.push(neighbor);
            }
        }
    }
}

int main() {
    std::map<std::string, std::vector<std::string>> tree = {
        {"A", {"B", "C", "D", "E", "F"}},
        {"B", {"G", "H", "I"}},
        {"C", {"J", "K"}},
        {"D", {"L", "M", "N"}},
        {"E", {"O", "P", "Q"}},
        {"F", {"R", "S"}},
        {"G", {"T", "U"}},
        {"H", {"V"}},
        {"I", {"W", "X", "Y"}},
        {"J", {"Z", "AA"}},
        {"K", {"AB"}},
        {"L", {"AC", "AD", "AE"}},
        {"M", {"AF", "AG"}},
        {"N", {"AH"}},
        {"O", {"AI", "AJ"}},
        {"P", {"AK", "AL"}},
        {"Q", {"AM"}},
        {"R", {"AN", "AO"}},
        {"S", {"AP"}},
        {"T", {}},
        {"U", {"AQ"}},
        {"V", {"AR"}},
        {"W", {"AS"}},
        {"X", {"AT", "AU"}},
        {"Y", {}},
        {"Z", {"AV"}},
        {"AA", {"AW", "AX"}},
        {"AB", {}},
        {"AC", {}},
        {"AD", {}},
        {"AE", {"AY", "AZ"}},
        {"AF", {}},
        {"AG", {}},
        {"AH", {}},
        {"AI", {}},
        {"AJ", {"BA", "BB"}},
        {"AK", {}},
        {"AL", {"BC"}},
        {"AM", {}},
        {"AN", {}},
        {"AO", {"BD", "BE"}},
        {"AP", {}},
        {"AQ", {}},
        {"AR", {}},
        {"AS", {}},
        {"AT", {}},
        {"AU", {"BF"}},
        {"AV", {}},
        {"AW", {}},
        {"AX", {}},
        {"AY", {}},
        {"AZ", {}},
        {"BA", {}},
        {"BB", {}},
        {"BC", {}},
        {"BD", {}},
        {"BE", {}},
        {"BF", {}}
    };

    auto inicio = std::chrono::high_resolution_clock::now();
    bfs(tree, "A");
    auto fin = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duracion = fin - inicio;

    std::cout << "\nTiempo de ejecución: " << duracion.count() << " segundos\n";

    return 0;
}