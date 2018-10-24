########单元测试 导入import unittest：
#########测试用例 unittest.TestCase
import unittest
import com.lsx.exercises.Method as m
class simpleTest(unittest.TestCase):

    def test_method_name(self):
        name = 'armote'
        nowName = m.getName(name)
        self.assertAlmostEqual(nowName, 'armote')
        #self.assertAlmostEqual(nowName, 'armote1') #assertAlmostEqual方法将检测测试方法的返回值和自己预期的返回值是否一致

    def test_method_add(self):
        add = '武汉'
        nowAdd = m.getAdd(add)
        self.assertAlmostEqual(nowAdd, '武汉')
        #self.assertAlmostEqual(nowAdd, 'armote1') #assertAlmostEqual方法将检测测试方法的返回值和自己预期的返回值是否一致

if __name__=="__main__":
    unittest.main()