import unittest
import calculation

class NewTest(unittest.TestCase):
    def test_txt_add(self):
        print("orig_0.8_add.txt的相似度 ")

        file = open("D:\\sim_0.8\\orig.txt", "r", encoding='UTF-8')
        orig_text = file.read()
        file.close()
        origin = calculation.Split_sentence(orig_text)

        file = open("D:\\sim_0.8\\orig_0.8_add.txt", "r", encoding='UTF-8')
        orig_add_text = file.read()
        file.close()
        origin_add = calculation.Split_sentence(orig_add_text)

        sim = calculation.Calculation_Similiarity(origin, origin_add)
        sim = str("%.2f") % sim
        print(sim)

    def test_txt_del(self):
        print("orig_0.8_del.txt的相似度 ")

        file = open("D:\\sim_0.8\\orig.txt", "r", encoding='UTF-8')
        orig_text = file.read()
        file.close()
        origin = calculation.Split_sentence(orig_text)

        file = open("D:\\sim_0.8\\orig_0.8_del.txt", "r", encoding='UTF-8')
        orig_add_text = file.read()
        file.close()
        origin_add = calculation.Split_sentence(orig_add_text)

        sim = calculation.Calculation_Similiarity(origin, origin_add)
        sim = str("%.2f") % sim
        print(sim)

    def test_txt_dis_1(self):
        print("orig_0.8_dis_1.txt的相似度 ")

        file = open("D:\\sim_0.8\\orig.txt", "r", encoding='UTF-8')
        orig_text = file.read()
        file.close()
        origin = calculation.Split_sentence(orig_text)

        file = open("D:\\sim_0.8\\orig_0.8_dis_1.txt", "r", encoding='UTF-8')
        orig_add_text = file.read()
        file.close()
        origin_add = calculation.Split_sentence(orig_add_text)

        sim = calculation.Calculation_Similiarity(origin, origin_add)
        sim = str("%.2f") % sim
        print(sim)

    def test_txt_dis_3(self):
        print("orig_0.8_dis_3.txt的相似度 ")

        file = open("D:\\sim_0.8\\orig.txt", "r", encoding='UTF-8')
        orig_text = file.read()
        file.close()
        origin = calculation.Split_sentence(orig_text)

        file = open("D:\\sim_0.8\\orig_0.8_dis_3.txt", "r", encoding='UTF-8')
        orig_add_text = file.read()
        file.close()
        origin_add = calculation.Split_sentence(orig_add_text)

        sim = calculation.Calculation_Similiarity(origin, origin_add)
        sim = str("%.2f") % sim
        print(sim)

    def test_txt_dis_7(self):
        print("orig_0.8_dis_7.txt的相似度 ")

        file = open("D:\\sim_0.8\\orig.txt", "r", encoding='UTF-8')
        orig_text = file.read()
        file.close()
        origin = calculation.Split_sentence(orig_text)

        file = open("D:\\sim_0.8\\orig_0.8_dis_7.txt", "r", encoding='UTF-8')
        orig_add_text = file.read()
        file.close()
        origin_add = calculation.Split_sentence(orig_add_text)

        sim = calculation.Calculation_Similiarity(origin, origin_add)
        sim = str("%.2f") % sim
        print(sim)

    def test_txt_dis_10(self):
        print("orig_0.8_dis_10.txt的相似度 ")

        file = open("D:\\sim_0.8\\orig.txt", "r", encoding='UTF-8')
        orig_text = file.read()
        file.close()
        origin = calculation.Split_sentence(orig_text)

        file = open("D:\\sim_0.8\\orig_0.8_dis_10.txt", "r", encoding='UTF-8')
        orig_add_text = file.read()
        file.close()
        origin_add = calculation.Split_sentence(orig_add_text)

        sim = calculation.Calculation_Similiarity(origin, origin_add)
        sim = str("%.2f") % sim
        print(sim)

    def test_txt_dis_15(self):
        print("orig_0.8_dis_15.txt的相似度 ")

        file =  open("D:\\sim_0.8\\orig.txt", "r", encoding='UTF-8')
        orig_text = file.read()
        file.close()
        origin = calculation.Split_sentence(orig_text)

        file = open("D:\\sim_0.8\\orig_0.8_dis_15.txt", "r", encoding='UTF-8')
        orig_add_text = file.read()
        file.close()
        origin_add = calculation.Split_sentence(orig_add_text)

        sim = calculation.Calculation_Similiarity(origin, origin_add)
        sim = str("%.2f") % sim
        print(sim)

    def test_txt_mix(self):
        print("orig_0.8_mix.txt的相似度 ")
        file = open("D:\\sim_0.8\\orig.txt", "r", encoding='UTF-8')
        orig_text = file.read()
        file.close()
        origin = calculation.Split_sentence(orig_text)

        file = open("D:\\sim_0.8\\orig_0.8_mix.txt", "r", encoding='UTF-8')
        orig_add_text = file.read()
        file.close()
        origin_add = calculation.Split_sentence(orig_add_text)

        sim = calculation.Calculation_Similiarity(origin, origin_add)
        sim = str("%.2f") % sim
        print(sim)

    def test_txt_rep(self):
        print("orig_0.8_rep.txt的相似度 ")

        file = open("D:\\sim_0.8\\orig.txt", "r", encoding='UTF-8')
        orig_text = file.read()
        file.close()
        origin = calculation.Split_sentence(orig_text)

        file = open("D:\\sim_0.8\\orig_0.8_rep.txt", "r", encoding='UTF-8')
        orig_add_text = file.read()
        file.close()
        origin_add = calculation.Split_sentence(orig_add_text)

        sim = calculation.Calculation_Similiarity(origin, origin_add)
        sim = str("%.2f") % sim
        print(sim)

    def test_txt_ori(self):
        print("orig.txt的相似度 ")

        file = open("D:\\sim_0.8\\orig.txt", "r", encoding='UTF-8')
        orig_text = file.read()
        file.close()
        origin = calculation.Split_sentence(orig_text)

        file = open("D:\\sim_0.8\\orig.txt", "r", encoding='UTF-8')
        orig_add_text = file.read()
        file.close()
        origin_add = calculation.Split_sentence(orig_add_text)

        sim = calculation.Calculation_Similiarity(origin, origin_add)
        sim = str("%.2f") % sim
        print(sim)


if __name__ == '__main__':

    unittest.main()
