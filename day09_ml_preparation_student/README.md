# 第9天学生项目：机器学习零基础数据准备

## 运行方法

```bash
python -m pip install -r requirements.txt
python validate_day09_environment.py
jupyter lab
```

打开`notebooks/day09_ml_preparation_student.ipynb`。Notebook已经提供完整处理骨架，你只需完成少量关键填空、运行检查点并撰写解释。

## 学生信息

- 姓名：姚佳凤
- 学号：24012435
- 班级：信计二班

## 用自己的话回答

- 什么是特征，什么是标签：特征是描述样本的输入属性，作为模型的判断依据；标签是答案
- 为什么要保留测试集：要用于检验模型对陌生数据的真实预测能力
- 为什么83%准确率仍可能没有用：因为召回率很低，如果为0表明这个模型完全找不到任何一个要流失的客户，无法开展挽留运营，没有任何实际业务价值
