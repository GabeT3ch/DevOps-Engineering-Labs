# Lab 04 - CI/CD Pipeline

## Overview

A GitHub Actions CI/CD pipeline that automatically runs linting, security scanning, and code quality checks against Labs 1-3 on every push and pull request. This is the lab where DevOps meets DevSecOps — security is baked into the workflow, not bolted on after the fact.

The pipeline lives in `.github/workflows/ci.yml` at the root of the repo. This folder contains documentation explaining how the pipeline works.

## What This Lab Covers

- GitHub Actions workflow syntax (YAML)
- Continuous Integration — automated checks on every PR
- Security scanning with Bandit (Python SAST)
- Secret detection with Gitleaks
- Code linting with flake8
- Branch protection — nothing merges to main without passing checks
- Git branching and PR workflow

## How It Works

1. Developer creates a feature branch and pushes code
2. Developer opens a Pull Request to merge into main
3. GitHub Actions automatically triggers the pipeline
4. Pipeline runs three jobs in parallel:
   - **Lint** — checks code style and syntax with flake8
   - **Security Scan** — scans Python code for vulnerabilities with Bandit
   - **Secret Detection** — scans for hardcoded secrets and credentials with Gitleaks
5. PR shows green checkmarks (pass) or red X (fail) for each job
6. Code only merges to main if all checks pass

## Pipeline Triggers

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
```

The pipeline runs on every push to main and every PR targeting main.

## Tools Used

- **GitHub Actions** — CI/CD platform, runs directly in the repo
- **flake8** — Python linter, catches syntax errors and style issues
- **Bandit** — Python Static Application Security Testing (SAST), finds common security vulnerabilities
- **Gitleaks** — scans git history for hardcoded secrets, API keys, and credentials

## File Structure

```
.github/
└── workflows/
    └── ci.yml                  ← the actual pipeline (required location)

Lab_4-CICD-Pipeline/
└── README.md                   ← this file (documentation)
```

GitHub Actions requires workflow files to be in `.github/workflows/` at the repo root. The pipeline cannot live inside the lab folder.

## Viewing Pipeline Results

After pushing or opening a PR, go to the **Actions** tab in the GitHub repo to see pipeline runs, logs, and pass/fail status for each job.

## Skills Demonstrated

- CI/CD pipeline design and implementation
- Security-first DevSecOps workflow
- GitHub Actions YAML configuration
- Automated code quality and security enforcement
- Branch protection and PR-based development workflow