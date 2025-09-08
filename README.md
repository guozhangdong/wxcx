# Futu Autotrade (Simplified)

This repository contains a minimal trading pipeline used for demonstration.

## 模型输入体检与常见错误

`debug_probe.py` 可用于检查特征是否与模型输入一致。
常见问题包括缺失列、NaN/Inf 以及 dtype 不符，运行体检可以生成
`debug_report.json` 帮助定位问题。
