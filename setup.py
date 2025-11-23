#!/usr/bin/env python3
"""
Setup script for Multi-Agent RAG System
Author: Anupama Sharma
"""

from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="multi-agent-rag-system",
    version="1.0.0",
    description="A hierarchical multi-agent system combining RAG with LangGraph for intelligent document research and content generation",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/AnupamaSharma2000/MultiAgent_RAG",
    author="Anupama Sharma",
    author_email="sharma25@umd.edu",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="multi-agent ai rag langgraph langchain nlp machine-learning",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "langgraph>=0.0.40",
        "langchain>=0.1.0",
        "langchain-openai>=0.1.0",
        "langchain-experimental>=0.0.50",
        "langchain-community>=0.0.20",
        "langchain-core>=0.1.0",
        "qdrant-client>=1.7.0",
        "tavily-python>=0.3.0",
        "pymupdf>=1.23.0",
        "tiktoken>=0.5.0",
        "python-mermaid>=0.1.0",
        "python-dotenv>=1.0.0",
        "requests>=2.31.0",
        "httpx>=0.25.0",
        "typing-extensions>=4.8.0",
        "pydantic>=2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-asyncio>=0.21.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.5.0",
        ],
        "jupyter": [
            "jupyter>=1.0.0",
            "ipykernel>=6.25.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "multi-agent-rag=multi_agent_rag:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/AnupamaSharma2000/MultiAgent_RAG/issues",
        "Source": "https://github.com/AnupamaSharma2000/MultiAgent_RAG",
        "Portfolio": "https://github.com/AnupamaSharma2000",
        "LinkedIn": "https://www.linkedin.com/in/anupama-sharma22/",
    },
)
