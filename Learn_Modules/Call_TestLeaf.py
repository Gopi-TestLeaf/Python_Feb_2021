# Way 01
import Learn_Modules.TL_Module

obj1 = Learn_Modules.TL_Module.TestLeaf01()
obj1.devOps()
obj1.Python()

# Way 02
from Learn_Modules.TL_Module import TestLeaf02
obj2 = TestLeaf02()
obj2.automation()

# Way 03
from Learn_Modules.TL_Module import TestLeaf03 as t3
obj3 = t3()
obj3.bigData()

# Way 04
from Learn_Modules.TL_Module import TestLeaf01, TestLeaf02

# Way 05
from Learn_Modules.TL_Module import TestLeaf01 as t1, TestLeaf02 as t2