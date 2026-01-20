# GitHub Actions 工作流说明 / GitHub Actions Workflow Guide

这个目录包含了 GitHub Actions 的工作流文件，用于自动化测试和部署。

This directory contains GitHub Actions workflow files for automated testing and deployment.

## 📁 文件说明 / File Description

### `ci.yml`
这是一个综合性的 CI（持续集成）工作流示例，包含：

This is a comprehensive CI (Continuous Integration) workflow example that includes:

1. **基础测试任务 / Basic Test Job** (`test`):
   - 检出代码 / Checkout code
   - 设置 Python 环境 / Setup Python environment  
   - 运行 Python 脚本 / Run Python scripts
   - 测试模块导入 / Test module imports

2. **多版本测试任务 / Multi-version Test Job** (`multi-version-test`):
   - 在多个 Python 版本上测试代码 / Test code on multiple Python versions
   - 使用矩阵策略并行运行 / Use matrix strategy for parallel execution
   - 支持 Python 3.9, 3.10, 3.11, 3.12

## 🚀 工作流触发条件 / Workflow Triggers

此工作流在以下情况下触发：

This workflow is triggered when:

- 代码推送到 `main` 或 `master` 分支 / Code is pushed to `main` or `master` branch
- 创建针对 `main` 或 `master` 的拉取请求 / A pull request is created targeting `main` or `master`
- 手动触发（通过 GitHub Actions 界面）/ Manual trigger (via GitHub Actions UI)

## 📚 学习资源 / Learning Resources

### GitHub Actions 基础概念 / GitHub Actions Basics

- **Workflow（工作流）**: 自动化过程的完整定义 / Complete definition of an automated process
- **Job（任务）**: 工作流中的一组步骤 / A set of steps in a workflow
- **Step（步骤）**: 任务中的单个操作 / A single action in a job
- **Action（动作）**: 可重用的代码单元 / Reusable unit of code

### 常用 Actions / Common Actions

- `actions/checkout@v4`: 检出仓库代码 / Checkout repository code
- `actions/setup-python@v5`: 设置 Python 环境 / Setup Python environment
- `actions/upload-artifact@v4`: 上传构建产物 / Upload build artifacts
- `actions/download-artifact@v4`: 下载构建产物 / Download build artifacts

### 矩阵策略 / Matrix Strategy

矩阵策略允许你在多个配置上并行运行任务：

Matrix strategy allows you to run jobs in parallel across multiple configurations:

```yaml
strategy:
  matrix:
    python-version: ['3.9', '3.10', '3.11']
    os: [ubuntu-latest, windows-latest]
```

这将创建 6 个并行任务（3 个 Python 版本 × 2 个操作系统）

This creates 6 parallel jobs (3 Python versions × 2 operating systems)

## 🔍 查看工作流运行结果 / View Workflow Results

1. 访问仓库的 "Actions" 标签页 / Go to the "Actions" tab in your repository
2. 选择一个工作流运行 / Select a workflow run
3. 查看各个任务和步骤的详细日志 / View detailed logs for each job and step

## 🛠️ 自定义工作流 / Customize Workflow

你可以根据需要修改工作流：

You can modify the workflow as needed:

- 添加更多测试步骤 / Add more test steps
- 集成代码质量检查工具（如 flake8, pylint）/ Integrate code quality tools (e.g., flake8, pylint)
- 添加部署步骤 / Add deployment steps
- 配置通知（邮件、Slack 等）/ Configure notifications (email, Slack, etc.)

## 📖 更多资源 / More Resources

- [GitHub Actions 官方文档 / Official Documentation](https://docs.github.com/en/actions)
- [GitHub Actions 市场 / Marketplace](https://github.com/marketplace?type=actions)
- [工作流语法参考 / Workflow Syntax Reference](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
