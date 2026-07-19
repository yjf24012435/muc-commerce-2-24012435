from pathlib import Path

import pandas as pd


def answer_question(base_dir: Path, question: str) -> str:
    data_dir = base_dir / "data"
    metrics_df = pd.read_csv(data_dir / "overall_metrics.csv", encoding="utf-8-sig")
    metrics = dict(zip(metrics_df["指标"], metrics_df["数值"]))
    normalized = question.replace(" ", "").lower()

    segment_df = pd.read_csv(data_dir / "segment_analysis.csv", encoding="utf-8-sig")
    category_df = pd.read_csv(data_dir / "category_analysis.csv", encoding="utf-8-sig")

    if any(word in normalized for word in ["多少用户", "用户数", "总用户"]):
        return f"数据集中共有{int(metrics['用户数']):,}名用户。"
    # TODO 4-1：补充“流失率”“偏好品类”“生命周期风险”和“订单”四类问答。
    # 每个回答都必须引用data目录中已经计算的指标，不得编造数值。
    #流失率
    if any(word in normalized for word in ["流失率","流失人数","多少人流失"]):
        churn_num = int(metrics["流失人数"])
        return f"平台总流失用户{churn_num}人，整体流失率{metrics['流失率']:.2%}。"
    # 3. 偏好品类
    if any(word in normalized for word in ["哪个偏好品类用户最多", "最多用户的品类"]):
        top_cat = category_df.loc[category_df["用户数"].idxmax()]
        return f"用户规模最高的品类是{top_cat['PreferedOrderCat']}，共有{int(top_cat['用户数']):,}人。"
    # 4. 生命周期风险
    if any(word in normalized for word in ["哪个阶段流失最高", "风险最高", "流失风险"]):
        max_risk = segment_df.loc[segment_df["流失率"].idxmax()]
        return f"流失风险最高的生命周期阶段：{max_risk['TenureGroup']}，该阶段流失率{max_risk['流失率']:.2%}。"

    # 5. 订单情况
    if any(word in normalized for word in ["平均订单", "订单均值", "人均订单"]):
        avg_order = metrics["平均订单数"]
        return f"平台用户平均订单数为{avg_order:.2f}单/人。"
    return (
        "基础问答尚未完成。目前只能回答总用户数、总体流失率、偏好品类、生命周期风险、订单情况"
        "请换一种更具体的问法。"
    )
