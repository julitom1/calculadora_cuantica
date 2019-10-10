import calculadora_cuantica
import unittest

import imaginar

class unit_calculadora_cuantica(unittest.TestCase):
        
        def test_booleano(self):
                self.assertEqual(calculadora_cuantica.booleano([[0,0,1,0,0],[0,0,0,0,1],[0,0,1,0,0],[0,1,0,0,0],[0,0,0,1,0]],[2,3,4,1,5],3),[4, 3, 4, 1, 5])

        def test_booleanoFraccion(self):

                self.assertEqual(calculadora_cuantica.booleanoFraccion([[0,1/3,2/3],[1/6,1/2,1/3],[5/6,1/6,0]],[1/5,7/10,1/10],4),[0.35, 0.33, 0.33])
            
        def test_multirenijas(self):

                self.assertEqual(calculadora_cuantica.multiRenijas(2,3),([[0.0, 0.0, 0.0, 0, 0, 0, 0, 0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.17, 0.33, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.17, 0.33, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.34, 0.33, 0.33, 0.0, 0.0, 1.0, 0.0, 0.0], [0.17, 0.0, 0.33, 0.0, 0.0, 0.0, 1.0, 0.0], [0.17, 0.0, 0.33, 0.0, 0.0, 0.0, 0.0, 1.0]], [[0.0], [0.0], [0.0], [0.17], [0.17], [0.34], [0.17], [0.17]]))

        def test_booleanoFraccionimaginarios(self):

                self.assertEqual(calculadora_cuantica.booleanoFraccionimaginarios([[(1/2**(1/2),0),(1/2**(1/2),0)],[(0,1/2**(1/2)),(0,-1/2**(1/2))]],[(1,0),(0,0)],2),[[(0.5, 0.5)], [(0.5, 0.5)]])

        def test_multiRenijasimaginarios(self):
                self.assertEqual(calculadora_cuantica.multiRenijasimaginarios(2,3),([[0, 0, 0, 0, 0, 0, 0, 0], [0.5, 0, 0, 0, 0, 0, 0, 0], [0.5, 0, 0, 0, 0, 0, 0, 0], [0, 0.33, 0, 1, 0, 0, 0, 0], [0, 0.33, 0, 0, 1, 0, 0, 0], [0, 0.33, 0.33, 0, 0, 1, 0, 0], [0, 0, 0.33, 0, 0, 0, 1, 0], [0, 0, 0.33, 0, 0, 0, 0, 1]]))
                
if True:
    unittest.main()
