from departamento import *

def test_profesoresPorAsignatura(profesores): 
    print(profesoresPorAsignatura(profesores))

def test_profesoresQueSoloImpartenAsignaturasQueCoordinan(profesores):
    print(profesoresQueSoloImpartenAsignaturasQueCoordinan(profesores))

def  test_departamentoResponsable(profesores):
    print(departamentoResponsable(profesores))

def test_ordenarProfesoresPorNumeroCreditosTeoricos(profesores):
    print(ordenarProfesoresPorNumeroCreditosTeoricos(profesores))

def test_añoIncorporacionMasCoordinadores(profesores):
    print(añoIncorporacionMasCoordinadores(profesores))

def test_num_examenes_por_profe(profesores, n=100, asig='FP'):
    print(num_examenes_por_profe(profesores, n, asig))

if __name__=="__main__":
    profesores=lee_fichero('data/profesores.csv')
    #imprimimos los primeros 5 profesores
    for p in profesores[:5]:
        print(p)
    
    print("#############################################")

    print("\nEjercicio 1 - profesoresPorAsignatura")
    test_profesoresPorAsignatura(profesores)

    print("#############################################")

    print("\nEjercicio 2 - profesoresQueSoloImpartenAsignaturasQueCoordinan")
    test_profesoresQueSoloImpartenAsignaturasQueCoordinan(profesores)

    print("#############################################")
    print("\nEjercicio 3 - departamentoResponsable")
    test_departamentoResponsable(profesores)

    print("#############################################")  
    print("\nEjercicio 4 - ordenarProfesoresPorNumeroCreditosTeoricos")
    test_ordenarProfesoresPorNumeroCreditosTeoricos(profesores)

    print("#############################################")
    print("\nEjercicio 5 - añoIncorporacionMasCoordinadores")
    test_añoIncorporacionMasCoordinadores(profesores)

  



    