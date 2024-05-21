#include <iostream>
#include <ginac/ginac.h>

using namespace std;
using namespace GiNaC;

// Función para resolver la ecuación cuadrática
void tcp(const ex &a, const ex &b, const ex &c) {
    try {
        if (a == 0) {
            throw invalid_argument("El coeficiente 'a' no puede ser 0.");
        }

        ex discriminante = pow(b, 2) - 4 * a * c;

        ex raiz1 = (-b + sqrt(discriminante)) / (2 * a);
        ex raiz2 = (-b - sqrt(discriminante)) / (2 * a);

        cout << "Las soluciones de la ecuación son:" << endl;
        cout << "x1 = " << raiz1 << endl;
        cout << "x2 = " << raiz2 << endl;

    } catch (const invalid_argument &e) {
        cerr << "Error: " << e.what() << endl;
    } catch (const exception &e) {
        cerr << "Error inesperado: " << e.what() << endl;
    }
}

int main() {
    double a_num, b_num, c_num;

    cout << "Ingrese el coeficiente a: ";
    cin >> a_num;

    cout << "Ingrese el coeficiente b: ";
    cin >> b_num;

    cout << "Ingrese el coeficiente c: ";
    cin >> c_num;

    ex a = a_num, b = b_num, c = c_num;

    tcp(a, b, c);

    return 0;
}
